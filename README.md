# mbdb-app

## Python development

1. install pdm - https://pdm.fming.dev/latest/#recommended-installation-method
2. make sure you have node 14/16, python 3.9/3.10 active
3. run `nrp develop`, say that you do not want to run it inside docker

### Useful commands

```bash
nrp invenio db destroy
nrp invenio db init
nrp invenio db create

nrp invenio index destroy
nrp invenio index init

nrp oarepo cf init
nrp oarepo reindex

nrp oarepo fixtures load

nrp oarepo fixtures load --no-system-fixtures ../../sample_data
```

## UI development

1. run `nrp develop` and agree running it inside docker
