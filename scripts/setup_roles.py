"""Create the roles used by common/workflows, safe to run repeatedly:

    invenio shell scripts/setup_roles.py                 # production: roles only
    invenio shell scripts/setup_roles.py test-users    # dev/stage: also a user for each role

Reviewer roles follow the registered models, rerun after adding a model.
In production assign people with `invenio roles add <email> <role>`.
The test users' password is asked for, or taken from USERS_PASSWORD.
"""

import getpass
import os
import sys
from datetime import datetime, timezone

from flask_security.utils import hash_password
from invenio_access.models import ActionRoles
from invenio_accounts.proxies import current_datastore
from invenio_db import db
from oarepo_runtime import current_runtime

from common.workflows.generators import reviewer_role

DOMAIN = "email.cz"


def setup_roles():
    names = [reviewer_role(model) for model in current_runtime.rdm_models]
    for name in names + ["editor", "administrator"]:
        role = current_datastore.find_role(name)
        if role is None:
            role = current_datastore.create_role(id=name, name=name)
            current_datastore.commit()  # each on its own, see setup_test_user
            print(f"created role {name}")
        yield role


def setup_test_user(name, password, role=None):
    email = f"mbdb_{name}@{DOMAIN}"
    user = current_datastore.get_user(email)
    if user is None:
        user = current_datastore.create_user(
            email=email,
            password=hash_password(password),
            active=True,
            confirmed_at=datetime.now(timezone.utc),
            user_profile={"full_name": name.replace("_", " ").title()},
            # otherwise the others see an anonymous user in requests
            preferences={"visibility": "public"},
        )
        print(f"created user {email}")
    if role is not None and role not in user.roles:
        current_datastore.add_role_to_user(user, role)
        print(f"added {email} to {role.name}")
    # commit each user: Invenio indexes only those not flushed before the commit, and
    # users missing from the index get no notifications
    current_datastore.commit()


def allow_administration(role):
    for action in ("administration-access", "administration-moderation"):
        if not ActionRoles.query.filter_by(action=action, role_id=role.id).first():
            db.session.add(ActionRoles(action=action, role=role))
            print(f"allowed {action} to {role.name}")


def ask_password():
    password = getpass.getpass("Password for the test users: ")
    if not password or password != getpass.getpass("Confirm password: "):
        sys.exit("Passwords are empty or do not match.")
    return password


if __name__ == "__main__":
    test_users = "test-users" in sys.argv[1:]
    password = (os.environ.get("USERS_PASSWORD") or ask_password()) if test_users else None
    roles = list(setup_roles())
    if test_users:
        setup_test_user("user", password)
        for role in roles:
            setup_test_user(role.name, password, role)
        # as in rdm-12, only dev/stage administrators get the administration pages
        allow_administration(next(r for r in roles if r.name == "administrator"))
    current_datastore.commit()
