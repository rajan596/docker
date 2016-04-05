from django import forms
from index.models import document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=document
        fields=[
            "doc_title",
            "doc_type",
            "doc_tags",
            "doc_description",
            "doc_uploaded_by",
            "doc_path",
        ]

