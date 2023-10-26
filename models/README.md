# `models` folder

Contains generated models.

## Installing and updating models

All Installation commands should be issued from the top level folder of app

### Creating model schemas

The schema needs to adhere to certain standards and converted to a
representation compatible with the nrp tools. The details of how to do this
can be found in the [mdbd-model](https://github.com/Molecular-Biophysics-Database/mbdb-model).


## Creating models

```bash
nrp model add <model-name> --config <custom config> \
  --use <custom model>[:<jsonpath>] \
  --no-input
```

Will create a new model. You can provide your own oarepo.yaml (see example below)
config for the model via the --config option (to get the format,
run the command without --config, answer all the questions
and then copy the model part of the oarepo.yaml to your own file)

You can also include a custom model. The file will be copied
to the destination and referenced from the generated model file.
If no path is specified, it will be referenced from the root
of the file, with path the reference will be put there.

Use `--no-input` to disable asking questions (and be sure to
run it with `--config`)

#### oarepo.yaml model config example

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
use_drafts: 'yes'
use_files: 'no'
use_relations: 'yes'
use_requests: 'no'
use_vocabularies: 'yes'
pid_type: xxx                          <--

```
## Compiling models

```bash
nrp model compile <model-name>
```

This command will compile your model into invenio sources.


If marshmallow raises errors about unknown properties, make sure that the custom
data types are installed:

```bash
.venv/oarepo-model-builder/bin/pip install -U 'oarepo-model-builder-ui>=4.0.0' oarepo-model-builder-polymorphic
```

## Installing models

```bash
nrp model install <model-name> [<site-name>]
```

Will install the model into the given site. Site name
can be omitted if there is only one site in the monorepo.


## Uninstalling models

```bash
nrp model uninstall <model-name> [<site-name>] [--remove-directory]
```

Will uninstall the model from the given site. Site name
can be omitted if there is only one site in the monorepo.
