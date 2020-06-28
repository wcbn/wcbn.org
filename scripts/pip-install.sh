# install python package in conatiner
# USAGE ./scripts/pip-install.sh $pip-pkg-name
docker-compose run web sh -c "pip3 install $1; pip3 freeze > requirements.txt"
