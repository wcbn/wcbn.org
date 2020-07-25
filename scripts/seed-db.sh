echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@wcbn.org', 'admin')" | docker-compose run web python manage.py shell

docker-compose run web python manage.py loaddata events concerts flatpages
