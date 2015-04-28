from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.conf import settings
from account.models import User, UserForm, Info, InfoForm
from models import Status, StatusForm

# Create your views here.
def status(request):
    user_id = request.session["user_id"]
    user_obj = User.objects.get(id=user_id)
    email = user_obj.email
    friends_list = user_obj.friends.all()

    friend_status = []
    for friend in friends_list:
        friend_status_obj = Status.objects.filter(user=friend)
        friend_status += friend_status_obj.all().order_by('-timestamp')

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
    user_list = User.objects.all()
    context = {'user_obj': user_obj, 'status': status, 'info_obj': info_obj, 'status_form': status_form, \
               'email': email, 'user_list': user_list, 'friends_list': friends_list, 'friend_status': friend_status}
    template = 'publish/status.html'
    return render(request, template, context)