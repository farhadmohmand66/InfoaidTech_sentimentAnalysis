from django.shortcuts import render
import numpy as np

from joblib import load
model = load('./savedModels/nbModelPred.joblib')
vect = load('./savedModels/vect.joblib')
# from nltk.corpus import stopwords # to remove the stopwrods
# from nltk.stem.porter import PorterStemmer # steam to root word every
import re
# steamer = PorterStemmer()

def predictor(request):
    if request.method == 'POST':
        opinion = request.POST['opinion']
        opinion = re.sub('[^a-zA-Z]', ' ', opinion)
        opinion = opinion.lower()
        opinion = opinion.split()
#         steamer = PorterStemmer()
#         stopwordAll = stopwords.words('english')
#         stopwordAll.remove('not')
#         opinion = [steamer.stem(word) for word in opinion if not word in set(stopwordAll)]
        opinion = ' '.join(opinion)
        corpusNew = [opinion]
        y_pred = model.predict(vect.transform(corpusNew))
        if y_pred == 0:
            y_pred = 'Your review is negative'
        elif y_pred == 1:
            y_pred = 'Your review is positive'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')

