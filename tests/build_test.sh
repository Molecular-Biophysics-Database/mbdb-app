#!/bin/bash

set -e

export NRP_USE_UV=1
export PYTHON=`which python3.12`

echo "use_docker: false" > .oarepo-user.yaml

set

./nrp upgrade

source .venv/bin/activate

invenio db init
invenio db create
invenio index init
invenio oarepo cf init
invenio oarepo fixtures load
invenio files location create --default default file:////tmp/data

MODELS=(bli mst itc spr)
for model in ${MODELS[@]}
do
    invenio oarepo fixtures load --no-system-fixtures sample_data/$model
done


invenio users create --password 123456 -a -c test@test.com
TOKEN=$(invenio tokens create -n test -u test@test.com)

./nrp run 2>&1 | tee nrp-server.log &
NRP_SERVER_PID=$!

trap "kill $NRP_SERVER_PID" EXIT

sleep 20

curl --retry-max-time 120 -k -H "Authorization: Bearer $TOKEN" -X GET https://127.0.0.1:5000/api/records/mst/
