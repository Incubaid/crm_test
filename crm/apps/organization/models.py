from crm.db import db, BaseModel, RootModel
from crm.mailer import sendemail


class Organization(db.Model, BaseModel, RootModel):

    __tablename__ = "organizations"

    name = db.Column(
        db.String(255),
        nullable=False,
        index=True
    )

    # should be markdown
    description = db.Column(
        db.Text(),
        default="",
        index=True
    )

    emails = db.relationship(
        'Email',
        backref='organization',
        primaryjoin="Organization.id==Email.organization_id"
    )

    tasks = db.relationship(
        "Task",
        backref="organization"
    )

    comments = db.relationship(
        "Comment",
        backref="organization"
    )

    users = db.relationship(
        "User",
        secondary="users_organizations",
        secondaryjoin="User.id==UsersOrganizations.user_id",
        backref="organizations"
    )

    links = db.relationship(
        "Link",
        backref="organization"
    )

    messages = db.relationship(
        "Message",
        backref="organization"
    )

    owner_id = db.Column(
        db.String(5),
        db.ForeignKey('users.id')
    )

    parent_id = db.Column(
        db.String(5),
        db.ForeignKey("organizations.id")
    )

    @property
    def notification_emails(self):
        """
        :return: list of all emails to send notifications to
        :rtype: list
        """
        return [e.email for e in self.emails]

    def __str__(self):
        return self.name
