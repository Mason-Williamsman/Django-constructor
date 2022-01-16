import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Projects(models.Model): # Question
    # project_name = models.CharField(max_length=200, help_text="feald_it_in_the_snake_case_name_please...") # question_text
    project_name = models.SlugField(max_length=200, help_text="feald_it_in_the_snake_case_name_please...")  # question_text
    # label = "name",
    # n = models.SlugField()
    # u = models.URLField()
    git_repository = models.URLField(max_length=400)
    project_path = models.CharField(max_length=400)
    project_public_url = models.URLField(max_length=200, default='0.0.0.0', help_text="public domain name, by default it 0.0.0.0")
    # label = "URL",
    project_port = models.SmallIntegerField(max_length=5, default=8000)
    # favicon_path
    # db_connector
    # run_status
    # resource_availability_check
    # author
    # licence
    # mppk
    # description_short

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_name # question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # def project_port_number(self):
    #     return self.project_port=8000


class Applications(models.Model): # Choice
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    application_name = models.CharField(max_length=200) # choice_text
    pub_date = models.DateTimeField('date published')
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.application_name, self.pub_date >= timezone.now() - datetime.timedelta(days=1) #choice_text
