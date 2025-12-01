from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length = 30, primary_key = True)
    password = models.CharField(max_length = 30)
    
    def get_password(self, input_password):
        """Return the stored password for comparison"""
        return self.password