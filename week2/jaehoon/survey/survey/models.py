from django.db import models

class Survey(models.Model):
    idx = models.AutoField(primary_key=True)
    question = models.TextField(null=True)
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)
    status = models.CharField(max_length=1, default='y')

    def __str__(self):
        return f"survey_idx : {self.idx}  질문 : {self.question} \n ans1 : {self.ans1}, ans2 : {self.ans2}, ans3 : {self.ans3}, ans4 : {self.ans4} "

    class Meta :
        db_table = 'survey_table'
        verbose_name = '질문'
        verbose_name_plural = '질문들'

class Answer(models.Model):
    idx = models.AutoField(primary_key=True)
    survey_idx = models.IntegerField()
    ans = models.TextField()

    def __str__(self):
        return f"idx : {self.idx}, survey_idx : {self.survey_idx}, ans : {self.ans}"


    class Meta :
        db_table = 'answer_table'
        verbose_name = '정답'
        verbose_name_plural = '정답들'