from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import blogs

# mtd:get
# url: social/posts/
class PostView(APIView):
    def get(self,request,*args,**kwargs):
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            data=blogs[0:limit]
            return Response(data)
        if "liked_by" in request.query_params:
            id=int(request.query_params.get("liked_by"))
            liked_post=[blog for blog in blogs if id in blog["liked_by"]]
            return Response(data=liked_post)
        else:
            return Response({"data":blogs})
# mtd: post
# data >>> "postId": 2,"userId": 1,"title": "goomorning","content": "hello"
    def post(self,request,*args,**kwargs):
        blog=request.data
        blogs.append(blog)
        return Response(data=blog)

# url: social/posts/{postid}
# mtd:get
class SpView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==pid].pop()
        return Response(data=blog)
    def delete(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog = [b for b in blogs if b["postId"]==pid].pop()
        blogs.remove(blog)
        return Response(data=blog)
    def put(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog = [b for b in blogs if
                b["postId"] == pid].pop()
        blog.update(request.data)
        return Response(data=blog)

# 1 id ulla user 2 postid ulla post like cheyyanam
# url:social/post/likes/<int:pid>
# mtd :post
# data :{user id :1}

class AddLikeView(APIView):
    def post(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        user=request.data.get("userid")
        blog=[b for b in blogs if b["postId"]==pid].pop()
        blog["liked_by"].append(user)
        return Response(data=blog)