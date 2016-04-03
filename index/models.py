from django.db import models

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

"""
Document Details table
"""
class document(models.Model):
    doc_title=models.CharField(max_length=50)
    doc_type=models.CharField(max_length=10)
    doc_tags=models.CharField(max_length=50,default="")
    doc_description=models.CharField(max_length=100,default="")
    doc_uploaded_by=models.ForeignKey(Users)
    doc_path=models.FileField(upload_to='documents')
    doc_uploaded_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doc_title
