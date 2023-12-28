from collections import UserDict
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, User

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta: 
      model = Women
      fields = ['title', 'slug', 'content', 'photo', 'cat' , 'is_published']
      widgets = {
         'title': forms.TextInput(attrs={'class': 'form-input'}),
         'content': forms.Textarea(attrs={'cols':60, 'rows': 10}),
      }

      def clean_title(self):
         title = self.clean_data['title']
         if len(title) > 200:
            raise forms.ValidationError('Длина привышает 200 синволов')
         
         return title


class RegisterUserForm(UserCreationForm):
   username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-imput'}))
   email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-imput'}))
   password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-imput'}))
   password2 = forms.CharField(label='Павтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-imput'}))

   class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')
  
      

