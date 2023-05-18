#!/bin/bash

python3 --version
docker --version

cd `dirname $0`/..

test -d .venv || mkdir .venv
test -d .venv/nrp-cli || (
  python3 -m venv .venv/nrp-cli
  .venv/nrp-cli/bin/pip install -U setuptools pip wheel
)
.venv/nrp-cli/bin/pip install oarepo-cli --no-cache-dir
