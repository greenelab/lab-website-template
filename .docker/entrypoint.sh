#!/bin/bash

if [ "${FORCE_POLLING:-0}" = "1" ]; then
    echo "* enabled polling, since the runtime doesn't support notify-based mechanisms"
    WATCHMEDO_POLLING_ARG="--debug-force-polling"
    JEKYLL_POLLING_ARG="--force_polling"
else
    WATCHMEDO_POLLING_ARG=""
    JEKYLL_POLLING_ARG=""
fi

# run citation generator
watchmedo shell-command ${WATCHMEDO_POLLING_ARG} \
    --command='python3 /usr/src/app/_cite/cite.py' \
    ./_data/sources.yaml &

# serve the site in hot-reload mode forever.
# reboot server whenever _config.yaml changes, as that's the only
# thing jekyll can't hot-reload when it's modified
watchmedo auto-restart ${WATCHMEDO_POLLING_ARG} --pattern='./_config.yaml' --signal SIGTERM \
    -- bundle exec jekyll serve --host=0.0.0.0 --open-url ${JEKYLL_POLLING_ARG} --livereload --trace
