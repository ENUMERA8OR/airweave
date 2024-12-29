"""Add connection model

Revision ID: 153d267e9152
Revises: 6836af24ebf3
Create Date: 2024-12-29 13:47:30.112216

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '153d267e9152'
down_revision = '6836af24ebf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('connection',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('integration_type', sa.Enum('SOURCE', 'DESTINATION', 'EMBEDDING_MODEL', name='integrationtype'), nullable=False),
    sa.Column('status', sa.Enum('ACTIVE', 'INACTIVE', 'ERROR', name='connectionstatus'), nullable=False),
    sa.Column('integration_credential_id', sa.UUID(), nullable=False),
    sa.Column('source_id', sa.UUID(), nullable=True),
    sa.Column('destination_id', sa.UUID(), nullable=True),
    sa.Column('embedding_model_id', sa.UUID(), nullable=True),
    sa.Column('organization_id', sa.UUID(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('created_by_email', sa.String(), nullable=False),
    sa.Column('modified_by_email', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['created_by_email'], ['user.email'], ),
    sa.ForeignKeyConstraint(['destination_id'], ['destination.id'], ),
    sa.ForeignKeyConstraint(['embedding_model_id'], ['embedding_model.id'], ),
    sa.ForeignKeyConstraint(['integration_credential_id'], ['integration_credential.id'], ),
    sa.ForeignKeyConstraint(['modified_by_email'], ['user.email'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('integration_credential_source_id_fkey', 'integration_credential', type_='foreignkey')
    op.drop_constraint('integration_credential_embedding_model_id_fkey', 'integration_credential', type_='foreignkey')
    op.drop_constraint('integration_credential_destination_id_fkey', 'integration_credential', type_='foreignkey')
    op.drop_column('integration_credential', 'embedding_model_id')
    op.drop_column('integration_credential', 'source_id')
    op.drop_column('integration_credential', 'destination_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('integration_credential', sa.Column('destination_id', sa.UUID(), autoincrement=False, nullable=True))
    op.add_column('integration_credential', sa.Column('source_id', sa.UUID(), autoincrement=False, nullable=True))
    op.add_column('integration_credential', sa.Column('embedding_model_id', sa.UUID(), autoincrement=False, nullable=True))
    op.create_foreign_key('integration_credential_destination_id_fkey', 'integration_credential', 'destination', ['destination_id'], ['id'])
    op.create_foreign_key('integration_credential_embedding_model_id_fkey', 'integration_credential', 'embedding_model', ['embedding_model_id'], ['id'])
    op.create_foreign_key('integration_credential_source_id_fkey', 'integration_credential', 'source', ['source_id'], ['id'])
    op.drop_table('connection')
    op.execute("DROP TYPE IF EXISTS connectionstatus")
    op.execute("DROP TYPE IF EXISTS integrationtype")
    # ### end Alembic commands ###
