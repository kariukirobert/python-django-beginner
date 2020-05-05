from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'publish_date']


    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        instance = self.instance
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title already exists")
        
        return title

    
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if email.endswith('.com'):
    #         raise forms.ValidationError("This email already exists")
        
    #     return email