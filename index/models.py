from django.db import models
from django.contrib import admin

"""
User table
"""
class Users(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    fullname=models.CharField(max_length=50)
    account_created_on=models.DateTimeField(auto_now_add=True)
    usertype=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username','fullname','email','usertype','account_created_on')

"""
Document Details table
"""
class document(models.Model):
    doc_title=models.CharField(max_length=50,default="")
    doc_type=models.CharField(max_length=10,default="")
    doc_tags=models.CharField(max_length=50,default="")
    doc_description=models.CharField(max_length=100,default="")
    doc_uploaded_by=models.ForeignKey(Users)
    doc_path=models.FileField()
    doc_uploaded_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doc_title

class documentAdmin(admin.ModelAdmin):
    list_display = ('doc_title','doc_uploaded_by','doc_tags','doc_description','doc_path')

"""
Stats Table
"""
class Stats(models.Model):
    keyword=models.CharField(max_length=10)
    frequency=models.IntegerField(default=0)

    def __str__(self):
        return self.keyword

class StatsAdmin(admin.ModelAdmin):
    list_display=('keyword','frequency')