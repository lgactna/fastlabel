
"""
Auto-generated classes from the SHACL graph in identity.ttl.

This file was generated using the `case_models.py` script.
"""

class EventsFacet(identity.IdentityFacet):
    """
    Events is a grouping of characteristics unique to information related to
    specific relevant things that happen in the lifetime of an entity.
    """


class RelatedIdentityFacet(identity.IdentityFacet):
    """
    <Needs fleshed out from CIQ>
    """


class Organization(identity.Identity):
    """
    An organization is a grouping of identifying characteristics unique to a
    group of people who work together in an organized way for a shared purpose.
    [based on
    https://dictionary.cambridge.org/us/dictionary/english/organization]
    """


class Identity(core.IdentityAbstraction):
    """
    An identity is a grouping of identifying characteristics unique to an
    individual or organization.
    """


class SimpleNameFacet(identity.IdentityFacet):
    """
    A simple name facet is a grouping of characteristics unique to the personal
    name (e.g., Dr. John Smith Jr.) held by an identity.
    """

    familyName: Optional[str] = None
    givenName: Optional[str] = None
    honorificPrefix: Optional[str] = None
    honorificSuffix: Optional[str] = None

class BirthInformationFacet(identity.IdentityFacet):
    """
    Birth information is a grouping of characteristics unique to information
    pertaining to the birth of an entity.
    """

    birthdate: Optional[str] = None

class QualificationFacet(identity.IdentityFacet):
    """
    Qualification is a grouping of characteristics unique to particular skills,
    capabilities or their related achievements (educational, professional, etc.)
    of an entity.
    """


class LanguagesFacet(identity.IdentityFacet):
    """
    Languages is a grouping of characteristics unique to specific syntactically
    and grammatically standardized forms of communication (human or computer) in
    which an entity has proficiency (comprehends, speaks, reads, or writes).
    """


class NationalityFacet(identity.IdentityFacet):
    """
    Nationality is a grouping of characteristics unique to the condition of an
    entity belonging to a particular nation.
    """


class IdentityFacet(core.Facet):
    """
    An identity facet is a grouping of characteristics unique to a particular
    aspect of an identity.
    """


class Person(identity.Identity):
    """
    A person is a grouping of identifying characteristics unique to a human
    being regarded as an individual. [based on
    https://www.lexico.com/en/definition/person]
    """


class PhysicalInfoFacet(identity.IdentityFacet):
    """
    Physical info is a grouping of characteristics unique to the outwardly
    observable nature of an individual person.
    """


class OccupationFacet(identity.IdentityFacet):
    """
    Occupation is a grouping of characteristics unique to the job or profession
    of an entity.
    """


class AffiliationFacet(identity.IdentityFacet):
    """
    An affiliation is a grouping of characteristics unique to the established
    affiliations of an entity.
    """


class PersonalDetailsFacet(identity.IdentityFacet):
    """
    Personal details is a grouping of characteristics unique to an identity
    representing an individual person.
    """


class CountryOfResidenceFacet(identity.IdentityFacet):
    """
    Country of residence is a grouping of characteristics unique to information
    related to the country, or countries, where an entity resides.
    """


class AddressFacet(identity.IdentityFacet):
    """
    An address facet is a grouping of characteristics unique to an
    administrative identifier for a geolocation associated with a specific
    identity.
    """

    address: Optional[Location] = None

class OrganizationDetailsFacet(identity.IdentityFacet):
    """
    Organization details is a grouping of characteristics unique to an identity
    representing an administrative and functional structure.
    """


class VisaFacet(identity.IdentityFacet):
    """
    Visa is a grouping of characteristics unique to information related to a
    person's ability to enter, leave, or stay for a specified period of time in
    a country.
    """


class IdentifierFacet(identity.IdentityFacet):
    """
    Identifier is a grouping of characteristics unique to information that
    uniquely and specifically identities an entity.
    """


