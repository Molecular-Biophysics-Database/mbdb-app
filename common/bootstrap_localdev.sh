#!/bin/bash
# Script to populate roles in localdev.
set -e
# --- ANSI Color Codes ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'
# ------------------------

unset USERS_PASSWORD

# Password Setup
if [ -z "$USERS_PASSWORD" ]; then
  echo -e "${RED}ERROR: USERS_PASSWORD is not set${NC}" >&2
  echo -e "${CYAN}--- User Password Setup ---${NC}"
  echo -e "Please enter the password for default users (reviewer, editor, administrator):"

  while true; do
    read -r -s -p "Password: " USERS_PASSWORD
    echo
    read -r -s -p "Confirm password: " USERS_PASSWORD_CONFIRM
    echo

    if [ -z "$USERS_PASSWORD" ]; then
      echo -e "${RED}Password cannot be empty.${NC}"
      continue
    fi

    if [ "$USERS_PASSWORD" != "$USERS_PASSWORD_CONFIRM" ]; then
      echo -e "${RED}Passwords do not match. Try again.${NC}"
      continue
    fi

    break
  done

  export USERS_PASSWORD
fi

echo -e "${CYAN}--- Creating system roles ---${NC}"
ROLES=(reviewer editor administrator)

# Create roles if they do not exist locally
for role in "${ROLES[@]}"; do
    if invenio roles create "$role" 2>/dev/null; then
        echo -e "${RED}Created role '$role'${NC}"
    else
        echo -e "${YELLOW}Role '$role' already exists. Skipping.${NC}"
    fi
done


# Run stage setup script afterwards
echo -e "${CYAN}--- Running stage setup (user creation) script ---${NC}"
bash -e "$(dirname "$0")/../scripts/stage_setup.sh"

echo -e "${CYAN}--- Role and User setup complete ---${NC}"
