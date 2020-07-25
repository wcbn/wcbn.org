from django.db.models import CharField


class CharField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 65000)
        super(CharField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'text'
