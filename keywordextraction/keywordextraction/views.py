from django.shortcuts import render
from .helpers import TextRank4Keyword

def index(request):
    if request.POST:
        text = request.POST['text']
        textrank = TextRank4Keyword()
        textrank.analyze(text, candidate_pos=['NOUN', 'PROPN'], window_size=4, lower=False)
        keywords = textrank.get_keywords(10)
        count = len(keywords)
        return render(request, 'index.html', {'keywords': keywords, 'count': count, })
    return render(request, 'index.html')