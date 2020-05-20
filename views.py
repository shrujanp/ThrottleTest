from django.http import HttpResponse,JsonResponse


from .models import Member


def member_list(request):
    members=Member.objects.all()
    print(type(members))
    data=[{"user_id":member.user_id,"real_name":member.real_name,"tz":member.tz,"activity_periods":[{"start_time":u.start_time,"end_time":u.end_time} for u in member.activity_set.all()]} for member in members ]
    return JsonResponse({"ok":True,"members":data})

