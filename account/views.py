from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.conf import settings
from models import User, UserForm, Info, InfoForm

# Create your views here.
def home(request):
    template = 'account/login.html'
    login = UserForm()
    context = {'login': login}
    return render(request, template, context)

def login(request):
    if request.method == 'POST':
        login = UserForm(request.POST)
        form_email = request.POST.get('email')
        form_password = request.POST.get('password')
        try:
            user_obj = User.objects.get(email=form_email)
        except:
            user_obj = None
            return HttpResponse('no user!!!')

        if form_password == user_obj.password:
            request.session['user_id'] = user_obj.id
            return HttpResponseRedirect('/status/')
        else:
            return HttpResponse('wrong!!!')
       
    else:
        login = UserForm(request.POST)

    template = 'account/login.html'
    login = UserForm()
    context = {'login': login}
    return render(request, template, context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        new_register = form.save(commit=False)
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

#         print email
#          
#         try:
#             user_obj = User.objects.get(email=email)
#         except:
#             user_obj = None
#         if user_obj:
#             return HttpResponse("this has been registered")

        new_register, created = User.objects.get_or_create(first_name=first_name, \
                                                           last_name=last_name, \
                                                           password=password, \
                                                           email=email)
        if created:
            new_register.save()
            request.session['session_user_id'] = new_register.id
            return HttpResponseRedirect('info')
    else:
        print "not valid"

    template = 'account/register.html'
    context = {'form': form}
    return render(request, template, context)


def info(request):
    if request.method == 'POST':
        info = InfoForm(request.POST, request.FILES)
        if info.is_valid():
            try:
                user_id = request.session["session_user_id"]
                user_obj = User.objects.get(id=user_id)
                email = user_obj.email
            except:
                user_obj = None
                
            gender = info.cleaned_data['gender']
            pic = info.cleaned_data['pic']
            profile = info.cleaned_data['profile']
            email = info.cleaned_data['email']
            phone = info.cleaned_data['phone']
            address = info.cleaned_data['address']
            age = info.cleaned_data['age']
            major = info.cleaned_data['major']
            new_info, created = Info.objects.get_or_create(gender=gender, \
                                                           pic=pic, \
                                                           profile=profile, \
                                                           email=email, \
                                                           phone=phone, \
                                                           age=age, \
                                                           major=major, \
                                                           address=address)
            if created:
                new_info.save()
                return HttpResponse("You have updated info for %s" %email)
    else:
        info = InfoForm()

    user_list = User.objects.all()
    user_obj = User.objects.get(id=request.session['session_user_id'])
    email = user_obj.email
    print user_list
    
    context = {'info': info, 'email': email, 'user_list': user_list}
    template = 'account/user_info.html'
    return render(request, template, context)

# def homepage(request):
#     context = {'info': info, 'email': email, 'user_list': user_list}
#     template = 'account/user_info.html'
#     return render(request, template, context)
