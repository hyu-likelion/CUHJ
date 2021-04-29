from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView 
from .models import Survey, Answer
from .forms import SurveyForm

# Create your views here.

class SurveyView(FormView):
    template_name = 'survey.html'
    form_class = SurveyForm
    success_url = '/success'

    survey = Survey.objects.filter(status='y').order_by('-idx')[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['survey_idx'], context['ques'], context['ans1'], context['ans2'], context['ans3'], context['ans4'] = str(self.survey).split(", ")
        context['survey_idx'] = context['survey_idx'][-1]
        return context 

    def form_valid(self, form):
        answer = Answer(
            survey_idx = self.survey.idx,
            ans = form.data.get('ans')
        )
        answer.save()

        return super().form_valid(form)


class AnswerView(ListView):
    model = Answer
    template_name='answer.html'
    context_object_name = 'ans_list'
    question_id = 0

    def get_queryset(self): # 컨텍스트 오버라이딩
        question_id = self.kwargs.get('question_id')
        return Answer.objects.filter(survey_idx=question_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_id = self.kwargs['question_id']
        return context 


class SuccessView(TemplateView):
    template_name = 'success.html'