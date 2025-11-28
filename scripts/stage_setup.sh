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

    invenio users create -a -c "$EMAIL" --password "$DUMMY_PASSWORD" --profile "$PROFILE_JSON" &

done

wait

for role in "${ROLES[@]}"; do
    EMAIL="${role}@mbdb.org"
    invenio roles add "$EMAIL" "$role" &
    invenio access allow administration-access role "$role" &
done

wait
