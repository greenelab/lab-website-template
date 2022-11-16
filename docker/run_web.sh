#!/usr/bin/env bash

# the name of the image
IMAGE_NAME=lab-website-renderer
IMAGE_TAG=latest
IMAGE=${IMAGE_NAME}:${IMAGE_TAG}

# the name of the running container
CONTAINER_NAME=lab-website-renderer

# PLATFORM="--platform=linux/amd64"
# for now, use the default platform
PLATFORM=""

CUR_DIR=$(realpath "$(dirname "${BASH_SOURCE[0]}")")

cd ${CUR_DIR}/..

# build the image using the project root as context.
# if that succeeds, move on to running it
docker build ${PLATFORM} \
    -t ${IMAGE} -f ./docker/Dockerfile . && \
docker run --name ${CONTAINER_NAME} \
    --init \
    ${PLATFORM} --rm -it \
    -p 4000:4000 \
    -p 35729:35729 \
    -v $PWD:/usr/src/app \
    ${IMAGE}
