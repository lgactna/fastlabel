"""
Replicate https://caseontology.org/examples/asgard using our bindings as closely
as possible.
"""

from pprint import pprint

from fastlabel.uco import observable

disk_facet = observable.FileFacet(
    observableCreatedTime="2019-03-30T22:12:19.32Z",
    extension="dd",
    fileName="AsgardPD-2019033001-01.dd",
    filePath="C:/evidence/AsgardPD-2019033001-01.dd",
    isDirectory=False,
    sizeInBytes=160080500,
)

# TODO: apparently hasFacet is an iterable?? looks like there is some work to be
# done here... i don't know when things should be considered lists or not, either
# we have to edit the .ttl or change the logic used to determine iterable vs. scalar
obj = observable.Image(hasFacet=disk_facet)

# https://docs.pydantic.dev/latest/concepts/serialization/#serializing-with-duck-typing
# Normally models are dumped recursively, but fields present in a subclass and not
# in a parent class are not dumped by default. serialize_as_any must be passed.
pprint(obj.model_dump(serialize_as_any=True))


# TODO: honestly i don't know how IRIs work anymore lmao
application_version = observable.ApplicationVersion(
    version="1.0",
)
application_facet = observable.ApplicationFacet(
    installedVersionHistory=application_version
)
pprint(application_facet.model_dump(serialize_as_any=True))
