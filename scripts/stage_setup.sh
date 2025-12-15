#!/bin/bash
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Password setup
if [ -z "${USERS_PASSWORD:-}" ]; then
  echo -e "${RED}ERROR: USERS_PASSWORD is not set${NC}" >&2
  echo -e "${CYAN}--- User Password Setup ---${NC}"
  echo -e "Please enter the password for default users (reviewer, editor, administrator):"

  while true; do
    read -r -s -p "Password: " USERS_PASSWORD; echo
    read -r -s -p "Confirm password: " USERS_PASSWORD_CONFIRM; echo

    [ -n "$USERS_PASSWORD" ] || { echo -e "${RED}Password cannot be empty.${NC}"; continue; }
    [ "$USERS_PASSWORD" = "$USERS_PASSWORD_CONFIRM" ] || { echo -e "${RED}Passwords do not match. Try again.${NC}"; continue; }
    break
  done

  export USERS_PASSWORD
fi

DOMAIN="email.cz"
METHODS=(mst bli spr itc mp)
ROLES=(reviewer editor administrator)

add_role() {
  local email="$1"
  local role="$2"

  if ! err=$(invenio roles add "$email" "$role" 2>&1 >/dev/null); then
    # Make this tolerant: treat "already" as skip, otherwise fail hard.
    if echo "$err" | grep -qiE "already|exists"; then
      echo -e "${YELLOW}Role '$role' already assigned (or exists) for '$email'. Skipping.${NC}"
    else
      echo -e "${RED}FATAL ERROR assigning role '$role' to '$email':${NC}" >&2
      echo -e "${RED}$err${NC}" >&2
      exit 1
    fi
  else
    echo -e "${GREEN}Role '$role' assigned to '$email'.${NC}"
  fi
}

create_role_if_missing() {
  local role="$1"
  if ! err=$(invenio roles create "$role" 2>&1 >/dev/null); then
    if echo "$err" | grep -qiE "already|exists"; then
      echo -e "${YELLOW}Role '$role' already exists. Skipping.${NC}"
    else
      echo -e "${RED}FATAL ERROR creating role '$role':${NC}" >&2
      echo -e "${RED}$err${NC}" >&2
      exit 1
    fi
  else
    echo -e "${GREEN}Created role '$role'.${NC}"
  fi
}

echo -e "${CYAN}--- Creating method-specific roles ---${NC}"
for method in "${METHODS[@]}"; do
  create_role_if_missing "reviewer_$method"
done

echo -e "${CYAN}--- Creating users and profiles ---${NC}"

for method in "${METHODS[@]}"; do
  EMAIL="mbdb_reviewer_${method}@${DOMAIN}"
  FULL_NAME="Reviewer ${method^}"
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

  add_role "$EMAIL" "reviewer_$method"
  add_role "$EMAIL" "reviewer"
done

for role in "${ROLES[@]}"; do
  EMAIL="mbdb_${role}@${DOMAIN}"
  FULL_NAME="${role^}"
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

echo -e "${CYAN}--- Assigning base roles ---${NC}"
for role in "${ROLES[@]}"; do
  add_role "mbdb_${role}@${DOMAIN}" "$role"
done

echo -e "${CYAN}--- Granting administration access ---${NC}"
if ! err=$(invenio access allow administration-access role administrator 2>&1 >/dev/null); then
  if echo "$err" | grep -qiE "already|exists"; then
    echo -e "${YELLOW}Administrator already has administration-access assigned. Skipping.${NC}"
  else
    echo -e "${RED}FATAL ERROR granting administration-access:${NC}" >&2
    echo -e "${RED}$err${NC}" >&2
    exit 1
  fi
else
  echo -e "${GREEN}Granted administration-access to role 'administrator'.${NC}"
fi

echo -e "${CYAN}--- Script finished successfully ---${NC}"
