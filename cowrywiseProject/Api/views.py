from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserDetailsSerializer
from .models import *

# Create your views here.


@api_view(['GET'])
def all_data(request):
    raw = []
    if request.method == 'GET':
        UserDetails.objects.create()

    user = UserDetails.objects.all().order_by('-TimeStamp')

    userSerializer = UserDetailsSerializer(user, many=True)
    users = userSerializer.data
    for i in users:
        data = {
            i['TimeStamp']: i['user_id']
        }
        raw.append(data)

    print(raw)

    return Response(raw)
