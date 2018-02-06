from django.shortcuts import render
# -*- coding: utf-8 -*


from django.shortcuts import render_to_response

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
class UserList(APIView):
    def get(self, request, format=None):
        try:
            te = User.objects.all()
            # serializer = OrderSerializer(te, many=True)
            # data = serializer.data
            # print data
            # return Response(data={'retCode': 0, 'message': 'success', 'result': data})
            return Response(len(te))
        except Exception as e:
            return Response(data={'retCode': 1400, 'message': e.message, 'result': ''})

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
    return render_to_response('test.html')


from .form import UserForm


def login(request):
    if request.method == 'POST':  # 当提交表单时

        form = UserForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = UserForm()
    return render(request, 'index.html', {'form': form})

def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('Register success!!')
        else:
            return HttpResponse('Register failed!!')
    else:
        uf = UserForm()
        return render_to_response('register.html',  context=( {'uf':uf}))