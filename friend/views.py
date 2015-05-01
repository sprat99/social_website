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

    # search friends
    search = request.GET.get('friend')
    try:
        friends = User.objects.filter(full_name__contains=search)
    except:
        friends = None
        try:
            friends = User.objects.filter( Q(first_name__contains=search)\
                                        | Q(last_name__iexact=search)\
                                        | Q(email__contains=search)
                                        )
        except:
            friends = None
    
    # get friends info and status
    friends_info_list = []
    friends_status_list = []
    for friend in friends:
        friends_info_list += Info.objects.filter(email=friend)
        friends_status_list += Status.objects.filter(user=friend)

    # add friends
    if request.method == 'POST':
        try:
            friend_id = request.POST.get('friend_id')
            friend_add = User.objects.get(id=friend_id)
            user_obj.friends.add(friend_add)
            print "ok"
            return HttpResponseRedirect('/status/')
        except:
            print "failed"

    context = { 'user_obj': user_obj, \
               'info_obj':info_obj, \
               'friends':friends, \
               'friends_info_list':friends_info_list, \
               'friends_status_list':friends_status_list }
    template = 'friend/friend_add.html'
    return render(request, template, context)