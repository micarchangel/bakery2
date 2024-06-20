from django.db import models

class UserForm(models.Model):
    userName = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.userName

    class Meta:
        verbose_name_plural = 'Пользователи'
