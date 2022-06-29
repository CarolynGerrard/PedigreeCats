#!/bin/bash
CONTAINER_NAME=pedigree-cats-service

CONTAINER=`docker container ls -q --filter name=${CONTAINER_NAME}`
if [ ! -z ${CONTAINER} ];
then
	docker stop ${CONTAINER}
	docker rm ${CONTAINER}	
fi

docker build -t ${CONTAINER_NAME} .

docker-compose up > ../logs/pedigree-cats-service.log




