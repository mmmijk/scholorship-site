# comment/forms.py
from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    email = forms.CharField(
            label='Email',
            max_length=50,
            widget=forms.widgets.Input(
                    attrs={'class': 'form-control', 'style': "width: 60%;"}
                    )
            )
    website = forms.CharField(
            label='网站',
            max_length=100,
            widget=forms.widgets.URLInput(
                    attrs={'class': 'form-control', 'class': 'form-control'}
                    )
            )
    content = forms.CharField(
            label='内容',
            max_length=500,
            widget=forms.widgets.Textarea(
                    attrs={'rows':6, 'cols':60,'class':'form-control'}
                    )
            )
            
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('评论太短可没有效果哦，多说说理由吧')
        return content
    
    class Meta:
        model = Comment
        fields = ['email','website','content']