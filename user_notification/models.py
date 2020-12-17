from django.db import models
from django.conf import settings


class JobAlert(models.Model):
    user_account_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, blank=True, null=True)
    alert_message = models.TextField()
    alert_frequency = models.CharField(max_length=20)
    job_alert_type = models.CharField(max_length=50)
    job_alert_scope = models.CharField(max_length=50)
    job_alert_city = models.CharField(max_length=50)
    job_alert_company_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.UserAccount_id)


class JobType(models.Model):
    job_type_name = models.CharField(max_length=20)


class JobCity(models.Model):
    job_city_name = models.CharField(max_length=20)
