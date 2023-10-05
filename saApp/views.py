from django.shortcuts import render
import os
import joblib
from joblib import load
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
model_file_path = os.path.join(BASE_DIR, 'savedModels', 'nbModelPred.joblib')
vect_file_path = os.path.join(BASE_DIR, 'savedModels', 'vect.joblib')

try:
    model = load(model_file_path)
    vect = load(vect_file_path)
    # model = load('./savedModels/nbModelPred.joblib')
    # vect = load('./savedModels/vect.joblib')


    def predictor(request):
        if request.method == 'POST':
            opinion = request.POST['opinion']
            opinion = re.sub('[^a-zA-Z]', ' ', opinion)
            opinion = opinion.lower()
            opinion = opinion.split()
            opinion = ' '.join(opinion)
            corpusNew = [opinion]
            y_pred = model.predict(vect.transform(corpusNew))
            if y_pred == 0:
                y_pred = 'Your review is negative'
            elif y_pred == 1:
                y_pred = 'Your review is positive'
            return render(request, 'main.html', {'result' : y_pred})
        return render(request, 'main.html')


except Exception as e:
        # By this way we can know about the type of error occurring
        print("The error is: ",e)
