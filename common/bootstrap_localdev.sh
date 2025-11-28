#!/bin/bash
# Script to populate roles in localdev.

set -e
set -x

ROLES=(reviewer editor administrator)

for role in "${ROLES[@]}"; do
    if invenio roles create "$role" 2>/dev/null; then
        echo "Created role '$role'"
    else
        echo "Role '$role' already exists. Skipping."
    fi
done

# Run stage setup script afterwards
bash "$(dirname "$0")/../scripts/stage_setup.sh"
