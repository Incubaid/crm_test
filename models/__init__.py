from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy() # init later in app.py

class Telephone(db.Model):
    __tablename__ = "telephones"
    id = db.Column('telephone_id',db.Integer, primary_key=True)
    number = db.Column(db.String(10))  # how long is phoneumber
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    company_id = db.Column(db.Integer, db.ForeignKey("companies.company_id"))

    def __str__(self):
        return self.number

class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column('contact_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    firstname = db.Column(db.String(15))
    lastname = db.Column(db.String(15))
    email = db.Column(db.String(30))
    message_channels = db.Column(db.String(10))
    description = db.Column(db.Text())  #should be markdown.
    
    # timestamps
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    isuser = db.Column(db.Boolean, default=False)


    #relations
    telephones = db.relationship("Telephone", backref="contact")
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.organization_id"))

    deals = db.relationship("Deal", backref="contact") 
    comments = db.relationship("Comment", backref="contact")
    # links = db.relationship("Link", backref="contact")
    tasks = db.relationship("Task", backref="assignee") 
    messages = db.relationship("Message", backref="contact") 


    owner_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    owner = db.relationship('Contact', primaryjoin=('Contact.owner_id==Contact.id'), backref='ownedusers', remote_side=id)

    ownerbackup_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    ownerbackup = db.relationship('Contact', primaryjoin=('Contact.ownerbackup_id==Contact.id'), backref='backupownedusers', remote_side=id)

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column('company_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    name = db.Column(db.String(10))
    description = db.Column(db.String(100))  #should be markdown.
    email = db.Column(db.String(10))


    isuser = db.Column(db.Boolean, default=False)

    # timestamps
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    #relations
    telephones = db.relationship("Telephone", backref="company")
    deals = db.relationship("Deal", backref="company") 
#     messages = db.relationship("Message", back_populates="company") 
    tasks = db.relationship("Task", backref="company") 
    comments = db.relationship("Comment", backref="company") 

    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    owner = db.relationship("Contact", backref="ownedcompanies")
    ownerbackup = db.relationship("Contact", backref="backupownedcompanies")
    
    def __str__(self):
        return self.name



#  manytomany through table.
class ContactsOrganizations(db.Model):
    __tablename__ = 'contacts_organizations'
    id = db.Column(db.Integer(), primary_key=True)
    contact_id = db.Column(db.Integer(), db.ForeignKey('contacts.contact_id')) #, ondelete='CASCADE'))
    organization_id  = db.Column(db.Integer(), db.ForeignKey('organizations.organization_id')) #, ondelete='CASCADE'))



class Organization(db.Model):
    __tablename__ = "organizations"
    id = db.Column('organization_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    name = db.Column(db.String(10))
    description = db.Column(db.String(100))  #should be markdown.
    email = db.Column(db.String(10))
    # timestamps
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

#     #relations
    users = db.relationship("Contact", backref="organization")
    tasks = db.relationship("Task", backref="organization") 

    comments = db.relationship("Comment", backref="organization") 
    users = db.relationship("Contact", secondary="contacts_organizations", backref=db.backref("organizations"), lazy="dynamic")

    # links = db.relationship("Link", backref="organization") 
    messages = db.relationship("Message", backref="organization") 
    sprints = db.relationship("Sprint", backref="organization") 
    promoter = db.relationship("Contact", backref="promotedorganizations")
    gauridan = db.relationship("Contact", backref="gaurdianedorganizations")
    parent_id = db.Column(db.Integer, db.ForeignKey("organizations.organization_id"))
    owner = db.relationship('Organization', primaryjoin=('Organization.parent_id==Organization.id'), backref='ownedusers', remote_side=id)

    def __str__(self):
        return self.name

class DealState(Enum):
    NEW, INTERESTED, CONFIRMED, WAITINGCLOSED, CLOSED = range(5)

class DealType(Enum):
    HOSTER, ITO, PTO, PREPTO = range(4)

class DealCurrency(Enum):
    USD, EUR, AED, GBP = range(4)


class Deal(db.Model):
    __tablename__ = "deals"
    id = db.Column('deal_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    name = db.Column(db.String(10))
    remarks = db.Column(db.String(100))  #should be markdown.
    amount = db.Column(db.Integer)  # default to int.
    currency = db.Column(db.Enum(DealCurrency), default=DealCurrency.EUR)
    deal_type = db.Column(db.Enum(DealType), default=DealType.HOSTER)
    deal_state = db.Column(db.Enum(DealState), default=DealState.NEW)

    isuser = db.Column(db.Boolean, default=False)
    # timestamps
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    closed_at= db.Column(db.TIMESTAMP, nullable=True) # should be?

    # relations
    company_id = db.Column(db.Integer, db.ForeignKey("companies.company_id"))
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))

    tasks = db.relationship("Task", backref="deal") 
    comments = db.relationship("Comment", backref="deal") 
    messages = db.relationship("Message", backref="deal") 
    # links = db.relationship("Links", backref="deal") 
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    owner = db.relationship("Contact", backref="owneddeals")
    ownerbackup = db.relationship("Contact", backref="backupowneddeals")

    def __str__(self):
        return self.name


#  manytomany through table.
class ContactsProjects(db.Model):
    __tablename__ = 'contacts_projects'
    id = db.Column(db.Integer(), primary_key=True)
    contact_id = db.Column(db.Integer(), db.ForeignKey('contacts.contact_id')) #, ondelete='CASCADE'))
    project_id  = db.Column(db.Integer(), db.ForeignKey('projects.project_id')) #, ondelete='CASCADE'))


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column('project_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    name = db.Column(db.String(10))
    description = db.Column(db.String(100))  #should be markdown.
    
    start_date = db.Column(db.TIMESTAMP)
    deadline = db.Column(db.TIMESTAMP) 
    # timestamps
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

#     # relations
    comments = db.relationship("Comment", backref="project")
    # links = db.relationship("Links", backref="project")

    tasks = db.relationship("Task", backref="project")
    sprint = db.relationship("Sprint", backref="projects")

    messages = db.relationship("Message", backref="project") 
    users = db.relationship("Contact", secondary="contacts_projects", backref=db.backref("projects"), lazy="dynamic")

    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    promoter = db.relationship("Contact", backref="promotedprojects")
    gauridan = db.relationship("Contact", backref="gaurdiansprojects")

    #parent organization
    parent_id = db.Column(db.Integer, db.ForeignKey("organizations.organization_id"))
    parent = db.relationship('Organization', backref='childprojects')

    def percentage_done():
        pass

# manytomany through table.
class ContactsSprints(db.Model):
    __tablename__ = 'contacts_sprints'
    id = db.Column(db.Integer(), primary_key=True)
    contact_id = db.Column(db.Integer(), db.ForeignKey('contacts.contact_id')) #, ondelete='CASCADE'))
    sprint_id = db.Column(db.Integer(), db.ForeignKey('sprints.sprint_id')) #, ondelete='CASCADE'))
    def __str__(self):
        return self.name

class Sprint(db.Model):
    __tablename__ = "sprints"
    id = db.Column('sprint_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    name = db.Column(db.String(10))
    description = db.Column(db.String(100))  #should be markdown.
    start_date = db.Column(db.TIMESTAMP)
    deadline = db.Column(db.TIMESTAMP) 
    # timestamps
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


    #relations

    users = db.relationship("Contact", secondary="contacts_sprints", backref=db.backref("sprints"), lazy="dynamic")
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"))
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.organization_id"))
    tasks = db.relationship("Task", backref="sprint")
    comments = db.relationship("Comment", backref="sprint") 
    # links = db.relationship("Link", backref="sprint") 
    messages = db.relationship("Message", backref="sprint") 
    
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    promoter = db.relationship("Contact", backref="promotedsprints")
    gauridan = db.relationship("Contact", backref="gaurdiansprints")

    #parent organization
    parent = db.relationship('Organization', backref='childsprints')

    def percentage_done():
        pass

    def hours_open():
        pass

    def hours_open_person_avg():
        pass

    def hours_open_person_max():
        pass

#     # uid = random 4 letters/numbers e.g. sie7 (generated at start, check is unique)
#     # contact_uid
#     # deal_uid
#     # project_uid
#     # organization_uid
#     # task_uid
#     # sprint_uid
#     # content (is markdown)
#     # owner (link to 1 contact which is users)

    def __str__(self):
        return self.name

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column('comment_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    name = db.Column(db.String(10))
    remarks = db.Column(db.Text())  #should be markdown. 
    content = db.Column(db.Text())  #should be markdown.

    # timestamps
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


     # relations
    company_id = db.Column(db.Integer, db.ForeignKey("companies.company_id"))
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    deal_id = db.Column(db.Integer, db.ForeignKey("deals.deal_id"))
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.task_id"))
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.organization_id"))
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"))
    sprint_id = db.Column(db.Integer, db.ForeignKey("sprints.sprint_id"))


    def __str__(self):
        return self.name


# class Link(db.Model):
#     __tablename__ = "links"
#     id = db.Column('link_id', db.Integer, primary_key=True)
#     uid = db.Column(db.String(4))
#     url = db.Column(db.String(255))
#     labels = db.Column(db.Text())  #should be markdown. 

#     # timestamps
#     created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
#     updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


#     # relations
#     contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
#     deal_id = db.Column(db.Integer, db.ForeignKey("deals.deal_id"))
#     task_id = db.Column(db.Integer, db.ForeignKey("tasks.task_id"))
#     organization_id = db.Column(db.Integer, db.ForeignKey("organizations.organization_id"))
#     project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"))
#     # comment_id = db.Column(db.Integer, db.ForeignKey("comments.comment_id")) 

#     def __str__(self):
#         return self.name


class TaskType(Enum):
    FEATURE, QUESTION, TASK, STORY, CONTACT = range(5)


class TaskPriority(Enum):
    MINOR, NORMAL, URGENT, CRITICAL = range(4)

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column('task_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    title = db.Column(db.String(255))
    description = db.Column(db.Text())  #should be markdown.
    remarks = db.Column(db.Text())  #should be markdown. 
    content = db.Column(db.Text())  #should be markdown.
    type = db.Column(db.Enum(TaskType), default=TaskType.FEATURE)
    priortiy = db.Column(db.Enum(TaskPriority), default=TaskPriority.MINOR)


    # time_done means time be spent on that task.
    eta = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    time_done = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


    # relations
    company_id = db.Column(db.Integer, db.ForeignKey("companies.company_id"))
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    deal_id = db.Column(db.Integer, db.ForeignKey("deals.deal_id"))
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.organization_id"))
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"))
    sprint_id = db.Column(db.Integer, db.ForeignKey("sprints.sprint_id"))
    comments = db.relationship("Comment", backref="task") 
    messages = db.relationship("Message", backref="task") 

    def __str__(self):
        return self.name

    def percent_completed(self):
        return "0%"

class MessageChannel(Enum):
    TELEGRAM, EMAIL, SMS, INTERCOM = range(4)

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column('comment_id', db.Integer, primary_key=True)
    uid = db.Column(db.String(4))
    title = db.Column(db.String(10))
    content = db.Column(db.String(100))  #should be markdown.
    channel = db.Column(db.String(100))  #should be markdown. 
    time_tosend = db.Column(db.TIMESTAMP)
    time_sent = db.Column(db.TIMESTAMP)

    # timestamps
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # relations
    company_id = db.Column(db.Integer, db.ForeignKey("companies.company_id"))
    contact_id = db.Column(db.Integer, db.ForeignKey("contacts.contact_id"))
    deal_id = db.Column(db.Integer, db.ForeignKey("deals.deal_id"))
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.task_id"))
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.organization_id"))
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"))
    sprint_id = db.Column(db.Integer, db.ForeignKey("sprints.sprint_id"))

    def __str__(self):
        return self.title