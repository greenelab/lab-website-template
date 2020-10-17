start http://127.0.0.1:4000/lab-website-template/ || true
xdg-open http://127.0.0.1:4000/lab-website-template/ || true
bundle
bundle exec jekyll serve --livereload --trace
