## prediction/forms.py

# from django import forms

### class PredictionForm(forms.Form):
  #  pregnancies = forms.IntegerField(label='Pregnancies')
  #  glucose = forms.FloatField(label='Glucose')
  #  blood_pressure = forms.FloatField(label='Blood Pressure')
  #  skin_thickness = forms.FloatField(label='Skin Thickness')
  #  insulin = forms.FloatField(label='Insulin')
  #  bmi = forms.FloatField(label='BMI')
  #  diabetes_pedigree_function = forms.FloatField(label='Diabetes Pedigree Function')
  #  age = forms.IntegerField(label='Age')

from django import forms

class PredictionForm(forms.Form):
    pregnancies = forms.IntegerField(label='Pregnancies', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    glucose = forms.FloatField(label='Glucose', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    blood_pressure = forms.FloatField(label='Blood Pressure', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    skin_thickness = forms.FloatField(label='Skin Thickness', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    insulin = forms.FloatField(label='Insulin', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    bmi = forms.FloatField(label='BMI', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    diabetes_pedigree_function = forms.FloatField(label='Diabetes Pedigree Function', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
