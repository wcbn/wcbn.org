from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        updated field is updated even if it is not given as
        a parameter to the update field argument.
        """
        if 'update_fields' in kwargs and 'updated_at' not in kwargs['update_fields']:
            kwargs['update_fields'] += ['updated_at']
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
