from django import forms
from library.models import Lib_Man_Sys_Table

class CourseForm(forms.ModelForm):

    #name=forms.CharField()
    #price=forms.IntegerField()
    #category=forms.CharField()

    class Meta:
        model = Lib_Man_Sys_Table
        fields ="__all__"
        #fields = ['name','price']
