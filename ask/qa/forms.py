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
    text = forms.CharField(label='Comment', widget=forms.Textarea(attrs={"class": "form-control"}))

    def __init__(self, question=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question = question

    def clean(self):
        pass

    def get_question_url(self):
        return self.question.get_url()

    def save(self):
        self.cleaned_data['question'] = self.question 
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer