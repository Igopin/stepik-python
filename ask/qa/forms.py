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
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    def __init__(self, question, *args, **kwargs):
       self.question = question
       super(AnswerForm, self).__init__(*args, **kwargs)

    #def clean_text(self):
    #    text = self.cleaned_data.get('text', '')
    #    if text:
    #        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer