# coding=utf-8
from django import forms
from django.shortcuts import get_object_or_404

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError('Title is empty', code='validation_error')
        return self.cleaned_data

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError('Сообщение не корректно', code=12)
        return self.cleaned_data

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
            raise forms.ValidationError(u'Question number incorrect', code='validation_error')
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
