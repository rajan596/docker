from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from index.models import Users, document , Stats
from api.serializers import UserListSerializer, DocumentSerializer
from .forms import DocumentForm

from django.db.models import Q

import json

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
        doc.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method=="POST":
        return HttpResponse(str(request))

@api_view(["POST"])
def upload_document(request):

    if request.method=="POST":
        form=DocumentForm(request.POST or None, request.data or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","POST"])
def search_documents(request):
    """
    Pass JSON Array Having following optional {key,balue} pairs
    Exa :
    {
        "doc_uploaded_by":"rajan",
        "doc_title":"Linked List",
        "doc_tags":ds",
        "doc_description":"list",
        "doc_type":"pdf",
    }
    """
    try:
        # accessing json object
        q=json.loads(request.body.decode("utf-8"))

        # filtering objects
        docs=document.objects.all()

        # only { search_type and query }
        if "search_type" in q:
            docs=docs.filter(Q(doc_title__contains=q["query"]) |
                             Q(doc_uploaded_by__username__contains=q["query"]) |
                             Q(doc_tags__contains=q["query"]) |
                             Q(doc_description__contains=q["query"]) |
                             Q(doc_path__contains=q["query"])
                             )
            serializer=DocumentSerializer(docs,many=True)
            return Response(serializer.data)

        # filter by uploader
        try:
            if "doc_uploaded_by" in q:
                docs=docs.filter(Q(doc_uploaded_by__username=q["doc_uploaded_by"])|
                                 Q(doc_uploaded_by__fullname__contains=q["doc_uploaded_by"])
                                 )
        except e:
            print("+")

        # filter by doc_title
        try:
            if "doc_title" in q:
                docs = docs.filter(Q(doc_title__contains=q["doc_title"]))
        except e:
            print("+")

        # search by tags
        try:
            if "doc_tags" in q:
                docs = docs.filter(Q(doc_tags__contains=q["doc_tags"]))

        except e:
            print("+")

        # search by description
        try:
            if "doc_description" in q:
                docs = docs.filter(Q(doc_description__contains=q["doc_description"]))
        except e:
            print("+")

        # search by type
        try:
            if "doc_type" in q:
                docs = docs.filter(Q(doc_path__contains=str("."+q["doc_type"])))
        except e:
            print("+")

        # serialize data
        serializer=DocumentSerializer(docs,many=True)
        return Response(serializer.data)

    except:
       return Response(status.HTTP_404_NOT_FOUND)
