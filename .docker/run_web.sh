#!/usr/bin/env bash


# the name of the image
IMAGE_NAME=lab-website-renderer
IMAGE_TAG=latest
IMAGE=${IMAGE_NAME}:${IMAGE_TAG}


# the name of the running container
CONTAINER_NAME=lab-website-renderer


# PLATFORM="--platform=linux/amd64"
# for now, use the default platform
PLATFORM="--platform=linux/amd64"


CUR_DIR=$(realpath "$(dirname "${BASH_SOURCE[0]}")")


cd ${CUR_DIR}/..

DOCKER_RUN_CMD="docker run"

# set the docker run command based our platform
# (e.g., if we're in windows, run it through winpty)
case "$OSTYPE" in
  # solaris*) 
    # echo "SOLARIS" ;;
  darwin*)  
    echo "Detected OS X"
    if [[  "${PLATFORM}" == *"amd64"*  ]]; then
        echo "...and requested platform is not native, forcing polling"
        FORCE_POLLING="1"
    fi
    ;;

  # linux*)   
    # echo "LINUX" ;;
  # bsd*)     
    # echo "BSD" ;;

  msys*)
    echo "Detected Windows-esque OS"
    DOCKER_RUN_CMD="winpty docker run" 
    FORCE_POLLING="1"
    ;;
esac

# build the image using the project root as context.
# if that succeeds, move on to running it
docker build ${PLATFORM} \
    -t ${IMAGE} -f ./.docker/Dockerfile . && \
${DOCKER_RUN_CMD} --name ${CONTAINER_NAME} ${PLATFORM} \
    --init \
    --rm -it \
    -p 4000:4000 \
    -p 35729:35729 \
    -v $PWD:/usr/src/app \
    -e FORCE_POLLING="${FORCE_POLLING:-0}" \
    ${IMAGE} "$@"
