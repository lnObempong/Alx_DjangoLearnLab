from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


# ============================
# User Registration Form
# ============================
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# ============================
# Post Form with Tag Support
# ============================
class PostForm(forms.ModelForm):
    # Optional comma-separated tag input
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas. Example: django, python, web",
        widget=forms.TextInput(attrs={"placeholder": "tag1, tag2"})
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]


# ============================
# Comment Form
# ============================
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 3, "placeholder": "Write a comment..."}
        ),
        max_length=2000,
        label=""
    )

    class Meta:
        model = Comment
        fields = ["content"]

from django import forms
from taggit.forms import TagWidget
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(attrs={"placeholder": "Add tags separated by commas"}),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        max_length=2000,
        label=''
    )

    class Meta:
        model = Comment
        fields = ["content"]
