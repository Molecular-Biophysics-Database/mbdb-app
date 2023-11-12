#!/bin/bash

set -e

export PATH=$PWD:$PATH

nrp upgrade --outside-container
nrp build

nrp invenio db init
nrp invenio db create
nrp invenio index init
nrp oarepo cf init
nrp oarepo fixtures load
nrp invenio files location create --default default file:////tmp/data
nrp oarepo fixtures load --no-system-fixtures sample_data/mst


nrp run 2>&1 | tee nrp-server.log &
NRP_SERVER_PID=$!

trap "kill $NRP_SERVER_PID" EXIT

sleep 5

curl -X https://127.0.0.1:5000/api/mbdb-mst
