Start docker
==========================

* build docker by executing `docker-compose build --no-cache`
* build docker by executing `docker-compose up -d --force-recreate`
* apply migrations by executing `docker container exec -it flask_app yoyo apply`
* open [link](http://localhost:5000/load_data) to load data
* open [link](http://localhost:5000/) to visit main page
