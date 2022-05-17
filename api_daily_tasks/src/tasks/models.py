from django.db import models

class Task(models.Model):
    STATUS_TASK = [
        (0, 'To-do'),
        (1, 'Doing'),
        (2, 'Finished')
    ]
    title = models.CharField("Name", max_length=255, unique=False, blank=False, null=False)
    status = models.IntegerField(choices=STATUS_TASK)
