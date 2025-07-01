#!/bin/bash

invenio alembic upgrade heads
$(dirname "$0")/initialize_communities.sh