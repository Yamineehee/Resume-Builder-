from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profile_images/')
    about_you = models.TextField()
    skills = models.ManyToManyField('Skill', related_name='resumes', blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='educations', on_delete=models.CASCADE)
    inst_name = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=10)
    study = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.inst_name} ({self.passing_year})"

class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experiences', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    duration_in_months = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.job_title

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
