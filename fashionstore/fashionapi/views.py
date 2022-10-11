from django.shortcuts import render #ithinte aavashyam illa by default vannathaanu
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from functools import reduce
# get post put patch delete

class GreetingsView(APIView):
    def get(self,request,*args,**kwargs):
        c_date=datetime.datetime.now()
        c_hour=c_date.hour
        msg=""
        if c_hour<12:
            msg="good morning"
        elif c_hour<18:
            msg="good afternoon"
        elif c_hour<24:
            msg="good night"
        return Response({"msg":msg})

class HelloWorldView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"hello world"})
class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"good morning"})
class GoodEveningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"good evening"})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        num=request.data.get("num")
        res=num**3
        return Response({"res":res})

class FactorView(APIView):
    def post(self,request,*args,**kwargs):
        num=request.data.get("num")
        fact=reduce(lambda n1,n2:n1*n2,range(1,num+1))
        return Response({"res":fact})
class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get("txt")
        wc={}
        words=txt.split(" ")
        for word in words:
            if word not in wc:
                wc[word]=1
            else:
                wc[word]+=1
        return Response({"wordcount:":wc})

