#! /bin/bash

# go to root dir
cd $(dirname $0) 
cd ..

# build image
CDT=$(date -Iseconds -u | sed 's/+.*//' | tr ':' '-')
docker build . -f sites/mbdb-site/docker/Dockerfile.production -t mbdb-app:latest  \
  --build-arg REPOSITORY_SITE_NAME="mbdb-site" \
  --build-arg REPOSITORY_SITE_ORGANIZATION="mbdb-site" \
  --build-arg REPOSITORY_IMAGE_URL="https://apps.du.cesnet.cz/mbdb-app" \
  --build-arg REPOSITORY_AUTHOR="Emildandanell.agerschou@ibt.cas.cz" \
  --build-arg REPOSITORY_GITHUB_URL="https://github.com/Molecular-Biophysics-Database/mbdb-app" \
  --build-arg REPOSITORY_URL="https://mbdb.test.du.cesnet.cz" \
  --build-arg REPOSITORY_DOCUMENTATION="https://mbdb.test.du.cesnet.cz" \
  --compress \
  --force-rm 