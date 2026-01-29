#!/bin/bash
set -euo pipefail

# Script to populate roles in localdev.
# --- ANSI Color Codes ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'
# ------------------------

# ---- Config that MUST match stage_setup.sh ----
DOMAIN="email.cz"
METHODS=(mst bli spr itc mp)
BASE_ROLES=(reviewer editor administrator)

# Helper to run command quietly - suppress stdout+stderr
quiet() { "$@" >/dev/null 2>&1; }

# Helper to run command, suppress stdout, capture stderr
capture_err() {
  local err
  err=$({ "$@" >/dev/null; } 2>&1) || { printf '%s' "$err"; return 1; }
  printf '%s' "$err"
  return 0
}

unset USERS_PASSWORD

# Password Setup
if [ -z "${USERS_PASSWORD:-}" ]; then
  echo -e "${RED}ERROR: USERS_PASSWORD is not set${NC}" >&2
  echo -e "${CYAN}--- User Password Setup ---${NC}"
  echo -e "Please enter the password for default users (reviewer, editor, administrator):"

  while true; do
    read -r -s -p "Password: " USERS_PASSWORD; echo
    read -r -s -p "Confirm password: " USERS_PASSWORD_CONFIRM; echo

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

# Create roles if they do not exist locally (quiet Invenio output)
for role in "${ROLES[@]}"; do
  if quiet invenio roles create "$role"; then
    echo -e "${GREEN}Created role '$role'${NC}"
  else
    # We intentionally don't print Invenio's error noise
    echo -e "${YELLOW}Role '$role' already exists. Skipping.${NC}"
  fi
done

echo -e "${CYAN}--- Creating test user ---${NC}"
if quiet invenio users create --password "$USERS_PASSWORD" -a -c test@test.org; then
  echo -e "${GREEN}Created user 'test@test.org'${NC}"
else
  echo -e "${YELLOW}User 'test@test.org' already exists. Skipping.${NC}"
fi

echo -e "${CYAN}--- Running stage setup (user creation) script ---${NC}"
bash -e "$(dirname "$0")/../scripts/stage_setup.sh"
echo -e "${CYAN}--- Role and User setup complete ---${NC}"

echo -e "${CYAN}--- Generating REST tokens and writing instructions to Desktop ---${NC}"

# Desktop output
DESKTOP_DIR="${HOME}/Desktop"
OUTPUT_FILE="${DESKTOP_DIR}/mbdb_localdev_tokens.txt"
mkdir -p "$DESKTOP_DIR"
: > "$OUTPUT_FILE"
chmod 600 "$OUTPUT_FILE"

# Build the list of users that exist after stage_setup.sh
declare -a USERS=()
USERS+=("test@test.org")

for m in "${METHODS[@]}"; do
  USERS+=("mbdb_reviewer_${m}@${DOMAIN}")
done

for r in "${BASE_ROLES[@]}"; do
  USERS+=("mbdb_${r}@${DOMAIN}")
done

# Write header
{
  echo "# MBDB localdev tokens"
  echo "# Generated on: $(date)"
  echo
  echo "# Usage:"
  echo "#   source <(grep -A2 \"User: test@test.org\" \"$OUTPUT_FILE\" | tail -n 2)"
  echo "# or just copy/paste the export line you need."
  echo
} >> "$OUTPUT_FILE"

# Token generation
# Note: token names should be unique per user to avoid collisions on reruns.
# If tokens with the same name already exist, Invenio may fail. We handle that gracefully.
for email in "${USERS[@]}"; do
  localpart="${email%@*}"
  token_name="resttest-${localpart}"

  # Create token quietly but capture output (the token itself)
  token=""
  if token=$(invenio tokens create -n resttest -u "$email" 2>/dev/null); then
    {
      echo "User: $email"
      echo "$token"
      echo "echo \$REPOTOKEN"
      echo
    } >> "$OUTPUT_FILE"
    echo -e "${GREEN}Token created for '$email'${NC}"
  else
    echo -e "${YELLOW}Token NOT created for '$email' (maybe already exists: '$token_name'). Skipping.${NC}"
  fi
done

echo -e "${GREEN}Token instructions written to:${NC} $OUTPUT_FILE"
