from django.shortcuts import render_to_response
from django.template import RequestContext


def check(request):
        return render_to_response('util/index.html',
                                  context_instance=RequestContext(request))
