#!/bin/bash

set -e

pth=$(readlink -f $(dirname $0))
echo "Source data for installation are in $pth"

if [ a"$NR_DOCS_DIR" == "a" ] ; then
  NR_DOCS_DIR="$pth/../.."
fi

echo "Will create nr documents at $NR_DOCS_DIR"

# rm -rf "$NR_DOCS_DIR"

curl https://raw.githubusercontent.com/oarepo/oarepo-cli/v11.0/nrp-installer.sh > nrp-installer.sh
chmod 755 nrp-installer.sh

# -- directory and site
( 
  cd $(dirname $NR_DOCS_DIR)
  $pth/nrp-installer.sh app --config $pth/mbdb-repository-site.yaml --no-input $@ 
)

exit 0

# -- data model
(
  cd $NR_DOCS_DIR
  ./nrp-cli model add mbdb-mst --merge $pth/mst-repository-schema.yaml=model.yaml --no-input --config $pth/mst-repository-model.yaml
  ./nrp-cli model compile mbdb-mst --no-input
  ./nrp-cli model install mbdb-mst --no-input
)


# -- vocabulary patch
# this is problem with vocabularies - their indices has not been created as when site (and indices) are created,
# vocabularies are not installed yet. Moreover invenio index init can not ignore existing indices.
# do need to wipe them and recreate.
# fortunately at this point the indices are empty

( 
  cd $NR_DOCS_DIR/sites/uct-repository
  pipenv run invenio index destroy --yes-i-know
  pipenv run invenio index init 
  # create custom fields for hierarchies
  pipenv run invenio oarepo cf init  
)

# -- installing fixtures - TODO: should be part of nr-cli
( 
  cd $NR_DOCS_DIR/sites/uct-repository 
  pipenv run invenio oarepo fixtures load
)


# ui
# (
#   cd $NR_DOCS_DIR
#   ./nrp-cli ui add docs-app --config $pth/ui.yaml --no-input
# )
