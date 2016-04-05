from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import APIView,parser_classes

from index.models import Users, document
from api.serializers import UserListSerializer, DocumentSerializer
from .forms import DocumentForm

import os
# Create your views here.
def home(request):
    return HttpResponse("Home")

@api_view(['GET'])
def users_list(request):
    """
    List all users if GET request
    """
    if request.method=="GET":
        users = Users.objects.all()
        serializer = UserListSerializer(users,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_detail(request,pk):
    """
    Insert/delete/update/display Perticular user
    """

    try:
        user=Users.objects.get(username=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=UserListSerializer(user)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def document_list(request):
    """
    display all documents
    """

    try:
        doc=document.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=DocumentSerializer(doc,many=True)
        return Response(serializer.data)

    return Response(status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST','DELETE','PUT'])
def document_detail(request,pk):
    """
    GET / POST / DELETE based on doc_id
    """

    try:
        doc=document.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=DocumentSerializer(doc)
        return Response(serializer.data)

    elif request.method=="PUT":
        serializer=DocumentSerializer(doc,data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        # delete document from folder
        doc.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method=="POST":
        return HttpResponse(str(request))

@api_view(["POST"])
def upload_document(request):
    form=DocumentForm(request.POST or None, request.data or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
