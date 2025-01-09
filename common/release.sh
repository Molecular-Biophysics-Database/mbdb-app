#
# Import script for 2025-01-17 release
#
# Usage:
# ./scripts/release.sh [--destroy]
#
#

cd "$(dirname $0)/.."

set -e
set -x

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --destroy) DESTROY=true ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

export DESTROY

if [ -d .venv ]; then
    source .venv/bin/activate
fi

if [ -z "$BUCKET_NAME" ] ; then
    echo "BUCKET_NAME is not set"
    exit 1
fi

if [ "$DESTROY" == "true" ] ; then
    invenio db destroy --yes-i-know || true
    invenio index destroy --force --yes-i-know || true
    invenio db init create
    invenio index init
fi

invenio oarepo cf init
invenio communities custom-fields init
invenio files location create --default default s3://${BUCKET_NAME};

# Load vocabularies only
invenio oarepo fixtures load --verbose

# Define roles
ROLES=(reviewer editor administrator)
for role in ${ROLES[@]}
do
    invenio roles create $role
done