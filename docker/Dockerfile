FROM ruby:3.1.2

ENV BUNDLER_VERSION  2.3.5

# this needs to match the 'BUNDLED WITH' version in Gemfile.lock
RUN gem install bundler:${BUNDLER_VERSION}

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle _${BUNDLER_VERSION}_ config --global frozen 1

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./

# and install deps from the Gemfile/lockfile
RUN bundle _${BUNDLER_VERSION}_ install

# add in dependencies for citeproc and watching changes (i.e., watchdog)
RUN apt update && apt install -y python3 python3-pip && \
    pip install 'watchdog[watchmedo]'
COPY ./auto-cite/requirements.txt /tmp/auto-cite/requirements.txt
RUN python3 -m pip install --upgrade --requirement /tmp/auto-cite/requirements.txt

EXPOSE 4000
EXPOSE 35729

COPY docker/entrypoint.sh /var/entrypoint.sh

# finally, run jekyll in livereload mode
CMD [ "/var/entrypoint.sh" ]
