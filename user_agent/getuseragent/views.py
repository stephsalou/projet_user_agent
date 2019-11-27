from django.shortcuts import render , HttpResponse
from django.http import JsonResponse

# Create your views here.

def get_user_agent(request):

    data = {
        'is_mobile':request.user_agent.is_mobile,
        'is_tablet':request.user_agent.is_tablet,
        'is_touch_capable':request.user_agent.is_touch_capable,
        'is_pc':request.user_agent.is_pc,
        'is_bot':request.user_agent.is_bot,
        'browser':request.user_agent.browser ,
        'browser_family':str(request.user_agent.browser.family) ,
        'browser_version':request.user_agent.browser.version_string ,
        'os':str(request.user_agent.os),
        'os_family':request.user_agent.os.family,
        'os_version':request.user_agent.os.version_string,
        'device':str(request.user_agent.device),
        'device_family':request.user_agent.device.family ,

    }
    print(data)
    return JsonResponse(data)