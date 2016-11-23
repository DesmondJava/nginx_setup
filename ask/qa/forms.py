# coding=utf-8
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404

from qa.models import Question, Answer, User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError('Title is empty', code='validation_error')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError('Сообщение не корректно', code=12)
        return text

    def save(self):
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError('Text is empty', code='validation_error')
        return text

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError('Question number incorrect', code='validation_error')
        return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    email = forms.EmailField()
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError('Username is empty', code='validation_error')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username "%s" is already in use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.strip() == '':
            raise forms.ValidationError('Email is empty', code='validation_error')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError('Password is empty', code='validation_error')
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
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

    # username = forms.CharField(max_length=100)
    # password = forms.CharField(widget=forms.PasswordInput)

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
