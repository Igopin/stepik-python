from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    def clean(self):
        pass

    def save(self):
        question  = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    #question = forms.IntegerField(widget=forms.HiddenInput())
    question = forms.IntegerField()
    text = forms.CharField(label='Comment', widget=forms.Textarea(attrs={"class": "form-control"}))

    def clean(self):
        pass

    def save(self):
        self.cleaned_data['question'] = Question.objects.get(pk=self.cleaned_data['question']) 
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer