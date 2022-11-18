#!/bin/bash

# run citation generator
watchmedo shell-command \
    --command='python3 /usr/src/app/auto-cite/auto-cite.py' \
    ./_data/sources.yaml &

# serve the site in hot-reload mode forever.
# reboot server whenever _config.yaml changes, as that's the only
# thing jekyll can't hot-reload when it's modified
watchmedo auto-restart --pattern='./_config.yaml' --signal SIGTERM \
    -- bundle exec jekyll serve --host=0.0.0.0 --livereload --trace
