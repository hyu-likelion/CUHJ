from django.shortcuts import render
from .models import Survey, Answer
# Create your views here.

def main(request) :
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    return render(request, 'main.html', {'survey' :survey})

def save_survey(request) :
    survey_idx = request.POST["survey_idx"]
    print("Type : ", type(survey_idx))
    # survey_survey primary key -> 1:n 질문에 대한 답변의 값(survey)
    # num :선택한 설문의 항목 번호
    dto = Answer(survey_idx=int(request.POST["survey_idx"]), num=request.POST["num"])
    # insert query 가 호출
    dto.save()

    return render(request, "complete.html", {'survey_idx': survey_idx})

def show_result(request) :
    # 문제 번호
    idx = request.GET["survey_idx"]

    # select * from survey where survey_idx=1 과 같다.
    ans = Survey.objects.get(survey_idx=idx)

    # 각 문항에 대한 값으로 리스트를 만들어 놓는다.
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]

    # Survey.objects.raw("""SQL문""")
    surveyList = Survey.objects.raw("""
        SELECT survey_idx, num, count(num) sum_num FROM survey_answer
            WHERE survey_idx=%s
            GROUP BY survey_idx,num
            ORDER BY num
        """, idx)

    surveyList = zip(surveyList, answer)

    return render(request, "result.html", {'surveyList': surveyList})