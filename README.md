# mbdb-app
Security note! Running an instance of the MBDB as described below is suitable for local development.
**IT SHOULD NOT BE USED IN PRODUCTION**. Use a WSGI server for that.     

## Python development

1. install pdm - <https://pdm.fming.dev/latest/#recommended-installation-method>
2. make sure you have node 14/16, python 3.9/3.10 active
3. run `nrp develop`, say that you do not want to run it inside docker

### Useful commands

```bash
nrp invenio db destroy --yes-i-know
nrp invenio db init
nrp invenio db create

nrp invenio index destroy --yes-i-know
nrp invenio index init

nrp oarepo cf init

nrp invenio files location create --default default s3://default

nrp oarepo fixtures load

nrp oarepo fixtures load --no-system-fixtures ../../sample_data/mst

# for reindexing the whole repo
nrp oarepo index reindex
```

## UI development

1. run `nrp develop` and agree running it inside docker

## Installation from scratch (models etc.)

Recommendation: run outside of docker for this

**Note:** different database migrations might be generated. If you already have some data that need to be kept,
backup the contents of alembic directory and restore it after model compile.

1. remove the containers as they might be incompatible
2. remove .venv, sites/mbdb-site/.venv (just to be sure there are no obsolete packages)
3. remove all the models inside the models directory (and back up and remove all the uis)
4. remove requirements.txt to get rid of cached requirements
5. if you added your custom configuration to invenio.cfg, comment it out temporarily.
6. run `nrp build` - should not fail as it will skip the not-found directories
7. call `nrp develop`, wait for the server to start up (you might want to check that homepage can be opened)
   and shut it down. This will create the database and initialize all the containers
8. clone mbdb model inside the same directory where the app is
9. call `nrp model add mbdb-mst --use ../mbdb-model/models/oarepo/MST.yaml`
10. call `nrp model compile mbdb-mst`. If you've saved alembic, put it back now into the generated sources
11. call `nrp model install mbdb-mst`
12. call `nrp oarepo fixtures load` to load the fixtures contained in `local/mbdb-common/mbdb_common/fixtures`
13. call `nrp oarepo fixtures load --no-system-fixtures $PWD/sample_data/mst` to import sample data for mst
    (note: nrp runs the command internally inside the site directory, so need to use $PWD or ../.. here)
14. call `nrp develop` and have a look at `https://127.0.0.1:5000/api/mbdb-mst`

## Setting up ORCID authentication

1. Create an ORCID user account - https://orcid.org/register (it's free of charge)
2. Register a public API https://info.orcid.org/documentation/integration-guide/registering-a-public-api-client/
3. Add your domain(s) to list of the redirect URIs:
   1. If you're only running locally, add https://127.0.0.1:5000/oauth/authorized/orcid/
4. Register the public API credentials in the mbdb-app:
    1. in mbdb-app/sites/mbdb-site/ locate the files .env and variables 
    2. if .env is a symbolic link:
       1. delete it
       2. make a new file called .env 
       3. copy the content of the variables file to .env
    3. Inside .env, locate the following lines:
    ```
    INVENIO_ORCID_APP_KEY='changeme'
    INVENIO_ORCID_APP_SECRET='changeme'
    ``` 
    4. Change the 'changeme' to the ORCID public APIs Client ID and Client secret, respectively 
5. (.env is already in the .gitignore, so your information won't be leaked)

# REST API

```bash
# create user
> ./nrp invenio users create -a -c miroslav.simek@cesnet.cz

{'email': 'miroslav.simek@cesnet.cz', 'password': '****', 'active': True, ...}


# get token
> export REPOTOKEN=$(./nrp invenio tokens create -n resttest -u miroslav.simek@cesnet.cz); echo $REPOTOKEN

BtMgKKIxJl838fN25PHRQtacuTJwTan0GYvDbXDB7PXoPYSHcugjZSrXQu6Y

# create a sample record
> curl -k -XPOST -H "Authorization: Bearer $REPOTOKEN" \
  -H "Content-Type: application/json" \
  -d "$(jq '.[0]' sample_data/mst/MST.json)" \
  https://127.0.0.1:5000/api/mbdb-mst/

{"links": {
  "draft": "https://127.0.0.1:5000/api/mbdb-mst/zv0gv-btp27/draft", 
  "files": "https://127.0.0.1:5000/api/mbdb-mst/zv0gv-btp27/draft/files"
}...


# try to get the draft (note draft url)
> curl -k -H "Authorization: Bearer $REPOTOKEN" \
   https://127.0.0.1:5000/api/mbdb-mst/zv0gv-btp27/draft

{ok json}

# try to list drafts (currently these are "user" files, that's why "user" is in the path)
> curl -k -H "Authorization: Bearer $REPOTOKEN" \
   https://127.0.0.1:5000/api/user/mbdb-mst/

{ok json}


# get the files section, note there are none at the moment
> curl -k -H "Authorization: Bearer $REPOTOKEN" \
   https://127.0.0.1:5000/api/mbdb-mst/zv0gv-btp27/draft/files

{"enabled": true, "links": {"self": "zv0gv-btp27/draft/files"}, "entries": [], "default_preview": null, "order": []}


# start creating a file - in this step, just send 
# a list of file names that will be later uploaded
> curl -k -XPOST -H "Authorization: Bearer $REPOTOKEN" \
  -H "Content-Type: application/json" \
  -d '[{"key": "blah.txt"}]' \
  https://127.0.0.1:5000/api/mbdb-mst/zv0gv-btp27/draft/files

{"enabled": true, 
 "links": {"self": "zv0gv-btp27/draft/files"}, 
 "entries": [{"metadata": null, "status": "pending", 
              "links": {"commit": "zv0gv-btp27/draft/files/blah.txt/commit", 
              "content": "zv0gv-btp27/draft/files/blah.txt/content", 
              "self": "zv0gv-btp27/draft/files/blah.txt"}, 
              "key": "blah.txt"}]}

# upload single file in one chunk
> curl -k -XPUT -H "Authorization: Bearer $REPOTOKEN" \
  -H "Content-Type: application/octet-stream" \
  -d 'txt file content' \
  https://127.0.0.1:5000/api/mbdb-mst/zv0gv-btp27/draft/files/blah.txt/content

# add the file metadata  
> curl -k -XPUT -H "Authorization: Bearer $REPOTOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "blah"}' \
  https://127.0.0.1:5000/api/mbdb-mst/zv0gv-btp27/draft/files/blah.txt

{"metadata": {"name": "blah"}, "status": "pending", ...}

# commit the changes - the file with all metadata will get created at this point
> curl -k -XPOST -H "Authorization: Bearer $REPOTOKEN" \
  https://127.0.0.1:5000/api/mbdb-mst/zv0gv-btp27/draft/files/blah.txt/commit
{
  "metadata": {
    "name": "blah"
  },
  "version_id": "b0965ba0-2148-4d75-bcb4-7572bf34ee7b",
  "file_id": "9e57f76a-7274-4e9a-9f62-102a89638def",
  "status": "completed",
  "size": 16,
  "created": "2023-09-13T09:01:48.229176+00:00",
  "links": {
    "commit": "zv0gv-btp27/draft/files/blah.txt/commit",
    "content": "zv0gv-btp27/draft/files/blah.txt/content",
    "self": "zv0gv-btp27/draft/files/blah.txt"
  },
  "updated": "2023-09-13T09:06:57.472556+00:00",
  "key": "blah.txt",
  "bucket_id": "aa25811f-dc12-49f8-9fba-76d64e724331",
  "checksum": "md5:05b731d7a66565cbafe7380174ea80c3",
  "storage_class": "L",
  "mimetype": "text/plain"
}
```
