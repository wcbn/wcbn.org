# NOTE 1. Docker must be running a local development environment
#      2. You may need to install some image tools like graphviz
# TODO 3. automate this to run whenever models change
docker-compose run web python manage.py graph_models -a -g -X TimeStampedModel | dot -Tpng >./docs/schema-diagram-$(date +"%Y%m%d").png
