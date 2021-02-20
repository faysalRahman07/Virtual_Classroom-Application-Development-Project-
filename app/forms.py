from django import forms
from .models import Post, Comment
from .snippets import choices


class PostCreateForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter title'}))
    # image = forms.ImageField(widget=forms.FileInput(
    #     attrs={'class': 'form-control-file'}))
    # video = forms.FileField(widget=forms.FileInput(
    #     attrs={'class': 'form-control-file'}))
    # description = forms.CharField(widget=forms.Textarea(
    #     attrs={'class': 'form-control'}))

    # category = forms.ChoiceField(widget=forms.Select(
    #     attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'attachment', 'description']
