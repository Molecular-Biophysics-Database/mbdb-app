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
from sqlalchemy.dialects import mysql
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'mbdb_app_3'
down_revision = 'mbdb_app_2'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bli_metadata_version',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), autoincrement=False, nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), autoincrement=False, nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), autoincrement=False, nullable=True),
    sa.Column('version_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('index', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name=op.f('pk_bli_metadata_version'))
    )
    op.create_index(op.f('ix_bli_metadata_version_end_transaction_id'), 'bli_metadata_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_bli_metadata_version_operation_type'), 'bli_metadata_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_bli_metadata_version_transaction_id'), 'bli_metadata_version', ['transaction_id'], unique=False)
    op.create_table('bli_parent_record_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bli_parent_record_metadata'))
    )
    op.create_table('mst_metadata_version',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), autoincrement=False, nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), autoincrement=False, nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), autoincrement=False, nullable=True),
    sa.Column('version_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('index', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name=op.f('pk_mst_metadata_version'))
    )
    op.create_index(op.f('ix_mst_metadata_version_end_transaction_id'), 'mst_metadata_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_mst_metadata_version_operation_type'), 'mst_metadata_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_mst_metadata_version_transaction_id'), 'mst_metadata_version', ['transaction_id'], unique=False)
    op.create_table('mst_parent_record_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_mst_parent_record_metadata'))
    )
    op.create_table('spr_metadata_version',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), autoincrement=False, nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), autoincrement=False, nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), autoincrement=False, nullable=True),
    sa.Column('version_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('index', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name=op.f('pk_spr_metadata_version'))
    )
    op.create_index(op.f('ix_spr_metadata_version_end_transaction_id'), 'spr_metadata_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_spr_metadata_version_operation_type'), 'spr_metadata_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_spr_metadata_version_transaction_id'), 'spr_metadata_version', ['transaction_id'], unique=False)
    op.create_table('spr_parent_record_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_spr_parent_record_metadata'))
    )
    op.create_table('bli_draft_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('fork_version_id', sa.Integer(), nullable=True),
    sa.Column('expires_at', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['bucket_id'], ['files_bucket.id'], name=op.f('fk_bli_draft_metadata_bucket_id_files_bucket')),
    sa.ForeignKeyConstraint(['parent_id'], ['bli_parent_record_metadata.id'], name=op.f('fk_bli_draft_metadata_parent_id_bli_parent_record_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bli_draft_metadata'))
    )
    op.create_table('bli_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['bucket_id'], ['files_bucket.id'], name=op.f('fk_bli_metadata_bucket_id_files_bucket')),
    sa.ForeignKeyConstraint(['parent_id'], ['bli_parent_record_metadata.id'], name=op.f('fk_bli_metadata_parent_id_bli_parent_record_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bli_metadata'))
    )
    op.create_table('mst_draft_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('fork_version_id', sa.Integer(), nullable=True),
    sa.Column('expires_at', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['bucket_id'], ['files_bucket.id'], name=op.f('fk_mst_draft_metadata_bucket_id_files_bucket')),
    sa.ForeignKeyConstraint(['parent_id'], ['mst_parent_record_metadata.id'], name=op.f('fk_mst_draft_metadata_parent_id_mst_parent_record_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_mst_draft_metadata'))
    )
    op.create_table('mst_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['bucket_id'], ['files_bucket.id'], name=op.f('fk_mst_metadata_bucket_id_files_bucket')),
    sa.ForeignKeyConstraint(['parent_id'], ['mst_parent_record_metadata.id'], name=op.f('fk_mst_metadata_parent_id_mst_parent_record_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_mst_metadata'))
    )
    op.create_table('spr_draft_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('fork_version_id', sa.Integer(), nullable=True),
    sa.Column('expires_at', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['bucket_id'], ['files_bucket.id'], name=op.f('fk_spr_draft_metadata_bucket_id_files_bucket')),
    sa.ForeignKeyConstraint(['parent_id'], ['spr_parent_record_metadata.id'], name=op.f('fk_spr_draft_metadata_parent_id_spr_parent_record_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_spr_draft_metadata'))
    )
    op.create_table('spr_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('bucket_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['bucket_id'], ['files_bucket.id'], name=op.f('fk_spr_metadata_bucket_id_files_bucket')),
    sa.ForeignKeyConstraint(['parent_id'], ['spr_parent_record_metadata.id'], name=op.f('fk_spr_metadata_parent_id_spr_parent_record_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_spr_metadata'))
    )
    op.create_table('bli_file_draft_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Text().with_variant(mysql.VARCHAR(length=255), 'mysql'), nullable=False),
    sa.Column('record_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('object_version_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['object_version_id'], ['files_object.version_id'], name=op.f('fk_bli_file_draft_metadata_object_version_id_files_object'), ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['record_id'], ['bli_draft_metadata.id'], name=op.f('fk_bli_file_draft_metadata_record_id_bli_draft_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bli_file_draft_metadata'))
    )
    op.create_index('uidx_bli_file_draft_metadata_id_key', 'bli_file_draft_metadata', ['id', 'key'], unique=True)
    op.create_table('bli_file_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Text().with_variant(mysql.VARCHAR(length=255), 'mysql'), nullable=False),
    sa.Column('record_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('object_version_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['object_version_id'], ['files_object.version_id'], name=op.f('fk_bli_file_metadata_object_version_id_files_object'), ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['record_id'], ['bli_metadata.id'], name=op.f('fk_bli_file_metadata_record_id_bli_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bli_file_metadata'))
    )
    op.create_index('uidx_bli_file_metadata_id_key', 'bli_file_metadata', ['id', 'key'], unique=True)
    op.create_table('bli_parent_state',
    sa.Column('latest_index', sa.Integer(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('latest_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('next_draft_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['latest_id'], ['bli_metadata.id'], name=op.f('fk_bli_parent_state_latest_id_bli_metadata')),
    sa.ForeignKeyConstraint(['next_draft_id'], ['bli_draft_metadata.id'], name=op.f('fk_bli_parent_state_next_draft_id_bli_draft_metadata')),
    sa.ForeignKeyConstraint(['parent_id'], ['bli_parent_record_metadata.id'], name=op.f('fk_bli_parent_state_parent_id_bli_parent_record_metadata'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('parent_id', name=op.f('pk_bli_parent_state'))
    )
    op.create_table('mst_file_draft_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Text().with_variant(mysql.VARCHAR(length=255), 'mysql'), nullable=False),
    sa.Column('record_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('object_version_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['object_version_id'], ['files_object.version_id'], name=op.f('fk_mst_file_draft_metadata_object_version_id_files_object'), ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['record_id'], ['mst_draft_metadata.id'], name=op.f('fk_mst_file_draft_metadata_record_id_mst_draft_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_mst_file_draft_metadata'))
    )
    op.create_index('uidx_mst_file_draft_metadata_id_key', 'mst_file_draft_metadata', ['id', 'key'], unique=True)
    op.create_table('mst_file_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Text().with_variant(mysql.VARCHAR(length=255), 'mysql'), nullable=False),
    sa.Column('record_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('object_version_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['object_version_id'], ['files_object.version_id'], name=op.f('fk_mst_file_metadata_object_version_id_files_object'), ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['record_id'], ['mst_metadata.id'], name=op.f('fk_mst_file_metadata_record_id_mst_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_mst_file_metadata'))
    )
    op.create_index('uidx_mst_file_metadata_id_key', 'mst_file_metadata', ['id', 'key'], unique=True)
    op.create_table('mst_parent_state',
    sa.Column('latest_index', sa.Integer(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('latest_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('next_draft_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['latest_id'], ['mst_metadata.id'], name=op.f('fk_mst_parent_state_latest_id_mst_metadata')),
    sa.ForeignKeyConstraint(['next_draft_id'], ['mst_draft_metadata.id'], name=op.f('fk_mst_parent_state_next_draft_id_mst_draft_metadata')),
    sa.ForeignKeyConstraint(['parent_id'], ['mst_parent_record_metadata.id'], name=op.f('fk_mst_parent_state_parent_id_mst_parent_record_metadata'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('parent_id', name=op.f('pk_mst_parent_state'))
    )
    op.create_table('spr_file_draft_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Text().with_variant(mysql.VARCHAR(length=255), 'mysql'), nullable=False),
    sa.Column('record_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('object_version_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['object_version_id'], ['files_object.version_id'], name=op.f('fk_spr_file_draft_metadata_object_version_id_files_object'), ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['record_id'], ['spr_draft_metadata.id'], name=op.f('fk_spr_file_draft_metadata_record_id_spr_draft_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_spr_file_draft_metadata'))
    )
    op.create_index('uidx_spr_file_draft_metadata_id_key', 'spr_file_draft_metadata', ['id', 'key'], unique=True)
    op.create_table('spr_file_metadata',
    sa.Column('created', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('updated', sa.DateTime().with_variant(mysql.DATETIME(fsp=6), 'mysql'), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('json', sa.JSON().with_variant(sqlalchemy_utils.types.json.JSONType(), 'mysql').with_variant(postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), 'postgresql').with_variant(sqlalchemy_utils.types.json.JSONType(), 'sqlite'), nullable=True),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Text().with_variant(mysql.VARCHAR(length=255), 'mysql'), nullable=False),
    sa.Column('record_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('object_version_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['object_version_id'], ['files_object.version_id'], name=op.f('fk_spr_file_metadata_object_version_id_files_object'), ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['record_id'], ['spr_metadata.id'], name=op.f('fk_spr_file_metadata_record_id_spr_metadata'), ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_spr_file_metadata'))
    )
    op.create_index('uidx_spr_file_metadata_id_key', 'spr_file_metadata', ['id', 'key'], unique=True)
    op.create_table('spr_parent_state',
    sa.Column('latest_index', sa.Integer(), nullable=True),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('latest_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.Column('next_draft_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['latest_id'], ['spr_metadata.id'], name=op.f('fk_spr_parent_state_latest_id_spr_metadata')),
    sa.ForeignKeyConstraint(['next_draft_id'], ['spr_draft_metadata.id'], name=op.f('fk_spr_parent_state_next_draft_id_spr_draft_metadata')),
    sa.ForeignKeyConstraint(['parent_id'], ['spr_parent_record_metadata.id'], name=op.f('fk_spr_parent_state_parent_id_spr_parent_record_metadata'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('parent_id', name=op.f('pk_spr_parent_state'))
    )
    op.drop_index('ix_uq_partial_files_object_is_head', table_name='files_object')
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_uq_partial_files_object_is_head', 'files_object', ['bucket_id', 'key'], unique=False)
    op.drop_table('spr_parent_state')
    op.drop_index('uidx_spr_file_metadata_id_key', table_name='spr_file_metadata')
    op.drop_table('spr_file_metadata')
    op.drop_index('uidx_spr_file_draft_metadata_id_key', table_name='spr_file_draft_metadata')
    op.drop_table('spr_file_draft_metadata')
    op.drop_table('mst_parent_state')
    op.drop_index('uidx_mst_file_metadata_id_key', table_name='mst_file_metadata')
    op.drop_table('mst_file_metadata')
    op.drop_index('uidx_mst_file_draft_metadata_id_key', table_name='mst_file_draft_metadata')
    op.drop_table('mst_file_draft_metadata')
    op.drop_table('bli_parent_state')
    op.drop_index('uidx_bli_file_metadata_id_key', table_name='bli_file_metadata')
    op.drop_table('bli_file_metadata')
    op.drop_index('uidx_bli_file_draft_metadata_id_key', table_name='bli_file_draft_metadata')
    op.drop_table('bli_file_draft_metadata')
    op.drop_table('spr_metadata')
    op.drop_table('spr_draft_metadata')
    op.drop_table('mst_metadata')
    op.drop_table('mst_draft_metadata')
    op.drop_table('bli_metadata')
    op.drop_table('bli_draft_metadata')
    op.drop_table('spr_parent_record_metadata')
    op.drop_index(op.f('ix_spr_metadata_version_transaction_id'), table_name='spr_metadata_version')
    op.drop_index(op.f('ix_spr_metadata_version_operation_type'), table_name='spr_metadata_version')
    op.drop_index(op.f('ix_spr_metadata_version_end_transaction_id'), table_name='spr_metadata_version')
    op.drop_table('spr_metadata_version')
    op.drop_table('mst_parent_record_metadata')
    op.drop_index(op.f('ix_mst_metadata_version_transaction_id'), table_name='mst_metadata_version')
    op.drop_index(op.f('ix_mst_metadata_version_operation_type'), table_name='mst_metadata_version')
    op.drop_index(op.f('ix_mst_metadata_version_end_transaction_id'), table_name='mst_metadata_version')
    op.drop_table('mst_metadata_version')
    op.drop_table('bli_parent_record_metadata')
    op.drop_index(op.f('ix_bli_metadata_version_transaction_id'), table_name='bli_metadata_version')
    op.drop_index(op.f('ix_bli_metadata_version_operation_type'), table_name='bli_metadata_version')
    op.drop_index(op.f('ix_bli_metadata_version_end_transaction_id'), table_name='bli_metadata_version')
    op.drop_table('bli_metadata_version')
    # ### end Alembic commands ###
