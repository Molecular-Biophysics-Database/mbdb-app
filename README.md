# Molecular Biophysics Database

Security note! Running an instance of the MBDB as described below is suitable for local development.
**IT SHOULD NOT BE USED IN PRODUCTION**. Use a WSGI server for that.

## Repository layout

The repository contains the following files and directories:

- `oarepo.yaml` - the main configuration file for the repository
- `pyproject.toml` - python dependencies and plugins
- `site` - directory with the site sources, including styles, images, fonts, and docker files
- `ui` - directory containing the UI sources, such as title page, search page, record detail page, etc.
  - `ui/branding` - branding information, including colors, logo, favicon etc.
- `models` - directory containing the metadata schemas
- `tests` - directory containing tests for the repository
- `shared` - directory with shared code, local implementation etc.
- `nrp` - the nrp command line tool

The following files/directories are generated automatically
and should not be modified:

- `<modelname>` - one or more directories containing generated code for the models
- `.venv` - virtual environment for the repository
- `.venv-*` - additional virtual environments for tools

## Basic commands

### Checking requirements

To check that the requirements are met, type:

```bash
nrp check
```

This will check that all the requirements are met
and the repository can be run. If there are any errors,
they will be reported and the command will exit with
a non-zero exit code.

To fix the problems, run the command with '--fix' option:

```bash
nrp check --fix
```

### Running the repository in development mode

To run the repository in development mode, type:

```bash
nrp develop --extra-library <path-to-library>
```

This will check the prerequisites, start the docker containers,
install the python dependencies, compile UI and start the development
server. The UI will be available at https://127.0.0.1:5000, the API
at https://127.0.0.1:5000/api

If `extra-library` parameter is given, this library will be installed
in an editable mode to the repository's virtual environment. You can
repeat this parameter multiple times to install multiple libraries.

Removal of extra libraries can be done by:

- calling `nrp build` or `nrp upgrade` commands
- removing the `.venv` directory and calling `nrp develop` again

After the first run of `nrp develop`, you can speed up the subsequent
runs by adding `--skip-checks` commandline option.

### Building the repository for production

```bash
nrp build
```

This will build the repository for production. It will check that
the python dependencies are up to date (to skip the check, run
`nrp build --skip-checks`). It will also clear the virtual environment
and reinstall all the dependencies before building the repository.

### Running the repository in production mode

To run the repository in production mode, type:

```bash
nrp run
```

This will just run the repository, depending on it having been built
beforehand. If the repository has not been built, it will fail.

In production mode, python/js sources are not watched for changes,
and the UI is build beforehand with minification and optimizations.

### Creating production images

To create a production image, type:

```bash
nrp image <image-name> <image-tag> <image-tag>
```

This will create a production image with the given name and tags.
The production image will be based on the `oarepo:oarepo-base-production:<invenio-version>`.
The image will be tagged with the given tags and also with the
`<image-name>:latest` tag.

This steps expects that the repository has been built beforehand.
If not it will fail.

Note: the image will not be pushed to the registry. To push the image
to the registry, use the `docker push` command.

### Testing the repository

To run test scenarios (integration API tests and UI tests), type:

```bash
nrp test
```

This command will create new containers, run the API tests and UI tests
within the docker then destroy the database. If any of the tests fail,
it will report the failure and exit with a non-zero exit code.

The command expects the repository to be built beforehand. If not, it
will fail.

### Upgrading dependencies of the repository

Run the following command to upgrade the dependencies of the repository:

```bash
nrp upgrade
```

This will upgrade the dependencies of the repository to the latest
versions (python and node dependencies). After this it will run the
build via `nrp build --production` and `nrp test` to make sure that
the dependencies will build.

## Handling models

### Creating new models

To create a new model, type:

```bash
nrp model create <model-name>
```

The command will ask a couple of questions and will create
`<model-name>.yaml` file in the `models` directory.
Please edit the file to add the fields and other information
about the model.

### Compiling and installing the model

To compile the model, type:

```bash
nrp model compile <model-name>
```

This will compile the model and generate python code for it.
The generated sources and entrypoints are placed in the
`<model-name>` directory and to `pyproject.toml` file.

Alembic migrations will be generated (this requires that the containers
are running - run `nrp develop` or `nrp check` before running this command).

After the model is compiled, run `nrp develop` and check that the
model is working correctly under the `/api` endpoint.

## Handling UI

### build Tailwind CSS

```bash
./compileTailwind.sh --watch
```

### Creating UI pages for models

To create UI pages for a model, type:

```bash
nrp ui model create --model <model-name> <ui-name>
```

The `ui-name` is optional, if not specified, it will be the same
as the `model-name`. The command will ask a couple of questions
and will create jinjax templates and react pages for displaying
a listing of the model, a detail page and a form for creating
and editing the model.

### Creating UI pages for custom endpoints

To create UI pages for a custom endpoint, type:

```bash
nrp ui page create <page-name> <page-endpoint>
```

The `page-endpoint` is the endpoint of the page, for example
`/about` or `/search`. The `page-name` is the name of the page,
for example `about` or `search`.

If `page-endpoint` is not specified, it will be the same as
`page-name`.

The command will create a jinjax template for the page and register
the page to the flask application.

If you run the command with `--react` option, it will also create
react endpoint for the page and reference it from the jinjax template.

### Useful commands

These should run using the invenio installation from the .venv:

```bash
source .venv/bin/activate
```

```bash
invenio db destroy --yes-i-know
invenio db init
invenio db create

invenio index destroy --yes-i-know
invenio index init

invenio oarepo cf init

invenio files location create --default default s3://default

invenio oarepo fixtures load

invenio oarepo fixtures load --no-system-fixtures sample_data/mst

# for reindexing the whole repo
invenio oarepo index reindex
```

## UI development

1. run `./nrp develop`

## Installation from scratch (models etc.)

Recommendation: run outside of docker for this

**Note:** different database migrations might be generated. If you already have some data that need to be kept,
backup the contents of alembic directory and restore it after model compile.

1. remove the containers as they might be incompatible
2. remove .nrp, .venv
3. remove requirements.txt to get rid of cached requirements
4. if you added your custom configuration to invenio.cfg, comment it out temporarily.
5. run `./nrp build` - should not fail as it will skip the not-found directories
6. call `./nrp develop`, wait for the server to start up (you might want to check that homepage can be opened)
   and shut it down. This will create the database and initialize all the containers
7. clone mbdb model inside the same directory where the app is
8. copy `../mbdb-model/models/oarepo/*.yaml` to the models folder
9. call `./nrp model compile mst`. If you've saved alembic, put it back now into the generated sources
10. call `invenio oarepo fixtures load` to load the fixtures contained in `common/fixtures`
11. call `invenio oarepo fixtures load sample_data/mst` to import sample data for mst
12. call `./nrp develop` and have a look at `https://127.0.0.1:5000/api/records/mst`

## Setting up ORCID authentication

1. Create an ORCID user account - https://orcid.org/register (it's free of charge)
2. Register a public API https://info.orcid.org/documentation/integration-guide/registering-a-public-api-client/
3. Add your domain(s) to list of the redirect URIs:
   1. If you're only running locally, add https://127.0.0.1:5000/oauth/authorized/orcid/
4. Register the public API credentials in the mbdb-app:
   1. create `~/.envrc.local`
   2. put the following lines into it:
   ```
    export INVENIO_ORCID_APP_KEY='changeme'
    export INVENIO_ORCID_APP_SECRET='changeme'
   ```
   Change the 'changeme' to the ORCID public APIs Client ID and Client secret, respectively

# REST API

```bash
# create user
> invenio users create --password 123456 -a -c test.user@fake.no

{'email': 'test.user@fake.no', 'password': '****', 'active': True, ...}


# get token
> export REPOTOKEN=$(invenio tokens create -n resttest -u test.user@fake.no); echo $REPOTOKEN

BtMgKKIxJl838fN25PHRQtacuTJwTan0GYvDbXDB7PXoPYSHcugjZSrXQu6Y

# create a sample record
> curl -k -XPOST -H "Authorization: Bearer $REPOTOKEN" \
  -H "Content-Type: application/json" \
  -d "$(jq '.[0]' sample_data/mst/MST.json)" \
  https://127.0.0.1:5000/api/records/mst/

{"links": {
  "draft": "https://127.0.0.1:5000/api/records/mst/zv0gv-btp27/draft",
  "files": "https://127.0.0.1:5000/api/records/mst/zv0gv-btp27/draft/files"
}...


# try to get the draft (note draft url)
> curl -k -H "Authorization: Bearer $REPOTOKEN" \
   https://127.0.0.1:5000/api/records/mst/zv0gv-btp27/draft

{ok json}

# try to list drafts (currently these are "user" files, that's why "user" is in the path)
> curl -k -H "Authorization: Bearer $REPOTOKEN" \
   https://127.0.0.1:5000/api/user/mbdb-mst/

{ok json}


# get the files section, note there are none at the moment
> curl -k -H "Authorization: Bearer $REPOTOKEN" \
   https://127.0.0.1:5000/api/records/mst/zv0gv-btp27/draft/files

{"enabled": true, "links": {"self": "zv0gv-btp27/draft/files"}, "entries": [], "default_preview": null, "order": []}


# start creating a file - in this step, just send
# a list of file names that will be later uploaded
> curl -k -XPOST -H "Authorization: Bearer $REPOTOKEN" \
  -H "Content-Type: application/json" \
  -d '[{"key": "blah.txt"}]' \
  https://127.0.0.1:5000/api/records/mst/zv0gv-btp27/draft/files

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
  https://127.0.0.1:5000/api/records/mst/zv0gv-btp27/draft/files/blah.txt/content

# add the file metadata
> curl -k -XPUT -H "Authorization: Bearer $REPOTOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "blah"}' \
  https://127.0.0.1:5000/api/records/mst/zv0gv-btp27/draft/files/blah.txt

{"metadata": {"name": "blah"}, "status": "pending", ...}

# commit the changes - the file with all metadata will get created at this point
> curl -k -XPOST -H "Authorization: Bearer $REPOTOKEN" \
  https://127.0.0.1:5000/api/records/mst/zv0gv-btp27/draft/files/blah.txt/commit
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
