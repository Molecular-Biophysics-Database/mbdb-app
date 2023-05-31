# MBDB

## Local UI development

### Prerequisites

* git
* python 3.9+
* docker
* pipenv (optional)
* direnv (optional)

### Local bootstrap

```bash
mkdir mbdb
cd mbdb
git clone https://github.com/Molecular-Biophysics-Database/mbdb-app.git
cd mbdb-app
./scripts/bootstrap_docker_development.sh
```

### Running development application inside docker

#### First run

During the first run, docker image will be created.

*Note:* you need to run it this way whenever you change requirements in Pipfile

If you have pipenv installed
```bash
./nrp-cli develop
```

If not (will reuse the previously generated requirements)
```bash
./nrp-cli develop --no-rebuild-requirements
```

#### Subsequent runs

To speed up subsequent runs, call

```bash
./nrp-cli develop --no-rebuild
```

### Using the docker image

When the docker image is running, wait until the UI
has finished rebuilding (this will happen two times - once
during a full rebuild and second time during assets watch).

Then the server should be up and web accessible at https://localhost:5000

The docker container accepts the following user commands:

`server<enter>` - restarts the python server
`ui<enter>` - rebuilds the ui from scratch
`build<enter>` - restarts the python server and rebuilds the ui

The docker container waits for any changes to source files
and rebuilds the UI on the fly (if you change css, javascript, templates),
just reload the page.

If you get manifest error during reload, wait a few seconds and try again.

## Initial data

The repository is currently set to be without authentication.
To import a record via API, call:

```bash
curl -k -X POST \
     -H "content-type: application/json" \
     https://localhost:5000/api/mbdb-mst/ \
     -d @data/mst_test_001.json
```

## Directory structure

| Directory       | Comment                               |
|-----------------|---------------------------------------|
| `data/*`          | sample data files                     |
| `scripts/*`       | various scripts                       |
| `models/mbdb-mst` | The mst model, including translations |
| `sites/mbdb-site` | The main site (including styles, homepage, model-agnostic stuff |
| `ui/mst-ui` | Implementation of UI for MST model |

## Important files

## sites/mbdb-site/assets/less

This directory contains the global configuration.
Here you can change the look and feel of semantic-ui
components and the overall CSS.


| File                          | Usage                                                                                       |
|-------------------------------|---------------------------------------------------------------------------------------------|
| `theme.config`                | defines skin of semantic ui componets                                                       |
| `theme.less`                  | helper file that defines order of `less` imports and location of user components and styles |
| `site/globals/site.variables` | top-level variables, such as colors                                                         |
| `site/globals/site.overrides` | overrides the CSS style, can use the variables defined in site.variables                    |
| `site/css.overrides`          | This overrides the styling of components, not the whole page                                |

## sites/mbdb-site/site/mbdb_site/templates/semantic-ui

The base templates are defined in invenio-theme package. See
https://github.com/inveniosoftware/invenio-theme/blob/7893ec0cac832fbde16ee85881d0f16feccfadf3/invenio_theme/templates/semantic-ui/invenio_theme/page.html
for page blocks

| File                       | Usage                                                    |
|----------------------------|----------------------------------------------------------|
| `mbdb-site/frontpage.html` | jinja template for the front page                        |
| `oarepo-ui/detail.html`    | generic detail page, blocks are filled in ui application |


## ui/mst-ui/templates/semantic-ui

Templates for MST pages

| File                                   | Usage                                                     |
|----------------------------------------|-----------------------------------------------------------|
| `mst_ui/search.html`                   | page for searching in MST (https://localhost:5000/mst/)   |
| `mst_ui/main.html`                     | main part of the record detail page                       |
| `mst_ui/sidebar.html`                  | sidebar of the record detail page (for links and similar) |
| `oarepo_ui/components/100-macros.html` | jinja macros used in main & sidebar                       |

To get an inspiration, see https://github.com/Narodni-repozitar/nr-docs/tree/main/ui/docs-app/docs_app/templates/semantic-ui

## ui/mst-ui/theme

### webpack

Webpack defines which javascript/css files will be built for the search & edit & detail applications.

### Custom Jinja components

Custom jinja components are in `assets/semantic-ui/less/mst_ui`. Just now the folder contains just a sample component. For a real life example, see  custom components defined for https://github.com/Narodni-repozitar/nr-docs/tree/main/ui/docs-app/docs_app/theme/assets/semantic-ui/less/docs_app

Note: each component created here **MUST** be registered in
`sites/mbdb-site/assets/less/theme.config`

## ui/mst-ui/theme/assets/semantic-ui/js/mst_ui/search

Source files of MST search.

### .../components/ResultListItem.jsx

This defines a single search result, how it is diplayed in the list.
The main part is `ResultsListItemComponent` which defines
the UI of a single component.

Feel free to create small components for different parts of the result item,
see https://github.com/Narodni-repozitar/nr-docs/tree/main/ui/docs-app/docs_app/theme/assets/semantic-ui/js/docs_app/search/components
for a real world example


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
scripts/generator/, however it should be done to make it easier to see
how a given model was build.


### Creating the model schema

The schema needs to adhere to certain standards and converted to a
representation compatible with the nrp-cli tools. The details of how to do this
can be found in the [mdbd-model](https://github.com/Molecular-Biophysics-Database/mbdb-model).

The oarepo type schema should be placed in the mbdb-app/scripts/generator/.
Again, this is not strictly necessary to build a model, however it does make it
easier to see how a given model was build.

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
        "index.mapping.total_fields.limit": 2000,
        "index.mapping.nested_fields.limit": 200
    },
```

The model is now installed and reachable trough API after invoking a
`./nrp-cli develop` as described above.
