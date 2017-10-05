import enum
from crm.db import db, BaseModel, RootModel
from crm.countries import countries

CountriesEnum = enum.Enum('Countries', {v: v for k, v in countries.items()})

CountriesEnum.__str__ = lambda self: self.value


class Address(db.Model, BaseModel, RootModel):

    __tablename__ = "addresses"

    street_number = db.Column(
        db.String(255),
        nullable=""
    )

    street_name = db.Column(
        db.String(255),
        default=""
    )
    description = db.Column(
        db.Text(),
        default=""
    )

    zip_code = db.Column(
        db.String(255)
    )

    country = db.Column(db.Enum(CountriesEnum),
                        default=CountriesEnum.Belgium)

    contact_id = db.Column(
        db.String(5),
        db.ForeignKey('contacts.id')
    )

    @property
    def formatted_address(self):
        return "{} {} {}".format(self.street_number or '', self.street_name or '', self.country or '').strip()

    def __str__(self):
        return self.formatted_address
