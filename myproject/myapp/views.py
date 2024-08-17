from django.shortcuts import render

# Create your views here.
def start(element):
    copy_plan = [
        {"name":"Students","pay":8,"text":"Personal License","active":True},
        {"name":"professional","pay":19,"text":"Professional License Email Support","active":False},
        {"name":"agency","pay":49,"text":"1-12 Team Members Phone Support","active":False},
        {"name":"enterprise","pay":79,"text":"Unlimited Team Members 24/ 7 Phone Support","active":False},
    ]
    
    copy_li = [
        {"name":"Home","url":"index","active":True},
        {"name":"Company","url":"index","active":True},
        {"name":"About Sports","url":"index","active":True},
        {"name":"Subscription","url":"index","active":True},
        {"name":"Contact Us","url":"index","active":True},
    ]
    copy_about = [
        {"img":"static/images/graph-04.svg","name":"Riding Mountain Bike","text":"Aenean cursus imperdiet nisl id fermentum. Aliquam pharetra dui laoreet vulputate dignissim. Sed id metus id quam auctor molestie eget ut augue.",},
        {"img":"static/images/graph-03.svg","name":"Volley Ball Intense Training","text":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.",},
        {"img":"static/images/graph-02.svg","name":"Learn Surfing From Experts","text":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.",},
        {"img":"static/images/graph-01.svg","name":"Archers Club","text":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.",},
    ]
    copy_fun = {"copy_plan":copy_plan,"copy_li":copy_li,"copy_about":copy_about}
    return render(element,"index.html",copy_fun)