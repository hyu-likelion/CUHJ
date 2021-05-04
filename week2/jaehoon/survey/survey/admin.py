from django.contrib import admin
from .models import Survey, Answer

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('idx','question','ans1','ans2','ans3','ans4','status',)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('idx','survey_idx', 'ans')
    
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer, AnswerAdmin)
