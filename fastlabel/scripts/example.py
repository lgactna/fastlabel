"""
This script emulates the CASE-Mapping-Python example script to demonstrate feature
parity.

https://github.com/casework/CASE-Mapping-Python/blob/main/example.py
"""

import json
from datetime import UTC, datetime, timedelta

from rdflib import Graph, Namespace

from fastlabel import case, uco

bundle_identity = uco.identity.Identity()
bundle_identity_name = uco.identity.SimpleNameFacet(
    givenName="Maurice", familyName="Moss"
)
bundle_identity.hasFacet.append(bundle_identity_name)

bundle_created_time = datetime.strptime(
    "2024-04-28T21:38:19", "%Y-%m-%dT%H:%M:%S"
).astimezone(UTC)
bundle_modified_time = datetime.strptime(
    "2024-05-02T21:38:19", "%Y-%m-%dT%H:%M:%S"
).astimezone(UTC)

# This is an example of where bundle_identity ought to be passed in as a
# reference. This means that only the @id field is attached to this node,
# even though this is technically a copy of the "full" object.
bundle = uco.core.Bundle(
    createdBy=[bundle_identity.ref()],
    description="An Example Case File",
    modifiedTime=bundle_modified_time,
    name="json ld file",
    objectCreatedTime=bundle_created_time,
    specVersion="UCO/CASE 2.0",
    tag="Artifacts extracted from a mobile phone",
)
bundle.object.append(bundle_identity)

investigation_items: list[uco.core.UcoObject] = []

############################################
# A DeviceFacet and a OperatingSystemFacet #
############################################

device_camera = uco.observable.ObservableObject()
manufacturer_nikon = uco.identity.Organization(name="Nikon")
bundle.object.append(manufacturer_nikon)
device1 = uco.observable.DeviceFacet(manufacturer=manufacturer_nikon, model="D750")
os_date = datetime.strptime("2023-02-19T09:22:09", "%Y-%m-%dT%H:%M:%S").astimezone(UTC)

os_env_vars = {
    "path": "/opt/local/bin:/opt/local/sbin:/usr/bin:",
    "temp": "/tmp:/usr/temp",
    "systemroot": "/root",
}
manufacturer_apple = uco.identity.Organization(name="Apple")

# uco-observable:manufacturer and uco-observable:version were deprecated in UCO 2.0.
os_facet = uco.observable.OperatingSystemFacet(
    advertisingID="DX4CDXKN",
    bitness="64-bit",
    installDate=os_date,
    isLimitAdTrackingEnabled=True,
    environmentVariables=uco.types.Dictionary.from_dict(os_env_vars),
)

device_camera.hasFacet.extend([device1, os_facet])
bundle.object.append(device_camera)

##################################
# A file to be added to the case #
##################################

sd_card = uco.observable.ObservableObject()
investigation_items.append(sd_card)

f_date_created = datetime.strptime(
    "2024-04-18T12:06:33", "%Y-%m-%dT%H:%M:%S"
).astimezone(UTC)
f_date_modified = datetime.strptime(
    "2024-04-21T12:06:33", "%Y-%m-%dT%H:%M:%S"
).astimezone(UTC)
f_date_metadata = datetime.strptime(
    "2024-04-21T10:16:43", "%Y-%m-%dT%H:%M:%S"
).astimezone(UTC)

# uco-observable:MimeType only exists on ContentDataFacet. I don't know
# if this was a UCO 2.0 change.
file1 = uco.observable.FileFacet(
    allocationStatus="Contiguous Allocation",
    extension="jpg",
    fileName="IMG_0123.jpg",
    filePath="/sdcard/IMG_0123.jpg",
    isDirectory=False,
    metadataChangeTime=f_date_metadata,
    modifiedTime=f_date_modified,
    observableCreatedTime=f_date_created,
    sizeInBytes=35002,
)

# hashmethod and hashvalue are not members of ContentDataFacet in UCO 2.0.
file_content1 = uco.observable.ContentDataFacet(
    byteOrder=uco.vocabulary.EndiannessTypeVocab.BIG_ENDIAN,
    magicNumber="/9j/ww==",
    mimeType="image/jpeg",
    sizeInBytes=35000,
    dataPayload="<base 64 encoded data of the file>",
    hash=uco.types.Hash(
        hashMethod=uco.vocabulary.HashNameVocab.SHA256,
        hashValue=uco.XMLSchema.xsd_hexBinary(
            "11122273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"
        ),
    ),
)
file_raster1 = uco.observable.RasterPictureFacet(
    pictureType="jpg", pictureHeight=12345, pictureWidth=12346, bitsPerPixel=2
)

exif = {"Make": "Canon", "Model": "Powershot"}
file_exif1 = uco.observable.EXIFFacet(
    exifData=uco.types.ControlledDictionary.from_dict(exif)
)
sd_card.hasFacet.extend([file1, file_content1, file_raster1, file_exif1])
bundle.object.append(sd_card)

#######################################
# An investigative action on a device #
#######################################

inv_act = case.investigation.InvestigativeAction(
    name="annotated",
    startTime=datetime.now(UTC),
    endTime=datetime.now(UTC),
)
investigation_items.append(inv_act)
bundle.object.append(manufacturer_apple)

device_iphone = uco.observable.DeviceFacet(
    deviceType="iPhone",
    manufacturer=manufacturer_apple,
    model="6XS",
    serialNumber="77",
)
inv_act.hasFacet.append(device_iphone)
bundle.object.append(inv_act)

#############################################################
# Another investigative action on a device, multiple facets #
#############################################################

inv_act9 = case.investigation.InvestigativeAction(
    name="annotated",
    startTime=datetime.now(UTC),
    endTime=datetime.now(UTC),
)
dummy_observable = uco.observable.ObservableObject(
    state="this is a dummy observable created as an example"
)

manufacturer_oneplus = uco.identity.Organization(name="oneplus")
manufacturer_oneplus = uco.identity.Organization(name="oneplus")
bundle.object.append(manufacturer_oneplus)

device9 = uco.observable.DeviceFacet(
    deviceType="Android",
    manufacturer=manufacturer_oneplus,
    model="8",
    serialNumber="123123",
)
inv_act9.hasFacet.append(device9)
bundle.object.append(inv_act9)

##############################
# Adding a CASE Relationship #
##############################

cyber_rel1 = uco.observable.ObservableRelationship(
    source=device_camera,
    target=sd_card,
    kindOfRelationship=uco.vocabulary.ObservableObjectRelationshipVocab.CONTAINED_WITHIN,
    isDirectional=True,
)
path_rel1 = uco.observable.PathRelationFacet(path="/sdcard/IMG_0123.jpg")
cyber_rel1.hasFacet.append(path_rel1)
bundle.object.append(cyber_rel1)

##############################
#       Adding an Email      #
##############################

# Email addresses
email_address_object_1 = uco.observable.ObservableObject()
email_address_1 = uco.observable.EmailAddressFacet(
    addressValue="info@example.com",
    displayName="Example User",
)
email_address_object_1.hasFacet.append(email_address_1)

email_account_object_1 = uco.observable.ObservableObject()
account_1 = uco.observable.EmailAccountFacet(emailAddress=email_account_object_1)
# If we don't use a reference here, we get infinite recursion
email_account_object_1.hasFacet.append(account_1.ref())
bundle.object.extend([email_account_object_1, email_address_object_1])

email_address_object_2 = uco.observable.ObservableObject()
email_address_2 = uco.observable.EmailAddressFacet(
    addressValue="admin@example.com",
    displayName="Example Admin",
)
email_address_object_2.hasFacet.append(email_address_2)

email_account_object_2 = uco.observable.ObservableObject()
account_2 = uco.observable.EmailAccountFacet(emailAddress=email_account_object_2)
email_account_object_2.hasFacet.append(account_2.ref())
bundle.object.extend([email_account_object_2, email_address_object_2])

##############################
#  Adding an Email Message   #
##############################

cyber_item3 = uco.observable.ObservableObject()
email_msg = uco.observable.EmailMessageFacet(
    to=[email_account_object_1, email_account_object_2],
    from_=email_address_object_1,
    subject="Thoughts on Our Next Book Club Pick?",
    body="Hello fellow bookworms! It's that time again.",
    sentTime=datetime.now(UTC),
    receivedTime=datetime.now(UTC),
    messageID="<1234567890@example.com>",
)
cyber_item3.hasFacet.append(email_msg)
bundle.object.append(cyber_item3)

###################################################
#  Adding a UrlHistoryFacet and UrlHistoryEntries #
###################################################

url_object = uco.observable.ObservableObject()
url_facet = uco.observable.URLFacet(
    fullValue="www.docker.com/howto",
)
url_object.hasFacet.append(url_facet)
bundle.object.append(url_object)

browser_object = uco.observable.ObservableObject()
browser_facet = uco.observable.ApplicationFacet(
    applicationIdentifier="Safari",
)
browser_object.hasFacet.append(browser_facet)
bundle.object.append(browser_object)

url_date_expiration = datetime.strptime(
    "2024-12-27T14:55:01", "%Y-%m-%dT%H:%M:%S"
).astimezone(UTC)
url_date_first = datetime.strptime(
    "2024-01-02T15:55:01", "%Y-%m-%dT%H:%M:%S"
).astimezone(UTC)
url_date_last = datetime.strptime(
    "2024-02-10T10:55:01", "%Y-%m-%dT%H:%M:%S"
).astimezone(UTC)

history_entry_1 = uco.observable.URLHistoryEntry(
    browserUserProfile="Jill",
    expirationTime=url_date_expiration,
    firstVisit=url_date_first,
    hostname="case_test",
    keywordSearchTerm="docker",
    lastVisit=url_date_last,
    manuallyEnteredCount=10,
    pageTitle="Docker tutorial",
    referrerUrl=url_object,
    url=url_object,
    visitCount=18,
)

history_entry_2 = uco.observable.URLHistoryEntry(
    browserUserProfile="Tamasin",
    expirationTime=url_date_expiration,
    firstVisit=url_date_first,
    hostname="case_test",
    keywordSearchTerm="git actions",
    lastVisit=url_date_last,
    manuallyEnteredCount=21,
    pageTitle="GitHub actions tutorial",
    referrerUrl=url_object,
    url=url_object,
    visitCount=38,
)

url_history_entry_object = uco.observable.ObservableObject()

url_history_facet = uco.observable.URLHistoryFacet(
    browserInformation=browser_object,
    urlHistoryEntry=[history_entry_1, history_entry_2],
)
url_history_entry_object.hasFacet.append(url_history_facet)
bundle.object.append(url_history_entry_object)

############################
# Adding an SMS Account    #
############################

# Phone accounts
phone_account_object = uco.observable.ObservableObject()
phone_account1 = uco.observable.PhoneAccountFacet(
    phoneNumber="123456",
)
phone_account_object.hasFacet.append(phone_account1)
bundle.object.append(phone_account_object)

phone_account_object2 = uco.observable.ObservableObject()
phone_account2 = uco.observable.PhoneAccountFacet(
    phoneNumber="987654",
)
phone_account_object2.hasFacet.append(phone_account2)
bundle.object.append(phone_account_object2)

############################
# Adding an SMS Message    #
############################
cyber_item4 = uco.observable.ObservableObject()
application_cyber_item = uco.observable.ObservableObject()
sms_application = uco.observable.ApplicationFacet(
    applicationIdentifier="WhatsApp",
)
application_cyber_item.hasFacet.append(sms_application)

sms_msg = uco.observable.MessageFacet(
    to=[phone_account_object, phone_account_object2],
    from_=phone_account_object,
    messageText="Are you free this weekend?",
    sentTime=datetime.now(UTC),
    application=application_cyber_item,
)

cyber_item4.hasFacet.append(sms_msg)
bundle.object.extend([cyber_item4, application_cyber_item])

############################
#     Adding an Identity   #
############################

identity = uco.identity.Identity()
identity_name = uco.identity.SimpleNameFacet(
    givenName="Davey",
    familyName="Jones",
)
identity_birth = uco.identity.BirthInformationFacet(
    birthdate=datetime.now(UTC) - timedelta(days=30 * 365),
)
identity.hasFacet.extend([identity_name, identity_birth])
bundle.object.append(identity)

############################
#     Adding a Location    #
############################

location1 = uco.location.Location()
lat_long = uco.location.LatLongCoordinatesFacet(
    latitude=61.185055,
    longitude=9.468836,
)
location1.hasFacet.append(lat_long)
bundle.object.append(location1)

##################################
# Adding the investigation items #
##################################

investigation = case.investigation.Investigation(
    focus="Transfer of Illicit Materials",
    name="Crime A",
    description=(
        "Inquiry into the transfer of illicit materials and "
        "the devices used to do so"
    ),
    object=investigation_items,
)
bundle.object.append(investigation)

# ... There's more, but this is sufficient to prove it works

with open("example.jsonld", "wt+") as f:
    # model_dump_json doesn't work because XMLSchema doesn't have any JSOON
    # serializers provided - this is fine, though not great
    data = bundle.model_dump(serialize_as_any=True)
    f.write(json.dumps(data, indent=2))

# Demonstrate that this is a legal JSON-LD file
g = Graph()

# Parse the local JSON-LD file
g.parse("example.jsonld", format="json-ld")

# Print the number of triples in the graph
print(f"Graph has {len(g)} triples.")

UCO_CORE = Namespace("https://ontology.unifiedcyberontology.org/uco/core/")

# Query the graph to extract all "uco-core:createdBy" entries
created_by_entries = set()
for _s, _p, o in g.triples((None, UCO_CORE.createdBy, None)):
    created_by_entries.add(o)

# Print the extracted "uco-core:createdBy" entries
for entry in created_by_entries:
    print("uco-core:createdBy")
    for s, p, o in g.triples((entry, None, None)):
        print(f"  {s} {p} {o}")
