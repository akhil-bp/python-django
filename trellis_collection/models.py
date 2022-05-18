from django.db import models


# Create your models here.
class Collections(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_name = models.CharField("client_name", max_length=240,null=True)
    collection_title = models.CharField("collection_title", max_length=400)
    roadshow_uuid = models.CharField("roadshow_uuid", max_length=240,null=True)
    type = models.CharField("type", max_length=240,null=True)
    due_date = models.CharField("due_date", max_length=240,null=True)
    agents = models.JSONField(encoder=None, decoder=None,null=True)
    clients = models.JSONField(encoder=None, decoder=None,null=True)
    stats = models.JSONField(encoder=None, decoder=None,null=True)
    requests = models.JSONField(encoder=None, decoder=None,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.CharField("start_date", max_length=240,null=True)
    mark_as_ready=models.BooleanField(default=False)
    dr_opportunity_id=models.CharField("dr_opportunity_id",max_length=240,null=True)
    dr_opportunity_code=models.CharField("dr_opportunity_code",max_length=240,null=True)
    issuer_id=models.CharField("issuer_id", max_length=240,null=True)
    external_storage = models.JSONField("external_storage", encoder=None, decoder=None, null=True)