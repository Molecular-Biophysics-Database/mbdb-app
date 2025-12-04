#!/bin/bash
# Script to create users, assign system roles, and grant administration access to administrator.
# Requires the environment variable $USERS_PASSWORD to be set before running.

set -e

# --- ANSI Color Codes ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'
# ------------------------

if [ -z "$USERS_PASSWORD" ] ; then
  echo -e "${RED}ERROR: USERS_PASSWORD is not set${NC}" >&2
  exit 1
fi

DOMAIN="mbdb-data.org"
ROLES=(reviewer editor administrator)

# Create users (skip if they already exist)
echo -e "${CYAN}--- Creating users and profiles ---${NC}"
for role in "${ROLES[@]}"; do

    EMAIL="${role}@${DOMAIN}"

    if [[ "$role" == "administrator" ]]; then
        FULL_NAME="Administrátor"
    else
        FULL_NAME="${role^}"
    fi

    PROFILE_JSON="{\"full_name\": \"$FULL_NAME\"}"

    if ! ERROR_OUTPUT=$(invenio users create -a -c "$EMAIL" --password "$USERS_PASSWORD" --profile "$PROFILE_JSON" 2>&1 >/dev/null); then
        if echo "$ERROR_OUTPUT" | grep -q "already associated with an account"; then
            echo -e "${YELLOW}User '$EMAIL' already exists. Skipping.${NC}"
        else
            echo -e "${RED}FATAL ERROR creating user '$EMAIL':${NC}" >&2
            echo -e "${RED}$ERROR_OUTPUT${NC}" >&2
            exit 1
        fi
    else
        echo -e "${GREEN}User '$EMAIL' created successfully.${NC}"
    fi

done

# Assign each user their role
echo -e "${CYAN}--- Assigning roles ---${NC}"
for role in "${ROLES[@]}"; do
    EMAIL="${role}@${DOMAIN}"
    invenio roles add "$EMAIL" "$role" 2>/dev/null || echo -e "${YELLOW}Role '$role' already assigned to '$EMAIL'. Skipping.${NC}"
done

# Allow administration access to the admin role
echo -e "${CYAN}--- Granting administration access ---${NC}"
invenio access allow administration-access role administrator 2>/dev/null || \
    echo -e "${YELLOW}Administrator already has administration-access assigned. Skipping.${NC}"

echo -e "${CYAN}--- Script finished successfully ---${NC}"