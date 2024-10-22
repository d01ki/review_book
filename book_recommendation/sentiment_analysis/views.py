from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReviewForm  # ここでReviewFormをインポート
from textblob import TextBlob  # TextBlobを使用

def index(request):
    result = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():  # is_valid()メソッドを使用
            review_text = form.cleaned_data['review']
            # 感情分析を行う
            analysis = TextBlob(review_text)
            if analysis.sentiment.polarity > 0:
                result = 'Positive'
            elif analysis.sentiment.polarity < 0:
                result = 'Negative'
            else:
                result = 'Neutral'
    else:
        form = ReviewForm()
    
    return render(request, 'sentiment_analysis/index.html', {'form': form, 'result': result})
