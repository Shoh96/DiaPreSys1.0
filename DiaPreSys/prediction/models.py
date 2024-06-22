# prediction/models.py

from django.db import models

class Patient(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.IntegerField()

    def __str__(self):
        return f"Patient {self.id}: Age {self.age}"

class Prediction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    result = models.CharField(max_length=10)  # Positive or Negative
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction {self.id}: {self.result} on {self.date}"
