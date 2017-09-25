"""empty message

Revision ID: 3aca7dcaac89
Revises: 
Create Date: 2017-09-25 14:56:18.575135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aca7dcaac89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('company_id', sa.String(length=5), nullable=True),
    sa.Column('contact_id', sa.String(length=5), nullable=True),
    sa.Column('user_id', sa.String(length=5), nullable=True),
    sa.Column('deal_id', sa.String(length=5), nullable=True),
    sa.Column('task_id', sa.String(length=5), nullable=True),
    sa.Column('organization_id', sa.String(length=5), nullable=True),
    sa.Column('project_id', sa.String(length=5), nullable=True),
    sa.Column('sprint_id', sa.String(length=5), nullable=True),
    sa.Column('link_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.ForeignKeyConstraint(['deal_id'], ['deals.id'], ),
    sa.ForeignKeyConstraint(['link_id'], ['links.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('companies',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('vatnumber', sa.String(length=255), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('emails', sa.Text(), nullable=True),
    sa.Column('telephones', sa.Text(), nullable=True),
    sa.Column('owner_id', sa.String(length=5), nullable=True),
    sa.Column('ownerbackup_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['ownerbackup_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('companies_contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.String(length=5), nullable=True),
    sa.Column('contact_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contacts',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('firstname', sa.String(length=255), nullable=False),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('message_channels', sa.String(length=255), nullable=True),
    sa.Column('owner_id', sa.String(length=5), nullable=True),
    sa.Column('ownerbackup_id', sa.String(length=5), nullable=True),
    sa.Column('parent_id', sa.String(length=5), nullable=True),
    sa.Column('emails', sa.Text(), nullable=True),
    sa.Column('telephones', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['ownerbackup_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contacts_projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact_id', sa.String(length=5), nullable=True),
    sa.Column('project_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contacts_sprints',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact_id', sa.String(length=5), nullable=True),
    sa.Column('sprint_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deals',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('currency', sa.Enum('USD', 'EUR', 'AED', 'GBP', name='dealcurrency'), nullable=True),
    sa.Column('deal_type', sa.Enum('HOSTER', 'ITO', 'PTO', 'AMBASSADOR', name='dealtype'), nullable=True),
    sa.Column('deal_state', sa.Enum('NEW', 'INTERESTED', 'CONFIRMED', 'PENDING', 'CLOSED', name='dealstate'), nullable=True),
    sa.Column('closed_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('company_id', sa.String(length=5), nullable=True),
    sa.Column('contact_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('links',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('labels', sa.Text(), nullable=True),
    sa.Column('contact_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('deal_id', sa.String(), nullable=True),
    sa.Column('task_id', sa.String(), nullable=True),
    sa.Column('organization_id', sa.String(), nullable=True),
    sa.Column('project_id', sa.String(), nullable=True),
    sa.Column('sprint_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.ForeignKeyConstraint(['deal_id'], ['deals.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('channel', sa.String(length=255), nullable=True),
    sa.Column('time_tosend', sa.TIMESTAMP(), nullable=True),
    sa.Column('time_sent', sa.TIMESTAMP(), nullable=True),
    sa.Column('company_id', sa.String(), nullable=True),
    sa.Column('contact_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('deal_id', sa.String(), nullable=True),
    sa.Column('task_id', sa.String(), nullable=True),
    sa.Column('organization_id', sa.String(), nullable=True),
    sa.Column('project_id', sa.String(), nullable=True),
    sa.Column('sprint_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.ForeignKeyConstraint(['deal_id'], ['deals.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organizations',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('emails', sa.Text(), nullable=True),
    sa.Column('owner_id', sa.String(length=5), nullable=True),
    sa.Column('parent_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['organizations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('start_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('deadline', sa.TIMESTAMP(), nullable=True),
    sa.Column('sprint_id', sa.String(length=5), nullable=True),
    sa.Column('promoter_id', sa.String(length=5), nullable=True),
    sa.Column('guardian_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['guardian_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['promoter_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sprints',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('start_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('deadline', sa.TIMESTAMP(), nullable=True),
    sa.Column('owner_id', sa.String(length=5), nullable=True),
    sa.Column('project_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.Enum('FEATURE', 'QUESTION', 'TASK', 'STORY', 'CONTACT', name='tasktype'), nullable=True),
    sa.Column('priority', sa.Enum('MINOR', 'NORMAL', 'URGENT', 'CRITICAL', name='taskpriority'), nullable=True),
    sa.Column('state', sa.Enum('NEW', 'PROGRESS', 'QUESTION', 'VERIFICATION', 'CLOSED', name='taskstate'), nullable=True),
    sa.Column('assignee_id', sa.String(), nullable=True),
    sa.Column('deadline', sa.TIMESTAMP(), nullable=False),
    sa.Column('eta', sa.TIMESTAMP(), nullable=False),
    sa.Column('time_estimate', sa.Integer(), nullable=True),
    sa.Column('time_done', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.String(), nullable=True),
    sa.Column('contact_id', sa.String(), nullable=True),
    sa.Column('deal_id', sa.String(), nullable=True),
    sa.Column('organization_id', sa.String(), nullable=True),
    sa.Column('project_id', sa.String(), nullable=True),
    sa.Column('sprint_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['assignee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.ForeignKeyConstraint(['deal_id'], ['deals.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasktrackings',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('remarks', sa.Text(), nullable=True),
    sa.Column('time_done', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('firstname', sa.String(length=255), nullable=False),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('message_channels', sa.String(length=255), nullable=True),
    sa.Column('emails', sa.Text(), nullable=True),
    sa.Column('telephones', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=5), nullable=True),
    sa.Column('organization_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=5), nullable=True),
    sa.Column('project_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_sprints',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=5), nullable=True),
    sa.Column('sprint_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_sprints')
    op.drop_table('users_projects')
    op.drop_table('users_organizations')
    op.drop_table('users')
    op.drop_table('tasktrackings')
    op.drop_table('tasks')
    op.drop_table('sprints')
    op.drop_table('projects')
    op.drop_table('organizations')
    op.drop_table('messages')
    op.drop_table('links')
    op.drop_table('deals')
    op.drop_table('contacts_sprints')
    op.drop_table('contacts_projects')
    op.drop_table('contacts')
    op.drop_table('companies_contacts')
    op.drop_table('companies')
    op.drop_table('comments')
    # ### end Alembic commands ###
