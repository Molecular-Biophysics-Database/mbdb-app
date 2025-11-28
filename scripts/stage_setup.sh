#!/bin/bash
#
# Script to create users, assign system roles, and grant admin access.
#

set -e
set -x

if [ -z "$USERS_PASSWORD" ] ; then
  echo "USERS_PASSWORD is not set"
  exit 1
fi

ROLES=(reviewer editor administrator)


for role in "${ROLES[@]}"; do

    EMAIL="${role}@mbdb.org"

    if [[ "$role" == "administrator" ]]; then
        FULL_NAME="Administrátor"
    else
        FULL_NAME="${role^}"
    fi

    PROFILE_JSON="{\"full_name\": \"$FULL_NAME\"}"

    if ! invenio users create -a -c "$EMAIL" --password "$USERS_PASSWORD" --profile "$PROFILE_JSON" 2>err.out; then
        if grep -q "already associated with an account" err.out; then
            echo "User '$EMAIL' already exists. Skipping."
        else
            echo "Error creating user '$EMAIL':"
            cat err.out
            exit 1
        fi
    fi

done

# ------------------------------------------------------
# Assign each user their role
# ------------------------------------------------------
for role in "${ROLES[@]}"; do
    EMAIL="${role}@mbdb.org"
    invenio roles add "$EMAIL" "$role" || echo "Role '$role' already assigned to '$EMAIL'. Skipping."
done

# ------------------------------------------------------
# Allow administration access to the admin role
# ------------------------------------------------------
invenio access allow administration-access role administrator || \
    echo "administrator already has administration-access assigned."
