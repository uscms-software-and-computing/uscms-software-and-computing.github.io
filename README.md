# USCMS Software & Computing Website Source

This repository is for the US CMS Software & Computing website.

Changes can be made by performing a pull request from this repository.

# Testing pages locally

You can test your changes out using the Jekyll docker image:
```bash
docker run --rm -it \
      --volume="$PWD:/srv/jekyll"  \
      -p 4000:4000 \
      jekyll/builder:stable jekyll serve --incremental
```
*Note* - you need to run the command from the top-level of your local repo.

This will mount your checked out copy of this repo, then build and start the
jekyll server mapping it to port 4000 on your computer. You can make changes
locally and view them at http://localhost:4000
