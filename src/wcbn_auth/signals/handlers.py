from guardian.shortcuts import assign_perm


def user_post_save(sender, instance, created, **kwargs):
    if created:
        assign_perm('change_user', instance, instance)
