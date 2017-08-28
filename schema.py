from models import Telephone as TelephoneModel, Contact as ContactModel, Company as CompanyModel, Organization as OrganizationModel, Deal as DealModel, Deal as DealModel, Link as LinkModel, Project as ProjectModel, Sprint as SprintModel, Task as TaskModel, Comment as CommentModel, Message as MessageModel
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Telephone(SQLAlchemyObjectType):

    class Meta:
        model = TelephoneModel


class Contact(SQLAlchemyObjectType):

    class Meta:
        model = ContactModel


class Company(SQLAlchemyObjectType):

    class Meta:
        model = CompanyModel


class Organization(SQLAlchemyObjectType):

    class Meta:
        model = OrganizationModel


class Deal(SQLAlchemyObjectType):

    class Meta:
        model = DealModel


class Link(SQLAlchemyObjectType):

    class Meta:
        model = LinkModel


class Project(SQLAlchemyObjectType):

    class Meta:
        model = ProjectModel


class Sprint(SQLAlchemyObjectType):

    class Meta:
        model = SprintModel


class Task(SQLAlchemyObjectType):

    class Meta:
        model = TaskModel


class Comment(SQLAlchemyObjectType):

    class Meta:
        model = CommentModel


class Message(SQLAlchemyObjectType):

    class Meta:
        model = MessageModel


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    telephones = graphene.List(Telephone)
    contacts = graphene.List(Contact)
    companies = graphene.List(Company)
    organizations = graphene.List(Organization)
    deals = graphene.List(Deal)
    links = graphene.List(Link)
    projects = graphene.List(Project)
    sprints = graphene.List(Sprint)
    tasks = graphene.List(Task)
    comments = graphene.List(Comment)
    messages = graphene.List(Message)

    def resolve_telephones(self, args, context, info):
        query = Telephone.get_query(context)  # SQLAlchemy query
        return query.all()

    def resolve_contacts(self, args, context, info):
        query = Contact.get_query(context)  # SQLAlchemy query
        return query.all()

    def resolve_companies(self, args, context, info):
        query = Company.get_query(context)  # SQLAlchemy query
        return query.all()

    def reslove_organizations(self, args, context, info):
        query = Organization.get_query(context)  # SQLAlchemy query
        return query.all()

    def resolve_deals(self, args, context, info):
        query = Deal.get_query(context)  # SQLAlchemy query
        return query.all()

    def resolve_links(self, args, context, info):
        query = Link.get_query(context)  # SQLAlchemy query
        return query.all()

    def reslove_projects(self, args, context, info):
        query = Project.get_query(context)  # SQLAlchemy query
        return query.all()

    def reslove_sprints(self, args, context, info):
        query = Sprint.get_query(context)  # SQLAlchemy query
        return query.all()

    def resolve_tasks(self, args, context, info):
        query = Task.get_query(context)  # SQLAlchemy query
        return query.all()

    def resolve_comments(self, args, context, info):
        query = Comment.get_query(context)  # SQLAlchemy query
        return query.all()

    def resolve_messages(self, args, context, info):
        query = Message.get_query(context)  # SQLAlchemy query
        return query.all()


schema = graphene.Schema(query=Query, types=[
                         Telephone, Contact, Company, Organization, Deal, Project, Task, Link, Sprint, Comment, Message])