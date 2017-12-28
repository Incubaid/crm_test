from crm.db import db, BaseModel, RootModel, ManyToManyBaseModel
from crm.mailer import sendemail


class CompanyTags(db.Model, ManyToManyBaseModel):
    __tablename__ = "companies_tags"

    tag_id = db.Column(
        db.String(5),
        db.ForeignKey('tags.id')
    )

    company_id = db.Column(
        db.String(5),
        db.ForeignKey("companies.id")
    )


class Company(db.Model, BaseModel, RootModel):

    __tablename__ = "companies"

    name = db.Column(
        db.String(255),
        nullable=False,
        index=True
    )

    # should be markdown.
    description = db.Column(
        db.Text(),
        default="",
        index=True
    )

    vatnumber = db.Column(
        db.String(255),
        index=True
    )

    website = db.Column(
        db.String(255),
        index=True
    )

    # Comma  separated emails
    emails = db.Column(
        db.Text(),
        index=True
    )

    # Comma separated phones
    telephones = db.Column(
        db.Text(),
        index=True
    )

    deals = db.relationship(
        "Deal",
        backref="company"
    )

    messages = db.relationship(
        "Message",
        backref="company"
    )

    tasks = db.relationship(
        "Task",
        backref="company"
    )

    comments = db.relationship(
        "Comment",
        backref="company"
    )

    contacts = db.relationship(
        "Contact",
        secondary="companies_contacts",
        backref='companies',
    )

    owner_id = db.Column(
        db.String(5),
        db.ForeignKey('users.id')
    )

    ownerbackup_id = db.Column(
        db.String(5),
        db.ForeignKey('users.id')
    )

    links = db.relationship(
        "Link",
        backref="company"
    )

    addresses = db.relationship(
        "Address",
        backref="company"
    )

    @property
    def notification_emails(self):
        """
        :return: list of all emails to send notifications to
        :rtype: list
        """
        return self.emails or ''

    def __str__(self):
        return self.name
