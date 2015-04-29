from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from account.models import User, Info
from models import Status, StatusForm

# Create your views here.
def status(request):
    user_id = request.session["user_id"]
    user_obj = User.objects.get(id=user_id)
    email = user_obj.email
    friends_list = user_obj.friends.all()
    user_list = User.objects.all()
    status_list = Status.objects.all().order_by('-timestamp')    

    if request.method == 'POST':
        status_form = StatusForm(request.POST, request.FILES)
        if status_form.is_valid():
            user = status_form.cleaned_data['user']
            message = status_form.cleaned_data['message']
            picture = status_form.cleaned_data['picture']

            new_status, created = Status.objects.get_or_create(user=user, \
                                                               message=message, \
                                                               picture=picture
                                                               )
            if created:
                new_status.save()
                return HttpResponseRedirect('/status/')
    else:
        status_form = StatusForm()

    info_obj = Info.objects.get(email=user_obj)
    status_obj = Status.objects.filter(user=user_obj)
    status = status_obj.all().order_by('-timestamp')
    info_list = Info.objects.all()

    context = {'user_obj': user_obj, 'status': status, 'info_obj': info_obj, 'status_form': status_form, \
               'user_list': user_list, 'friends_list': friends_list, 'status_list':status_list, 'info_list':info_list}
    template = 'publish/status.html'
    return render(request, template, context)