from django.shortcuts import render

# Create your views here.
def start(element):
    copy_plan = [
        {"name":"Students","pay":8,"text":"Personal License","active":True},
        {"name":"professional","pay":19,"text":"Professional License Email Support","active":False},
        {"name":"agency","pay":49,"text":"1-12 Team Members Phone Support","active":False},
        {"name":"enterprise","pay":79,"text":"Unlimited Team Members 24/ 7 Phone Support","active":False},
    ]
    
    
    copy_fun = {"copy_plan":copy_plan}
    return render(element,"index.html",copy_fun)