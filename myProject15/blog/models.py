from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=6,
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
        ],
    )
    def __str__(self):
        return str(self.name)
    
class Profile(models.Model):
  
    Branch = models.CharField(max_length=100)
    Cource = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    collage = models.CharField(
        max_length= 500,
        choices= [
        ("Technocrats instute of technology Main", "Technocrats instute of technology Main"),
        ("Technocrats instute of technology Excellence", "Technocrats instute of technology Excellecne"),
        ("Technocrats instute of technology Science", "Technocrats instute of technology Science"),
        ("Technocrats instute of technology Advance", "Technocrats instute of technology Advance"),
        ]

    )
    def __str__(self):
        return str(self.Cource)