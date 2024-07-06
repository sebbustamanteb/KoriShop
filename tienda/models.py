from django.db import models

class form_consultas(models.Model):
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Consulta de {self.email} - {self.created_at.strftime("%Y-%m-%d %H:%M")}'