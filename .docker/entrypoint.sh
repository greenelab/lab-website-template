#! /bin/bash

# print folder contents for debugging
echo "Contents:"
echo ""
ls
echo ""

# run jekyll serve in hot-reload mode.
# rerun whenever _config.yaml changes (jekyll hot-reload doesn't work with this file).
watchmedo auto-restart \
    --debug-force-polling \
    --patterns="_config.yaml" \
    --signal SIGTERM \
    -- bundle exec jekyll serve --open-url --force_polling --livereload --trace --host=0.0.0.0 \
    | sed 's/0.0.0.0/localhost/g' &

# run cite process.
# rerun whenever _data files change.
watchmedo shell-command \
    --debug-force-polling \
    --recursive \
    --command="python3 _cite/cite.py" \
    --patterns="_data/sources*;_data/orcid*;_data/pubmed*;_data/google-scholar*" \
