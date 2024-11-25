"""
Auto-generated classes from the SHACL graph in observable.ttl.

This file was generated using the `case_models.py` script.
"""

from enum import Enum

from pydantic import AwareDatetime, Field

from fastlabel.uco import (
    XMLSchema,
    action,
    configuration,
    core,
    identity,
    location,
    types,
    vocabulary,
)


class NetworkSocketAddressFamily(str, Enum):
    AF_APPLETALK = "af_appletalk"
    AF_BTH = "af_bth"
    AF_INET = "af_inet"
    AF_INET6 = "af_inet6"
    AF_IPX = "af_ipx"
    AF_IRDA = "af_irda"
    AF_NETBIOS = "af_netbios"
    AF_UNSPEC = "af_unspec"


class NetworkSocketProtocolFamily(str, Enum):
    PF_APPLETALK = "pf_appletalk"
    PF_ASH = "pf_ash"
    PF_ATMPVC = "pf_atmpvc"
    PF_ATMSVC = "pf_atmsvc"
    PF_AX25 = "pf_ax25"
    PF_BLUETOOTH = "pf_bluetooth"
    PF_BRIDGE = "pf_bridge"
    PF_DECNET = "pf_decnet"
    PF_ECONET = "pf_econet"
    PF_INET = "pf_inet"
    PF_INET6 = "pf_inet6"
    PF_IPX = "pf_ipx"
    PF_IRDA = "pf_irda"
    PF_KEY = "pf_key"
    PF_NETBEUI = "pf_netbeui"
    PF_NETLINK = "pf_netlink"
    PF_NETROM = "pf_netrom"
    PF_PACKET = "pf_packet"
    PF_PPPOX = "pf_pppox"
    PF_ROSE = "pf_rose"
    PF_ROUTE = "pf_route"
    PF_SECURITY = "pf_security"
    PF_SNA = "pf_sna"
    PF_WANPIPE = "pf_wanpipe"
    PF_X25 = "pf_x25"


class NetworkSocketType(str, Enum):
    SOCK_DGRAM = "sock_dgram"
    SOCK_RAW = "sock_raw"
    SOCK_RDM = "sock_rdm"
    SOCK_SEQPACKET = "sock_seqpacket"
    SOCK_STREAM = "sock_stream"


class RegistryDatatype(str, Enum):
    REG_BINARY = "reg_binary"
    REG_DWORD = "reg_dword"
    REG_DWORD_BIG_ENDIAN = "reg_dword_big_endian"
    REG_EXPAND_SZ = "reg_expand_sz"
    REG_FULL_RESOURCE_DESCRIPTOR = "reg_full_resource_descriptor"
    REG_INVALID_TYPE = "reg_invalid_type"
    REG_LINK = "reg_link"
    REG_MULTI_SZ = "reg_multi_sz"
    REG_NONE = "reg_none"
    REG_QWORD = "reg_qword"
    REG_RESOURCE_LIST = "reg_resource_list"
    REG_RESOURCE_REQUIREMENTS_LIST = "reg_resource_requirements_list"
    REG_SZ = "reg_sz"


class WindowsPEBinaryType(str, Enum):
    DLL = "dll"
    EXE = "exe"
    SYS = "sys"


class WindowsServiceStartType(str, Enum):
    SERVICE_AUTO_START = "service_auto_start"
    SERVICE_BOOT_START = "service_boot_start"
    SERVICE_DEMAND_START = "service_demand_start"
    SERVICE_DISABLED = "service_disabled"
    SERVICE_SYSTEM_ALERT = "service_system_alert"


class WindowsServiceStatus(str, Enum):
    SERVICE_CONTINUE_PENDING = "service_continue_pending"
    SERVICE_PAUSE_PENDING = "service_pause_pending"
    SERVICE_PAUSED = "service_paused"
    SERVICE_RUNNING = "service_running"
    SERVICE_START_PENDING = "service_start_pending"
    SERVICE_STOP_PENDING = "service_stop_pending"
    SERVICE_STOPPED = "service_stopped"


class WindowsServiceType(str, Enum):
    SERVICE_FILE_SYSTEM_DRIVER = "service_file_system_driver"
    SERVICE_KERNEL_DRIVER = "service_kernel_driver"
    SERVICE_WIN32_OWN_PROCESS = "service_win32_own_process"
    SERVICE_WIN32_SHARE_PROCESS = "service_win32_share_process"


class DefinedEffectFacet(core.Facet):
    """
    A defined effect facet is a grouping of characteristics unique to the effect
    of an observable action in relation to one or more observable objects.
    """


class NTFSFilePermissionsFacet(core.Facet):
    """
    An NTFS file permissions facet is a grouping of characteristics unique to
    the access rights (e.g., view, change, navigate, execute) of a file on an
    NTFS (new technology filesystem) file system.
    """


class UNIXFilePermissionsFacet(core.Facet):
    """
    A UNIX file permissions facet is a grouping of characteristics unique to the
    access rights (e.g., view, change, navigate, execute) of a file on a UNIX
    file system.
    """


class AccountAuthenticationFacet(core.Facet):
    """
    An account authentication facet is a grouping of characteristics unique to
    the mechanism of accessing an account.
    """

    passwordLastChanged: AwareDatetime | None = None
    password: str | None = None
    passwordType: str | None = None


class ArchiveFileFacet(core.Facet):
    """
    An archive file facet is a grouping of characteristics unique to a file that
    is composed of one or more computer files along with metadata.
    """

    archiveType: str | None = None
    comment: str | None = None
    version: str | None = None


class CellSiteFacet(core.Facet):
    """
    A cell site facet contains the metadata surrounding the cell site.
    """

    cellSiteCountryCode: str | None = None
    cellSiteIdentifier: str | None = None
    cellSiteLocationAreaCode: str | None = None
    cellSiteNetworkCode: str | None = None
    cellSiteType: str | None = None


class DigitalAddressFacet(core.Facet):
    """
    A digital address facet is a grouping of characteristics unique to an
    identifier assigned to enable routing and management of digital
    communication.
    """

    addressValue: str | None = None
    displayName: str | None = None


class EncodedStreamFacet(core.Facet):
    """
    An encoded stream facet is a grouping of characteristics unique to the
    conversion of a body of data content from one form to another form.
    """

    encodingMethod: str | None = None


class EncryptedStreamFacet(core.Facet):
    """
    An encrypted stream facet is a grouping of characteristics unique to the
    conversion of a body of data content from one form to another obfuscated
    form in such a way that reversing the conversion to obtain the original data
    form can only be accomplished through possession and use of a specific key.
    """

    encryptionMethod: str | None = None
    encryptionMode: str | None = None
    encryptionIV: str | list[str] | None = []
    encryptionKey: str | list[str] | None = []


class ImageFacet(core.Facet):
    """
    An image facet is a grouping of characteristics unique to a complete copy of
    a hard disk, memory, or other digital media.
    """

    imageType: str | None = None


class LibraryFacet(core.Facet):
    """
    A library facet is a grouping of characteristics unique to a suite of data
    and programming code that is used to develop software programs and
    applications. [based on
    https://www.techopedia.com/definition/3828/software-library]
    """

    libraryType: str | None = None


class MobileAccountFacet(core.Facet):
    """
    A mobile account facet is a grouping of characteristics unique to an
    arrangement with an entity to enable and control the provision of some
    capability or service on a portable computing device. [based on
    https://www.lexico.com/definition/mobile_device]
    """

    IMSI: str | None = None
    MSISDN: str | None = None
    MSISDNType: str | None = None


class PathRelationFacet(core.Facet):
    """
    A path relation facet is a grouping of characteristics unique to the
    location of one object within another containing object.
    """

    path: str | list[str] | None = []


class PhoneAccountFacet(core.Facet):
    """
    A phone account facet is a grouping of characteristics unique to an
    arrangement with an entity to enable and control the provision of a
    telephony capability or service.
    """

    phoneNumber: str | None = None


class PropertiesEnumeratedEffectFacet(core.Facet):
    """
    A properties enumerated effect facet is a grouping of characteristics unique
    to the effects of actions upon observable objects where a characteristic of
    the observable object is enumerated. An example of this would be startup
    parameters for a process.
    """

    properties: str | None = None


class UNIXVolumeFacet(core.Facet):
    """
    A UNIX volume facet is a grouping of characteristics unique to a single
    accessible storage area (volume) with a single UNIX file system. [based on
    https://en.wikipedia.org/wiki/Volume_(computing)]
    """

    mountPoint: str | None = None
    options: str | None = None


class WindowsAccountFacet(core.Facet):
    """
    A Windows account facet is a grouping of characteristics unique to a user
    account on a Windows operating system.
    """

    groups: str | list[str] | None = []


class WindowsActiveDirectoryAccountFacet(core.Facet):
    """
    A Windows Active Directory account facet is a grouping of characteristics
    unique to an account managed by directory-based identity-related services of
    a Windows operating system.
    """

    objectGUID: str | None = None
    activeDirectoryGroups: str | list[str] | None = []


class WindowsRegistryHiveFacet(core.Facet):
    """
    A Windows registry hive facet is a grouping of characteristics unique to a
    particular logical group of keys, subkeys, and values in a Windows registry
    (a hierarchical database that stores low-level settings for the Microsoft
    Windows operating system and for applications that opt to use the registry).
    [based on https://en.wikipedia.org/wiki/Windows_Registry]
    """

    hiveType: str | None = None


class WindowsServiceFacet(core.Facet):
    """
    A Windows service facet is a grouping of characteristics unique to a
    specific Windows service (a computer program that operates in the background
    of a Windows operating system, similar to the way a UNIX daemon runs on
    UNIX). [based on https://en.wikipedia.org/wiki/Windows_service]
    """

    displayName: str | None = None
    groupName: str | None = None
    serviceName: str | None = None
    serviceStatus: str | None = None
    serviceType: str | None = None
    startCommandLine: str | None = None
    startType: str | None = None
    descriptions: str | list[str] | None = []


class WirelessNetworkConnectionFacet(core.Facet):
    """
    A wireless network connection facet is a grouping of characteristics unique
    to a connection (completed or attempted) across an IEEE 802.11
    standards-conformant digital network (a group of two or more computer
    systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]
    """

    baseStation: str | None = None
    password: str | None = None
    ssid: str | None = None


class X509V3ExtensionsFacet(core.Facet):
    """
    An X.509 v3 certificate extensions facet is a grouping of characteristics
    unique to a public key digital identity certificate conformant to the X.509
    v3 PKI (Public Key Infrastructure) standard.
    """

    privateKeyUsagePeriodNotAfter: AwareDatetime | None = None
    privateKeyUsagePeriodNotBefore: AwareDatetime | None = None
    authorityKeyIdentifier: str | None = None
    basicConstraints: str | None = None
    certificatePolicies: str | None = None
    crlDistributionPoints: str | None = None
    extendedKeyUsage: str | None = None
    inhibitAnyPolicy: str | None = None
    issuerAlternativeName: str | None = None
    keyUsage: str | None = None
    nameConstraints: str | None = None
    policyConstraints: str | None = None
    policyMappings: str | None = None
    subjectAlternativeName: str | None = None
    subjectDirectoryAttributes: str | None = None
    subjectKeyIdentifier: str | None = None


class DigitalAccountFacet(core.Facet):
    """
    A digital account facet is a grouping of characteristics unique to an
    arrangement with an entity to enable and control the provision of some
    capability or service within the digital domain.
    """

    isDisabled: bool | None = None
    firstLoginTime: AwareDatetime | None = None
    lastLoginTime: AwareDatetime | None = None
    displayName: str | None = None
    accountLogin: str | list[str] | None = []


class DomainNameFacet(core.Facet):
    """
    A domain name facet is a grouping of characteristics unique to an
    identification string that defines a realm of administrative autonomy,
    authority or control within the Internet. [based on
    https://en.wikipedia.org/wiki/Domain_name]
    """

    isTLD: bool | None = None
    value: str | None = None


class MutexFacet(core.Facet):
    """
    A mutex facet is a grouping of characteristics unique to a mechanism that
    enforces limits on access to a resource when there are many threads of
    execution. A mutex is designed to enforce a mutual exclusion concurrency
    control policy, and with a variety of possible methods there exists multiple
    unique implementations for different applications. [based on
    https://en.wikipedia.org/wiki/Lock_(computer_science)]
    """

    isNamed: bool | None = None
    mutexName: str | None = None


class SMSMessageFacet(core.Facet):
    """
    A SMS message facet is a grouping of characteristics unique to a message
    conformant to the short message service (SMS) communication protocol
    standards.
    """

    isRead: bool | None = None


class TableFieldFacet(core.Facet):
    """
    A database record facet contains properties associated with a specific table
    record value from a database.
    """

    recordFieldIsNull: bool | None = None
    recordFieldName: str | None = None
    tableName: str | None = None
    tableSchema: str | None = None


class UserAccountFacet(core.Facet):
    """
    A user account facet is a grouping of characteristics unique to an account
    controlling a user's access to a network, system, or platform.
    """

    canEscalatePrivs: bool | None = None
    isPrivileged: bool | None = None
    isServiceAccount: bool | None = None
    homeDirectory: str | None = None


class AccountFacet(core.Facet):
    """
    An account facet is a grouping of characteristics unique to an arrangement
    with an entity to enable and control the provision of some capability or
    service.
    """

    accountIssuer: core.UcoObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    owner: core.UcoObject | None = Field(default=None, json_schema_extra={"IRI": True})
    isActive: bool | None = None
    expirationTime: AwareDatetime | None = None
    modifiedTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    accountIdentifier: str | None = None
    accountType: (
        vocabulary.AccountTypeVocab | list[vocabulary.AccountTypeVocab] | None
    ) = []


class FilePermissionsFacet(core.Facet):
    """
    A file permissions facet is a grouping of characteristics unique to the
    access rights (e.g., view, change, navigate, execute) of a file on a file
    system.
    """

    owner: core.UcoObject | None = Field(default=None, json_schema_extra={"IRI": True})


class Observable(core.UcoObject):
    """
    An observable is a characterizable item or action within the digital domain.
    """


class AudioFacet(core.Facet):
    """
    An audio facet is a grouping of characteristics unique to a digital
    representation of sound.
    """

    bitRate: int | None = None
    duration: int | None = None
    audioType: str | None = None
    format: str | None = None


class DataRangeFacet(core.Facet):
    """
    A data range facet is a grouping of characteristics unique to a particular
    contiguous scope within a block of digital data.
    """

    rangeOffset: int | None = None
    rangeSize: int | None = None
    rangeOffsetType: str | None = None


class DiskPartitionFacet(core.Facet):
    """
    A disk partition facet is a grouping of characteristics unique to a
    particular managed region on a storage mechanism.
    """

    observableCreatedTime: AwareDatetime | None = None
    partitionLength: int | None = None
    partitionOffset: int | None = None
    spaceLeft: int | None = None
    spaceUsed: int | None = None
    totalSpace: int | None = None
    diskPartitionType: str | None = None
    mountPoint: str | None = None
    partitionID: str | None = None


class ExtInodeFacet(core.Facet):
    """
    An extInode facet is a grouping of characteristics unique to a file system
    object (file, directory, etc.) conformant to the extended file system (EXT
    or related derivations) specification.
    """

    extDeletionTime: AwareDatetime | None = None
    extInodeChangeTime: AwareDatetime | None = None
    extFileType: int | None = None
    extFlags: int | None = None
    extHardLinkCount: int | None = None
    extInodeID: int | None = None
    extPermissions: int | None = None
    extSGID: int | None = None
    extSUID: int | None = None


class FileFacet(core.Facet):
    """
    A file facet is a grouping of characteristics unique to the storage of a
    file (computer resource for recording data discretely in a computer storage
    device) on a file system (process that manages how and where data on a
    storage device is stored, accessed and managed). [based on
    https://en.wikipedia.org/Computer_file and
    https://www.techopedia.com/definition/5510/file-system]
    """

    isDirectory: bool | list[bool] | None = []
    accessedTime: AwareDatetime | None = None
    metadataChangeTime: AwareDatetime | None = None
    modifiedTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    sizeInBytes: int | None = None
    allocationStatus: str | None = None
    extension: str | None = None
    fileName: str | list[str] | None = []
    filePath: str | list[str] | None = []


class FileSystemFacet(core.Facet):
    """
    A file system facet is a grouping of characteristics unique to the process
    that manages how and where data on a storage medium is stored, accessed and
    managed. [based on https://www.techopedia.com/definition/5510/file-system]
    """

    clusterSize: int | None = None
    fileSystemType: str | None = None


class FragmentFacet(core.Facet):
    """
    A fragment facet is a grouping of characteristics unique to an individual
    piece of the content of a file.
    """

    fragmentIndex: int | list[int] | None = []
    totalFragments: int | list[int] | None = []


class MftRecordFacet(core.Facet):
    """
    An MFT record facet is a grouping of characteristics unique to the details
    of a single file as managed in an NTFS (new technology filesystem) master
    file table (which is a collection of information about all files on an NTFS
    filesystem). [based on
    https://docs.microsoft.com/en-us/windows/win32/devnotes/master-file-table]
    """

    mftFileNameAccessedTime: AwareDatetime | None = None
    mftFileNameCreatedTime: AwareDatetime | None = None
    mftFileNameModifiedTime: AwareDatetime | None = None
    mftFileNameRecordChangeTime: AwareDatetime | None = None
    mftRecordChangeTime: AwareDatetime | None = None
    mftFileID: int | None = None
    mftFileNameLength: int | None = None
    mftFlags: int | None = None
    mftParentID: int | None = None
    ntfsHardLinkCount: int | None = None
    ntfsOwnerID: str | None = None
    ntfsOwnerSID: str | None = None


class MobileDeviceFacet(core.Facet):
    """
    A mobile device facet is a grouping of characteristics unique to a portable
    computing device. [based on https://www.lexico.com/definition/mobile_device]
    """

    mockLocationsAllowed: bool | None = None
    clockSetting: AwareDatetime | None = None
    phoneActivationTime: AwareDatetime | None = None
    storageCapacityInBytes: int | None = None
    ESN: str | None = None
    bluetoothDeviceName: str | None = None
    keypadUnlockCode: str | None = None
    network: str | None = None
    IMEI: str | list[str] | None = []


class StorageMediumFacet(core.Facet):
    """
    A storage medium facet is a grouping of characteristics unique to a the
    storage capabilities of a piece of equipment or a mechanism designed to
    serve a special purpose or perform a special function.
    """

    totalStorageCapacityInBytes: int | None = None


class UNIXAccountFacet(core.Facet):
    """
    A UNIX account facet is a grouping of characteristics unique to an account
    on a UNIX operating system.
    """

    gid: int | None = None
    shell: str | None = None


class UNIXProcessFacet(core.Facet):
    """
    A UNIX process facet is a grouping of characteristics unique to an instance
    of a computer program executed on a UNIX operating system.
    """

    openFileDescriptor: int | list[int] | None = []
    ruid: int | list[int] | None = []


class VolumeFacet(core.Facet):
    """
    A volume facet is a grouping of characteristics unique to a single
    accessible storage area (volume) with a single file system. [based on
    https://en.wikipedia.org/wiki/Volume_(computing)]
    """

    sectorSize: int | None = None
    volumeID: str | None = None


class AlternateDataStreamFacet(core.Facet):
    """
    An alternate data stream facet is a grouping of characteristics unique to
    data content stored within an NTFS file that is independent of the standard
    content stream of the file and is hidden from access by default NTFS file
    viewing mechanisms.
    """

    hashes: types.Hash | None = Field(default=None, json_schema_extra={"IRI": True})
    size: int | None = None
    name: str | None = None


class AndroidDeviceFacet(core.Facet):
    """
    An Android device facet is a grouping of characteristics unique to an
    Android device. [based on
    https://en.wikipedia.org/wiki/Android_(operating_system)]
    """

    isADBRootEnabled: bool | None = None
    isSURootEnabled: bool | None = None
    androidID: XMLSchema.xsd_hexBinary | None = None
    androidFingerprint: str | None = None
    androidVersion: str | None = None


class ICMPConnectionFacet(core.Facet):
    """
    An ICMP connection facet is a grouping of characteristics unique to portions
    of a network connection that are conformant to the Internet Control Message
    Protocol (ICMP) standard.
    """

    icmpCode: XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None = []
    icmpType: XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None = []


class TCPConnectionFacet(core.Facet):
    """
    A TCP connection facet is a grouping of characteristics unique to portions
    of a network connection that are conformant to the Transmission Control
    Protocl (TCP) standard.
    """

    destinationFlags: XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None = (
        []
    )
    sourceFlags: XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None = []


class AntennaFacet(core.Facet):
    """
    An antenna alignment facet contains the metadata surrounding the cell
    tower's antenna position.
    """

    antennaHeight: float | None = None
    azimuth: float | None = None
    elevation: float | None = None
    horizontalBeamWidth: float | None = None
    signalStrength: float | None = None
    skew: float | None = None


class CompressedStreamFacet(core.Facet):
    """
    A compressed stream facet is a grouping of characteristics unique to the
    application of a size-reduction process to a body of data content.
    """

    compressionRatio: float | None = None
    compressionMethod: str | None = None


class ApplicationVersion(core.UcoInherentCharacterizationThing):
    """
    An application version is a grouping of characteristics unique to a
    particular software program version.
    """

    installDate: AwareDatetime | None = None
    uninstallDate: AwareDatetime | None = None
    version: str | None = None


class EnvironmentVariable(core.UcoInherentCharacterizationThing):
    """
    An environment variable is a grouping of characteristics unique to a
    dynamic-named value that can affect the way running processes will behave on
    a computer. [based on https://en.wikipedia.org/wiki/Environment_variable]
    """

    name: str | None = None
    value: str | None = None


class GlobalFlagType(core.UcoInherentCharacterizationThing):
    """
    A global flag type is a grouping of characteristics unique to the Windows
    systemwide global variable named NtGlobalFlag that enables various internal
    debugging, tracing, and validation support in the operating system. [based
    on "Windows Global Flags, Chapter 3: System Mechanisms of Windows Internals
    by Solomon, Russinovich, and Ionescu]
    """

    hexadecimalValue: XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None = (
        []
    )
    abbreviation: str | None = None
    destination: str | None = None
    symbolicName: str | None = None


class IComHandlerActionType(core.UcoInherentCharacterizationThing):
    """
    An IComHandler action type is a grouping of characteristics unique to a
    Windows Task-related action that fires a Windows COM handler (smart code in
    the client address space that can optimize calls between a client and
    server). [based on
    https://docs.microsoft.com/en-us/windows/win32/taskschd/comhandleraction]
    """

    comClassID: str | None = None
    comData: str | None = None


class IExecActionType(core.UcoInherentCharacterizationThing):
    """
    An IExec action type is a grouping of characteristics unique to an action
    that executes a command-line operation on a Windows operating system. [based
    on
    https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-iexecaction?redirectedfrom=MSDN]
    """

    execProgramHashes: types.Hash | list[types.Hash] | None = []
    execArguments: str | None = None
    execProgramPath: str | None = None
    execWorkingDirectory: str | None = None


class IShowMessageActionType(core.UcoInherentCharacterizationThing):
    """
    An IShow message action type is a grouping of characteristics unique to an
    action that shows a message box when a task is activate. [based on
    https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-ishowmessageaction?redirectedfrom=MSDN]
    """

    showMessageBody: str | None = None
    showMessageTitle: str | None = None


class WindowsPEFileHeader(core.UcoInherentCharacterizationThing):
    """
    A Windows PE file header is a grouping of characteristics unique to the
    'header' of a Windows PE (Portable Executable) file, consisting of a
    collection of metadata about the overall nature and structure of the file.
    """

    timeDateStamp: AwareDatetime | None = None


class WindowsPESection(core.UcoInherentCharacterizationThing):
    """
    A Windows PE section is a grouping of characteristics unique to a specific
    default or custom-defined region of a Windows PE (Portable Executable) file,
    consisting of an individual portion of the actual executable content of the
    file delineated according to unique purpose and memory protection
    requirements.
    """

    hashes: types.Hash | list[types.Hash] | None = []
    entropy: float | None = None
    size: int | None = None
    name: str | None = None


class WindowsRegistryValue(core.UcoInherentCharacterizationThing):
    """
    A Windows registry value is a grouping of characteristics unique to a
    particular value within a Windows registry (a hierarchical database that
    stores low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry. [based on
    https://en.wikipedia.org/wiki/Windows_Registry]
    """

    name: str | None = None
    data: str | None = None
    dataType: str | None = None


class AutonomousSystemFacet(core.Facet):
    """
    An autonomous system facet is a grouping of characteristics unique to a
    collection of connected Internet Protocol (IP) routing prefixes under the
    control of one or more network operators on behalf of a single
    administrative entity or domain that presents a common, clearly defined
    routing policy to the Internet. [based on
    https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]
    """

    regionalInternetRegistry: (
        vocabulary.RegionalRegistryTypeVocab
        | list[vocabulary.RegionalRegistryTypeVocab]
        | None
    ) = []
    number: int | None = None
    asHandle: str | None = None


class DeviceFacet(core.Facet):
    """
    A device facet is a grouping of characteristics unique to a piece of
    equipment or a mechanism designed to serve a special purpose or perform a
    special function. [based on
    https://www.merriam-webster.com/dictionary/device]
    """

    manufacturer: identity.Identity | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    deviceType: str | None = None
    model: str | None = None
    serialNumber: str | None = None


class DigitalSignatureInfoFacet(core.Facet):
    """
    A digital signature info facet is a grouping of characteristics unique to a
    value calculated via a mathematical scheme for demonstrating the
    authenticity of an electronic message or document.
    """

    certificateSubject: core.UcoObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    certificateIssuer: identity.Identity | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    signatureExists: bool | None = None
    signatureVerified: bool | None = None
    signatureDescription: str | None = None


class SIMCardFacet(core.Facet):
    """
    A SIM card facet is a grouping of characteristics unique to a subscriber
    identification module card intended to securely store the international
    mobile subscriber identity (IMSI) number and its related key, which are used
    to identify and authenticate subscribers on mobile telephony devices (such
    as mobile phones and computers). [based on
    https://en.wikipedia.org/wiki/SIM_card]
    """

    carrier: identity.Identity | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    storageCapacityInBytes: int | None = None
    ICCID: str | None = None
    IMSI: str | None = None
    PIN: str | None = None
    PUK: str | None = None
    SIMForm: str | None = None
    SIMType: str | None = None


class SoftwareFacet(core.Facet):
    """
    A software facet is a grouping of characteristics unique to a software
    program (a definitively scoped instance of a collection of data or computer
    instructions that tell the computer how to work). [based on
    https://en.wikipedia.org/wiki/Software]
    """

    manufacturer: identity.Identity | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    cpeid: str | None = None
    language: str | None = None
    swid: str | None = None
    version: str | None = None


class ContactAddress(core.UcoInherentCharacterizationThing):
    """
    A contact address is a grouping of characteristics unique to a geolocation
    address of a contact entity.
    """

    geolocationAddress: location.Location | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactAddressScope: (
        vocabulary.ContactAddressScopeVocab
        | list[vocabulary.ContactAddressScopeVocab]
        | None
    ) = []


class EXIFFacet(core.Facet):
    """
    An EXIF (exchangeable image file format) facet is a grouping of
    characteristics unique to the formats for images, sound, and ancillary tags
    used by digital cameras (including smartphones), scanners and other systems
    handling image and sound files recorded by digital cameras conformant to
    JEIDA/JEITA/CIPA specifications. [based on
    https://en.wikipedia.org/wiki/Exif]
    """

    exifData: types.ControlledDictionary | list[types.ControlledDictionary] | None = []


class PDFFileFacet(core.Facet):
    """
    A PDF file facet is a grouping of characteristics unique to a PDF (Portable
    Document Format) file.
    """

    documentInformationDictionary: types.ControlledDictionary | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isOptimized: bool | None = None
    pdfCreationDate: AwareDatetime | None = None
    pdfModDate: AwareDatetime | None = None
    pdfId1: str | None = None
    version: str | None = None
    pdfId0: str | list[str] | None = []


class OperatingSystemFacet(core.Facet):
    """
    An operating system facet is a grouping of characteristics unique to the
    software that manages computer hardware, software resources, and provides
    common services for computer programs. [based on
    https://en.wikipedia.org/wiki/Operating_system]
    """

    environmentVariables: types.Dictionary | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isLimitAdTrackingEnabled: bool | None = None
    installDate: AwareDatetime | None = None
    bitness: str | None = None
    advertisingID: str | list[str] | None = []


class WindowsProcessFacet(core.Facet):
    """
    A Windows process facet is a grouping of characteristics unique to a program
    running on a Windows operating system.
    """

    startupInfo: types.Dictionary | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    aslrEnabled: bool | None = None
    depEnabled: bool | None = None
    ownerSID: str | None = None
    priority: str | None = None
    windowTitle: str | None = None


class ExtractedString(core.UcoInherentCharacterizationThing):
    """
    An extracted string is a grouping of characteristics unique to a series of
    characters pulled from an observable object.
    """

    byteStringValue: XMLSchema.xsd_base64Binary | None = None
    length: int | None = None
    encoding: str | None = None
    englishTranslation: str | None = None
    language: str | None = None
    stringValue: str | None = None


class MemoryFacet(core.Facet):
    """
    A memory facet is a grouping of characteristics unique to a particular
    region of temporary information storage (e.g., RAM (random access memory),
    ROM (read only memory)) on a digital device.
    """

    isInjected: bool | None = None
    isMapped: bool | None = None
    isProtected: bool | None = None
    isVolatile: bool | None = None
    regionEndAddress: XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None = (
        []
    )
    regionStartAddress: (
        XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None
    ) = []
    regionSize: int | None = None
    blockType: (
        vocabulary.MemoryBlockTypeVocab | list[vocabulary.MemoryBlockTypeVocab] | None
    ) = []


class ObservableAction(action.Action):
    """
    An observable action is a grouping of characteristics unique to something
    that may be done or performed within the digital domain.
    """


class Observation(action.Action):
    """
    An observation is a temporal perception of an observable.
    """

    name: str


class ObservableObject(core.Item):
    """
    An observable object is a grouping of characteristics unique to a distinct
    article or unit within the digital domain.
    """

    hasChanged: bool | None = None
    state: str | None = None


class RecoveredObjectFacet(core.Facet):
    """
    Recoverability status of name, metadata, and content.
    """

    contentRecoveredStatus: (
        vocabulary.RecoveredObjectStatusVocab
        | list[vocabulary.RecoveredObjectStatusVocab]
        | None
    ) = []
    metadataRecoveredStatus: (
        vocabulary.RecoveredObjectStatusVocab
        | list[vocabulary.RecoveredObjectStatusVocab]
        | None
    ) = []
    nameRecoveredStatus: (
        vocabulary.RecoveredObjectStatusVocab
        | list[vocabulary.RecoveredObjectStatusVocab]
        | None
    ) = []


class SQLiteBlobFacet(core.Facet):
    """
    An SQLite blob facet is a grouping of characteristics unique to a blob
    (binary large object) of data within an SQLite database. [based on
    https://en.wikipedia.org/wiki/SQLite]
    """

    rowIndex: (
        XMLSchema.xsd_positiveInteger | list[XMLSchema.xsd_positiveInteger] | None
    ) = []
    columnName: str | None = None
    rowCondition: str | None = None
    tableName: str | None = None


class TriggerType(core.UcoInherentCharacterizationThing):
    """
    A trigger type is a grouping of characterizes unique to a set of criteria
    that, when met, starts the execution of a task within a Windows operating
    system. [based on
    https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers]
    """

    isEnabled: bool | None = None
    triggerBeginTime: AwareDatetime | None = None
    triggerEndTime: AwareDatetime | None = None
    triggerDelay: str | None = None
    triggerMaxRunTime: str | None = None
    triggerSessionChangeType: str | None = None
    triggerFrequency: (
        vocabulary.TriggerFrequencyVocab | list[vocabulary.TriggerFrequencyVocab] | None
    ) = []
    triggerType: (
        vocabulary.TriggerTypeVocab | list[vocabulary.TriggerTypeVocab] | None
    ) = []


class WindowsPEOptionalHeader(core.UcoInherentCharacterizationThing):
    """
    A Windows PE optional header is a grouping of characteristics unique to the
    'optional header' of a Windows PE (Portable Executable) file, consisting of
    a collection of metadata about the executable code structure of the file.
    """

    majorLinkerVersion: XMLSchema.xsd_byte | list[XMLSchema.xsd_byte] | None = []
    minorLinkerVersion: XMLSchema.xsd_byte | list[XMLSchema.xsd_byte] | None = []
    addressOfEntryPoint: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    baseOfCode: XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None = []
    checksum: XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None = []
    fileAlignment: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    imageBase: XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None = []
    loaderFlags: XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None = []
    numberOfRVAAndSizes: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    sectionAlignment: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    sizeOfCode: XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None = []
    sizeOfHeaders: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    sizeOfHeapCommit: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    sizeOfHeapReserve: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    sizeOfImage: XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None = []
    sizeOfInitializedData: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    sizeOfStackCommit: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    sizeOfStackReserve: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    sizeOfUninitializedData: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    win32VersionValue: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []
    dllCharacteristics: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []
    magic: XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None = []
    majorImageVersion: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []
    majorOSVersion: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []
    majorSubsystemVersion: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []
    minorImageVersion: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []
    minorOSVersion: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []
    minorSubsystemVersion: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []
    subsystem: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []


class WindowsThreadFacet(core.Facet):
    """
    A Windows thread facet is a grouping os characteristics unique to a single
    thread of execution within a Windows process.
    """

    observableCreatedTime: AwareDatetime | None = None
    parameterAddress: XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None = (
        []
    )
    startAddress: XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None = []
    priority: int | None = None
    stackSize: int | list[int] | None = []
    threadID: int | list[int] | None = []
    context: str | None = None
    runningStatus: str | None = None
    securityAttributes: str | None = None
    creationFlags: (
        XMLSchema.xsd_unsignedInt | list[XMLSchema.xsd_unsignedInt] | None
    ) = []


class WindowsVolumeFacet(core.Facet):
    """
    A Windows volume facet is a grouping of characteristics unique to a single
    accessible storage area (volume) with a single Windows file system. [based
    on https://en.wikipedia.org/wiki/Volume_(computing)]
    """

    driveLetter: str | None = None
    driveType: (
        vocabulary.WindowsDriveTypeVocab | list[vocabulary.WindowsDriveTypeVocab] | None
    ) = []
    windowsVolumeAttributes: (
        vocabulary.WindowsVolumeAttributeVocab
        | list[vocabulary.WindowsVolumeAttributeVocab]
        | None
    ) = []


class PropertyReadEffectFacet(DefinedEffectFacet):
    """
    A properties read effect facet is a grouping of characteristics unique to
    the effects of actions upon observable objects where a characteristic is
    read from an observable object. An example of this would be the current
    running state of a process.
    """

    propertyName: str | None = None
    value: str | None = None


class SendControlCodeEffectFacet(DefinedEffectFacet):
    """
    A send control code effect facet is a grouping of characteristics unique to
    the effects of actions upon observable objects where a control code, or
    other control-oriented communication signal, is sent to the observable
    object. An example of this would be an action sending a control code
    changing the running state of a process.
    """

    controlCode: str | None = None


class ValuesEnumeratedEffectFacet(DefinedEffectFacet):
    """
    A values enumerated effect facet is a grouping of characteristics unique to
    the effects of actions upon observable objects where a value of the
    observable object is enumerated. An example of this would be the values of a
    registry key.
    """

    values: str | None = None


class EmailAddressFacet(DigitalAddressFacet):
    """
    An email address facet is a grouping of characteristics unique to an
    identifier for an electronic mailbox to which electronic mail messages
    (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and
    delivered to.
    """


class IPAddressFacet(DigitalAddressFacet):
    """
    An IP address facet is a grouping of characteristics unique to an Internet
    Protocol (IP) standards conformant identifier assigned to a device to enable
    routing and management of IP standards conformant communication to or from
    that device.
    """


class InstantMessagingAddressFacet(DigitalAddressFacet):
    """
    An instant messaging address facet is a grouping of characteristics unique
    to an identifier assigned to enable routing and management of instant
    messaging digital communication.
    """


class MACAddressFacet(DigitalAddressFacet):
    """
    A MAC address facet is a grouping of characteristics unique to a media
    access control standards conformant identifier assigned to a network
    interface to enable routing and management of communications at the data
    link layer of a network segment.
    """


class SIPAddressFacet(DigitalAddressFacet):
    """
    A SIP address facet is a grouping of characteristics unique to a Session
    Initiation Protocol (SIP) standards conformant identifier assigned to a user
    to enable routing and management of SIP standards conformant communication
    to or from that user loosely coupled from any particular devices.
    """


class X509CertificateFacet(core.Facet):
    """
    A X.509 certificate facet is a grouping of characteristics unique to a
    public key digital identity certificate conformant to the X.509 PKI (Public
    Key Infrastructure) standard.
    """

    x509v3extensions: X509V3ExtensionsFacet | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    issuerHash: types.Hash | None = Field(default=None, json_schema_extra={"IRI": True})
    subjectHash: types.Hash | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    thumbprintHash: types.Hash | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isSelfSigned: bool | None = None
    validityNotAfter: AwareDatetime | None = None
    validityNotBefore: AwareDatetime | None = None
    subjectPublicKeyExponent: int | None = None
    issuer: str | None = None
    serialNumber: str | None = None
    signature: str | None = None
    signatureAlgorithm: str | None = None
    subject: str | None = None
    subjectPublicKeyAlgorithm: str | None = None
    subjectPublicKeyModulus: str | None = None
    version: str | None = None


class ObservablePattern(Observable):
    """
    An observable pattern is a grouping of characteristics unique to a logical
    pattern composed of observable object and observable action properties.
    """


class ObservableRelationship(core.Relationship):
    """
    An observable relationship is a grouping of characteristics unique to an
    assertion of an association between two observable objects.
    """

    # MANUAL: The current Python bindings point this at core.UCOObject,
    # not Observable (like the RDF suggests). ObservableObject appears
    # to be more applicable here than the generic UCOObject.
    source: ObservableObject
    target: ObservableObject


class ExtractedStringsFacet(core.Facet):
    """
    An extracted strings facet is a grouping of characteristics unique to one or
    more sequences of characters pulled from an observable object.
    """

    strings: ExtractedString | list[ExtractedString] | None = []


class API(ObservableObject):
    """
    An API (application programming interface) is a computing interface that
    defines interactions between multiple software or mixed hardware-software
    intermediaries. It defines the kinds of calls or requests that can be made,
    how to make them, the data formats that should be used, the conventions to
    follow, etc. [based on https://en.wikipedia.org/wiki/API]
    """


class ARPCache(ObservableObject):
    """
    An ARP cache is a collection of Address Resolution Protocol (ARP) entries
    (mostly dynamic) that are created when an IP address is resolved to a MAC
    address (so the computer can effectively communicate with the IP address).
    [based on https://en.wikipedia.org/wiki/ARP_cache]
    """


class ARPCacheEntry(ObservableObject):
    """
    An ARP cache entry is a single Address Resolution Protocol (ARP) response
    record that is created when an IP address is resolved to a MAC address (so
    the computer can effectively communicate with the IP address). [based on
    https://en.wikipedia.org/wiki/ARP_cache]
    """


class Account(ObservableObject):
    """
    An account is an arrangement with an entity to enable and control the
    provision of some capability or service.
    """


class Address(ObservableObject):
    """
    An address is an identifier assigned to enable routing and management of
    information.
    """


class Application(ObservableObject):
    """
    An application is a particular software program designed for end users.
    """


class ApplicationAccountFacet(core.Facet):
    """
    An application account facet is a grouping of characteristics unique to an
    account within a particular software program designed for end users.
    """

    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )


class ApplicationFacet(core.Facet):
    """
    An application facet is a grouping of characteristics unique to a particular
    software program designed for end users.
    """

    installedVersionHistory: ApplicationVersion | list[ApplicationVersion] | None = []
    operatingSystem: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    numberOfLaunches: int | None = None
    applicationIdentifier: str | None = None
    version: str | None = None


class Audio(ObservableObject):
    """
    Audio is a digital representation of sound.
    """


class AutonomousSystem(ObservableObject):
    """
    An autonomous system is a collection of connected Internet Protocol (IP)
    routing prefixes under the control of one or more network operators on
    behalf of a single administrative entity or domain that presents a common,
    clearly defined routing policy to the Internet. [based on
    https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]
    """


class BotConfiguration(ObservableObject):
    """
    A bot configuration is a set of contextual settings for a software
    application that runs automated tasks (scripts) over the Internet at a much
    higher rate than would be possible for a human alone.
    """


class BrowserBookmark(ObservableObject):
    """
    A browser bookmark is a saved shortcut that directs a WWW (World Wide Web)
    browser software program to a particular WWW accessible resource. [based on
    https://techterms.com/definition/bookmark]
    """


class BrowserBookmarkFacet(core.Facet):
    """
    A browser bookmark facet is a grouping of characteristics unique to a saved
    shortcut that directs a WWW (World Wide Web) browser software program to a
    particular WWW accessible resource. [based on
    https://techterms.com/definition/bookmark]
    """

    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    urlTargeted: XMLSchema.xsd_anyURI | list[XMLSchema.xsd_anyURI] | None = []
    accessedTime: AwareDatetime | None = None
    modifiedTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    visitCount: int | None = None
    bookmarkPath: str | None = None


class BrowserCookie(ObservableObject):
    """
    A browser cookie is a piece of of data sent from a website and stored on the
    user's computer by the user's web browser while the user is browsing. [based
    on https://en.wikipedia.org/wiki/HTTP_cookie]
    """


class BrowserCookieFacet(core.Facet):
    """
    A browser cookie facet is a grouping of characteristics unique to a piece of
    data sent from a website and stored on the user's computer by the user's web
    browser while the user is browsing. [based on
    https://en.wikipedia.org/wiki/HTTP_cookie]
    """

    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    cookieDomain: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isSecure: bool | None = None
    accessedTime: AwareDatetime | None = None
    expirationTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    cookieName: str | None = None
    cookiePath: str | None = None


class Calendar(ObservableObject):
    """
    A calendar is a collection of appointments, meetings, and events.
    """


class CalendarEntry(ObservableObject):
    """
    A calendar entry is an appointment, meeting or event within a collection of
    appointments, meetings and events.
    """


class CalendarEntryFacet(core.Facet):
    """
    A calendar entry facet is a grouping of characteristics unique to an
    appointment, meeting, or event within a collection of appointments,
    meetings, and events.
    """

    owner: core.UcoObject | None = Field(default=None, json_schema_extra={"IRI": True})
    attendant: identity.Identity | list[identity.Identity] | None = []
    location_: location.Location | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isPrivate: bool | None = None
    endTime: AwareDatetime | None = None
    modifiedTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    remindTime: AwareDatetime | None = None
    startTime: AwareDatetime | None = None
    duration: int | None = None
    eventStatus: str | None = None
    eventType: str | None = None
    recurrence: str | None = None
    subject: str | None = None


class CalendarFacet(core.Facet):
    """
    A calendar facet is a grouping of characteristics unique to a collection of
    appointments, meetings, and events.
    """

    owner: core.UcoObject | None = Field(default=None, json_schema_extra={"IRI": True})
    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )


class Call(ObservableObject):
    """
    A call is a connection as part of a realtime cyber communication between one
    or more parties.
    """


class CallFacet(core.Facet):
    """
    A call facet is a grouping of characteristics unique to a connection as part
    of a realtime cyber communication between one or more parties.
    """

    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    from_: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    participant: ObservableObject | list[ObservableObject] | None = []
    to: ObservableObject | list[ObservableObject] | None = []
    endTime: AwareDatetime | None = None
    startTime: AwareDatetime | None = None
    duration: int | None = None
    callType: str | None = None


class CapturedTelecommunicationsInformation(ObservableObject):

    pass


class CellSite(ObservableObject):

    pass


class Code(ObservableObject):
    """
    Code is a direct representation (source, byte or binary) of a collection of
    computer instructions that form software which tell a computer how to work.
    [based on https://en.wikipedia.org/wiki/Software]
    """


class ComputerSpecification(ObservableObject):
    """
    A computer specification is the hardware and software of a programmable
    electronic device that can store, retrieve, and process data. {based on
    merriam-webster.com/dictionary/computer]
    """


class ComputerSpecificationFacet(core.Facet):
    """
    A computer specificaiton facet is a grouping of characteristics unique to
    the hardware and software of a programmable electronic device that can
    store, retrieve, and process data. [based on
    merriam-webster.com/dictionary/computer]
    """

    networkInterface: ObservableObject | list[ObservableObject] | None = []
    biosDate: AwareDatetime | None = None
    biosReleaseDate: AwareDatetime | None = None
    currentSystemDate: AwareDatetime | None = None
    localTime: AwareDatetime | None = None
    systemTime: AwareDatetime | None = None
    availableRam: int | None = None
    totalRam: int | None = None
    biosManufacturer: str | None = None
    biosSerialNumber: str | None = None
    biosVersion: str | None = None
    cpu: str | None = None
    cpuFamily: str | None = None
    gpu: str | None = None
    gpuFamily: str | None = None
    hostname: str | None = None
    processorArchitecture: str | None = None
    timezoneDST: str | None = None
    timezoneStandard: str | None = None
    uptime: str | None = None


class Contact(ObservableObject):
    """
    A contact is a set of identification and communication related details for a
    single entity.
    """


class ContactEmail(core.UcoInherentCharacterizationThing):
    """
    A contact email is a grouping of characteristics unique to details for
    contacting a contact entity by email.
    """

    emailAddress: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactEmailScope: (
        vocabulary.ContactEmailScopeVocab
        | list[vocabulary.ContactEmailScopeVocab]
        | None
    ) = []


class ContactList(ObservableObject):
    """
    A contact list is a set of multiple individual contacts such as that found
    in a digital address book.
    """


class ContactListFacet(core.Facet):
    """
    A contact list facet is a grouping of characteristics unique to a set of
    multiple individual contacts such as that found in a digital address book.
    """

    sourceApplication: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contact: ObservableObject | list[ObservableObject] | None = []


class ContactMessaging(core.UcoInherentCharacterizationThing):
    """
    A contact messaging is a grouping of characteristics unique to details for
    contacting a contact entity by digital messaging.
    """

    contactMessagingPlatform: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    messagingAddress: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )


class ContactPhone(core.UcoInherentCharacterizationThing):
    """
    A contact phone is a grouping of characteristics unique to details for
    contacting a contact entity by telephone.
    """

    contactPhoneNumber: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactPhoneScope: (
        vocabulary.ContactPhoneScopeVocab
        | list[vocabulary.ContactPhoneScopeVocab]
        | None
    ) = []


class ContactProfile(core.UcoInherentCharacterizationThing):
    """
    A contact profile is a grouping of characteristics unique to details for
    contacting a contact entity by online service.
    """

    contactProfilePlatform: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    profile: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )


class ContactSIP(core.UcoInherentCharacterizationThing):
    """
    A contact SIP is a grouping of characteristics unique to details for
    contacting a contact entity by Session Initiation Protocol (SIP).
    """

    sipAddress: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactSIPScope: (
        vocabulary.ContactSIPScopeVocab | list[vocabulary.ContactSIPScopeVocab] | None
    ) = []


class ContactURL(core.UcoInherentCharacterizationThing):
    """
    A contact URL is a grouping of characteristics unique to details for
    contacting a contact entity by Uniform Resource Locator (URL).
    """

    url: ObservableObject | None = Field(default=None, json_schema_extra={"IRI": True})
    contactURLScope: (
        vocabulary.ContactURLScopeVocab | list[vocabulary.ContactURLScopeVocab] | None
    ) = []


class ContentData(ObservableObject):
    """
    Content data is a block of digital data.
    """


class ContentDataFacet(core.Facet):
    """
    A content data facet is a grouping of characteristics unique to a block of
    digital data.
    """

    dataPayloadReferenceURL: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    hash: types.Hash | list[types.Hash] | None = []
    isEncrypted: bool | None = None
    entropy: float | None = None
    sizeInBytes: int | None = None
    dataPayload: str | None = None
    magicNumber: str | None = None
    mimeClass: str | None = None
    mimeType: str | list[str] | None = []
    byteOrder: (
        vocabulary.EndiannessTypeVocab | list[vocabulary.EndiannessTypeVocab] | None
    ) = []


class CookieHistory(ObservableObject):
    """
    A cookie history is the stored web cookie history for a particular web
    browser.
    """


class Credential(ObservableObject):
    """
    A credential is a single specific login and password combination for
    authorization of access to a digital account or system.
    """


class CredentialDump(ObservableObject):
    """
    A credential dump is a collection (typically forcibly extracted from a
    system) of specific login and password combinations for authorization of
    access to a digital account or system.
    """


class DNSCache(ObservableObject):
    """
    An DNS cache is a temporary locally stored collection of previous Domain
    Name System (DNS) query results (created when an domain name is resolved to
    a IP address) for a particular computer.
    """


class DNSRecord(ObservableObject):
    """
    A DNS record is a single Domain Name System (DNS) artifact specifying
    information of a particular type (routing, authority, responsibility,
    security, etc.) for a specific Internet domain name.
    """


class Device(ObservableObject):
    """
    A device is a piece of equipment or a mechanism designed to serve a special
    purpose or perform a special function. [based on
    https://www.merriam-webster.com/dictionary/device]
    """


class DigitalSignatureInfo(ObservableObject):
    """
    A digital signature info is a value calculated via a mathematical scheme for
    demonstrating the authenticity of an electronic message or document.
    """


class DiskFacet(core.Facet):
    """
    A disk facet is a grouping of characteristics unique to a storage mechanism
    where data is recorded by various electronic, magnetic, optical, or
    mechanical changes to a surface layer of one or more rotating disks.
    """

    partition: ObservableObject | list[ObservableObject] | None = []
    diskSize: int | None = None
    freeSpace: int | None = None
    diskType: str | None = None


class DiskPartition(ObservableObject):
    """
    A disk partition is a particular managed region on a storage mechanism where
    data is recorded by various electronic, magnetic, optical, or mechanical
    changes to a surface layer of one or more rotating disks. [based on
    https://en.wikipedia.org/wiki/Disk_storage]
    """


class DomainName(ObservableObject):
    """
    A domain name is an identification string that defines a realm of
    administrative autonomy, authority or control within the Internet. [based on
    https://en.wikipedia.org/wiki/Domain_name]
    """


class EmailAccountFacet(core.Facet):
    """
    An email account facet is a grouping of characteristics unique to an
    arrangement with an entity to enable and control the provision of electronic
    mail (email) capabilities or services.
    """

    emailAddress: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )


class EventLog(ObservableObject):
    """
    An event log is a collection of event records.
    """


class EventRecord(ObservableObject):
    """
    An event record is something that happens in a digital context (e.g.,
    operating system events).
    """


class EventRecordFacet(core.Facet):
    """
    An event record facet is a grouping of characteristics unique to something
    that happens in a digital context (e.g., operating system events).
    """

    cyberAction: ObservableAction | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    account: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    eventRecordDevice: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    endTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    startTime: AwareDatetime | None = None
    eventID: str | None = None
    eventRecordID: str | None = None
    eventRecordRaw: str | None = None
    eventRecordServiceName: str | None = None
    eventRecordText: str | None = None
    eventType: str | None = None


class FileSystem(ObservableObject):
    """
    A file system is the process that manages how and where data on a storage
    medium is stored, accessed and managed. [based on
    https://www.techopedia.com/definition/5510/file-system]
    """


class FileSystemObject(ObservableObject):
    """
    A file system object is an informational object represented and managed
    within a file system.
    """


class GUI(ObservableObject):
    """
    A GUI is a graphical user interface that allows users to interact with
    electronic devices through graphical icons and audio indicators such as
    primary notation, instead of text-based user interfaces, typed command
    labels or text navigation. [based on
    https://en.wikipedia.org/wiki/Graphical_user_interface]
    """


class GenericObservableObject(ObservableObject):
    """
    A generic observable object is an article or unit within the digital domain.
    """


class GeoLocationEntry(ObservableObject):
    """
    A geolocation entry is a single application-specific geolocation entry.
    """


class GeoLocationEntryFacet(core.Facet):
    """
    A geolocation entry facet is a grouping of characteristics unique to a
    single application-specific geolocation entry.
    """

    location_: location.Location | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    observableCreatedTime: AwareDatetime | None = None


class GeoLocationLog(ObservableObject):
    """
    A geolocation log is a record containing geolocation tracks and/or
    geolocation entries.
    """


class GeoLocationLogFacet(core.Facet):
    """
    A geolocation log facet is a grouping of characteristics unique to a record
    containing geolocation tracks and/or geolocation entries.
    """

    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    observableCreatedTime: AwareDatetime | None = None


class GeoLocationTrack(ObservableObject):
    """
    A geolocation track is a set of contiguous geolocation entries representing
    a path/track taken.
    """


class GeoLocationTrackFacet(core.Facet):
    """
    A geolocation track facet is a grouping of characteristics unique to a set
    of contiguous geolocation entries representing a path/track taken.
    """

    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    geoLocationEntry: ObservableObject | list[ObservableObject] | None = []
    endTime: AwareDatetime | None = None
    startTime: AwareDatetime | None = None


class HTTPConnectionFacet(core.Facet):
    """
    An HTTP connection facet is a grouping of characteristics unique to portions
    of a network connection that are conformant to the Hypertext Transfer
    Protocol (HTTP) standard.
    """

    httpMessageBodyData: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    httpRequestHeader: types.Dictionary | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    httpMesageBodyLength: int | None = None
    requestMethod: str | None = None
    requestValue: str | None = None
    requestVersion: str | None = None


class Hostname(ObservableObject):
    """
    A hostname is a label that is assigned to a device connected to a computer
    network and that is used to identify the device in various forms of
    electronic communication, such as the World Wide Web. A hostname may be a
    domain name, if it is properly organized into the domain name system. A
    domain name may be a hostname if it has been assigned to an Internet host
    and associated with the host's IP address. [based on
    https://en.wikipedia.org/wiki/Hostname]
    """


class IPNetmask(ObservableObject):
    """
    An IP netmask is a 32-bit 'mask' used to divide an IP address into subnets
    and specify the network's available hosts.
    """


class Image(ObservableObject):
    """
    An image is a complete copy of a hard disk, memory, or other digital media.
    """


class Library(ObservableObject):
    """
    A library is a suite of data and programming code that is used to develop
    software programs and applications. [based on
    https://www.techopedia.com/definition/3828/software-library]
    """


class Memory(ObservableObject):
    """
    Memory is a particular region of temporary information storage (e.g., RAM
    (random access memory), ROM (read only memory)) on a digital device.
    """


class Message(ObservableObject):
    """
    A message is a discrete unit of electronic communication intended by the
    source for consumption by some recipient or group of recipients. [based on
    https://en.wikipedia.org/wiki/Message]
    """


class MessageFacet(core.Facet):
    """
    A message facet is a grouping of characteristics unique to a discrete unit
    of electronic communication intended by the source for consumption by some
    recipient or group of recipients. [based on
    https://en.wikipedia.org/wiki/Message]
    """

    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    from_: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    to: ObservableObject | list[ObservableObject] | None = []
    sentTime: AwareDatetime | None = None
    messageID: str | None = None
    messageText: str | None = None
    messageType: str | None = None
    sessionID: str | None = None


class MessageThread(ObservableObject):
    """
    A message thread is a running commentary of electronic messages pertaining
    to one topic or question.
    """


class MimePartType(core.UcoInherentCharacterizationThing):
    """
    A mime part type is a grouping of characteristics unique to a component of a
    multi-part email body.
    """

    bodyRaw: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    body: str | None = None
    contentDisposition: str | None = None
    contentType: str | None = None


class Mutex(ObservableObject):
    """
    A mutex is a mechanism that enforces limits on access to a resource when
    there are many threads of execution. A mutex is designed to enforce a mutual
    exclusion concurrency control policy, and with a variety of possible methods
    there exists multiple unique implementations for different applications.
    [based on https://en.wikipedia.org/wiki/Lock_(computer_science)]
    """


class NetworkConnection(ObservableObject):
    """
    A network connection is a connection (completed or attempted) across a
    digital network (a group of two or more computer systems linked together).
    [based on https://www.webopedia.com/TERM/N/network.html]
    """


class NetworkConnectionFacet(core.Facet):
    """
    A network connection facet is a grouping of characteristics unique to a
    connection (complete or attempted) accross a digital network (a group of two
    or more computer systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]
    """

    src: core.UcoObject | list[core.UcoObject] | None = []
    dst: ObservableObject | list[ObservableObject] | None = []
    protocols: types.ControlledDictionary | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isActive: bool | None = None
    endTime: AwareDatetime | None = None
    startTime: AwareDatetime | None = None
    destinationPort: int | None = None
    sourcePort: int | None = None


class NetworkFlow(ObservableObject):
    """
    A network flow is a sequence of data transiting one or more digital network
    (a group or two or more computer systems linked together) connections.
    [based on https://www.webopedia.com/TERM/N/network.html]
    """


class NetworkFlowFacet(core.Facet):
    """
    A network flow facet is a grouping of characteristics unique to a sequence
    of data transiting one or more digital network (a group of two or more
    computer systems linked together) connections. [based on
    https://www.webopedia.com/TERM/N/network.html]
    """

    dstPayload: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    srcPayload: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    ipfix: types.Dictionary | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    dstBytes: int | None = None
    dstPackets: int | None = None
    srcBytes: int | None = None
    srcPackets: int | None = None


class NetworkInterface(ObservableObject):
    """
    A network interface is a software or hardware interface between two pieces
    of equipment or protocol layers in a computer network.
    """


class NetworkInterfaceFacet(core.Facet):
    """
    A network interface facet is a grouping of characteristics unique to a
    software or hardware interface between two pieces of equipment or protocol
    layers in a computer network.
    """

    macAddress: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    dhcpServer: ObservableObject | list[ObservableObject] | None = []
    ip: ObservableObject | list[ObservableObject] | None = []
    ipGateway: ObservableObject | list[ObservableObject] | None = []
    dhcpLeaseExpires: AwareDatetime | None = None
    dhcpLeaseObtained: AwareDatetime | None = None
    adapterName: str | None = None


class NetworkProtocol(ObservableObject):
    """
    A network protocol is an established set of structured rules that determine
    how data is transmitted between different devices in the same network.
    Essentially, it allows connected devices to communicate with each other,
    regardless of any differences in their internal processes, structure or
    design. [based on
    https://www.comptia.org/content/guides/what-is-a-network-protocol]
    """


class NetworkRoute(ObservableObject):
    """
    A network route is a specific path (of specific network nodes, connections
    and protocols) for traffic in a network or between or across multiple
    networks.
    """


class NetworkSubnet(ObservableObject):
    """
    A network subnet is a logical subdivision of an IP network. [based on
    https://en.wikipedia.org/wiki/Subnetwork]
    """


class Note(ObservableObject):
    """
    A note is a brief textual record.
    """


class NoteFacet(core.Facet):
    """
    A note facet is a grouping of characteristics unique to a brief textual
    record.
    """

    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    modifiedTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    text: str | None = None


class OnlineService(ObservableObject):
    """
    An online service is a particular provision mechanism of information access,
    distribution or manipulation over the Internet.
    """


class OnlineServiceFacet(core.Facet):
    """
    An online service facet is a grouping of characteristics unique to a
    particular provision mechanism of information access, distribution or
    manipulation over the Internet.
    """

    location_: location.Location | list[location.Location] | None = []
    inetLocation: ObservableObject | list[ObservableObject] | None = []
    name: str | None = None


class PaymentCard(ObservableObject):
    """
    A payment card is a physical token that is part of a payment system issued
    by financial institutions, such as a bank, to a customer that enables its
    owner (the cardholder) to access the funds in the customer's designated bank
    accounts, or through a credit account and make payments by electronic funds
    transfer and access automated teller machines (ATMs). [based on
    https://en.wikipedia.org/wiki/Payment_card]
    """


class Pipe(ObservableObject):
    """
    A pipe is a mechanism for one-way inter-process communication using message
    passing where data written by one process is buffered by the operating
    system until it is read by the next process, and this uni-directional
    channel disappears when the processes are completed. [based on
    https://en.wikipedia.org/wiki/Pipeline_(Unix) ;
    https://en.wikipedia.org/wiki/Anonymous_pipe]
    """


class Process(ObservableObject):
    """
    A process is an instance of a computer program executed on an operating
    system.
    """


class ProcessFacet(core.Facet):
    """
    A process facet is a grouping of characteristics unique to an instance of a
    computer program executed on an operating system.
    """

    binary: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    creatorUser: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    parent: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    environmentVariables: types.Dictionary | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isHidden: bool | None = None
    exitTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    exitStatus: int | None = None
    pid: int | None = None
    currentWorkingDirectory: str | None = None
    status: str | None = None
    arguments: str | list[str] | None = []


class ProcessThread(ObservableObject):
    """
    A process thread is the smallest sequence of programmed instructions that
    can be managed independently by a scheduler on a computer, which is
    typically a part of the operating system. It is a component of a process.
    Multiple threads can exist within one process, executing concurrently and
    sharing resources such as memory, while different processes do not share
    these resources. In particular, the threads of a process share its
    executable code and the values of its dynamically allocated variables and
    non-thread-local global variables at any given time. [based on
    https://en.wikipedia.org/wiki/Thread_(computing)]
    """


class Profile(ObservableObject):
    """
    A profile is an explicit digital representation of identity and
    characteristics of the owner of a single user account associated with an
    online service or application. [based on
    https://en.wikipedia.org/wiki/User_profile]
    """


class RasterPictureFacet(core.Facet):
    """
    A raster picture facet is a grouping of characteristics unique to a raster
    (or bitmap) image.
    """

    camera: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    bitsPerPixel: int | None = None
    pictureHeight: int | None = None
    pictureWidth: int | None = None
    imageCompressionMethod: str | None = None
    pictureType: str | None = None


class RecoveredObject(ObservableObject):
    """
    An observable object that was the result of a recovery operation.
    """


class SQLiteBlob(ObservableObject):
    """
    An SQLite blob is a blob (binary large object) of data within an SQLite
    database. [based on https://en.wikipedia.org/wiki/SQLite]
    """


class Semaphore(ObservableObject):
    """
    A semaphore is a variable or abstract data type used to control access to a
    common resource by multiple processes and avoid critical section problems in
    a concurrent system such as a multitasking operating system. [based on
    https://en.wikipedia.org/wiki/Semaphore_(programming)]
    """


class ShopListing(ObservableObject):
    """
    A shop listing is a listing of offered products on an online
    marketplace/shop.
    """


class Software(ObservableObject):
    """
    Software is a definitely scoped instance of a collection of data or computer
    instructions that tell the computer how to work. [based on
    https://en.wikipedia.org/wiki/Software]
    """


class StateChangeEffectFacet(DefinedEffectFacet):
    """
    A state change effect facet is a grouping of characteristics unique to the
    effects of actions upon observable objects where a state of the observable
    object is changed.
    """

    newObject: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    oldObject: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )


class SymbolicLinkFacet(core.Facet):
    """
    A symbolic link facet is a grouping of characteristics unique to a file that
    contains a reference to another file or directory in the form of an absolute
    or relative path and that affects pathname resolution. [based on
    https://en.wikipedia.org/wiki/Symbolic_link]
    """

    targetFile: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )


class TableField(ObservableObject):
    """
    A database table field and its associated value contained within a
    relational database.
    """


class TaskActionType(core.UcoInherentCharacterizationThing):
    """
    A task action type is a grouping of characteristics for a scheduled action
    to be completed.
    """

    iComHandlerAction: IComHandlerActionType | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    iExecAction: IExecActionType | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    iShowMessageAction: IShowMessageActionType | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    iEmailAction: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    actionID: str | None = None
    actionType: (
        vocabulary.TaskActionTypeVocab | list[vocabulary.TaskActionTypeVocab] | None
    ) = []


class TwitterProfileFacet(core.Facet):
    """
    A twitter profile facet is a grouping of characteristics unique to an
    explicit digital representation of identity and characteristics of the owner
    of a single Twitter user account. [based on
    https://en.wikipedia.org/wiki/User_profile]
    """

    profileBackgroundLocation: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    profileBannerLocation: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    profileImageLocation: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    profileBackgroundHash: types.Hash | list[types.Hash] | None = []
    profileBannerHash: types.Hash | list[types.Hash] | None = []
    profileImageHash: types.Hash | list[types.Hash] | None = []
    profileIsProtected: bool | None = None
    profileIsVerified: bool | None = None
    listedCount: int | None = None
    favoritesCount: int | None = None
    followersCount: int | None = None
    friendsCount: int | None = None
    statusesCount: int | None = None
    twitterHandle: str | None = None
    twitterId: str | None = None
    userLocationString: str | None = None


class URL(ObservableObject):
    """
    A URL is a uniform resource locator (URL) acting as a resolvable address to
    a particular WWW (World Wide Web) accessible resource.
    """


class URLFacet(core.Facet):
    """
    A URL facet is a grouping of characteristics unique to a uniform resource
    locator (URL) acting as a resolvable address to a particular WWW (World Wide
    Web) accessible resource.
    """

    host: ObservableObject | None = Field(default=None, json_schema_extra={"IRI": True})
    port: int | None = None
    fragment: str | None = None
    fullValue: str | None = None
    password: str | None = None
    path: str | None = None
    query: str | None = None
    scheme: str | None = None
    userName: str | None = None


class URLHistory(ObservableObject):
    """
    A URL history characterizes the stored URL history for a particular web
    browser
    """


class URLHistoryEntry(core.UcoInherentCharacterizationThing):
    """
    A URL history entry is a grouping of characteristics unique to the
    properties of a single URL history entry for a particular browser.
    """

    url: ObservableObject | None = Field(default=None, json_schema_extra={"IRI": True})
    referrerUrl: ObservableObject | list[ObservableObject] | None = []
    expirationTime: AwareDatetime | None = None
    firstVisit: AwareDatetime | None = None
    lastVisit: AwareDatetime | None = None
    visitCount: int | None = None
    manuallyEnteredCount: int | None = None
    browserUserProfile: str | None = None
    hostname: str | None = None
    pageTitle: str | None = None
    keywordSearchTerm: str | list[str] | None = []


class URLVisit(ObservableObject):
    """
    A URL visit characterizes the properties of a visit of a URL within a
    particular browser.
    """


class URLVisitFacet(core.Facet):
    """
    A URL visit facet is a grouping of characteristics unique to the properties
    of a visit of a URL within a particular browser.
    """

    browserInformation: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    fromURLVisit: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    url: ObservableObject | None = Field(default=None, json_schema_extra={"IRI": True})
    visitTime: AwareDatetime | None = None
    visitDuration: XMLSchema.xsd_duration | None = None
    urlTransitionType: (
        vocabulary.URLTransitionTypeVocab
        | list[vocabulary.URLTransitionTypeVocab]
        | None
    ) = []


class UserSession(ObservableObject):
    """
    A user session is a temporary and interactive information interchange
    between two or more communicating devices within the managed scope of a
    single user. [based on
    https://en.wikipedia.org/wiki/Session_(computer_science)]
    """


class UserSessionFacet(core.Facet):
    """
    A user session facet is a grouping of characteristics unique to a temporary
    and interactive information interchange between two or more communicating
    devices within the managed scope of a single user. [based on
    https://en.wikipedia.org/wiki/Session_(computer_science)]
    """

    effectiveUser: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    loginTime: AwareDatetime | None = None
    logoutTime: AwareDatetime | None = None
    effectiveGroup: str | None = None
    effectiveGroupID: str | None = None


class Volume(ObservableObject):
    """
    A volume is a single accessible storage area (volume) with a single file
    system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]
    """


class WebPage(ObservableObject):
    """
    A web page is a specific collection of information provided by a website and
    displayed to a user in a web browser. A website typically consists of many
    web pages linked together in a coherent fashion. [based on
    https://en.wikipedia.org/wiki/Web_page]
    """


class WhoIs(ObservableObject):
    """
    WhoIs is a response record conformant to the WHOIS protocol standard (RFC
    3912). [based on https://en.wikipedia.org/wiki/WHOIS]
    """


class WhoisRegistrarInfoType(core.UcoInherentCharacterizationThing):
    """
    A Whois registrar info type is a grouping of characteristics unique to
    registrar-related information present in a response record conformant to the
    WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]
    """

    geolocationAddress: location.Location | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactPhoneNumber: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    emailAddress: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    referralURL: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    whoisServer: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    registrarGUID: str | None = None
    registrarID: str | None = None
    registrarName: str | None = None


class Wiki(ObservableObject):
    """
    A wiki is an online hypertext publication collaboratively edited and managed
    by its own audience directly using a web browser. A typical wiki contains
    multiple pages/articles for the subjects or scope of the project and could
    be either open to the public or limited to use within an organization for
    maintaining its internal knowledge base. [based on
    https://en.wikipedia.org/wiki/Wiki]
    """


class WikiArticle(ObservableObject):
    """
    A wiki article is one or more pages in a wiki focused on characterizing a
    particular topic.
    """


class WindowsComputerSpecification(ObservableObject):
    """
    A Windows computer specification is the hardware ans software of a
    programmable electronic device that can store, retrieve, and process data
    running a Microsoft Windows operating system. [based on
    merriam-webster.com/dictionary/computer]
    """


class WindowsComputerSpecificationFacet(core.Facet):
    """
    A Windows computer specification facet is a grouping of characteristics
    unique to the hardware and software of a programmable electronic device that
    can store, retrieve, and process data running a Microsoft Windows operating
    system. [based on merriam-webster.com/dictionary/computer]
    """

    registeredOrganization: identity.Identity | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    registeredOwner: identity.Identity | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    globalFlagList: GlobalFlagType | list[GlobalFlagType] | None = []
    windowsDirectory: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    windowsSystemDirectory: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    windowsTempDirectory: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    lastShutdownDate: AwareDatetime | None = None
    osInstallDate: AwareDatetime | None = None
    osLastUpgradeDate: AwareDatetime | None = None
    msProductID: str | None = None
    msProductName: str | None = None
    netBIOSName: str | None = None
    domain: str | list[str] | None = []


class WindowsCriticalSection(ObservableObject):
    """
    A Windows critical section is a Windows object that provides synchronization
    similar to that provided by a mutex object, except that a critical section
    can be used only by the threads of a single process. Critical section
    objects cannot be shared across processes. Event, mutex, and semaphore
    objects can also be used in a single-process application, but critical
    section objects provide a slightly faster, more efficient mechanism for
    mutual-exclusion synchronization (a processor-specific test and set
    instruction). Like a mutex object, a critical section object can be owned by
    only one thread at a time, which makes it useful for protecting a shared
    resource from simultaneous access. Unlike a mutex object, there is no way to
    tell whether a critical section has been abandoned. [based on
    https://docs.microsoft.com/en-us/windows/win32/sync/critical-section-objects]
    """


class WindowsEvent(ObservableObject):
    """
    A Windows event is a notification record of an occurance of interest
    (system, security, application, etc.) on a Windows operating system.
    """


class WindowsFilemapping(ObservableObject):
    """
    A Windows file mapping is the association of a file's contents with a
    portion of the virtual address space of a process within a Windows operating
    system. The system creates a file mapping object (also known as a section
    object) to maintain this association. A file view is the portion of virtual
    address space that a process uses to access the file's contents. File
    mapping allows the process to use both random input and output (I/O) and
    sequential I/O. It also allows the process to work efficiently with a large
    data file, such as a database, without having to map the whole file into
    memory. Multiple processes can also use memory-mapped files to share data.
    Processes read from and write to the file view using pointers, just as they
    would with dynamically allocated memory. The use of file mapping improves
    efficiency because the file resides on disk, but the file view resides in
    memory.[based on
    https://docs.microsoft.com/en-us/windows/win32/memory/file-mapping]
    """


class WindowsHandle(ObservableObject):
    """
    A Windows handle is an abstract reference to a resource within the Windows
    operating system, such as a window, memory, an open file or a pipe. It is
    the mechanism by which applications interact with such resources in the
    Windows operating system.
    """


class WindowsHook(ObservableObject):
    """
    A Windows hook is a mechanism by which an application can intercept events,
    such as messages, mouse actions, and keystrokes within the Windows operating
    system. A function that intercepts a particular type of event is known as a
    hook procedure. A hook procedure can act on each event it receives, and then
    modify or discard the event. [based on
    https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks]
    """


class WindowsMailslot(ObservableObject):
    """
    A Windows mailslot is is a pseudofile that resides in memory, and may be
    accessed using standard file functions. The data in a mailslot message can
    be in any form, but cannot be larger than 424 bytes when sent between
    computers. Unlike disk files, mailslots are temporary. When all handles to a
    mailslot are closed, the mailslot and all the data it contains are deleted.
    [based on
    https://docs.microsoft.com/en-us/windows/win32/ipc/about-mailslots]
    """


class WindowsNetworkShare(ObservableObject):
    """
    A Windows network share is a Windows computer resource made available from
    one host to other hosts on a computer network. It is a device or piece of
    information on a computer that can be remotely accessed from another
    computer transparently as if it were a resource in the local machine.
    Network sharing is made possible by inter-process communication over the
    network. [based on https://en.wikipedia.org/wiki/Shared_resource]
    """


class WindowsPrefetch(ObservableObject):
    """
    The Windows prefetch contains entries in a Windows prefetch file (used to
    speed up application startup starting with Windows XP).
    """


class WindowsPrefetchFacet(core.Facet):
    """
    A Windows prefetch facet is a grouping of characteristics unique to entries
    in the Windows prefetch file (used to speed up application startup starting
    with Windows XP).
    """

    volume: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    accessedDirectory: ObservableObject | list[ObservableObject] | None = []
    accessedFile: ObservableObject | list[ObservableObject] | None = []
    firstRun: AwareDatetime | None = None
    lastRun: AwareDatetime | None = None
    timesExecuted: int | None = None
    applicationFileName: str | None = None
    prefetchHash: str | None = None


class WindowsRegistryHive(ObservableObject):
    """
    The Windows registry hive is a particular logical group of keys, subkeys,
    and values in a Windows registry (a hierarchical database that stores
    low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry). [based on
    https://en.wikipedia.org/wiki/Windows_Registry]
    """


class WindowsRegistryKey(ObservableObject):
    """
    A Windows registry key is a particular key within a Windows registry (a
    hierarchical database that stores low-level settings for the Microsoft
    Windows operating system and for applications that opt to use the registry).
    [based on https://en.wikipedia.org/wiki/Windows_Registry]
    """


class WindowsRegistryKeyFacet(core.Facet):
    """
    A Windows registry key facet is a grouping of characteristics unique to a
    particular key within a Windows registry (A hierarchical database that
    stores low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry). [based on
    https://en.wikipedia.org/wiki/Windows_Registry]
    """

    creator: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    registryValues: WindowsRegistryValue | list[WindowsRegistryValue] | None = []
    modifiedTime: AwareDatetime | None = None
    numberOfSubkeys: int | None = None
    key: str | None = None


class WindowsService(ObservableObject):
    """
    A Windows service is a specific Windows service (a computer program that
    operates in the background of a Windows operating system, similar to the way
    a UNIX daemon runs on UNIX). [based on
    https://en.wikipedia.org/wiki/Windows_service]
    """


class WindowsSystemRestore(ObservableObject):
    """
    A Windows system restore is a capture of a Windows computer's state
    (including system files, installed applications, Windows Registry, and
    system settings) at a particular point in time such that the computer can be
    reverted to that state in the event of system malfunctions or other
    problems. [based on https://en.wikipedia.org/wiki/System_Restore]
    """


class WindowsTask(ObservableObject):
    """
    A Windows task is a process that is scheduled to execute on a Windows
    operating system by the Windows Task Scheduler. [based on
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]
    """


class WindowsWaitableTime(ObservableObject):
    """
    A Windows waitable timer is a synchronization object within the Windows
    operating system whose state is set to signaled when a specified due time
    arrives. There are two types of waitable timers that can be created:
    manual-reset and synchronization. A timer of either type can also be a
    periodic timer. [based on
    https://docs.microsoft.com/en-us/windows/win32/sync/waitable-timer-objects]
    """


class X509Certificate(ObservableObject):
    """
    A X.509 certificate is a public key digital identity certificate conformant
    to the X.509 PKI (Public Key Infrastructure) standard.
    """


class X509V3Certificate(ObservableObject):
    """
    An X.509 v3 certificate is a public key digital identity certificate
    conformant to the X.509 v3 PKI (Public Key Infrastructure) standard.
    """


class WindowsPEBinaryFileFacet(core.Facet):
    """
    A Windows PE binary file facet is a grouping of characteristics unique to a
    Windows portable executable (PE) file.
    """

    optionalHeader: WindowsPEOptionalHeader | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    sections: WindowsPESection | list[WindowsPESection] | None = []
    fileHeaderHashes: types.Hash | list[types.Hash] | None = []
    timeDateStamp: AwareDatetime | None = None
    pointerToSymbolTable: (
        XMLSchema.xsd_hexBinary | list[XMLSchema.xsd_hexBinary] | None
    ) = []
    numberOfSections: int | None = None
    numberOfSymbols: int | None = None
    sizeOfOptionalHeader: int | None = None
    impHash: str | None = None
    peType: str | None = None
    machine: str | list[str] | None = []
    characteristics: (
        XMLSchema.xsd_unsignedShort | list[XMLSchema.xsd_unsignedShort] | None
    ) = []


class IPv4AddressFacet(IPAddressFacet):
    """
    An IPv4 (Internet Protocol version 4) address facet is a grouping of
    characteristics unique to an IPv4 standards conformant identifier assigned
    to a device to enable routing and management of IPv4 standards conformant
    communication to or from that device.
    """


class IPv6AddressFacet(IPAddressFacet):
    """
    An IPv6 (Internet Protocol version 6) address facet is a grouping of
    characteristics unique to an IPv6 standards conformant identifier assigned
    to a device to enable routing and management of IPv6 standards conformant
    communication to or from that device.
    """


class BluetoothAddressFacet(MACAddressFacet):
    """
    A Bluetooth address facet is a grouping of characteristics unique to a
    Bluetooth standard conformant identifier assigned to a Bluetooth device to
    enable routing and management of Bluetooth standards conformant
    communication to or from that device.
    """


class WifiAddressFacet(MACAddressFacet):
    """
    A Wi-Fi address facet is a grouping of characteristics unique to a media
    access control (MAC) standards conformant identifier assigned to a device
    network interface to enable routing and management of IEEE 802.11
    standards-conformant communications to and from that device.
    """


class DigitalAccount(Account):
    """
    A digital account is an arrangement with an entity to enable and control the
    provision of some capability or service within the digital domain.
    """


class DigitalAddress(Address):
    """
    A digital address is an identifier assigned to enable routing and management
    of digital communication.
    """


class SocketAddress(Address):
    """
    A socket address (combining and IP address and a port number) is a composite
    identifier for a network socket endpoint supporting internet protocol
    communications.
    """


class CapturedTelecommunicationsInformationFacet(core.Facet):
    """
    A captured telecommunications information facet represents certain
    information within captured or intercepted telecommunications data.
    """

    captureCellSite: CellSite = Field(json_schema_extra={"IRI": True})
    endTime: AwareDatetime | None = None
    startTime: AwareDatetime | None = None
    interceptedCallState: str | None = None


class ContactAffiliation(core.UcoInherentCharacterizationThing):
    """
    A contact affiliation is a grouping of characteristics unique to details of
    an organizational affiliation for a single contact entity.
    """

    contactOrganization: identity.Organization | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    organizationLocation: ContactAddress | list[ContactAddress] | None = []
    contactEmail: ContactEmail | list[ContactEmail] | None = []
    contactMessaging: ContactMessaging | list[ContactMessaging] | None = []
    contactPhone: ContactPhone | list[ContactPhone] | None = []
    contactProfile: ContactProfile | list[ContactProfile] | None = []
    contactURL: ContactURL | list[ContactURL] | None = []
    organizationDepartment: str | None = None
    organizationPosition: str | None = None


class ProfileFacet(core.Facet):
    """
    A profile facet is a grouping of characteristics unique to an explicit
    digital representation of identity and characteristics of the owner of a
    single user account associated with an online service or application. [based
    on https://en.wikipedia.org/wiki/User_profile]
    """

    profileIdentity: identity.Identity | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactAddress: ContactAddress | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactEmail: ContactEmail | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactMessaging: ContactMessaging | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactPhone: ContactPhone | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    contactURL: ContactURL | None = Field(default=None, json_schema_extra={"IRI": True})
    profileAccount: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    profileService: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    profileWebsite: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    profileCreated: AwareDatetime | None = None
    name: str | None = None
    displayName: str | None = None
    profileLanguage: str | list[str] | None = []


class Adaptor(Device):
    """
    An adaptor is a device that physically converts the pin outputs but does not
    alter the underlying protocol (e.g. uSD to SD, CF to ATA, etc.)
    """


class AndroidDevice(Device):
    """
    An Android device is a device running the Android operating system. [based
    on https://en.wikipedia.org/wiki/Android_(operating_system)]
    """


class AppleDevice(Device):
    """
    An apple device is a smart device that applies either the MacOS or iOS
    operating system.
    """


class Appliance(Device):
    """
    An appliance is a purpose-built computer with software or firmware that is
    designed to provide a specific computing capability or resource. [based on
    https://en.wikipedia.org/wiki/Computer_appliance]
    """


class Computer(Device):
    """
    A computer is an electronic device for storing and processing data,
    typically in binary, according to instructions given to it in a variable
    program. [based on 'Computer.' Oxford English Dictionary, Oxford University
    Press, 2022.]
    """


class DigitalCamera(Device):
    """
    A digital camera is a camera that captures photographs in digital memory as
    opposed to capturing images on photographic film.
    """


class EmbeddedDevice(Device):
    """
    An embedded device is a highly specialized microprocessor device meant for
    one or very few specific purposes and is usually embedded or included within
    another object or as part of a larger system. Examples include answer
    machine, door access logger, card scanner, etc.
    """


class GamingConsole(Device):
    """
    A gaming console (video game console or game console) is an electronic
    system that connects to a display, typically a TV or computer monitor, for
    the primary purpose of playing video games.
    """


class MobileDevice(Device):
    """
    A mobile device is a portable computing device. [based on
    https://www.lexico.com.definition/mobile_device]
    """


class ProtocolConverter(Device):
    """
    A protocol converter is a device that converts from one protocol to another
    (e.g. SD to USB, SATA to USB, etc.
    """


class SIMCard(Device):
    """
    A SIM card is a subscriber identification module card intended to securely
    store the international mobile subscriber identity (IMSI) number and its
    related key, which are used to identify and authenticate subscribers on
    mobile telephony. [based on https://en.wikipedia.org/wiki/SIM_card]
    """


class SmartDevice(Device):
    """
    A smart device is a microprocessor IoT device that is expected to be
    connected directly to cloud-based networks or via smartphone
    """


class StorageMedium(Device):
    """
    A storage medium is any digital storage device that applies electromagnetic
    or optical surfaces, or depends solely on electronic circuits as solid state
    storage, for storing digital data. Examples include HDD (PATA), SATA, SSD,
    Optical, Memory_Card, Tape, etc
    """


class WriteBlocker(Device):
    """
    A write blocker is a device that allows read-only access to storage mediums
    in order to preserve the integrity of the data being analyzed. Examples
    include Tableau, Cellibrite, Talon, etc.
    """


class AlternateDataStream(FileSystemObject):
    """
    An alternate data stream is data content stored within an NTFS file that is
    independent of the standard content stream of the file and is hidden from
    access by default NTFS file viewing mechanisms.
    """


class BlockDeviceNode(FileSystemObject):
    """
    A block device node is a UNIX filesystem special file that serves as a
    conduit to communicate with devices, providing buffered randomly accesible
    input and output. Block device nodes are used to apply access rights to the
    devices and to direct operations on the files to the appropriate device
    drivers. [based on https://en.wikipedia.org/wiki/Unix_file_types]
    """


class CharacterDeviceNode(FileSystemObject):
    """
    A character device node is a UNIX filesystem special file that serves as a
    conduit to communicate with devices, providing only a serial stream of input
    or accepting a serial stream of output. Character device nodes are used to
    apply access rights to the devices and to direct operations on the files to
    the appropriate device drivers. [based on
    https://en.wikipedia.org/wiki/Unix_file_types]
    """


class Directory(FileSystemObject):
    """
    A directory is a file system cataloging structure which contains references
    to other computer files, and possibly other directories. On many computers,
    directories are known as folders, or drawers, analogous to a workbench or
    the traditional office filing cabinet. In UNIX a directory is implemented as
    a special file. [based on
    https://en.wikipedia.org/wiki/Directory_(computing)]
    """


class File(FileSystemObject):
    """
    A file is a computer resource for recording data discretely on a computer
    storage device.
    """


class Junction(FileSystemObject):
    """
    A junction is a specific NTFS (New Technology File System) reparse point to
    redirect a directory access to another directory which can be on the same
    volume or another volume. A junction is similar to a directory symbolic link
    but may differ on whether they are processed on the local system or on the
    remote file server. [based on
    https://jp-andre.pagesperso-orange.fr/junctions.html]
    """


class NamedPipe(FileSystemObject):
    """
    A named pipe is a mechanism for FIFO (first-in-first-out) inter-process
    communication. It is persisted as a filesystem object (that can be deleted
    like any other file), can be written to or read from by any process and
    exists beyond the lifespan of any process interacting with it (unlike simple
    anonymous pipes). [based on https://en.wikipedia.org/wiki/Named_pipe]
    """


class ReparsePoint(FileSystemObject):
    """
    A reparse point is a type of NTFS (New Technology File System) object which
    is an optional attribute of files and directories meant to define some sort
    of preprocessing before accessing the said file or directory. For instance
    reparse points can be used to redirect access to files which have been moved
    to long term storage so that some application would retrieve them and make
    them directly accessible. A reparse point contains a reparse tag and data
    that are interpreted by a filesystem filter identified by the tag. [based on
    https://jp-andre.pagesperso-orange.fr/junctions.html ;
    https://en.wikipedia.org/wiki/NTFS_reparse_point]
    """


class Snapshot(FileSystemObject):
    """
    A snapshot is a file system object representing a snapshot of the contents
    of a part of a file system at a point in time.
    """


class Socket(FileSystemObject):
    """
    A socket is a special file used for inter-process communication, which
    enables communication between two processes. In addition to sending data,
    processes can send file descriptors across a Unix domain socket connection
    using the sendmsg() and recvmsg() system calls. Unlike named pipes which
    allow only unidirectional data flow, sockets are fully duplex-capable.
    [based on https://en.wikipedia.org/wiki/Unix_file_types]
    """


class SymbolicLink(FileSystemObject):
    """
    A symbolic link is a file that contains a reference to another file or
    directory in the form of an absolute or relative path and that affects
    pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]
    """


class EmailMessage(Message):
    """
    An email message is a message that is an instance of an electronic mail
    correspondence conformant to the internet message format described in RFC
    5322 and related RFCs.
    """


class ForumPost(Message):
    """
    A forum post is message submitted by a user account to an online forum where
    the message content (and typically metadata including who posted it and
    when) is viewable by any party with viewing permissions on the forum.
    """


class ForumPrivateMessage(Message):
    """
    A forum private message (aka PM or DM (direct message)) is a one-to-one
    message from one specific user account to another specific user account on
    an online form where transmission is managed by the online forum platform
    and the message is only viewable by the parties directly involved.
    """


class MessageThreadFacet(core.Facet):
    """
    A message thread facet is a grouping of characteristics unique to a running
    commentary of electronic messages pertaining to one topic or question.
    """

    n4151fc4a91fc4cbf87986287e9b360ceb463: Message | list[Message] | None = []
    n4151fc4a91fc4cbf87986287e9b360ceb467: Message | list[Message] | None = []
    n4151fc4a91fc4cbf87986287e9b360ceb471: Message | list[Message] | None = []
    n4151fc4a91fc4cbf87986287e9b360ceb475: Message | list[Message] | None = []
    participant: ObservableObject | list[ObservableObject] | None = []
    messageThread: types.Thread | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    visibility: bool | None = None


class Post(Message):
    """
    A post is message submitted to an online discussion/publishing site (forum,
    blog, etc.).
    """


class SMSMessage(Message):
    """
    An SMS message is a message conformant to the short message service (SMS)
    communication protocol standards.
    """


class Tweet(Message):
    """
    A tweet is message submitted by a Twitter user account to the Twitter
    microblogging platform.
    """


class EmailMessageFacet(core.Facet):
    """
    An email message facet is a grouping of characteristics unique to a message
    that is an instance of an electronic mail correspondence conformant to the
    internet message format described in RFC 5322 and related RFCs.
    """

    bodyMultipart: MimePartType | list[MimePartType] | None = []
    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    bodyRaw: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    from_: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    headerRaw: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    sender: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    xOriginatingIP: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    bcc: ObservableObject | list[ObservableObject] | None = []
    cc: ObservableObject | list[ObservableObject] | None = []
    references: ObservableObject | list[ObservableObject] | None = []
    to: ObservableObject | list[ObservableObject] | None = []
    otherHeaders: types.Dictionary | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isMimeEncoded: bool | None = None
    isMultipart: bool | None = None
    isRead: bool | None = None
    modifiedTime: AwareDatetime | None = None
    receivedTime: AwareDatetime | None = None
    sentTime: AwareDatetime | None = None
    body: str | None = None
    contentDisposition: str | None = None
    contentType: str | None = None
    inReplyTo: str | None = None
    messageID: str | None = None
    priority: str | None = None
    subject: str | None = None
    xMailer: str | None = None
    categories: str | list[str] | None = []
    labels: str | list[str] | None = []
    receivedLines: str | list[str] | None = []


class HTTPConnection(NetworkConnection):
    """
    An HTTP connection is network connection that is conformant to the Hypertext
    Transfer Protocol (HTTP) standard.
    """


class ICMPConnection(NetworkConnection):
    """
    An ICMP connection is a network connection that is conformant to the
    Internet Control Message Protocol (ICMP) standard.
    """


class TCPConnection(NetworkConnection):
    """
    A TCP connection is a network connection that is conformant to the Transfer
    """


class WirelessNetworkConnection(NetworkConnection):
    """
    A wireless network connection is a connection (completed or attempted)
    across an IEEE 802.11 standards-confromant digital network (a group of two
    or more computer systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]
    """


class UNIXProcess(Process):
    """
    A UNIX process is an instance of a computer program executed on a UNIX
    operating system.
    """


class WindowsProcess(Process):
    """
    A Windows process is a program running on a Windows operating system.
    """


class WindowsThread(ProcessThread):
    """
    A Windows thread is a single thread of execution within a Windows process.
    """


class ConfiguredSoftware(Software):
    """
    A ConfiguredSoftware is a Software that is known to be configured to run in
    a more specified manner than some unconfigured or less-configured Software.
    """

    usesConfiguration: configuration.Configuration | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    isConfigurationOf: Software | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )


class OperatingSystem(Software):
    """
    An operating system is the software that manages computer hardware, software
    resources, and provides common services for computer programs. [based on
    https://en.wikipedia.org/wiki/Operating_system]
    """


class WindowsTaskFacet(core.Facet):
    """
    A Windows Task facet is a grouping of characteristics unique to a Windows
    Task (a process that is scheduled to execute on a Windows operating system
    by the Windows Task Scheduler). [based on
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]
    """

    account: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    application: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    workItemData: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    workingDirectory: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    actionList: TaskActionType | list[TaskActionType] | None = []
    triggerList: TriggerType | list[TriggerType] | None = []
    mostRecentRunTime: AwareDatetime | None = None
    nextRunTime: AwareDatetime | None = None
    observableCreatedTime: AwareDatetime | None = None
    exitCode: int | None = None
    maxRunTime: int | None = None
    accountLogonType: str | None = None
    accountRunLevel: str | None = None
    imageName: str | None = None
    parameters: str | None = None
    taskComment: str | None = None
    taskCreator: str | None = None
    flags: vocabulary.TaskFlagVocab | list[vocabulary.TaskFlagVocab] | None = []
    priority: (
        vocabulary.TaskPriorityVocab | list[vocabulary.TaskPriorityVocab] | None
    ) = []
    status: vocabulary.TaskStatusVocab | list[vocabulary.TaskStatusVocab] | None = []


class URLHistoryFacet(core.Facet):
    """
    A URL history facet is a grouping of characteristics unique to the stored
    URL history for a particular web browser
    """

    browserInformation: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    urlHistoryEntry: URLHistoryEntry | list[URLHistoryEntry] | None = []


class WhoIsFacet(core.Facet):
    """
    A whois facet is a grouping of characteristics unique to a response record
    conformant to the WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]
    """

    regionalInternetRegistry: (
        vocabulary.RegionalRegistryTypeVocab
        | list[vocabulary.RegionalRegistryTypeVocab]
        | None
    ) = []
    domainName: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    ipAddress: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    registrantContactInfo: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    serverName: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    nameServer: ObservableObject | list[ObservableObject] | None = []
    registrarInfo: WhoisRegistrarInfoType | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    creationDate: AwareDatetime | None = None
    expirationDate: AwareDatetime | None = None
    lookupDate: AwareDatetime | None = None
    updatedDate: AwareDatetime | None = None
    domainID: str | None = None
    remarks: str | None = None
    sponsoringRegistrar: str | None = None
    registrantIDs: str | list[str] | None = []
    dnssec: vocabulary.WhoisDNSSECTypeVocab | None = None
    status: (
        vocabulary.WhoisStatusTypeVocab | list[vocabulary.WhoisStatusTypeVocab] | None
    ) = []


class ApplicationAccount(DigitalAccount):
    """
    An application account is an account within a particular software program
    designed for end users.
    """


class EmailAccount(DigitalAccount):
    """
    An email account is an arrangement with an entity to enable and control the
    provision of electronic mail (email) capabilities or services.
    """


class MobileAccount(DigitalAccount):
    """
    A mobile account is an arrangement with an entity to enable and control the
    provision of some capability or service on a portable computing device.
    [based on https://www.lexico.com/definition/mobile_device]
    """


class PhoneAccount(DigitalAccount):
    """
    A phone account is an arrangement with an entity to enable and control the
    provision of a telephony capability or service.
    """


class UNIXAccount(DigitalAccount):
    """
    A UNIX account is an account on a UNIX operating system.
    """


class UserAccount(DigitalAccount):
    """
    A user account is an account controlling a user's access to a network,
    system or platform.
    """


class WindowsAccount(DigitalAccount):
    """
    A Windows account is a user account on a Windows operating system.
    """


class WindowsActiveDirectoryAccount(DigitalAccount):
    """
    A Windows Active Directory account is an account managed by directory-based
    identity-related services of a Windows operating system.
    """


class EmailAddress(DigitalAddress):
    """
    An email address is an identifier for an electronic mailbox to which
    electronic mail messages (conformant to the Simple Mail Transfer Protocol
    (SMTP)) are sent from and delivered to.
    """


class IPAddress(DigitalAddress):
    """
    An IP address is an Internet Protocol (IP) standards conformant identifier
    assigned to a device to enable routing and management of IP standards
    conformant communication to or from that device.
    """


class InstantMessagingAddress(DigitalAddress):

    pass


class MACAddress(DigitalAddress):
    """
    A MAC address is a media access control standards conformant identifier
    assigned to a network interface to enable routing and management of
    communications at the data link layer of a network segment.
    """


class SIPAddress(DigitalAddress):
    """
    A SIP address is an identifier for Session Initiation Protocol (SIP)
    communication.
    """


class ContactFacet(core.Facet):
    """
    A contact facet is a grouping of characteristics unique to a set of
    identification and communication related details for a single entity.
    """

    contactAddress: ContactAddress | list[ContactAddress] | None = []
    contactAffiliation: ContactAffiliation | list[ContactAffiliation] | None = []
    contactEmail: ContactEmail | list[ContactEmail] | None = []
    contactMessaging: ContactMessaging | list[ContactMessaging] | None = []
    contactPhone: ContactPhone | list[ContactPhone] | None = []
    contactProfile: ContactProfile | list[ContactProfile] | None = []
    contactSIP: ContactSIP | list[ContactSIP] | None = []
    contactURL: ContactURL | list[ContactURL] | None = []
    sourceApplication: ObservableObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    birthdate: AwareDatetime | None = None
    lastTimeContacted: AwareDatetime | None = None
    numberTimesContacted: int | None = None
    contactID: str | None = None
    displayName: str | None = None
    firstName: str | None = None
    lastName: str | None = None
    middleName: str | None = None
    namePhonetic: str | None = None
    namePrefix: str | None = None
    nameSuffix: str | None = None
    contactGroup: str | list[str] | None = []
    contactNote: str | list[str] | None = []
    nickname: str | list[str] | None = []


class AndroidPhone(AndroidDevice):
    """
    An android phone is a smart phone that applies the Android mobile operating
    system.
    """


class IPhone(AppleDevice):
    """
    An iPhone is a smart phone that applies the iOS mobile operating system.
    """


class NetworkAppliance(Appliance):
    """
    A network appliance is a purpose-built computer with software or firmware
    that is designed to provide a specific network management function.
    """


class SecurityAppliance(Appliance):
    """
    A security appliance is a purpose-built computer with software or firmware
    that is designed to provide a specific security function to protect computer
    networks.
    """


class Laptop(Computer):
    """
    A laptop, laptop computer, or notebook computer is a small, portable
    personal computer with a screen and alphanumeric keyboard. These typically
    have a clam shell form factor with the screen mounted on the inside of the
    upper lid and the keyboard on the inside of the lower lid, although 2-in-1
    PCs with a detachable keyboard are often marketed as laptops or as having a
    laptop mode. (Devices categorized by their manufacturer as a Laptop)
    """


class Server(Computer):
    """
    A server is a server rack-mount based computer, minicomputer, supercomputer,
    etc.
    """


class SmartPhone(Computer):
    """
    A smartphone is a portable device that combines mobile telephone and
    computing functions into one unit. Examples include iPhone, Samsung Galaxy,
    Huawei, Blackberry. (Inferred by model and OperatingSystemFacet)
    """


class Tablet(Computer):
    """
    A tablet is a mobile computer that is primarily operated by touching the
    screen. (Devices categorized by their manufacturer as a Tablet)
    """


class Drone(MobileDevice):
    """
    A drone, unmanned aerial vehicle (UAV), is an aircraft without a human
    pilot, crew, or passengers that typically involve a ground-based controller
    and a system for communications with the UAV.
    """


class MobilePhone(MobileDevice):
    """
    A mobile phone is a portable telephone that at least can make and receive
    calls over a radio frequency link while the user is moving within a
    telephone service area. This category encompasses all types of mobiles,
    simple and smart and satellite ones all together.
    """


class WearableDevice(SmartDevice):
    """
    A wearable device is an electronic device that is designed to be worn on a
    person's body.
    """


class Disk(StorageMedium):
    """
    A disk is a storage mechanism where data is recorded by various electronic,
    magnetic, optical, or mechanical changes to a surface layer of one or more
    rotating disks.
    """


class NTFSFileFacet(core.Facet):
    """
    An NTFS file facet is a grouping of characteristics unique to a file on an
    NTFS (new technology filesystem) file system.
    """

    alternateDataStreams: AlternateDataStream | list[AlternateDataStream] | None = []
    entryID: int | None = None
    sid: str | None = None


class ArchiveFile(File):
    """
    An archive file is a file that is composed of one or more computer files
    along with metadata.
    """


class NTFSFile(File):
    """
    An NTFS file is a New Technology File System (NTFS) file.
    """


class PDFFile(File):
    """
    A PDF file is a Portable Document Format (PDF) file.
    """


class RasterPicture(File):
    """
    A raster picture is a raster (or bitmap) image.
    """


class UNIXFile(File):
    """
    A UNIX file is a file pertaining to the UNIX operating system.
    """


class WindowsPEBinaryFile(File):
    """
    A Windows PE binary file is a Windows portable executable (PE) file.
    """


class IPv4Address(IPAddress):
    """
    An IPv4 (Internet Protocol version 4) address is an IPv4 standards
    conformant identifier assigned to a device to enable routing and management
    of IPv4 standards conformant communication to or from that device.
    """


class IPv6Address(IPAddress):
    """
    An IPv6 (Internet Protocol version 6) address is an IPv6 standards
    conformant identifier assigned to a device to enable routing and management
    of IPv6 standards conformant communication to or from that device.
    """


class BluetoothAddress(MACAddress):
    """
    A Bluetooth address is a Bluetooth standard conformant identifier assigned
    to a Bluetooth device to enable routing and management of Bluetooth
    standards conformant communication to or from that device.
    """


class WifiAddress(MACAddress):
    """
    A Wi-Fi address is a media access control (MAC) standards-conformant
    identifier assigned to a device network interface to enable routing and
    management of IEEE 802.11 standards-conformant communications to and from
    that device.
    """


class WhoisContactFacet(ContactFacet):
    """
    A Whois contact type is a grouping of characteristics unique to
    contact-related information present in a response record conformant to the
    WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]
    """

    whoisContactType: (
        vocabulary.WhoisContactTypeVocab | list[vocabulary.WhoisContactTypeVocab] | None
    ) = []


class BlackberryPhone(SmartPhone):
    """
    A blackberry phone is a smart phone that applies the Blackberry OS mobile
    operating system. (Blackberry 10 re-introduces Blackberry OS, prior to that
    the OS was Android.)
    """
