echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@wcbn.org', '$PR_REVIEW_PW')" | docker-compose run web python manage.py shell

# TODO other models using django fixtures
# docker-compose run web python manage.py loaddata users
