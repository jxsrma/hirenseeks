from django.db import models

# Create your models here.

class userData(models.Model):
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    countryCode = models.CharField(max_length=5)
    contactNumber = models.CharField(max_length=10)
    dob =  models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    #profilePic = models.blob
    #coverPic = models.blob
    bio = models.CharField(max_length=300)
    skills = models.JSONField(default = '{"skills" : [] }')
    projects = models.JSONField(default = '{"projects" : [] }')
    linkGithub = models.TextField(blank=True)
    linkLinkedIn = models.TextField(blank=True)
    linkExtra = models.JSONField(default = '{"links" : [] }')
    dateJoined = models.DateField()
    #lastLogin = models.DateField()

class postedJob(models.Model):
    title = models.CharField(max_length=50)
    jobPos = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
    reqSkill = models.JSONField(default = '{"skills" : [] }')
    expLevel = models.CharField(max_length=50)
    postedBy = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    appliedPeople = models.JSONField(default = '{"ID" : [] }')

class compData(models.Model):
    userName = models.CharField(max_length=100)
    compName = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    countryCode = models.CharField(max_length=5)
    contactNumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    #profilePic = models.blob
    #coverPic = models.blob
    bio = models.CharField(max_length=300)
    linkGithub = models.TextField(blank=True)
    linkLinkedIn = models.TextField(blank=True)
    linkExtra = models.JSONField(default = '{"links" : [] }')

# 1. Delete your migrations files in your desired app
# 2. Thanks to raul answer: In the database: DELETE FROM django_migrations WHERE app = 'app_name'.
# 3. comment codes in models.py and all this models usage in views, signals and etc (to prevent error).
# 4. python manage.py makemigrations YOUR_APP_NAME
# 5. python manage.py migrate --fake
# 6. un-comment what you commented in step 3
# 7. python manage.py makemigrations YOUR_APP_NAME
# 8. migrate without --fake: python manage.py migrate