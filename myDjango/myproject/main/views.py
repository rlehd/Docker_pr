import requests, csv
from urllib.parse import quote
from django.shortcuts import render, redirect, get_object_or_404  
from .models import CsTerm
from django.http import HttpResponse


def export_csv(request):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cs_dictionary.csv"'
    response.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(response)
    
    writer.writerow(['단어명', '영어 표기', '나만의 쉬운 설명', '위키백과 공식 정의'])

    
    terms = CsTerm.objects.all().order_by('-pk')
    for term in terms:
        writer.writerow([term.word, term.english_word, term.easy_explanation, term.official_definition])

    return response


def index(request):
    terms = CsTerm.objects.all().order_by('-pk')
    return render(request, 'home.html', {'terms': terms})

def delete_word(request, pk):
    
    term = get_object_or_404(CsTerm, pk=pk)
    term.delete()
    return redirect('index')

def edit_word(request, pk):
    
    term = get_object_or_404(CsTerm, pk=pk)

    if request.method == 'POST':
        term.english_word = request.POST.get('english_word')
        term.easy_explanation = request.POST.get('easy_explanation')
        term.save() 

        return redirect('index')

    return render(request, 'edit.html', {'term': term})


def add_word(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        english_word = request.POST.get('english_word')
        easy_explanation = request.POST.get('easy_explanation')

        official_def = "위키백과에서 정의를 찾을 수 없습니다."

        try:
            if word:
                
                encoded_word = quote(word)
                url = f"https://ko.wikipedia.org/api/rest_v1/page/summary/{encoded_word}"

                
                headers = {
                    'User-Agent': 'MyCSDictionaryApp/1.0 (kgh@example.com)'
                }

                response = requests.get(url, headers=headers, timeout=5)

                
                if response.status_code == 200:
                    data = response.json()
                    official_def = data.get('extract', official_def)
        except Exception as e:
            print(f"API 호출 중 에러 발생: {e}")

        
        CsTerm.objects.create(
            word=word,
            english_word=english_word,
            easy_explanation=easy_explanation,
            official_definition=official_def
        )
        return redirect('index')

    
    return render(request, 'add.html')
