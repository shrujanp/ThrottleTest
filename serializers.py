from rest_framework import serializers
from .models import Member,Activity



class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model=Activity
        fields =[
            'start_time',
            'end_time'
        ]
        read_only_fields= ('user',)
class MemberSerializer(serializers.ModelSerializer):
    activitys=ActivitySerializer(many=True)

    class Meta:
        model = Member
        fields = [
            'user_id',
            'real_name',
            'tz',
            'activitys'
        ]
        read_only_fields=('activitys',)
