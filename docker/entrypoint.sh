#!/bin/bash

# run citation generator
watchmedo shell-command \
    --command='python3 /usr/src/app/auto-cite/auto-cite.py' \
    ./_data/sources.yaml &

# serve the site in hot-reload mode forever
bundle exec jekyll serve --host=0.0.0.0 --livereload --trace
