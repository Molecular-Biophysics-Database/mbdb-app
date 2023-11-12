#!/bin/bash

set -e

curl -sSL https://pdm-project.org/install-pdm.py | python - -p /tmp/pdm

export PATH=$PWD:/tmp/pdm/bin:$PATH

echo "use_docker: false" > .oarepo-user.yaml

set

# nrp upgrade
nrp build

nrp invenio db init
nrp invenio db create
nrp invenio index init
nrp oarepo cf init
nrp oarepo fixtures load
nrp invenio files location create --default default file:////tmp/data
nrp oarepo fixtures load --no-system-fixtures ../../sample_data/mst

nrp invenio users create --password 123456 -a -c test@test.com
TOKEN=$(nrp invenio tokens create -n test -u test@test.com)

nrp run 2>&1 | tee nrp-server.log &
NRP_SERVER_PID=$!

trap "kill $NRP_SERVER_PID" EXIT

sleep 20

curl --retry-max-time 120 -k -H "Authorization: Bearer $TOKEN" -X GET https://127.0.0.1:5000/api/mbdb-mst
