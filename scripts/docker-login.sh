#!/bin/bash

if [ -z ${DOCKER_USER} ];
then
  echo "DOCKER_USER variable not set"
  exit 1
fi

if [ ! -f ~/.docker_pat.txt ];
then
  echo "Create ~/.docker_pat.txt containing the docker hub PAT"
  exit 2
fi

cat ~/.docker_pat.txt | docker login --username ${DOCKER_USER} --password-stdin