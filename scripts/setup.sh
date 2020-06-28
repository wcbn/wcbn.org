#!/bin/bash
# setup

git remote add stage git@heroku.com:wcbn-org-stage.git
git remote add prod git@heroku.com:wcbn-org-prod.git

yarn --cwd src

docker build . -t wcbn
