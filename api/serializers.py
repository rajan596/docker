from rest_framework import serializers
from index.models import Users,document


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields = ('username', 'email', 'fullname', 'usertype')

class DocumentSerializer(serializers.ModelSerializer):
    doc_uploaded_by=UserListSerializer()

    class Meta:
        model=document
        fields=( 'id','doc_title' , 'doc_type' , 'doc_tags', 'doc_description' ,  'doc_path' , 'doc_image',
                 'doc_uploaded_on','doc_uploaded_by' )
