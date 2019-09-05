from django.http import HttpResponse
from django.core.cache import caches
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
import gssapi
import os
import logging
import base64



class GSSAPIMiddleware(MiddlewareMixin):
    """GSSAPI Middleware make user auth and cache user token
    and user name. Needed to fix gssstring response like
    spnego protocol says to return response with this string"""
    def process_view(self, request, *args, **kwargs):
        if not settings.GSSAPI_ENABLED_OPTION:
            return None
        unauthorized = False
        if 'HTTP_AUTHORIZATION' in request.META:
            kind, client_token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            if kind == 'Negotiate':
                # TODO make sys logging with sb_logging
                local = caches['local']
                service = settings.GSSAPI_SERVER
                os.environ['KRB5_KTNAME'] = settings.GSSAPI_KEYTAB_PATH
                os.environ['KRB5_CONFIG'] = '/etc/krb5.conf'
                ccache = settings.GSSAPI_CCACHE
                store = {'ccache': ccache,}
                server_name = gssapi.Name(service, name_type=gssapi.NameType.hostbased_service)
                server_creds = gssapi.Credentials(usage='accept', name=server_name)
                ctx = gssapi.SecurityContext(creds=server_creds, usage='accept')
                try:
                    _unused_server_tok = ctx.step(base64.b64decode(client_token))
                except:
                    unauthorized = True
                else:
                    user_name = ctx.initiator_name
                    principal = user_name.display_as(user_name.name_type)
                    ctx.delegated_creds.store(store, usage='initiate', overwrite=True)
                    local.set(settings.GSSAPI_USER_PRINCIPAL_KEY, principal)
            else:
                unauthorized = True
        else:
            unauthorized = True
        if unauthorized:
            return HttpResponse('Unauthorized', status=401)
        return None

    def process_request(self, request, *args, **kwargs):
        """function call for every view before Django
        choose witch view would be called. function
        ask user`s browser for Negotiate token"""
        if not settings.GSSAPI_ENABLED_OPTION:
            return None
        unauthorized = False
        if 'HTTP_AUTHORIZATION' in request.META:
            kind, initial_client_token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            if kind != 'Negotiate':
                unauthorized = True
        else:
            unauthorized = True
        if unauthorized:
            response = HttpResponse(request, status=401)
            response['WWW-Authenticate'] = 'Negotiate'
            return response
        return None
