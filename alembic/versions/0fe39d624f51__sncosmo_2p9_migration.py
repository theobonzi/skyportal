"""sncosmo 2.9.0 migration

Revision ID: 0fe39d624f51
Revises: 8e0f15cb11af
Create Date: 2022-03-17 11:41:30.500797

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '0fe39d624f51'
down_revision = '8e0f15cb11af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # add filters from sncosmo 2.9.0 in the right place
    with op.get_context().autocommit_block():
        op.execute(
            "ALTER TYPE bandpasses ADD VALUE IF NOT EXISTS 'gaia::gbp' AFTER '2massks'"
        )

        op.execute(
            "ALTER TYPE bandpasses ADD VALUE IF NOT EXISTS 'gaia::g' AFTER 'gaia::gbp'"
        )
        op.execute(
            "ALTER TYPE bandpasses ADD VALUE IF NOT EXISTS 'gaia::grp' AFTER 'gaia::g'"
        )
        op.execute(
            "ALTER TYPE bandpasses ADD VALUE IF NOT EXISTS 'gaia::grvs' AFTER 'gaia::grp'"
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###