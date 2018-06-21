from django.shortcuts import render
from django.http import HttpResponse

# New stuff I added to handle client calls
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# For simpler/custom JSON conversions
from django.forms.models import model_to_dict

# For complete serialization
from django.core.serializers import serialize
from django.shortcuts import render

import json

from .models import Transmission

class Encoder(json.JSONEncoder):
    '''To make datetime fields convert to ISO strings'''
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

def main_page(request):
    last = Transmission.objects.order_by('-recordtime','-sequence').all()[:100]
    context = {'transmissions': last}
    return render(request, 'frontend/main_page.html', context)

def reload(request):
    last = Transmission.objects.order_by('-recordtime','-sequence').all()[:100]
    context = {'transmissions': last}
    return render(request, 'frontend/tx_timeblock.html', context)

# Create your views here.
@csrf_exempt
def save_events_json(request):
    '''request.is_ajax is only proper for calls from an XMLHttpRequest in the
    browser so it can be used to distinguish between the two. In this case we
    are almost always taking the payload from a service so the validation of
    the json with loads should be sufficient'''
    if request.method != 'POST':
        return HttpResponse("No")

    # Assuming POST after this point
    payloadjson = json.loads(request.body)
    outstring=''
    for entry in payloadjson:
        outstring+=entry['transcript'] + '\n'
        t = Transmission(**entry)
        t.save()
    return HttpResponse(outstring)

def last(request):
    last = Transmission.objects.order_by('-recordtime','-sequence').all()[:10]
    lastj = [model_to_dict(x) for x in last]
    return HttpResponse(json.dumps(
        lastj, indent=4, sort_keys=False, cls=Encoder, default=str))

#b=model_to_dict(Transmission.objects.all()[7])
#json.dumps(b, indent=4, sort_keys=True, cls=Encoder, default=str)
