## Debugging Locally:

```
gem install bundler jekyll
bundle install
bundle exec jekyll serve
```

## Deploying

Run the following to generate the HTML pages:

```
JEKYLL_ENV=production bundle exec jekyll build
mv _site docs
```

Then push to github.