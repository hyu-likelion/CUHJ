from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'calculator/main.html')

def calculator(request):
    sick = request.GET['sick']
    result = eval(sick)
    return render(request, 'calculator/calculator.html', {'result':result})
