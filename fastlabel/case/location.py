"""
Auto-generated classes from the SHACL graph in location.ttl.

This file was generated using the `case_models.py` script.
"""

from typing import Any, Optional

from fastlabel.case import core


class SimpleAddressFacet(core.Facet):
    """
    A simple address facet is a grouping of characteristics unique to a
    geolocation expressed as an administrative address.
    """

    addressType: Optional[str] = None
    country: Optional[str] = None
    locality: Optional[str] = None
    postalCode: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None


class LatLongCoordinatesFacet(core.Facet):
    """
    A lat long coordinates facet is a grouping of characteristics unique to the
    expression of a geolocation as the intersection of specific latitude,
    longitude, and altitude values.
    """

    altitude: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class GPSCoordinatesFacet(core.Facet):
    """
    A GPS coordinates facet is a grouping of characteristics unique to the
    expression of quantified dilution of precision (DOP) for an asserted set of
    geolocation coordinates typically associated with satellite navigation such
    as the Global Positioning System (GPS).
    """

    hdop: Optional[float] = None
    pdop: Optional[float] = None
    tdop: Optional[float] = None
    vdop: Optional[float] = None


class Location(core.UcoObject):
    """
    A location is a geospatial place, site, or position.
    """

    pass
