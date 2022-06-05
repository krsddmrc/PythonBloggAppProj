from django.db import models

class User (models.Model):
    user_name=models.CharField(max_length=25)
    email_adress=models.CharField(max_length=40)
    


