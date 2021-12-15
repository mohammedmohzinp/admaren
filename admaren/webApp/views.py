from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
import requests
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK

)
from .models import *
from datetime import datetime
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SnippetsDetailSerializer, SnipppetsListSerialzer,TagsDetailSerializer
from rest_framework.pagination import LimitOffsetPagination



class Overview(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        snippet_count = Snippet.objects.count()
        array=[]
        array.append({"total count":snippet_count,"list":"none"})
        return Response(array)
        # return JsonResponse(list(array),safe=False)




class AddSnippet(APIView):
    permission_classes = (IsAuthenticated, )
  
    def post(self, request):
        title          = request.data.get("title")
        decription     = request.data.get("description")
        is_tag         = str_to_bool(request.data.get("is_tag"))
        current_user   = request.user
        tags           = request.data.get("tags")

        if(title == "" or title == None):
            return Response({"code": "422", "message": "title is required", "Response": False},status=HTTP_200_OK)

        elif(decription == "" or decription == None):
            return Response({"code": "422", "message": "description is required", "Response": False},status=HTTP_200_OK)

        elif(is_tag == "" or is_tag == None):
            return Response({"code": "422", "message": "validation faild required", "Response": False},status=HTTP_200_OK)
            
        else:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            date=datetime.now().date()
            print(current_time)
            print(date)


            snippet                = Snippet()
            snippet.title          = title
            snippet.sub_title      = decription
            snippet.created_user   = User.objects.get(username=current_user)
            snippet.snippet_tm     = current_time
            snippet.snippet_dt     = date
            snippet.is_tag         = is_tag
            snippet.save()

            if(is_tag == True):
                if(tags =="" or tags == None):
                    return Response({"code": "422", "message": "tags are required", "Response": False},status=HTTP_200_OK)
                tagmodel = Tags()
                tagmodel.snippet = snippet
                tagmodel.save()
                
                tagmodel.title.add(tags)

                


            return Response({"code": "200","message": "success","Response": True}, status=HTTP_200_OK)


class SnippetDetails(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):  
        snippetView = Snippet.objects.all()
        data=snippetView.values()
        return JsonResponse(list(data),safe=False)

class SnippetUpdate(APIView):
    permission_classes = (IsAuthenticated, )
  
    def patch(self, request):
        up_id          = request.data.get("id")
        title          = request.data.get("title")
        decription     = request.data.get("description")
        is_tag         = request.data.get("is_tag")
        current_user   = User.objects.get(username=request.user)
        tags           = request.data.get("tags")
        if(is_tag == '0'):
            is_tag = True
        else :
            is_tag = False


        Snippet.objects.filter(id=int(up_id)).update(title=title,sub_title=decription,is_tag=str_to_bool(is_tag),created_user=current_user)
        Tags.objects.filter(snippet=int(up_id)).update(title=title)
        return Response({"code": "200","message": "success","Response": True}, status=HTTP_200_OK)




class SnippetDelete(APIView):
    permission_classes = (IsAuthenticated, )
  
    def delete(self, request):
        id  = request.data.get("id")
        if id:
            delete_data     = Snippet.objects.get(id=int(id))
            if delete_data:
                Tags.objects.get(snippet=delete_data.id).delete()
                delete_data.delete()

                return Response({"code": "200","message": "success","Response": True}, status=HTTP_200_OK)
            else:
                return Response({"code": "400","message": "error","Response": True}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"code": "400","message": "error","Response": True}, status=HTTP_400_BAD_REQUEST)

class TagList(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, Testing'}
        return Response(content)

class TagList(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        tagsView = Tags.title.all()
        data=tagsView.values()
        return JsonResponse(list(data),safe=False)


class TagDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )

    queryset = Snippet.objects.all()
    serializer_class = TagsDetailSerializer




def str_to_bool(s):
    if s == 'true':
         return True
    elif s == 'false':
         return False
    else:
         return False





class SnippetsListView(ListAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnipppetsListSerialzer
  pagination_class = LimitOffsetPagination


class SnippetsDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetsDetailSerializer