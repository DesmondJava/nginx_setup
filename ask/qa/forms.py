# coding=utf-8
import re
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404

from qa.models import Question, Answer, User


# class AskForm(forms.Form):
#     title = forms.CharField(label="Title", max_length=100,
#                             widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'title'}))
#     text = forms.CharField(label="Question", max_length=500,
#                            widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'text'}))
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if title.strip() == '':
#             raise forms.ValidationError('Title is empty', code='validation_error')
#         if len(title.strip()) < 15:
#             raise forms.ValidationError('Title is short. Expand the question title.', code='validation_error')
#         return title
#
#     def clean_text(self):
#         text = self.cleaned_data['text']
#         if text.strip() == '':
#             raise forms.ValidationError('Incorrect message', code=12)
#         if len(text.strip()) < 50:
#             raise forms.ValidationError('Question is too short. Please, describe your question better.',
#                                         code='validation_error')
#         return text
#
#     def save(self):
#         if self._user.is_anonymous():
#             self.cleaned_data['author_id'] = 1
#         else:
#             self.cleaned_data['author'] = self._user
#         question = Question(**self.cleaned_data)
#         question.save()
#         return question


# class AnswerForm(forms.Form):
#     text = forms.CharField(label="Answer", max_length=500,
#                            widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'text'}))
#     question = forms.IntegerField(widget=forms.HiddenInput)
#
#     def clean_text(self):
#         text = self.cleaned_data['text']
#         if text.strip() == '':
#             raise forms.ValidationError('Text is empty', code='validation_error')
#         if len(text.strip()) < 20:
#             raise forms.ValidationError('Answer is too short. Add more information, please', code='validation_error')
#         return text
#
#     def clean_question(self):
#         question = self.cleaned_data['question']
#         if question == 0:
#             raise forms.ValidationError('Question number incorrect', code='validation_error')
#         return question
#
#     def save(self):
#         self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
#         if self._user.is_anonymous():
#             self.cleaned_data['author_id'] = 1
#         else:
#             self.cleaned_data['author'] = self._user
#         answer = Answer(**self.cleaned_data)
#         answer.save()
#         return answer


class SignupForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    email = forms.CharField(label="Email", max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError('Username is empty', code='validation_error')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username "%s" is already in use.' % username)
        if len(username.strip()) < 4:
            raise forms.ValidationError('Please, use minimum 3 characters for your name', code='validation_error')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.strip() == '':
            raise forms.ValidationError('Email is empty')
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise forms.ValidationError('Email is not valid! Correct email and send again.')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError('Password is empty', code='validation_error')
        if not re.match(r"^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$", password):
            raise forms.ValidationError('Password must be security! Try another, please.', code='validation_error')
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError('Username is empty', code='validation_error')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError('Password is empty', code='validation_error')
        return password

    def save(self):
        user = authenticate(**self.cleaned_data)
        return user
