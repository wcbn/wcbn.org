from django.apps import AppConfig
from django.db.models.signals import post_save


class WCBNAuthConfig(AppConfig):
    name = 'wcbn_auth'
    label = 'wcbn_auth'
    verbose_name = "WCBN Users"

    def ready(self):
        from wcbn_auth.signals import user_post_save
        sender = self.get_model('User')
        post_save.connect(user_post_save, sender=sender)
