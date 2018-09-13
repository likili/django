from django.db import models

# Create your models here.
# должности
class Position(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(verbose_name=u'Instructor Name', max_length=255, help_text="This is nanme")
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    # checkbox
    is_active = models.BooleanField(default=True)
    # ссылка на таблицу(ключ)
    position = models.ForeignKey(Position,  on_delete=models.CASCADE)


    # что бы отображались именна в админке
    def __str__(self):
        return self.name