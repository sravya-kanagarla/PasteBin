import uuid

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import Context
from django.template.loader import get_template
from django.views.generic import *
from models import *

class store(CreateView):
    model = data
    template_name = "index.html"
    fields = ["data","title"]

    def post(self, request, *args, **kwargs):
        token = uuid.uuid1().hex
        self.token = token
        k = data(token=token,user_id=self.request.user.id,data=request.POST['data'],title=request.POST['title'])
        k.save()
        return super(store, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        con = super(store, self).get_context_data(**kwargs)
        con['logged_in'] = False
        if self.request.user.is_authenticated():
            con['logged_in'] = self.request.user.is_authenticated()
        return con

    def get_success_url(self):
        return reverse("all")

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            msg="""
            <html>
            <head><title>Success</title>
            <script>
            window.location.href='/';
            </script>
            </head>
            <body>
            Registered Successfully... Redirecting to home page...
            </body>
            </html>
            """
            curr_user_id = User.objects.all().filter(username=request.POST['username'])[0].id
            return HttpResponse(msg)
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def get_all(request):
    sets = data.objects.all().filter(user_id=request.user.id)
    t = get_template("data.html")
    con={}
    con['logged_in'] = False
    if request.user.is_authenticated():
        con['logged_in'] = request.user.is_authenticated()
    return HttpResponse(t.render(Context({'sets':sets,'logged_in':con['logged_in']})))

def show(request,token):
    ans = data.objects.all().filter(token=token)[0]
    content = ans.data
    title = ans.title
    owner = User.objects.all().filter(id=ans.user_id)[0].username
    con={}
    con['logged_in'] = False
    if request.user.is_authenticated():
        con['logged_in'] = request.user.is_authenticated()
    t = get_template("msg.html")
    return HttpResponse(t.render(Context({'content':content,'title':title,'owner':owner,'logged_in':con['logged_in']})))