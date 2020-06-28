yarn --cwd src build
heroku container:login
heroku container:push web --remote prod
heroku container:release web --remote prod
