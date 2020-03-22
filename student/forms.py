from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
            
        return int(cleaned_data)
    def clean_studentID(self):
        cleaned_data = self.cleaned_data['studentID']   
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
            
        return int(cleaned_data)
    class Meta:
        model = Student
        fields = ('name','sex','studentID','major','email','qq','phone')