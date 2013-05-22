from django.http import HttpResponseRedirect
import re

from canteen.accounts.models import Whitelist


class IpLoginMiddleware(object):
    def __init__(self):
        self.allowed_ip_blocks = Whitelist.objects.all()

    def process_request(self, request):

        ip = request.META['REMOTE_ADDR']
        redirect_address_plus = ['/accounts/ipnotallowed/','/admin/']
        request_path = request.get_full_path()

        for redirect_address in redirect_address_plus:
            if re.match(redirect_address,request_path):
                return None

        ip_list = [ip_set.ip for ip_set in self.allowed_ip_blocks]

        if ip not in ip_list:
            return HttpResponseRedirect('/accounts/ipnotallowed')

        if not request.user.is_authenticated():
            from django.contrib.auth import login, authenticate
            #log the user in
            user = Whitelist.objects.select_related().get(ip=ip).user
            #mustbe auth the user
            user = authenticate(user=user)
            if user and user.is_active:
                login(request, user)

        return None
