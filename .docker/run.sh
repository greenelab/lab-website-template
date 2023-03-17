#! /bin/bash

# name of image
IMAGE=lab-website-renderer:latest

# name of running container
CONTAINER=lab-website-renderer

# choose platform flag
PLATFORM=""

# docker run command
DOCKER_RUN="docker run"

# fix for windows faux linux shells e.g. git bash
if [[ $OSTYPE == msys* ]] || [[ $OSTYPE == cygwin* ]]; then
    DOCKER_RUN="winpty docker run"
fi

# working directory
WORKING_DIR=$(pwd)

# working directory in windows path format
DOCKER_OSTYPE=$( docker info --format "{{json .OSType}}" )
if [[ $DOCKER_OSTYPE == windows ]]; then
    WORKING_DIR=$(cmd //c cd)
fi

# build docker image
docker build ${PLATFORM} \
    --tag ${IMAGE} \
    --file ./.docker/Dockerfile . && \

# run built docker image
${DOCKER_RUN} ${PLATFORM} \
    --name ${CONTAINER} \
    --init \
    --rm \
    --interactive \
    --tty \
    --publish 4000:4000 \
    --publish 35729:35729 \
    --volume "${WORKING_DIR}:/usr/src/app" \
    ${IMAGE} "$@"
