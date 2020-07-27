echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@wcbn.org', 'admin')" | docker-compose run web python manage.py shell

docker-compose run web python manage.py loaddata events concerts flatpages

# change default Site from example.com to localhost:8000
echo "from django.contrib.sites.models import Site;
x = Site.objects.first();
x.domain = 'localhost:8000';
x.name = 'localhost:8000';
x.save();" | docker-compose run web python manage.py shell
