# start with official ruby docker image as base
FROM ruby:3.1.2

# set working directory within container
WORKDIR /usr/src/app

# pull in ruby (jekyll) and python (cite process) package info
COPY Gemfile Gemfile.lock ./_cite/requirements.txt .

# command to get bundler version
ARG BUNDLER="grep -A 1 'BUNDLED WITH' Gemfile.lock | tail -n 1 | xargs"

# install ruby bundler
RUN gem install bundler --version $(eval ${BUNDLER})

# install ruby packages
RUN bundle _$(eval ${BUNDLER})_ install

# install python
RUN apt update && apt install -y python3 python3-pip

# install python packages
RUN python3 -m pip install --upgrade --requirement requirements.txt

# install python package for listening for file changes
RUN pip install "watchdog[watchmedo]"

# ports used by jekyll
EXPOSE 4000
EXPOSE 35729

# run jekyll and cite process
CMD [ ".docker/entrypoint.sh" ]
