"""
Auto-generated classes from the SHACL graph in location.ttl.

This file was generated using the `case_models.py` script.
"""

from fastlabel.uco import core


class GPSCoordinatesFacet(core.Facet):
    """
    A GPS coordinates facet is a grouping of characteristics unique to the
    expression of quantified dilution of precision (DOP) for an asserted set of
    geolocation coordinates typically associated with satellite navigation such
    as the Global Positioning System (GPS).
    """

    hdop: float | None = None
    pdop: float | None = None
    tdop: float | None = None
    vdop: float | None = None


class LatLongCoordinatesFacet(core.Facet):
    """
    A lat long coordinates facet is a grouping of characteristics unique to the
    expression of a geolocation as the intersection of specific latitude,
    longitude, and altitude values.
    """

    altitude: float | None = None
    latitude: float | None = None
    longitude: float | None = None


class Location(core.UcoObject):
    """
    A location is a geospatial place, site, or position.
    """


class SimpleAddressFacet(core.Facet):
    """
    A simple address facet is a grouping of characteristics unique to a
    geolocation expressed as an administrative address.
    """

    addressType: str | None = None
    country: str | None = None
    locality: str | None = None
    postalCode: str | None = None
    region: str | None = None
    street: str | None = None
