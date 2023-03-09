#! /bin/bash

# name of image
IMAGE=lab-website-renderer:latest

# name of running container
CONTAINER=lab-website-renderer

# choose platform
PLATFORM=""

# default docker run command
DOCKER_RUN="docker run"

# fix interactive on windows
if [[ $OSTYPE == msys* ]]; then
    DOCKER_RUN="winpty docker run"
fi

# build docker image
docker build ${PLATFORM} \
    --tag ${IMAGE} \
    --file ./.docker/Dockerfile .

# run built docker image
${DOCKER_RUN} ${PLATFORM} \
    --name ${CONTAINER} \
    --init \
    --rm \
    --interactive \
    --tty \
    --publish 4000:4000 \
    --publish 35729:35729 \
    --volume $PWD:/usr/src/app \
    ${IMAGE} "$@"
