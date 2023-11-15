from django.shortcuts import render, get_object_or_404
from channel.models import Channel



def channel_profile(request, channel_name):
    channel = get_object_or_404(Channel, id=channel_name)


    context = {
        
        "channel":channel
        
    }

    return render(request, "channel/channel.html", context)