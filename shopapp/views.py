from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import product_tbl,staff_tbl
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes
from rest_framework import *
import json

def success_response(response, status_code=None):
        data = {
        "hasError": False,
        "errorCode": -1,
        "message": "Success",
        }
        data["response"] = response
        if status_code is None:
            return Response(data, status=status.HTTP_200_OK)
        return Response(data, status=status_code)

def failure_response(response, status_code=None, error_code=1001, message="Failure"):
    json_obj = {
        "hasError": True,
        "errorCode": error_code,
        "message": message,
    }
    json_obj["response"] = response
    if status_code is None:
        return Response(json_obj, status=status.HTTP_200_OK)
    return Response(json_obj, status_code)
class addproduct(APIView):
     def post(self,request):
        data={}
        Response={}
        try:
               a=product_tbl()
               a.name=request.data['name']
               a.price=request.data['price']
               a.m_year=request.data['myear']
               a.colour=request.data['colour']
               a.brand=request.data['brand']
               a.save()
               data={
                    'name':a.name,
                    'price':a.price,
                    'myear':a.m_year,
                    'colour':a.colour,
                    'brand':a.brand
               }
        except Exception as e:
                    response['massage']="error"
                    return failure_response(response)
        response={}
        response["massage"]="data_inserted"
        response['data']=data
        return success_response(response)
class addstaff(APIView):
      def post(self,request):
            data={}
            Response={}
            try:
                  a=staff_tbl()
                  a.name=request.data['name']
                  a.age=request.data['age']
                  a.gender=request.data['gender']
                  a.designation=request.data['designation']
                  a.salary=request.data['salary']
                  a.save()
                  data={
                        'name':a.name,
                        'age':a.age,
                        'gender':a.gender,
                        'designation':a.designation,
                        'salary':a.salary

                  }
            except Exception as e:
                   response['massage']="error"
                   return failure_response(response)
            response={}
            response["massage"]="data_inserted"
            response['data']=data
            return success_response(response)
class viewproduct(APIView):
      def get(self,request):
            a=product_tbl.objects.all()
            data=[]
            Response={}
            try:
                if a:
                  for x in a:
                        info={
                              'name':x.name,
                              'price':x.price,
                              'm_year':x.m_year,
                              'colour':x.colour,
                              'brand':x.brand,

                        }
                        data.append(info)
                  else:
                        pass
            except Exception as e:
                    response['massage']="error"
                    return failure_response(response)
            response={}
            response["massage"]="data_inserted"
            response['data']=data
            return success_response(response)
class dleteproduct(APIView):
      def post(self,request):
        Response={}
        doc=request.data ['productid']
        try:
              a=product_tbl.objects.get(id=doc)
              if a:
                    a.delete()
              else:
                    pass
        except Exception as e:
               response['massage']="error"
               return failure_response(response)
        response={}
        response["massage"]="data_deleted"
        return success_response(response)
              
                    
                            
        


# Create your views here.
