import sqlalchemy_utils.types
import sqlalchemy_utils
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Nrp install revision."""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'mbdb_mst_3'
down_revision = 'ca932e1c4273'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_uq_partial_files_object_is_head', table_name='files_object')
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_uq_partial_files_object_is_head', 'files_object', ['bucket_id', 'key'], unique=False)
    # ### end Alembic commands ###
