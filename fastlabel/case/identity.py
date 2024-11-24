"""
Auto-generated classes from the SHACL graph in identity.ttl.

This file was generated using the `case_models.py` script.
"""

from enum import Enum
from typing import Any, Optional

from fastlabel.case import core, location


class Identity(core.IdentityAbstraction):
    """
    An identity is a grouping of identifying characteristics unique to an
    individual or organization.
    """

    pass


class IdentityFacet(core.Facet):
    """
    An identity facet is a grouping of characteristics unique to a particular
    aspect of an identity.
    """

    pass


class Organization(Identity):
    """
    An organization is a grouping of identifying characteristics unique to a
    group of people who work together in an organized way for a shared purpose.
    [based on
    https://dictionary.cambridge.org/us/dictionary/english/organization]
    """

    pass


class Person(Identity):
    """
    A person is a grouping of identifying characteristics unique to a human
    being regarded as an individual. [based on
    https://www.lexico.com/en/definition/person]
    """

    pass


class AddressFacet(IdentityFacet):
    """
    An address facet is a grouping of characteristics unique to an
    administrative identifier for a geolocation associated with a specific
    identity.
    """

    address: Optional[location.Location] = None


class AffiliationFacet(IdentityFacet):
    """
    An affiliation is a grouping of characteristics unique to the established
    affiliations of an entity.
    """

    pass


class BirthInformationFacet(IdentityFacet):
    """
    Birth information is a grouping of characteristics unique to information
    pertaining to the birth of an entity.
    """

    birthdate: Optional[str] = None


class CountryOfResidenceFacet(IdentityFacet):
    """
    Country of residence is a grouping of characteristics unique to information
    related to the country, or countries, where an entity resides.
    """

    pass


class EventsFacet(IdentityFacet):
    """
    Events is a grouping of characteristics unique to information related to
    specific relevant things that happen in the lifetime of an entity.
    """

    pass


class IdentifierFacet(IdentityFacet):
    """
    Identifier is a grouping of characteristics unique to information that
    uniquely and specifically identities an entity.
    """

    pass


class LanguagesFacet(IdentityFacet):
    """
    Languages is a grouping of characteristics unique to specific syntactically
    and grammatically standardized forms of communication (human or computer) in
    which an entity has proficiency (comprehends, speaks, reads, or writes).
    """

    pass


class NationalityFacet(IdentityFacet):
    """
    Nationality is a grouping of characteristics unique to the condition of an
    entity belonging to a particular nation.
    """

    pass


class OccupationFacet(IdentityFacet):
    """
    Occupation is a grouping of characteristics unique to the job or profession
    of an entity.
    """

    pass


class OrganizationDetailsFacet(IdentityFacet):
    """
    Organization details is a grouping of characteristics unique to an identity
    representing an administrative and functional structure.
    """

    pass


class PersonalDetailsFacet(IdentityFacet):
    """
    Personal details is a grouping of characteristics unique to an identity
    representing an individual person.
    """

    pass


class PhysicalInfoFacet(IdentityFacet):
    """
    Physical info is a grouping of characteristics unique to the outwardly
    observable nature of an individual person.
    """

    pass


class QualificationFacet(IdentityFacet):
    """
    Qualification is a grouping of characteristics unique to particular skills,
    capabilities or their related achievements (educational, professional, etc.)
    of an entity.
    """

    pass


class RelatedIdentityFacet(IdentityFacet):
    """
    <Needs fleshed out from CIQ>
    """

    pass


class SimpleNameFacet(IdentityFacet):
    """
    A simple name facet is a grouping of characteristics unique to the personal
    name (e.g., Dr. John Smith Jr.) held by an identity.
    """

    familyName: Optional[str] = None
    givenName: Optional[str] = None
    honorificPrefix: Optional[str] = None
    honorificSuffix: Optional[str] = None


class VisaFacet(IdentityFacet):
    """
    Visa is a grouping of characteristics unique to information related to a
    person's ability to enter, leave, or stay for a specified period of time in
    a country.
    """

    pass
