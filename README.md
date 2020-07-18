# wcbn.org

[![wcbn](https://circleci.com/gh/wcbn/wcbn.org.svg?style=svg)](https://app.circleci.com/pipelines/github/wcbn/wcbn.org)

# Getting Started

In order to run this web application, you’ll need to install Docker and Yarn. If you’re on a Mac, you can follow these instructions directly. Otherwise, hopefully they are useful as Google fodder.

        brew install yarn
        ./scripts/setup.sh

## Launch

        ./scripts/start.sh
        firefox http://localhost:8000/
        ./scripts/stop.sh

## Create a superuser

<!-- TODO automate this -->

        docker-compose run web sh
        python manage.py createsuperuser

## Django Shell

        docker-compose run web python manage.py shell

## Postgres Shell

        docker ps
        docker exec -it <PG CONTAINER ID> sh
        psql -U postgres

## Manual database migration

In general, `entrypoint.sh` will handle migrations, but in cases where you are prompted by Django for input, set `stdin_open: true` and `tty: true` for `web` in `docker-compose.yml`. Then:

        ./scripts/start
        docker-compose run web sh
        python3 manage.py makemigrations
        python3 manage.py migrate

## Javascript and CSS

We intentionally use very limited javascript, but tailwindcss is compiled with postcss which uses js, and webpack does some black magic for us.

### Turbolinks

Turbolinks requires that all javascript is put in the \<head\> tag

## Ionicons

To add an icon, go to [ionicons.com](https://ionicons.com/), download and save in `ionicons/templates/svgs`. Usage:

        {% ionicon name="my-icon-filename" %}

# Dev Ops

## Heroku - [admin](https://dashboard.heroku.com/teams/wcbn/apps)

This has a pipeline for reviewing PR's and deploying to a stage environment

## CircleCI - [admin](https://app.circleci.com/pipelines/github/wcbn/wcbn.org)

Find the config under `.circleci/config.yml`

Requires these environment variables that can be found in your `.env`:

        SECRET_KEY=insertrandomstringhere123
        DB_NAME=wcbn
        DJANGO_SETTINGS_MODULE=app.environments.test
