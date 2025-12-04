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

echo -e "${CYAN}--- User Password Setup ---${NC}"
echo -e "Please enter the password to be used for the default users (reviewer, editor, administrator):"

# Read the password without displaying it (silent mode: -s)
read -r -s USERS_PASSWORD

echo

# Check if the user entered anything
if [ -z "$USERS_PASSWORD" ]; then
    echo -e "${RED}ERROR: Password cannot be empty. Exiting.${NC}" >&2
    exit 1
fi

export USERS_PASSWORD
echo -e "${CYAN}USERS_PASSWORD has been set for this session.${NC}"

echo -e "${CYAN}--- Creating system roles ---${NC}"
ROLES=(reviewer editor administrator)

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
