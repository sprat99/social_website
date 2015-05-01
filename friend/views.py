from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from account.models import User, Info
from publish.models import Status
from resume.models import Education, Experience
from django.db.models import Q

# Create your views here.
def friend_home(request, friend_id):
    user_id = request.session["user_id"]
    user_obj = User.objects.get(id=user_id)
    info_obj = Info.objects.get(email=user_obj)
    friend = User.objects.get(id=friend_id)
    friend_info = Info.objects.get(email=friend)
    friends_list = user_obj.friends.all()
    friend_status_list = Status.objects.filter(user=friend)
    
    try:
        friend_education_obj = Education.objects.get(user=friend)
        friend_experience_obj = Experience.objects.get(user=friend)
    except:
        friend_education_obj = None
        friend_experience_obj = None

    context = { 'user_obj': user_obj, 'info_obj':info_obj, 'friend_education_obj':friend_education_obj, \
               'friend_experience_obj':friend_experience_obj, 'friends_list':friends_list, 'friend':friend, \
               'friend_info':friend_info, 'friend_status_list':friend_status_list}
    template = 'friend/friend_home.html'
    return render(request, template, context)

def friend_add(request):
    user_id = request.session["user_id"]
    user_obj = User.objects.get(id=user_id)
    info_obj = Info.objects.get(email=user_obj)

    search = request.GET.get('friend')
    
    try:
        friend = User.objects.get(first_name__contains=search)
    except:
        friend = None
        try:
            friend = User.objects.get( Q(first_name__iexact=search)\
                                        | Q(last_name__iexact=search)\
                                        | Q(email__contains=search) )
        except:
            friend = None


    context = { 'user_obj': user_obj, 'info_obj':info_obj, 'friend':friend}
    template = 'friend/friend_add.html'
    return render(request, template, context)