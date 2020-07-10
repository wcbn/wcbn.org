from django.db import models
from wcbn_auth.models import User

BOARD_ROLES = [
    ('Student', 'Student'),
    ('Alumni', 'Alumni'),
    ('UM Appointee', 'UM Appointee'),
    ('Faculty/Staff', 'Faculty/Staff'),
    ('General Manager', 'General Manager')
]


class ExecMember(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=35, null=True, blank=True)

    def __str__(self):
        return str(self.member)


class BoardMember(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=BOARD_ROLES)
    term = models.CharField(max_length=140, null=True, blank=True)

    def __str__(self):
        return str(self.member)


class Department(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    blurb = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(User, through='DepartmentMembership')

    def __str__(self):
        return self.name


class DepartmentMembership(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    is_lead = models.BooleanField(default=False)
