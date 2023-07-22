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

## Installation from scratch (models etc.)

**Note:** different database migrations might be generated. If you already have some data that need to be kept,
backup the contents of alembic directory and restore it after model compile.

1. remove the containers as they might be incompatible
2. remove .venv, sites/mbdb-site/.venv (just to be sure there are no obsolete packages)
3. remove all the models inside the models directory (and back up and remove all the uis)
4. remove requirements.txt to get rid of cached requirements
5. if you added your custom configuration to invenio.cfg, comment it out temporarily.
6. run `nrp build` - should not fail as it will skip the not-found directories
7. clone mbdb model inside the same directory where the app is
8. call `nrp model add mbdb-mst --use ../mbdb-model/models/oarepo/MST.yaml`
9. 