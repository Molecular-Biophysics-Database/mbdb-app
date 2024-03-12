#!/bin/bash

set -e

curl -sSL https://pdm-project.org/install-pdm.py | python - -p /tmp/pdm

export PATH=$PWD:/tmp/pdm/bin:$PATH
#which python
export PYTHON=/opt/hostedtoolcache/Python/3.10.13/x64/bin/python

echo "use_docker: false" > .oarepo-user.yaml

set

ls --all

nrp upgrade
# nrp build

source .venv/bin/activate

invenio db init
invenio db create
invenio index init
nrp oarepo cf init
invenio fixtures load
invenio files location create --default default file:////tmp/data
invenio fixtures load --no-system-fixtures ../../sample_data/mst

invenio users create --password 123456 -a -c test@test.com
TOKEN=$(nrp invenio tokens create -n test -u test@test.com)

nrp run 2>&1 | tee nrp-server.log &
NRP_SERVER_PID=$!

trap "kill $NRP_SERVER_PID" EXIT

sleep 20

curl --retry-max-time 120 -k -H "Authorization: Bearer $TOKEN" -X GET https://127.0.0.1:5000/api/mbdb-mst/
