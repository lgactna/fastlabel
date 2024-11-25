"""
Replicate https://caseontology.org/examples/asgard using our bindings as closely
as possible.
"""

import datetime
from pprint import pprint

from fastlabel.uco import observable

disk_facet = observable.FileFacet(
    observableCreatedTime=datetime.datetime.now(datetime.UTC),
    extension="dd",
    fileName="AsgardPD-2019033001-01.dd",
    filePath="C:/evidence/AsgardPD-2019033001-01.dd",
    isDirectory=False,
    sizeInBytes=160080500,
)

obj = observable.Image(hasFacet=disk_facet)

# https://docs.pydantic.dev/latest/concepts/serialization/#serializing-with-duck-typing
# Normally models are dumped recursively, but fields present in a subclass and not
# in a parent class are not dumped by default. serialize_as_any must be passed.
pprint(obj.model_dump(serialize_as_any=True))

application_version = observable.ApplicationVersion(
    version="1.0",
)

# The unknowability of knowing if something should be a reference or not means
# that I've decided to support both patterns. If you want something to be a reference,
# you can call the ref() method to get a copy of the object marked as a reference.
#
# At that point, you can work on either object, since the only thing that matters
# is the @id field, which is the same for both objects.
application_facet = observable.ApplicationFacet(
    installedVersionHistory=[application_version.ref(), application_version]
)

pprint(application_facet.model_dump(serialize_as_any=True))
