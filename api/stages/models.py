from django.db import models


class Stage(models.Model):
    class Meta:
        db_table = 'stage'

    stage_id = models.AutoField(primary_key=True)
    stage_name = models.CharField(max_length=64, null=False)
    order = models.IntegerField()
    STAGE_TYPES = (
        (1, 'Sourced'),
        (2, 'Applied'),
        (3, 'Shortlisted'),
        (4, 'Phone Screen'),
        (5, 'Assessment'),
        (6, 'Interview'),
        (7, 'Offer'),
        (8, 'Hired'),
    )
    stage_type = models.IntegerField(
        choices=STAGE_TYPES
    )