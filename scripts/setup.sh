#!/bin/bash
# setup

# git config
git remote add stage git@heroku.com:wcbn-org-stage.git
git remote add prod git@heroku.com:wcbn-org-prod.git

# add local environments variables
cat <<EOF >.env
DB_NAME=wcbn
DB_USER=postgres
DB_HOST=db
DB_PORT=5432
DB_PASSWORD=wcbnadm1n
SECRET_KEY=insertrandomstringhere123
DJANGO_SETTINGS_MODULE=app.environments.development
POSTGRES_DB=wcbn
POSTGRES_USER=postgres
POSTGRES_PASSWORD=wcbnadm1n
EOF

# bundle javascript packages
yarn --cwd src

# remove existing database
rm -rf data/

# build docker image
docker build . -t wcbn
