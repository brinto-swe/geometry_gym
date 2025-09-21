from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    ROLE_CHOICES = (
        ('member', 'Member'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    phone = models.CharField(max_length=20, blank=True, null=True)

    # Avoid reverse accessor clash with default auth.User
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='accounts_user_set',
        related_query_name='accounts_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='accounts_user_set_permissions',
        related_query_name='accounts_user_perm',
    )

    def is_member(self):
        return self.role == 'member'

    def is_staff_role(self):
        return self.role == 'staff'

    def is_admin_role(self):
        return self.role == 'admin' or self.is_superuser
