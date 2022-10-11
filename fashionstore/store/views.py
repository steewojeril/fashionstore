from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import products

# url :localhost:8000/products
# mtd : get
# mtd : post , data={"id":2,"title":"added product"}
class AllProductView(APIView):
    def get(self,request,*args,**kwargs):
        if "price" in request.query_params:
            price=float(request.query_params.get("price"))
            product=[p for p in products if price == p["price"]]
            return Response(data=product)
        else:
            return Response(data=products)

    def post(self,request,*args,**kwargs):
        product=request.data
        products.append(product)
        return Response(data=product)
    # def put(self,request,*args,**kwargs):
        

# url:localhost:8000/products/{productid}
# mtd: get
class SpProductView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        product=[p for p in products if p["id"]==pid]
        return Response(data=product)
    def delete(self,request,*args,**kwargs):
        pid = kwargs.get("pid")
        product = [p for p in products if p["id"] == pid].pop()
        products.remove(product)
        return Response(data=product)
    def put(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        data=request.data
        product=[p for p in products if p["id"]==pid].pop()
        product.update(data)
        return Response(data=product)

