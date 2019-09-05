from django.shortcuts import render
from django.conf import settings
import psycopg2
import logging
from django.template.response import TemplateResponse
#import kerberos
import psycopg2
import api_gss
from vm.models import VmModel
from django.core.cache import caches

# Create your views here.
def index(request):
    x = PRIVATE_DIR = getattr(settings, "GSSAPI_SERVER", None)
    # local = caches['local']
    # logger = logging.getLogger('startup')
    # logger.setLevel(logging.DEBUG)
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # ch.setFormatter(formatter)
    # logger.addHandler(ch)
    # if 'HTTP_AUTHORIZATION' in request.META:
    #     kind, initial_client_token = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
    #     if kind == 'Negotiate':
    #         # service = 'HTTP@ksa1c1sb.che.ru'
    #         # logger.debug(u'using service name %s', service)
    #         # logger.debug(u'Negotiate authstr %r', initial_client_token)
    #         # result, krb_context = kerberos.authGSSServerInit(service)
    #         # kerberos.authGSSServerStep(krb_context, initial_client_token)
    #         # # gssstring = kerberos.authGSSServerResponse(krb_context)
    #         # principal = kerberos.authGSSServerUserName(krb_context)
    #         principal = local.get(settings.GSSAPI_USER_PRINCIPAL_KEY)
    #         # _ignore_result = kerberos.authGSSServerStoreDelegate(krb_context)
    #         # local.set(settings.GSSAPI_USER_PRINCIPAL_KEY, principal)
    #         conn = psycopg2.connect(
    #             host='ksa1c1-opkpudb',
    #             user=principal,
    #             dbname='SPODB',
    #         )
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT version()")
    #         records = cursor.fetchall()
    #
    # else:
    #     response = TemplateResponse(request, 'sb_gssapi/index.html', status=401)
    #     response['WWW-Authenticate'] = 'Negotiate'
    #     return response
    # s = ''
    # username = local.get(settings.GSSAPI_USER_PRINCIPAL_KEY)
    # test_vm = Vm.objects.all()
    # content = {
    #            # 'req': result,
    #            'u': test_vm,
    #            # 'gssstring': gssstring,
    #            # 'principal': principal,
    #            'st': username,
    #            # 'r': str(request),
    #            'records': records
    # }
    return render(request, 'sb_gssapi/index.html', content)
