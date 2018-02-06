from django.shortcuts import render
# -*- coding: utf-8 -*


from django.shortcuts import render_to_response

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.core import serializers
from django.http import HttpResponse
from .serializers import UserSerializer
import uuid
# Create your views here.
# class UserList(APIView):
    # def get(self, request, format=None):
    #     try:
    #         te = User.objects.all()
    #         # serializer = OrderSerializer(te, many=True)
    #         # data = serializer.data
    #         # print data
    #         # return Response(data={'retCode': 0, 'message': 'success', 'result': data})
    #         return Response(len(te))
    #     except Exception as e:
    #         return Response(data={'retCode': 1400, 'message': e.message, 'result': ''})

    # def post(self,request,format=None):
    #     try:
    #         if request.is_ajax() and request.method == 'POST':
    #             for key in request.POST:
    #
    #                 valuelist = request.POST.getlist(key)
    #                 te = Order.objects.filter(id__in=valuelist).delete()
    #                 if te:
    #                     # return Response(data={'retCode': 0, 'message': 'success', 'result': data})
    #                     return Response(data={"success"})
    #
    #     except Exception as e:
    #         return Response(data={'retCode': 1400, 'message': e.message, 'result': ''})

def  index(request):
    return render_to_response('index.html')


from .form import UserForm

class Login(APIView):
    def get(self, request,format=None):
        if request.method == 'POST':
            name = request.POST['username']
            password = request.POST['password']
            if name and password is not None:
                user = User.objects.filter(name=name)
                if user:
                    serializer = UserSerializer(user, many=True)
                    data = serializer.data
                    if data[0]['pwd'] == password:
                        return render_to_response('test.html')
                    else:
                        return render_to_response('index.html')
                else:
                    return render_to_response('index.html')
            else:
                 return render_to_response('index.html')
        else:  # 当正常访问时
            return render_to_response('index.html')

    def post(self, request,format=None):
        if request.method == 'POST':
            name = request.POST['username']
            password = request.POST['password']
            if name and password is not None:
                id = uuid.uuid4()
                user = User.objects.create(id=id ,name=name,pwd=password)
                if user:
                    return render_to_response('test.html')
                else:
                    return render_to_response('index.html')
            else:
                 return render_to_response('index.html')
        else:  # 当正常访问时
            return render_to_response('index.html')

