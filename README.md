## Host Information:
- Ubuntu 22.04
- docker-compose version 1.29.2, build 5becea4c

## Steps to run:
- conda env create --file environment.yml -n <env_name>
- conda activate <env_name>
- mkdir docker_volume
- mkdir logs
- touch logs/app.log
- sudo docker-compose up

## Postman collection:
https://www.getpostman.com/collections/26834749f5bc00da35f2