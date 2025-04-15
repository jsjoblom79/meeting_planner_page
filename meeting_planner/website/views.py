
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.

def welcome(request):
    # The templates folder isn't needed because It knows where to look already.
    return render(request, "website/welcome.html",
                  {"all_meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse(f"This page was served at: {datetime.today()}")


def about(request):
    """This page is about me"""
    content = ("<p>Hi my name is Justin!<br>I am a programmer by trade, but currently am leading a small team"
               " of analysts and DBA's</p>")
    return HttpResponse(content)