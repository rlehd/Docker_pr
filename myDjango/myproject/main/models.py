from django.db import models

class CsTerm(models.Model):
    word = models.CharField(max_length=100) 
    english_word = models.CharField(max_length=100, blank=True) 
    easy_explanation = models.TextField()
    official_definition = models.TextField(blank= True, null = True)
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.word
