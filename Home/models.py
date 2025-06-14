from django.db import models

# Create your models here.

class AboutSection(models.Model):
    name = models.CharField(max_length=100)
    bg_image = models.ImageField(upload_to='img')
    prof_image = models.ImageField(upload_to='img')
    position = models.CharField(max_length=100)
    description_about = models.TextField()
    description_position = models.TextField()
    resume = models.FileField(upload_to='files', blank=True, null=True)
    experience = models.IntegerField(default=0)
    project_success = models.IntegerField(default=0)
    satisfication_rate = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class education(models.Model):
    college_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    certification = models.CharField(max_length=100, blank=True, null=True)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, default="Present")

    def __str__(self):
        return self.college_name
    

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, default="Present")
    description = models.TextField()

    def __str__(self):
        return self.company_name    
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    source_code = models.URLField(blank=True, null=True)
    view_project = models.URLField(blank=True, null=True)
    page_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.name