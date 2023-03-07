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

# move to the root of the repo
cd ${CUR_DIR}/..

# set a default 'docker run' command, which can be overridden for other platforms
DOCKER_RUN_CMD="docker run"

# set the docker run command based our platform
# (e.g., if we're in windows, run it through winpty)
# also set up other OS-specific options
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

# for now, we'll always force polling as it's more robust
# than relying on platform-specific file monitoring mechanisms
# (e.g., inotify, which isn't supported by qemu as of feb 2023)
FORCE_POLLING="1"

# extract bundler version from Gemfile.lock
# as docker needs to know it to build the image
BUNDLER_VERSION=$( grep -A1 'BUNDLED WITH' Gemfile.lock | tail -n 1 )

# build the image using the project root as context.
# if that succeeds, move on to running it
# (we echo the build arg to exploit echo stripping leading whitespace)
docker build ${PLATFORM} \
    -t ${IMAGE} \
    --build-arg BUNDLER_VERSION=$( echo ${BUNDLER_VERSION} ) \
    -f ./.docker/Dockerfile . && \
${DOCKER_RUN_CMD} --name ${CONTAINER_NAME} ${PLATFORM} \
    --init \
    --rm -it \
    -p 4000:4000 \
    -p 35729:35729 \
    -v $PWD:/usr/src/app \
    -e FORCE_POLLING="${FORCE_POLLING:-0}" \
    ${IMAGE} "$@"
