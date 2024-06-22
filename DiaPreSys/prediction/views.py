# prediction/views.py

from django.shortcuts import render
from .forms import PredictionForm
from .models import Patient, Prediction
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load('prediction/models/saved_model.pkl')
scaler = joblib.load('prediction/models/scaler.pkl')

def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            patient = Patient.objects.create(
                pregnancies=form.cleaned_data['pregnancies'],
                glucose=form.cleaned_data['glucose'],
                blood_pressure=form.cleaned_data['blood_pressure'],
                skin_thickness=form.cleaned_data['skin_thickness'],
                insulin=form.cleaned_data['insulin'],
                bmi=form.cleaned_data['bmi'],
                diabetes_pedigree_function=form.cleaned_data['diabetes_pedigree_function'],
                age=form.cleaned_data['age']
            )
            data = np.array([
                patient.pregnancies,
                patient.glucose,
                patient.blood_pressure,
                patient.skin_thickness,
                patient.insulin,
                patient.bmi,
                patient.diabetes_pedigree_function,
                patient.age
            ]).reshape(1, -1)
            model = joblib.load('prediction/models/saved_model.pkl')
            prediction_result = model.predict(data)[0]
            prediction = Prediction.objects.create(
                patient=patient,
                result='Positive' if prediction_result == 1 else 'Negative'
            )
            return render(request, 'result.html', {'prediction': prediction.result})
    else:
        form = PredictionForm()
    return render(request, 'predict.html', {'form': form})
