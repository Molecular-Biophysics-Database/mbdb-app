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


## Installing and updating models

All Installation commands should be issued from the top level folder.


### Make sure CLI tools are up to date (optional):

```bash
./nrp-hydrate
```

### Create models settings

To automatically generate models and sites a yaml file with the settings is
needed, and it should be created and placed in mbdb-app/scripts/generator/.

Apart from general settings, the model name (e.g. mst) needs to replace the `xxx`
in the three lines pointed to by the arrows

```yaml
author_email: john.doe@example.com
author_name: John Doe
installation_site: mbdb-site
model_dir: models/mbdb-xxx             <--
model_kind: empty
model_package: mbdb_xxx                <--
permissions_presets: read_only
run_tests: skip
update_opensearch: run
use_custom_fields: 'yes'
use_expandable_fields: 'no'
use_drafts: 'no'
use_files: 'no'
use_relations: 'yes'
use_requests: 'no'
use_vocabularies: 'no'
pid_type: xxx                          <--

```

Note that it's not required for the build that the settings file are placed in
scripts/generator/, however it should be done to make it easier to see how
models were build.


### Creating the model schema

The schema needs to adhere to certain standards and converted to a
representation compatible with the nrp tools. The details of how to do this
can be found in the [mdbd-model](https://github.com/Molecular-Biophysics-Database/mbdb-model).

The oarepo type schema should be placed in the mbdb-app/scripts/generator/.
Again, this is not strictly necessary to build a model, however it makes it
easier to see how models were build.

### Add model


Using the schema and the settings file from the previous two sections run:

```bash
./nrp-cli model add mbdb-xxx --merge scripts/generator/xxx-schema.yaml=model.yaml --no-input --config scripts/generator/xxx-settings.yaml

```

Note the name of the new model is the first parameter, and should match the ones
used in the settings file.

### Compile the model

Using the name of the model just generated run:

```bash
./nrp-cli model compile mbdb-xxx --no-input
```

If marshmallow raises errors about unknown properties, make sure that the custom
data types are installed:

```bash
.venv/oarepo-model-builder/bin/pip install -U 'oarepo-model-builder-ui>=4.0.0' oarepo-model-builder-polymorphic
```

### Install the model

Using the name of the model just generated run:

```bash
./nrp-cli model install mbdb-xxx --no-input
```

If an error occur during collection of installation of python packages, make
check that the files need by pip are not write protected and change permissions
accordingly.


### Change default model limits

Changes the default limits of mapping by placing following settings at the
topmost level in the json file found in models/mbdb-xxx/mbdb-xxx/records/mappings/os-v2/
(it should have a name similar to mbdb-xxx-1.0.0.json)


```json
"settings": {
        "index.mapping.total_fields.limit": 3000,
        "index.mapping.nested_fields.limit": 200
    },
```

The model is now installed and reachable trough API after invoking a
`./nrp-cli develop` as described above.
