## Host Information:
- Ubuntu 22.04

## Steps to run:
### Re-create conda env
- conda env create --file environment.yml -n <env_name>
- conda activate <env_name>

### Create dependant dirs and files
- mkdir docker_volume
- mkdir logs
- touch logs/app.log

### Run all services
- docker-compose up

## Postman collection:
https://www.getpostman.com/collections/26834749f5bc00da35f2