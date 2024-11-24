
"""
Auto-generated classes from the SHACL graph in observable.ttl.

This file was generated using the `case_models.py` script.
"""

from fastlabel.case import (identity, types, core, configuration, action, location)
from typing import Any, Optional
from enum import Enum

class NetworkSocketAddressFamily(str, Enum):
    AF_APPLETALK = 'af_appletalk'
    AF_BTH = 'af_bth'
    AF_INET = 'af_inet'
    AF_INET6 = 'af_inet6'
    AF_IPX = 'af_ipx'
    AF_IRDA = 'af_irda'
    AF_NETBIOS = 'af_netbios'
    AF_UNSPEC = 'af_unspec'

class NetworkSocketProtocolFamily(str, Enum):
    PF_APPLETALK = 'pf_appletalk'
    PF_ASH = 'pf_ash'
    PF_ATMPVC = 'pf_atmpvc'
    PF_ATMSVC = 'pf_atmsvc'
    PF_AX25 = 'pf_ax25'
    PF_BLUETOOTH = 'pf_bluetooth'
    PF_BRIDGE = 'pf_bridge'
    PF_DECNET = 'pf_decnet'
    PF_ECONET = 'pf_econet'
    PF_INET = 'pf_inet'
    PF_INET6 = 'pf_inet6'
    PF_IPX = 'pf_ipx'
    PF_IRDA = 'pf_irda'
    PF_KEY = 'pf_key'
    PF_NETBEUI = 'pf_netbeui'
    PF_NETLINK = 'pf_netlink'
    PF_NETROM = 'pf_netrom'
    PF_PACKET = 'pf_packet'
    PF_PPPOX = 'pf_pppox'
    PF_ROSE = 'pf_rose'
    PF_ROUTE = 'pf_route'
    PF_SECURITY = 'pf_security'
    PF_SNA = 'pf_sna'
    PF_WANPIPE = 'pf_wanpipe'
    PF_X25 = 'pf_x25'

class NetworkSocketType(str, Enum):
    SOCK_DGRAM = 'sock_dgram'
    SOCK_RAW = 'sock_raw'
    SOCK_RDM = 'sock_rdm'
    SOCK_SEQPACKET = 'sock_seqpacket'
    SOCK_STREAM = 'sock_stream'

class RegistryDatatype(str, Enum):
    REG_BINARY = 'reg_binary'
    REG_DWORD = 'reg_dword'
    REG_DWORD_BIG_ENDIAN = 'reg_dword_big_endian'
    REG_EXPAND_SZ = 'reg_expand_sz'
    REG_FULL_RESOURCE_DESCRIPTOR = 'reg_full_resource_descriptor'
    REG_INVALID_TYPE = 'reg_invalid_type'
    REG_LINK = 'reg_link'
    REG_MULTI_SZ = 'reg_multi_sz'
    REG_NONE = 'reg_none'
    REG_QWORD = 'reg_qword'
    REG_RESOURCE_LIST = 'reg_resource_list'
    REG_RESOURCE_REQUIREMENTS_LIST = 'reg_resource_requirements_list'
    REG_SZ = 'reg_sz'

class WindowsPEBinaryType(str, Enum):
    DLL = 'dll'
    EXE = 'exe'
    SYS = 'sys'

class WindowsServiceStartType(str, Enum):
    SERVICE_AUTO_START = 'service_auto_start'
    SERVICE_BOOT_START = 'service_boot_start'
    SERVICE_DEMAND_START = 'service_demand_start'
    SERVICE_DISABLED = 'service_disabled'
    SERVICE_SYSTEM_ALERT = 'service_system_alert'

class WindowsServiceStatus(str, Enum):
    SERVICE_CONTINUE_PENDING = 'service_continue_pending'
    SERVICE_PAUSE_PENDING = 'service_pause_pending'
    SERVICE_PAUSED = 'service_paused'
    SERVICE_RUNNING = 'service_running'
    SERVICE_START_PENDING = 'service_start_pending'
    SERVICE_STOP_PENDING = 'service_stop_pending'
    SERVICE_STOPPED = 'service_stopped'

class WindowsServiceType(str, Enum):
    SERVICE_FILE_SYSTEM_DRIVER = 'service_file_system_driver'
    SERVICE_KERNEL_DRIVER = 'service_kernel_driver'
    SERVICE_WIN32_OWN_PROCESS = 'service_win32_own_process'
    SERVICE_WIN32_SHARE_PROCESS = 'service_win32_share_process'


class LibraryFacet(core.Facet):
    """
    A library facet is a grouping of characteristics unique to a suite of data
    and programming code that is used to develop software programs and
    applications. [based on
    https://www.techopedia.com/definition/3828/software-library]
    """

    libraryType: Optional[str] = None

class ICMPConnectionFacet(core.Facet):
    """
    An ICMP connection facet is a grouping of characteristics unique to portions
    of a network connection that are conformant to the Internet Control Message
    Protocol (ICMP) standard.
    """

    icmpCode: Optional[str] = None
    icmpType: Optional[str] = None

class EncryptedStreamFacet(core.Facet):
    """
    An encrypted stream facet is a grouping of characteristics unique to the
    conversion of a body of data content from one form to another obfuscated
    form in such a way that reversing the conversion to obtain the original data
    form can only be accomplished through possession and use of a specific key.
    """

    encryptionMethod: Optional[str] = None
    encryptionMode: Optional[str] = None
    encryptionIV: Optional[str] = None
    encryptionKey: Optional[str] = None

class ArchiveFileFacet(core.Facet):
    """
    An archive file facet is a grouping of characteristics unique to a file that
    is composed of one or more computer files along with metadata.
    """

    archiveType: Optional[str] = None
    comment: Optional[str] = None
    version: Optional[str] = None

class UNIXVolumeFacet(core.Facet):
    """
    A UNIX volume facet is a grouping of characteristics unique to a single
    accessible storage area (volume) with a single UNIX file system. [based on
    https://en.wikipedia.org/wiki/Volume_(computing)]
    """

    mountPoint: Optional[str] = None
    options: Optional[str] = None

class X509V3ExtensionsFacet(core.Facet):
    """
    An X.509 v3 certificate extensions facet is a grouping of characteristics
    unique to a public key digital identity certificate conformant to the X.509
    v3 PKI (Public Key Infrastructure) standard.
    """

    privateKeyUsagePeriodNotAfter: Optional[str] = None
    privateKeyUsagePeriodNotBefore: Optional[str] = None
    authorityKeyIdentifier: Optional[str] = None
    basicConstraints: Optional[str] = None
    certificatePolicies: Optional[str] = None
    crlDistributionPoints: Optional[str] = None
    extendedKeyUsage: Optional[str] = None
    inhibitAnyPolicy: Optional[str] = None
    issuerAlternativeName: Optional[str] = None
    keyUsage: Optional[str] = None
    nameConstraints: Optional[str] = None
    policyConstraints: Optional[str] = None
    policyMappings: Optional[str] = None
    subjectAlternativeName: Optional[str] = None
    subjectDirectoryAttributes: Optional[str] = None
    subjectKeyIdentifier: Optional[str] = None

class PhoneAccountFacet(core.Facet):
    """
    A phone account facet is a grouping of characteristics unique to an
    arrangement with an entity to enable and control the provision of a
    telephony capability or service.
    """

    phoneNumber: Optional[str] = None

class MobileAccountFacet(core.Facet):
    """
    A mobile account facet is a grouping of characteristics unique to an
    arrangement with an entity to enable and control the provision of some
    capability or service on a portable computing device. [based on
    https://www.lexico.com/definition/mobile_device]
    """

    IMSI: Optional[str] = None
    MSISDN: Optional[str] = None
    MSISDNType: Optional[str] = None

class ImageFacet(core.Facet):
    """
    An image facet is a grouping of characteristics unique to a complete copy of
    a hard disk, memory, or other digital media.
    """

    imageType: Optional[str] = None

class PropertiesEnumeratedEffectFacet(core.Facet):
    """
    A properties enumerated effect facet is a grouping of characteristics unique
    to the effects of actions upon observable objects where a characteristic of
    the observable object is enumerated. An example of this would be startup
    parameters for a process.
    """

    properties: Optional[str] = None

class DefinedEffectFacet(core.Facet):
    """
    A defined effect facet is a grouping of characteristics unique to the effect
    of an observable action in relation to one or more observable objects.
    """

    pass

class DigitalAddressFacet(core.Facet):
    """
    A digital address facet is a grouping of characteristics unique to an
    identifier assigned to enable routing and management of digital
    communication.
    """

    addressValue: Optional[str] = None
    displayName: Optional[str] = None

class WindowsRegistryHiveFacet(core.Facet):
    """
    A Windows registry hive facet is a grouping of characteristics unique to a
    particular logical group of keys, subkeys, and values in a Windows registry
    (a hierarchical database that stores low-level settings for the Microsoft
    Windows operating system and for applications that opt to use the registry).
    [based on https://en.wikipedia.org/wiki/Windows_Registry]
    """

    hiveType: Optional[str] = None

class NTFSFilePermissionsFacet(core.Facet):
    """
    An NTFS file permissions facet is a grouping of characteristics unique to
    the access rights (e.g., view, change, navigate, execute) of a file on an
    NTFS (new technology filesystem) file system.
    """

    pass

class EncodedStreamFacet(core.Facet):
    """
    An encoded stream facet is a grouping of characteristics unique to the
    conversion of a body of data content from one form to another form.
    """

    encodingMethod: Optional[str] = None

class WindowsAccountFacet(core.Facet):
    """
    A Windows account facet is a grouping of characteristics unique to a user
    account on a Windows operating system.
    """

    groups: Optional[str] = None

class WindowsServiceFacet(core.Facet):
    """
    A Windows service facet is a grouping of characteristics unique to a
    specific Windows service (a computer program that operates in the background
    of a Windows operating system, similar to the way a UNIX daemon runs on
    UNIX). [based on https://en.wikipedia.org/wiki/Windows_service]
    """

    displayName: Optional[str] = None
    groupName: Optional[str] = None
    serviceName: Optional[str] = None
    serviceStatus: Optional[str] = None
    serviceType: Optional[str] = None
    startCommandLine: Optional[str] = None
    startType: Optional[str] = None
    descriptions: Optional[str] = None

class TCPConnectionFacet(core.Facet):
    """
    A TCP connection facet is a grouping of characteristics unique to portions
    of a network connection that are conformant to the Transmission Control
    Protocl (TCP) standard.
    """

    destinationFlags: Optional[str] = None
    sourceFlags: Optional[str] = None

class SQLiteBlobFacet(core.Facet):
    """
    An SQLite blob facet is a grouping of characteristics unique to a blob
    (binary large object) of data within an SQLite database. [based on
    https://en.wikipedia.org/wiki/SQLite]
    """

    rowIndex: Optional[str] = None
    columnName: Optional[str] = None
    rowCondition: Optional[str] = None
    tableName: Optional[str] = None

class WindowsActiveDirectoryAccountFacet(core.Facet):
    """
    A Windows Active Directory account facet is a grouping of characteristics
    unique to an account managed by directory-based identity-related services of
    a Windows operating system.
    """

    objectGUID: Optional[str] = None
    activeDirectoryGroups: Optional[str] = None

class UNIXFilePermissionsFacet(core.Facet):
    """
    A UNIX file permissions facet is a grouping of characteristics unique to the
    access rights (e.g., view, change, navigate, execute) of a file on a UNIX
    file system.
    """

    pass

class PathRelationFacet(core.Facet):
    """
    A path relation facet is a grouping of characteristics unique to the
    location of one object within another containing object.
    """

    path: Optional[str] = None

class CellSiteFacet(core.Facet):
    """
    A cell site facet contains the metadata surrounding the cell site.
    """

    cellSiteCountryCode: Optional[str] = None
    cellSiteIdentifier: Optional[str] = None
    cellSiteLocationAreaCode: Optional[str] = None
    cellSiteNetworkCode: Optional[str] = None
    cellSiteType: Optional[str] = None

class AccountAuthenticationFacet(core.Facet):
    """
    An account authentication facet is a grouping of characteristics unique to
    the mechanism of accessing an account.
    """

    passwordLastChanged: Optional[str] = None
    password: Optional[str] = None
    passwordType: Optional[str] = None

class AudioFacet(core.Facet):
    """
    An audio facet is a grouping of characteristics unique to a digital
    representation of sound.
    """

    bitRate: Optional[int] = None
    duration: Optional[int] = None
    audioType: Optional[str] = None
    format: Optional[str] = None

class WindowsThreadFacet(core.Facet):
    """
    A Windows thread facet is a grouping os characteristics unique to a single
    thread of execution within a Windows process.
    """

    observableCreatedTime: Optional[str] = None
    parameterAddress: Optional[str] = None
    startAddress: Optional[str] = None
    priority: Optional[int] = None
    stackSize: Optional[int] = None
    threadID: Optional[int] = None
    context: Optional[str] = None
    runningStatus: Optional[str] = None
    securityAttributes: Optional[str] = None
    creationFlags: Optional[str] = None

class StorageMediumFacet(core.Facet):
    """
    A storage medium facet is a grouping of characteristics unique to a the
    storage capabilities of a piece of equipment or a mechanism designed to
    serve a special purpose or perform a special function.
    """

    totalStorageCapacityInBytes: Optional[int] = None

class FragmentFacet(core.Facet):
    """
    A fragment facet is a grouping of characteristics unique to an individual
    piece of the content of a file.
    """

    fragmentIndex: Optional[int] = None
    totalFragments: Optional[int] = None

class VolumeFacet(core.Facet):
    """
    A volume facet is a grouping of characteristics unique to a single
    accessible storage area (volume) with a single file system. [based on
    https://en.wikipedia.org/wiki/Volume_(computing)]
    """

    sectorSize: Optional[int] = None
    volumeID: Optional[str] = None

class FileSystemFacet(core.Facet):
    """
    A file system facet is a grouping of characteristics unique to the process
    that manages how and where data on a storage medium is stored, accessed and
    managed. [based on https://www.techopedia.com/definition/5510/file-system]
    """

    clusterSize: Optional[int] = None
    fileSystemType: Optional[str] = None

class UNIXProcessFacet(core.Facet):
    """
    A UNIX process facet is a grouping of characteristics unique to an instance
    of a computer program executed on a UNIX operating system.
    """

    openFileDescriptor: Optional[int] = None
    ruid: Optional[int] = None

class MftRecordFacet(core.Facet):
    """
    An MFT record facet is a grouping of characteristics unique to the details
    of a single file as managed in an NTFS (new technology filesystem) master
    file table (which is a collection of information about all files on an NTFS
    filesystem). [based on
    https://docs.microsoft.com/en-us/windows/win32/devnotes/master-file-table]
    """

    mftFileNameAccessedTime: Optional[str] = None
    mftFileNameCreatedTime: Optional[str] = None
    mftFileNameModifiedTime: Optional[str] = None
    mftFileNameRecordChangeTime: Optional[str] = None
    mftRecordChangeTime: Optional[str] = None
    mftFileID: Optional[int] = None
    mftFileNameLength: Optional[int] = None
    mftFlags: Optional[int] = None
    mftParentID: Optional[int] = None
    ntfsHardLinkCount: Optional[int] = None
    ntfsOwnerID: Optional[str] = None
    ntfsOwnerSID: Optional[str] = None

class DiskPartitionFacet(core.Facet):
    """
    A disk partition facet is a grouping of characteristics unique to a
    particular managed region on a storage mechanism.
    """

    observableCreatedTime: Optional[str] = None
    partitionLength: Optional[int] = None
    partitionOffset: Optional[int] = None
    spaceLeft: Optional[int] = None
    spaceUsed: Optional[int] = None
    totalSpace: Optional[int] = None
    diskPartitionType: Optional[str] = None
    mountPoint: Optional[str] = None
    partitionID: Optional[str] = None

class DataRangeFacet(core.Facet):
    """
    A data range facet is a grouping of characteristics unique to a particular
    contiguous scope within a block of digital data.
    """

    rangeOffset: Optional[int] = None
    rangeSize: Optional[int] = None
    rangeOffsetType: Optional[str] = None

class UNIXAccountFacet(core.Facet):
    """
    A UNIX account facet is a grouping of characteristics unique to an account
    on a UNIX operating system.
    """

    gid: Optional[int] = None
    shell: Optional[str] = None

class ExtInodeFacet(core.Facet):
    """
    An extInode facet is a grouping of characteristics unique to a file system
    object (file, directory, etc.) conformant to the extended file system (EXT
    or related derivations) specification.
    """

    extDeletionTime: Optional[str] = None
    extInodeChangeTime: Optional[str] = None
    extFileType: Optional[int] = None
    extFlags: Optional[int] = None
    extHardLinkCount: Optional[int] = None
    extInodeID: Optional[int] = None
    extPermissions: Optional[int] = None
    extSGID: Optional[int] = None
    extSUID: Optional[int] = None

class AutonomousSystemFacet(core.Facet):
    """
    An autonomous system facet is a grouping of characteristics unique to a
    collection of connected Internet Protocol (IP) routing prefixes under the
    control of one or more network operators on behalf of a single
    administrative entity or domain that presents a common, clearly defined
    routing policy to the Internet. [based on
    https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]
    """

    regionalInternetRegistry: Optional[Any] = None
    regionalInternetRegistry: Optional[str] = None
    number: Optional[int] = None
    asHandle: Optional[str] = None
    regionalInternetRegistry: Optional[Any] = None

class RecoveredObjectFacet(core.Facet):
    """
    Recoverability status of name, metadata, and content.
    """

    contentRecoveredStatus: Optional[str] = None
    metadataRecoveredStatus: Optional[str] = None
    nameRecoveredStatus: Optional[str] = None
    nameRecoveredStatus: Optional[Any] = None
    metadataRecoveredStatus: Optional[Any] = None
    contentRecoveredStatus: Optional[Any] = None
    nameRecoveredStatus: Optional[Any] = None
    metadataRecoveredStatus: Optional[Any] = None
    contentRecoveredStatus: Optional[Any] = None

class WirelessNetworkConnectionFacet(core.Facet):
    """
    A wireless network connection facet is a grouping of characteristics unique
    to a connection (completed or attempted) across an IEEE 802.11
    standards-conformant digital network (a group of two or more computer
    systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]
    """

    baseStation: Optional[str] = None
    password: Optional[str] = None
    ssid: Optional[str] = None
    wirelessNetworkSecurityMode: Optional[Any] = None
    wirelessNetworkSecurityMode: Optional[Any] = None

class WindowsVolumeFacet(core.Facet):
    """
    A Windows volume facet is a grouping of characteristics unique to a single
    accessible storage area (volume) with a single Windows file system. [based
    on https://en.wikipedia.org/wiki/Volume_(computing)]
    """

    driveLetter: Optional[str] = None
    driveType: Optional[str] = None
    windowsVolumeAttributes: list[str] = None
    driveType: Optional[Any] = None
    driveType: Optional[Any] = None

class TableFieldFacet(core.Facet):
    """
    A database record facet contains properties associated with a specific table
    record value from a database.
    """

    recordFieldIsNull: Optional[bool] = None
    recordFieldName: Optional[str] = None
    tableName: Optional[str] = None
    tableSchema: Optional[str] = None
    recordFieldValue: Optional[Any] = None
    recordRowID: Optional[Any] = None

class MemoryFacet(core.Facet):
    """
    A memory facet is a grouping of characteristics unique to a particular
    region of temporary information storage (e.g., RAM (random access memory),
    ROM (read only memory)) on a digital device.
    """

    isInjected: Optional[bool] = None
    isMapped: Optional[bool] = None
    isProtected: Optional[bool] = None
    isVolatile: Optional[bool] = None
    regionEndAddress: Optional[str] = None
    regionStartAddress: Optional[str] = None
    regionSize: Optional[int] = None
    blockType: Optional[str] = None
    blockType: Optional[Any] = None
    blockType: Optional[Any] = None

class FileFacet(core.Facet):
    """
    A file facet is a grouping of characteristics unique to the storage of a
    file (computer resource for recording data discretely in a computer storage
    device) on a file system (process that manages how and where data on a
    storage device is stored, accessed and managed). [based on
    https://en.wikipedia.org/Computer_file and
    https://www.techopedia.com/definition/5510/file-system]
    """

    isDirectory: Optional[bool] = None
    accessedTime: Optional[str] = None
    metadataChangeTime: Optional[str] = None
    modifiedTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    sizeInBytes: Optional[int] = None
    allocationStatus: Optional[str] = None
    extension: Optional[str] = None
    fileName: Optional[str] = None
    filePath: Optional[str] = None

class MutexFacet(core.Facet):
    """
    A mutex facet is a grouping of characteristics unique to a mechanism that
    enforces limits on access to a resource when there are many threads of
    execution. A mutex is designed to enforce a mutual exclusion concurrency
    control policy, and with a variety of possible methods there exists multiple
    unique implementations for different applications. [based on
    https://en.wikipedia.org/wiki/Lock_(computer_science)]
    """

    isNamed: Optional[bool] = None
    mutexName: Optional[str] = None

class DomainNameFacet(core.Facet):
    """
    A domain name facet is a grouping of characteristics unique to an
    identification string that defines a realm of administrative autonomy,
    authority or control within the Internet. [based on
    https://en.wikipedia.org/wiki/Domain_name]
    """

    isTLD: Optional[bool] = None
    value: Optional[str] = None

class SMSMessageFacet(core.Facet):
    """
    A SMS message facet is a grouping of characteristics unique to a message
    conformant to the short message service (SMS) communication protocol
    standards.
    """

    isRead: Optional[bool] = None

class AndroidDeviceFacet(core.Facet):
    """
    An Android device facet is a grouping of characteristics unique to an
    Android device. [based on
    https://en.wikipedia.org/wiki/Android_(operating_system)]
    """

    isADBRootEnabled: Optional[bool] = None
    isSURootEnabled: Optional[bool] = None
    androidID: Optional[str] = None
    androidFingerprint: Optional[str] = None
    androidVersion: Optional[str] = None

class DigitalAccountFacet(core.Facet):
    """
    A digital account facet is a grouping of characteristics unique to an
    arrangement with an entity to enable and control the provision of some
    capability or service within the digital domain.
    """

    isDisabled: Optional[bool] = None
    firstLoginTime: Optional[str] = None
    lastLoginTime: Optional[str] = None
    displayName: Optional[str] = None
    accountLogin: Optional[str] = None

class UserAccountFacet(core.Facet):
    """
    A user account facet is a grouping of characteristics unique to an account
    controlling a user's access to a network, system, or platform.
    """

    canEscalatePrivs: Optional[bool] = None
    isPrivileged: Optional[bool] = None
    isServiceAccount: Optional[bool] = None
    homeDirectory: Optional[str] = None

class MobileDeviceFacet(core.Facet):
    """
    A mobile device facet is a grouping of characteristics unique to a portable
    computing device. [based on https://www.lexico.com/definition/mobile_device]
    """

    mockLocationsAllowed: Optional[bool] = None
    clockSetting: Optional[str] = None
    phoneActivationTime: Optional[str] = None
    storageCapacityInBytes: Optional[int] = None
    ESN: Optional[str] = None
    bluetoothDeviceName: Optional[str] = None
    keypadUnlockCode: Optional[str] = None
    network: Optional[str] = None
    IMEI: Optional[str] = None

class SoftwareFacet(core.Facet):
    """
    A software facet is a grouping of characteristics unique to a software
    program (a definitively scoped instance of a collection of data or computer
    instructions that tell the computer how to work). [based on
    https://en.wikipedia.org/wiki/Software]
    """

    manufacturer: Optional[identity.Identity] = None
    cpeid: Optional[str] = None
    language: Optional[str] = None
    swid: Optional[str] = None
    version: Optional[str] = None

class DeviceFacet(core.Facet):
    """
    A device facet is a grouping of characteristics unique to a piece of
    equipment or a mechanism designed to serve a special purpose or perform a
    special function. [based on
    https://www.merriam-webster.com/dictionary/device]
    """

    manufacturer: Optional[identity.Identity] = None
    deviceType: Optional[str] = None
    model: Optional[str] = None
    serialNumber: Optional[str] = None

class SIMCardFacet(core.Facet):
    """
    A SIM card facet is a grouping of characteristics unique to a subscriber
    identification module card intended to securely store the international
    mobile subscriber identity (IMSI) number and its related key, which are used
    to identify and authenticate subscribers on mobile telephony devices (such
    as mobile phones and computers). [based on
    https://en.wikipedia.org/wiki/SIM_card]
    """

    carrier: Optional[identity.Identity] = None
    storageCapacityInBytes: Optional[int] = None
    ICCID: Optional[str] = None
    IMSI: Optional[str] = None
    PIN: Optional[str] = None
    PUK: Optional[str] = None
    SIMForm: Optional[str] = None
    SIMType: Optional[str] = None

class AntennaFacet(core.Facet):
    """
    An antenna alignment facet contains the metadata surrounding the cell
    tower's antenna position.
    """

    antennaHeight: Optional[float] = None
    azimuth: Optional[float] = None
    elevation: Optional[float] = None
    horizontalBeamWidth: Optional[float] = None
    signalStrength: Optional[float] = None
    skew: Optional[float] = None

class CompressedStreamFacet(core.Facet):
    """
    A compressed stream facet is a grouping of characteristics unique to the
    application of a size-reduction process to a body of data content.
    """

    compressionRatio: Optional[float] = None
    compressionMethod: Optional[str] = None

class IShowMessageActionType(core.UcoInherentCharacterizationThing):
    """
    An IShow message action type is a grouping of characteristics unique to an
    action that shows a message box when a task is activate. [based on
    https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-ishowmessageaction?redirectedfrom=MSDN]
    """

    showMessageBody: Optional[str] = None
    showMessageTitle: Optional[str] = None

class WindowsPEOptionalHeader(core.UcoInherentCharacterizationThing):
    """
    A Windows PE optional header is a grouping of characteristics unique to the
    'optional header' of a Windows PE (Portable Executable) file, consisting of
    a collection of metadata about the executable code structure of the file.
    """

    majorLinkerVersion: Optional[str] = None
    minorLinkerVersion: Optional[str] = None
    addressOfEntryPoint: Optional[str] = None
    baseOfCode: Optional[str] = None
    checksum: Optional[str] = None
    fileAlignment: Optional[str] = None
    imageBase: Optional[str] = None
    loaderFlags: Optional[str] = None
    numberOfRVAAndSizes: Optional[str] = None
    sectionAlignment: Optional[str] = None
    sizeOfCode: Optional[str] = None
    sizeOfHeaders: Optional[str] = None
    sizeOfHeapCommit: Optional[str] = None
    sizeOfHeapReserve: Optional[str] = None
    sizeOfImage: Optional[str] = None
    sizeOfInitializedData: Optional[str] = None
    sizeOfStackCommit: Optional[str] = None
    sizeOfStackReserve: Optional[str] = None
    sizeOfUninitializedData: Optional[str] = None
    win32VersionValue: Optional[str] = None
    dllCharacteristics: Optional[str] = None
    magic: Optional[str] = None
    majorImageVersion: Optional[str] = None
    majorOSVersion: Optional[str] = None
    majorSubsystemVersion: Optional[str] = None
    minorImageVersion: Optional[str] = None
    minorOSVersion: Optional[str] = None
    minorSubsystemVersion: Optional[str] = None
    subsystem: Optional[str] = None

class ApplicationVersion(core.UcoInherentCharacterizationThing):
    """
    An application version is a grouping of characteristics unique to a
    particular software program version.
    """

    installDate: Optional[str] = None
    uninstallDate: Optional[str] = None
    version: Optional[str] = None

class WindowsRegistryValue(core.UcoInherentCharacterizationThing):
    """
    A Windows registry value is a grouping of characteristics unique to a
    particular value within a Windows registry (a hierarchical database that
    stores low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry. [based on
    https://en.wikipedia.org/wiki/Windows_Registry]
    """

    name: Optional[str] = None
    data: Optional[str] = None
    dataType: Optional[str] = None

class GlobalFlagType(core.UcoInherentCharacterizationThing):
    """
    A global flag type is a grouping of characteristics unique to the Windows
    systemwide global variable named NtGlobalFlag that enables various internal
    debugging, tracing, and validation support in the operating system. [based
    on "Windows Global Flags, Chapter 3: System Mechanisms of Windows Internals
    by Solomon, Russinovich, and Ionescu]
    """

    hexadecimalValue: Optional[str] = None
    abbreviation: Optional[str] = None
    destination: Optional[str] = None
    symbolicName: Optional[str] = None

class IComHandlerActionType(core.UcoInherentCharacterizationThing):
    """
    An IComHandler action type is a grouping of characteristics unique to a
    Windows Task-related action that fires a Windows COM handler (smart code in
    the client address space that can optimize calls between a client and
    server). [based on
    https://docs.microsoft.com/en-us/windows/win32/taskschd/comhandleraction]
    """

    comClassID: Optional[str] = None
    comData: Optional[str] = None

class TriggerType(core.UcoInherentCharacterizationThing):
    """
    A trigger type is a grouping of characterizes unique to a set of criteria
    that, when met, starts the execution of a task within a Windows operating
    system. [based on
    https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers]
    """

    isEnabled: Optional[bool] = None
    triggerBeginTime: Optional[str] = None
    triggerEndTime: Optional[str] = None
    triggerDelay: Optional[str] = None
    triggerMaxRunTime: Optional[str] = None
    triggerSessionChangeType: Optional[str] = None
    triggerFrequency: Optional[str] = None
    triggerType: Optional[str] = None
    triggerFrequency: Optional[Any] = None
    triggerType: Optional[Any] = None
    triggerFrequency: Optional[Any] = None
    triggerType: Optional[Any] = None

class WindowsPEFileHeader(core.UcoInherentCharacterizationThing):
    """
    A Windows PE file header is a grouping of characteristics unique to the
    'header' of a Windows PE (Portable Executable) file, consisting of a
    collection of metadata about the overall nature and structure of the file.
    """

    timeDateStamp: Optional[str] = None

class ExtractedString(core.UcoInherentCharacterizationThing):
    """
    An extracted string is a grouping of characteristics unique to a series of
    characters pulled from an observable object.
    """

    byteStringValue: Optional[str] = None
    length: Optional[int] = None
    encoding: Optional[str] = None
    englishTranslation: Optional[str] = None
    language: Optional[str] = None
    stringValue: Optional[str] = None

class EnvironmentVariable(core.UcoInherentCharacterizationThing):
    """
    An environment variable is a grouping of characteristics unique to a
    dynamic-named value that can affect the way running processes will behave on
    a computer. [based on https://en.wikipedia.org/wiki/Environment_variable]
    """

    name: Optional[str] = None
    value: Optional[str] = None

class EXIFFacet(core.Facet):
    """
    An EXIF (exchangeable image file format) facet is a grouping of
    characteristics unique to the formats for images, sound, and ancillary tags
    used by digital cameras (including smartphones), scanners and other systems
    handling image and sound files recorded by digital cameras conformant to
    JEIDA/JEITA/CIPA specifications. [based on
    https://en.wikipedia.org/wiki/Exif]
    """

    exifData: Optional[types.ControlledDictionary] = None

class PDFFileFacet(core.Facet):
    """
    A PDF file facet is a grouping of characteristics unique to a PDF (Portable
    Document Format) file.
    """

    documentInformationDictionary: Optional[types.ControlledDictionary] = None
    isOptimized: Optional[bool] = None
    pdfCreationDate: Optional[str] = None
    pdfModDate: Optional[str] = None
    pdfId1: Optional[str] = None
    version: Optional[str] = None
    pdfId0: Optional[str] = None

class OperatingSystemFacet(core.Facet):
    """
    An operating system facet is a grouping of characteristics unique to the
    software that manages computer hardware, software resources, and provides
    common services for computer programs. [based on
    https://en.wikipedia.org/wiki/Operating_system]
    """

    environmentVariables: Optional[types.Dictionary] = None
    isLimitAdTrackingEnabled: Optional[bool] = None
    installDate: Optional[str] = None
    bitness: Optional[str] = None
    advertisingID: Optional[str] = None
    manufacturer: Optional[Any] = None
    version: Optional[Any] = None

class WindowsProcessFacet(core.Facet):
    """
    A Windows process facet is a grouping of characteristics unique to a program
    running on a Windows operating system.
    """

    startupInfo: Optional[types.Dictionary] = None
    aslrEnabled: Optional[bool] = None
    depEnabled: Optional[bool] = None
    ownerSID: Optional[str] = None
    priority: Optional[str] = None
    windowTitle: Optional[str] = None

class AccountFacet(core.Facet):
    """
    An account facet is a grouping of characteristics unique to an arrangement
    with an entity to enable and control the provision of some capability or
    service.
    """

    accountIssuer: Optional[core.UcoObject] = None
    owner: Optional[core.UcoObject] = None
    isActive: Optional[bool] = None
    expirationTime: Optional[str] = None
    modifiedTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    accountIdentifier: Optional[str] = None
    accountType: Optional[str] = None
    accountType: Optional[Any] = None
    accountType: Optional[Any] = None

class Observable(core.UcoObject):
    """
    An observable is a characterizable item or action within the digital domain.
    """

    pass

class FilePermissionsFacet(core.Facet):
    """
    A file permissions facet is a grouping of characteristics unique to the
    access rights (e.g., view, change, navigate, execute) of a file on a file
    system.
    """

    owner: Optional[core.UcoObject] = None

class DigitalSignatureInfoFacet(core.Facet):
    """
    A digital signature info facet is a grouping of characteristics unique to a
    value calculated via a mathematical scheme for demonstrating the
    authenticity of an electronic message or document.
    """

    certificateSubject: Optional[core.UcoObject] = None
    certificateIssuer: Optional[identity.Identity] = None
    signatureExists: Optional[bool] = None
    signatureVerified: Optional[bool] = None
    signatureDescription: Optional[str] = None

class WindowsPESection(core.UcoInherentCharacterizationThing):
    """
    A Windows PE section is a grouping of characteristics unique to a specific
    default or custom-defined region of a Windows PE (Portable Executable) file,
    consisting of an individual portion of the actual executable content of the
    file delineated according to unique purpose and memory protection
    requirements.
    """

    hashes: Optional[types.Hash] = None
    entropy: Optional[float] = None
    size: Optional[int] = None
    name: Optional[str] = None

class IExecActionType(core.UcoInherentCharacterizationThing):
    """
    An IExec action type is a grouping of characteristics unique to an action
    that executes a command-line operation on a Windows operating system. [based
    on
    https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-iexecaction?redirectedfrom=MSDN]
    """

    execProgramHashes: Optional[types.Hash] = None
    execArguments: Optional[str] = None
    execProgramPath: Optional[str] = None
    execWorkingDirectory: Optional[str] = None

class AlternateDataStreamFacet(core.Facet):
    """
    An alternate data stream facet is a grouping of characteristics unique to
    data content stored within an NTFS file that is independent of the standard
    content stream of the file and is hidden from access by default NTFS file
    viewing mechanisms.
    """

    hashes: Optional[types.Hash] = None
    size: Optional[int] = None
    name: Optional[str] = None

class ObservableObject(core.Item):
    """
    An observable object is a grouping of characteristics unique to a distinct
    article or unit within the digital domain.
    """

    hasChanged: Optional[bool] = None
    state: Optional[str] = None

class ObservableAction(action.Action):
    """
    An observable action is a grouping of characteristics unique to something
    that may be done or performed within the digital domain.
    """

    pass

class Observation(action.Action):
    """
    An observation is a temporal perception of an observable.
    """

    name: str

class ContactAddress(core.UcoInherentCharacterizationThing):
    """
    A contact address is a grouping of characteristics unique to a geolocation
    address of a contact entity.
    """

    geolocationAddress: Optional[location.Location] = None
    contactAddressScope: Optional[str] = None
    contactAddressScope: Optional[Any] = None
    contactAddressScope: Optional[Any] = None

class X509CertificateFacet(core.Facet):
    """
    A X.509 certificate facet is a grouping of characteristics unique to a
    public key digital identity certificate conformant to the X.509 PKI (Public
    Key Infrastructure) standard.
    """

    x509v3extensions: Optional[X509V3ExtensionsFacet] = None
    issuerHash: Optional[types.Hash] = None
    subjectHash: Optional[types.Hash] = None
    thumbprintHash: Optional[types.Hash] = None
    isSelfSigned: Optional[bool] = None
    validityNotAfter: Optional[str] = None
    validityNotBefore: Optional[str] = None
    subjectPublicKeyExponent: Optional[int] = None
    issuer: Optional[str] = None
    serialNumber: Optional[str] = None
    signature: Optional[str] = None
    signatureAlgorithm: Optional[str] = None
    subject: Optional[str] = None
    subjectPublicKeyAlgorithm: Optional[str] = None
    subjectPublicKeyModulus: Optional[str] = None
    version: Optional[str] = None

class PropertyReadEffectFacet(DefinedEffectFacet):
    """
    A properties read effect facet is a grouping of characteristics unique to
    the effects of actions upon observable objects where a characteristic is
    read from an observable object. An example of this would be the current
    running state of a process.
    """

    propertyName: Optional[str] = None
    value: Optional[str] = None

class ValuesEnumeratedEffectFacet(DefinedEffectFacet):
    """
    A values enumerated effect facet is a grouping of characteristics unique to
    the effects of actions upon observable objects where a value of the
    observable object is enumerated. An example of this would be the values of a
    registry key.
    """

    values: Optional[str] = None

class SendControlCodeEffectFacet(DefinedEffectFacet):
    """
    A send control code effect facet is a grouping of characteristics unique to
    the effects of actions upon observable objects where a control code, or
    other control-oriented communication signal, is sent to the observable
    object. An example of this would be an action sending a control code
    changing the running state of a process.
    """

    controlCode: Optional[str] = None

class IPAddressFacet(DigitalAddressFacet):
    """
    An IP address facet is a grouping of characteristics unique to an Internet
    Protocol (IP) standards conformant identifier assigned to a device to enable
    routing and management of IP standards conformant communication to or from
    that device.
    """

    pass

class EmailAddressFacet(DigitalAddressFacet):
    """
    An email address facet is a grouping of characteristics unique to an
    identifier for an electronic mailbox to which electronic mail messages
    (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and
    delivered to.
    """

    pass

class MACAddressFacet(DigitalAddressFacet):
    """
    A MAC address facet is a grouping of characteristics unique to a media
    access control standards conformant identifier assigned to a network
    interface to enable routing and management of communications at the data
    link layer of a network segment.
    """

    pass

class SIPAddressFacet(DigitalAddressFacet):
    """
    A SIP address facet is a grouping of characteristics unique to a Session
    Initiation Protocol (SIP) standards conformant identifier assigned to a user
    to enable routing and management of SIP standards conformant communication
    to or from that user loosely coupled from any particular devices.
    """

    pass

class InstantMessagingAddressFacet(DigitalAddressFacet):
    """
    An instant messaging address facet is a grouping of characteristics unique
    to an identifier assigned to enable routing and management of instant
    messaging digital communication.
    """

    pass

class ExtractedStringsFacet(core.Facet):
    """
    An extracted strings facet is a grouping of characteristics unique to one or
    more sequences of characters pulled from an observable object.
    """

    strings: Optional[ExtractedString] = None

class ObservablePattern(Observable):
    """
    An observable pattern is a grouping of characteristics unique to a logical
    pattern composed of observable object and observable action properties.
    """

    pass

class ObservableRelationship(core.Relationship):
    """
    An observable relationship is a grouping of characteristics unique to an
    assertion of an association between two observable objects.
    """

    source: Optional[Observable] = None
    target: Optional[Observable] = None

class WindowsPEBinaryFileFacet(core.Facet):
    """
    A Windows PE binary file facet is a grouping of characteristics unique to a
    Windows portable executable (PE) file.
    """

    optionalHeader: Optional[WindowsPEOptionalHeader] = None
    sections: Optional[WindowsPESection] = None
    fileHeaderHashes: Optional[types.Hash] = None
    timeDateStamp: Optional[str] = None
    pointerToSymbolTable: Optional[str] = None
    numberOfSections: Optional[int] = None
    numberOfSymbols: Optional[int] = None
    sizeOfOptionalHeader: Optional[int] = None
    impHash: Optional[str] = None
    peType: Optional[str] = None
    machine: Optional[str] = None
    characteristics: Optional[str] = None

class GenericObservableObject(ObservableObject):
    """
    A generic observable object is an article or unit within the digital domain.
    """

    pass

class Note(ObservableObject):
    """
    A note is a brief textual record.
    """

    pass

class ApplicationFacet(core.Facet):
    """
    An application facet is a grouping of characteristics unique to a particular
    software program designed for end users.
    """

    installedVersionHistory: Optional[ApplicationVersion] = None
    operatingSystem: Optional[ObservableObject] = None
    numberOfLaunches: Optional[int] = None
    applicationIdentifier: Optional[str] = None
    version: Optional[str] = None

class SymbolicLinkFacet(core.Facet):
    """
    A symbolic link facet is a grouping of characteristics unique to a file that
    contains a reference to another file or directory in the form of an absolute
    or relative path and that affects pathname resolution. [based on
    https://en.wikipedia.org/wiki/Symbolic_link]
    """

    targetFile: Optional[ObservableObject] = None

class BrowserBookmark(ObservableObject):
    """
    A browser bookmark is a saved shortcut that directs a WWW (World Wide Web)
    browser software program to a particular WWW accessible resource. [based on
    https://techterms.com/definition/bookmark]
    """

    pass

class WindowsService(ObservableObject):
    """
    A Windows service is a specific Windows service (a computer program that
    operates in the background of a Windows operating system, similar to the way
    a UNIX daemon runs on UNIX). [based on
    https://en.wikipedia.org/wiki/Windows_service]
    """

    pass

class URL(ObservableObject):
    """
    A URL is a uniform resource locator (URL) acting as a resolvable address to
    a particular WWW (World Wide Web) accessible resource.
    """

    pass

class NetworkFlow(ObservableObject):
    """
    A network flow is a sequence of data transiting one or more digital network
    (a group or two or more computer systems linked together) connections.
    [based on https://www.webopedia.com/TERM/N/network.html]
    """

    pass

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

    pass

class ContactSIP(core.UcoInherentCharacterizationThing):
    """
    A contact SIP is a grouping of characteristics unique to details for
    contacting a contact entity by Session Initiation Protocol (SIP).
    """

    sipAddress: Optional[ObservableObject] = None
    contactSIPScope: Optional[str] = None
    contactSIPScope: Optional[Any] = None
    contactSIPScope: Optional[Any] = None

class TaskActionType(core.UcoInherentCharacterizationThing):
    """
    A task action type is a grouping of characteristics for a scheduled action
    to be completed.
    """

    iComHandlerAction: Optional[IComHandlerActionType] = None
    iExecAction: Optional[IExecActionType] = None
    iShowMessageAction: Optional[IShowMessageActionType] = None
    iEmailAction: Optional[ObservableObject] = None
    actionID: Optional[str] = None
    actionType: Optional[str] = None
    actionType: Optional[Any] = None
    actionType: Optional[Any] = None

class TableField(ObservableObject):
    """
    A database table field and its associated value contained within a
    relational database.
    """

    pass

class BrowserCookieFacet(core.Facet):
    """
    A browser cookie facet is a grouping of characteristics unique to a piece of
    data sent from a website and stored on the user's computer by the user's web
    browser while the user is browsing. [based on
    https://en.wikipedia.org/wiki/HTTP_cookie]
    """

    application: Optional[ObservableObject] = None
    cookieDomain: Optional[ObservableObject] = None
    isSecure: Optional[bool] = None
    accessedTime: Optional[str] = None
    expirationTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    cookieName: Optional[str] = None
    cookiePath: Optional[str] = None

class WindowsRegistryHive(ObservableObject):
    """
    The Windows registry hive is a particular logical group of keys, subkeys,
    and values in a Windows registry (a hierarchical database that stores
    low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry). [based on
    https://en.wikipedia.org/wiki/Windows_Registry]
    """

    pass

class ContactList(ObservableObject):
    """
    A contact list is a set of multiple individual contacts such as that found
    in a digital address book.
    """

    pass

class URLVisit(ObservableObject):
    """
    A URL visit characterizes the properties of a visit of a URL within a
    particular browser.
    """

    pass

class Image(ObservableObject):
    """
    An image is a complete copy of a hard disk, memory, or other digital media.
    """

    pass

class BrowserBookmarkFacet(core.Facet):
    """
    A browser bookmark facet is a grouping of characteristics unique to a saved
    shortcut that directs a WWW (World Wide Web) browser software program to a
    particular WWW accessible resource. [based on
    https://techterms.com/definition/bookmark]
    """

    application: Optional[ObservableObject] = None
    urlTargeted: Optional[str] = None
    accessedTime: Optional[str] = None
    modifiedTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    visitCount: Optional[int] = None
    bookmarkPath: Optional[str] = None

class IPNetmask(ObservableObject):
    """
    An IP netmask is a 32-bit 'mask' used to divide an IP address into subnets
    and specify the network's available hosts.
    """

    pass

class ContentDataFacet(core.Facet):
    """
    A content data facet is a grouping of characteristics unique to a block of
    digital data.
    """

    dataPayloadReferenceURL: Optional[ObservableObject] = None
    hash: Optional[types.Hash] = None
    isEncrypted: Optional[bool] = None
    entropy: Optional[float] = None
    sizeInBytes: Optional[int] = None
    dataPayload: Optional[str] = None
    magicNumber: Optional[str] = None
    mimeClass: Optional[str] = None
    mimeType: Optional[str] = None
    byteOrder: Optional[str] = None
    byteOrder: Optional[Any] = None
    byteOrder: Optional[Any] = None

class CookieHistory(ObservableObject):
    """
    A cookie history is the stored web cookie history for a particular web
    browser.
    """

    pass

class NoteFacet(core.Facet):
    """
    A note facet is a grouping of characteristics unique to a brief textual
    record.
    """

    application: Optional[ObservableObject] = None
    modifiedTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    text: Optional[str] = None

class WindowsWaitableTime(ObservableObject):
    """
    A Windows waitable timer is a synchronization object within the Windows
    operating system whose state is set to signaled when a specified due time
    arrives. There are two types of waitable timers that can be created:
    manual-reset and synchronization. A timer of either type can also be a
    periodic timer. [based on
    https://docs.microsoft.com/en-us/windows/win32/sync/waitable-timer-objects]
    """

    pass

class WikiArticle(ObservableObject):
    """
    A wiki article is one or more pages in a wiki focused on characterizing a
    particular topic.
    """

    pass

class Mutex(ObservableObject):
    """
    A mutex is a mechanism that enforces limits on access to a resource when
    there are many threads of execution. A mutex is designed to enforce a mutual
    exclusion concurrency control policy, and with a variety of possible methods
    there exists multiple unique implementations for different applications.
    [based on https://en.wikipedia.org/wiki/Lock_(computer_science)]
    """

    pass

class Software(ObservableObject):
    """
    Software is a definitely scoped instance of a collection of data or computer
    instructions that tell the computer how to work. [based on
    https://en.wikipedia.org/wiki/Software]
    """

    pass

class ShopListing(ObservableObject):
    """
    A shop listing is a listing of offered products on an online
    marketplace/shop.
    """

    pass

class WindowsComputerSpecificationFacet(core.Facet):
    """
    A Windows computer specification facet is a grouping of characteristics
    unique to the hardware and software of a programmable electronic device that
    can store, retrieve, and process data running a Microsoft Windows operating
    system. [based on merriam-webster.com/dictionary/computer]
    """

    registeredOrganization: Optional[identity.Identity] = None
    registeredOwner: Optional[identity.Identity] = None
    globalFlagList: Optional[GlobalFlagType] = None
    windowsDirectory: Optional[ObservableObject] = None
    windowsSystemDirectory: Optional[ObservableObject] = None
    windowsTempDirectory: Optional[ObservableObject] = None
    lastShutdownDate: Optional[str] = None
    osInstallDate: Optional[str] = None
    osLastUpgradeDate: Optional[str] = None
    msProductID: Optional[str] = None
    msProductName: Optional[str] = None
    netBIOSName: Optional[str] = None
    domain: Optional[str] = None

class API(ObservableObject):
    """
    An API (application programming interface) is a computing interface that
    defines interactions between multiple software or mixed hardware-software
    intermediaries. It defines the kinds of calls or requests that can be made,
    how to make them, the data formats that should be used, the conventions to
    follow, etc. [based on https://en.wikipedia.org/wiki/API]
    """

    pass

class WindowsRegistryKeyFacet(core.Facet):
    """
    A Windows registry key facet is a grouping of characteristics unique to a
    particular key within a Windows registry (A hierarchical database that
    stores low-level settings for the Microsoft Windows operating system and for
    applications that opt to use the registry). [based on
    https://en.wikipedia.org/wiki/Windows_Registry]
    """

    creator: Optional[ObservableObject] = None
    registryValues: Optional[WindowsRegistryValue] = None
    modifiedTime: Optional[str] = None
    numberOfSubkeys: Optional[int] = None
    key: Optional[str] = None

class EmailAccountFacet(core.Facet):
    """
    An email account facet is a grouping of characteristics unique to an
    arrangement with an entity to enable and control the provision of electronic
    mail (email) capabilities or services.
    """

    emailAddress: Optional[ObservableObject] = None

class NetworkProtocol(ObservableObject):
    """
    A network protocol is an established set of structured rules that determine
    how data is transmitted between different devices in the same network.
    Essentially, it allows connected devices to communicate with each other,
    regardless of any differences in their internal processes, structure or
    design. [based on
    https://www.comptia.org/content/guides/what-is-a-network-protocol]
    """

    pass

class Message(ObservableObject):
    """
    A message is a discrete unit of electronic communication intended by the
    source for consumption by some recipient or group of recipients. [based on
    https://en.wikipedia.org/wiki/Message]
    """

    pass

class ARPCache(ObservableObject):
    """
    An ARP cache is a collection of Address Resolution Protocol (ARP) entries
    (mostly dynamic) that are created when an IP address is resolved to a MAC
    address (so the computer can effectively communicate with the IP address).
    [based on https://en.wikipedia.org/wiki/ARP_cache]
    """

    pass

class Wiki(ObservableObject):
    """
    A wiki is an online hypertext publication collaboratively edited and managed
    by its own audience directly using a web browser. A typical wiki contains
    multiple pages/articles for the subjects or scope of the project and could
    be either open to the public or limited to use within an organization for
    maintaining its internal knowledge base. [based on
    https://en.wikipedia.org/wiki/Wiki]
    """

    pass

class WindowsPrefetch(ObservableObject):
    """
    The Windows prefetch contains entries in a Windows prefetch file (used to
    speed up application startup starting with Windows XP).
    """

    pass

class StateChangeEffectFacet(DefinedEffectFacet):
    """
    A state change effect facet is a grouping of characteristics unique to the
    effects of actions upon observable objects where a state of the observable
    object is changed.
    """

    newObject: Optional[ObservableObject] = None
    oldObject: Optional[ObservableObject] = None

class TwitterProfileFacet(core.Facet):
    """
    A twitter profile facet is a grouping of characteristics unique to an
    explicit digital representation of identity and characteristics of the owner
    of a single Twitter user account. [based on
    https://en.wikipedia.org/wiki/User_profile]
    """

    profileBackgroundLocation: Optional[ObservableObject] = None
    profileBannerLocation: Optional[ObservableObject] = None
    profileImageLocation: Optional[ObservableObject] = None
    profileBackgroundHash: Optional[types.Hash] = None
    profileBannerHash: Optional[types.Hash] = None
    profileImageHash: Optional[types.Hash] = None
    profileIsProtected: Optional[bool] = None
    profileIsVerified: Optional[bool] = None
    listedCount: Optional[int] = None
    favoritesCount: Optional[int] = None
    followersCount: Optional[int] = None
    friendsCount: Optional[int] = None
    statusesCount: Optional[int] = None
    twitterHandle: Optional[str] = None
    twitterId: Optional[str] = None
    userLocationString: Optional[str] = None

class WindowsHandle(ObservableObject):
    """
    A Windows handle is an abstract reference to a resource within the Windows
    operating system, such as a window, memory, an open file or a pipe. It is
    the mechanism by which applications interact with such resources in the
    Windows operating system.
    """

    pass

class ARPCacheEntry(ObservableObject):
    """
    An ARP cache entry is a single Address Resolution Protocol (ARP) response
    record that is created when an IP address is resolved to a MAC address (so
    the computer can effectively communicate with the IP address). [based on
    https://en.wikipedia.org/wiki/ARP_cache]
    """

    pass

class ComputerSpecificationFacet(core.Facet):
    """
    A computer specificaiton facet is a grouping of characteristics unique to
    the hardware and software of a programmable electronic device that can
    store, retrieve, and process data. [based on
    merriam-webster.com/dictionary/computer]
    """

    networkInterface: Optional[ObservableObject] = None
    biosDate: Optional[str] = None
    biosReleaseDate: Optional[str] = None
    currentSystemDate: Optional[str] = None
    localTime: Optional[str] = None
    systemTime: Optional[str] = None
    availableRam: Optional[int] = None
    totalRam: Optional[int] = None
    biosManufacturer: Optional[str] = None
    biosSerialNumber: Optional[str] = None
    biosVersion: Optional[str] = None
    cpu: Optional[str] = None
    cpuFamily: Optional[str] = None
    gpu: Optional[str] = None
    gpuFamily: Optional[str] = None
    hostname: Optional[str] = None
    processorArchitecture: Optional[str] = None
    timezoneDST: Optional[str] = None
    timezoneStandard: Optional[str] = None
    uptime: Optional[str] = None

class CapturedTelecommunicationsInformation(ObservableObject):

    pass

class Semaphore(ObservableObject):
    """
    A semaphore is a variable or abstract data type used to control access to a
    common resource by multiple processes and avoid critical section problems in
    a concurrent system such as a multitasking operating system. [based on
    https://en.wikipedia.org/wiki/Semaphore_(programming)]
    """

    pass

class Process(ObservableObject):
    """
    A process is an instance of a computer program executed on an operating
    system.
    """

    pass

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

    pass

class NetworkInterfaceFacet(core.Facet):
    """
    A network interface facet is a grouping of characteristics unique to a
    software or hardware interface between two pieces of equipment or protocol
    layers in a computer network.
    """

    macAddress: Optional[ObservableObject] = None
    dhcpServer: Optional[ObservableObject] = None
    ip: Optional[ObservableObject] = None
    ipGateway: Optional[ObservableObject] = None
    dhcpLeaseExpires: Optional[str] = None
    dhcpLeaseObtained: Optional[str] = None
    adapterName: Optional[str] = None

class Code(ObservableObject):
    """
    Code is a direct representation (source, byte or binary) of a collection of
    computer instructions that form software which tell a computer how to work.
    [based on https://en.wikipedia.org/wiki/Software]
    """

    pass

class NetworkFlowFacet(core.Facet):
    """
    A network flow facet is a grouping of characteristics unique to a sequence
    of data transiting one or more digital network (a group of two or more
    computer systems linked together) connections. [based on
    https://www.webopedia.com/TERM/N/network.html]
    """

    dstPayload: Optional[ObservableObject] = None
    srcPayload: Optional[ObservableObject] = None
    ipfix: Optional[types.Dictionary] = None
    dstBytes: Optional[int] = None
    dstPackets: Optional[int] = None
    srcBytes: Optional[int] = None
    srcPackets: Optional[int] = None

class HTTPConnectionFacet(core.Facet):
    """
    An HTTP connection facet is a grouping of characteristics unique to portions
    of a network connection that are conformant to the Hypertext Transfer
    Protocol (HTTP) standard.
    """

    httpMessageBodyData: Optional[ObservableObject] = None
    httpRequestHeader: Optional[types.Dictionary] = None
    httpMesageBodyLength: Optional[int] = None
    requestMethod: Optional[str] = None
    requestValue: Optional[str] = None
    requestVersion: Optional[str] = None

class Device(ObservableObject):
    """
    A device is a piece of equipment or a mechanism designed to serve a special
    purpose or perform a special function. [based on
    https://www.merriam-webster.com/dictionary/device]
    """

    pass

class ContactURL(core.UcoInherentCharacterizationThing):
    """
    A contact URL is a grouping of characteristics unique to details for
    contacting a contact entity by Uniform Resource Locator (URL).
    """

    url: Optional[ObservableObject] = None
    contactURLScope: Optional[str] = None
    contactURLScope: Optional[Any] = None
    contactURLScope: Optional[Any] = None

class WindowsEvent(ObservableObject):
    """
    A Windows event is a notification record of an occurance of interest
    (system, security, application, etc.) on a Windows operating system.
    """

    pass

class CredentialDump(ObservableObject):
    """
    A credential dump is a collection (typically forcibly extracted from a
    system) of specific login and password combinations for authorization of
    access to a digital account or system.
    """

    pass

class EventLog(ObservableObject):
    """
    An event log is a collection of event records.
    """

    pass

class Audio(ObservableObject):
    """
    Audio is a digital representation of sound.
    """

    pass

class ContactEmail(core.UcoInherentCharacterizationThing):
    """
    A contact email is a grouping of characteristics unique to details for
    contacting a contact entity by email.
    """

    emailAddress: Optional[ObservableObject] = None
    contactEmailScope: Optional[str] = None
    contactEmailScope: Optional[Any] = None
    contactEmailScope: Optional[Any] = None

class WindowsTask(ObservableObject):
    """
    A Windows task is a process that is scheduled to execute on a Windows
    operating system by the Windows Task Scheduler. [based on
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]
    """

    pass

class EventRecord(ObservableObject):
    """
    An event record is something that happens in a digital context (e.g.,
    operating system events).
    """

    pass

class DiskFacet(core.Facet):
    """
    A disk facet is a grouping of characteristics unique to a storage mechanism
    where data is recorded by various electronic, magnetic, optical, or
    mechanical changes to a surface layer of one or more rotating disks.
    """

    partition: Optional[ObservableObject] = None
    diskSize: Optional[int] = None
    freeSpace: Optional[int] = None
    diskType: Optional[str] = None

class CalendarFacet(core.Facet):
    """
    A calendar facet is a grouping of characteristics unique to a collection of
    appointments, meetings, and events.
    """

    owner: Optional[core.UcoObject] = None
    application: Optional[ObservableObject] = None

class RecoveredObject(ObservableObject):
    """
    An observable object that was the result of a recovery operation.
    """

    pass

class GUI(ObservableObject):
    """
    A GUI is a graphical user interface that allows users to interact with
    electronic devices through graphical icons and audio indicators such as
    primary notation, instead of text-based user interfaces, typed command
    labels or text navigation. [based on
    https://en.wikipedia.org/wiki/Graphical_user_interface]
    """

    pass

class UserSession(ObservableObject):
    """
    A user session is a temporary and interactive information interchange
    between two or more communicating devices within the managed scope of a
    single user. [based on
    https://en.wikipedia.org/wiki/Session_(computer_science)]
    """

    pass

class GeoLocationTrackFacet(core.Facet):
    """
    A geolocation track facet is a grouping of characteristics unique to a set
    of contiguous geolocation entries representing a path/track taken.
    """

    application: Optional[ObservableObject] = None
    geoLocationEntry: Optional[ObservableObject] = None
    endTime: Optional[str] = None
    startTime: Optional[str] = None

class Volume(ObservableObject):
    """
    A volume is a single accessible storage area (volume) with a single file
    system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]
    """

    pass

class WindowsNetworkShare(ObservableObject):
    """
    A Windows network share is a Windows computer resource made available from
    one host to other hosts on a computer network. It is a device or piece of
    information on a computer that can be remotely accessed from another
    computer transparently as if it were a resource in the local machine.
    Network sharing is made possible by inter-process communication over the
    network. [based on https://en.wikipedia.org/wiki/Shared_resource]
    """

    pass

class WindowsComputerSpecification(ObservableObject):
    """
    A Windows computer specification is the hardware ans software of a
    programmable electronic device that can store, retrieve, and process data
    running a Microsoft Windows operating system. [based on
    merriam-webster.com/dictionary/computer]
    """

    pass

class CalendarEntryFacet(core.Facet):
    """
    A calendar entry facet is a grouping of characteristics unique to an
    appointment, meeting, or event within a collection of appointments,
    meetings, and events.
    """

    owner: Optional[core.UcoObject] = None
    attendant: Optional[identity.Identity] = None
    location_: Optional[location.Location] = None
    application: Optional[ObservableObject] = None
    isPrivate: Optional[bool] = None
    endTime: Optional[str] = None
    modifiedTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    remindTime: Optional[str] = None
    startTime: Optional[str] = None
    duration: Optional[int] = None
    eventStatus: Optional[str] = None
    eventType: Optional[str] = None
    recurrence: Optional[str] = None
    subject: Optional[str] = None

class URLHistoryEntry(core.UcoInherentCharacterizationThing):
    """
    A URL history entry is a grouping of characteristics unique to the
    properties of a single URL history entry for a particular browser.
    """

    url: Optional[ObservableObject] = None
    referrerUrl: Optional[ObservableObject] = None
    expirationTime: Optional[str] = None
    firstVisit: Optional[str] = None
    lastVisit: Optional[str] = None
    visitCount: Optional[int] = None
    manuallyEnteredCount: Optional[int] = None
    browserUserProfile: Optional[str] = None
    hostname: Optional[str] = None
    pageTitle: Optional[str] = None
    keywordSearchTerm: Optional[str] = None

class GeoLocationEntry(ObservableObject):
    """
    A geolocation entry is a single application-specific geolocation entry.
    """

    pass

class Application(ObservableObject):
    """
    An application is a particular software program designed for end users.
    """

    pass

class URLHistory(ObservableObject):
    """
    A URL history characterizes the stored URL history for a particular web
    browser
    """

    pass

class CellSite(ObservableObject):

    pass

class DNSRecord(ObservableObject):
    """
    A DNS record is a single Domain Name System (DNS) artifact specifying
    information of a particular type (routing, authority, responsibility,
    security, etc.) for a specific Internet domain name.
    """

    pass

class FileSystem(ObservableObject):
    """
    A file system is the process that manages how and where data on a storage
    medium is stored, accessed and managed. [based on
    https://www.techopedia.com/definition/5510/file-system]
    """

    pass

class NetworkInterface(ObservableObject):
    """
    A network interface is a software or hardware interface between two pieces
    of equipment or protocol layers in a computer network.
    """

    pass

class ContactProfile(core.UcoInherentCharacterizationThing):
    """
    A contact profile is a grouping of characteristics unique to details for
    contacting a contact entity by online service.
    """

    contactProfilePlatform: Optional[ObservableObject] = None
    profile: Optional[ObservableObject] = None

class Calendar(ObservableObject):
    """
    A calendar is a collection of appointments, meetings, and events.
    """

    pass

class NetworkConnectionFacet(core.Facet):
    """
    A network connection facet is a grouping of characteristics unique to a
    connection (complete or attempted) accross a digital network (a group of two
    or more computer systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]
    """

    src: Optional[core.UcoObject] = None
    dst: Optional[ObservableObject] = None
    protocols: Optional[types.ControlledDictionary] = None
    isActive: Optional[bool] = None
    endTime: Optional[str] = None
    startTime: Optional[str] = None
    destinationPort: Optional[int] = None
    sourcePort: Optional[int] = None

class CalendarEntry(ObservableObject):
    """
    A calendar entry is an appointment, meeting or event within a collection of
    appointments, meetings and events.
    """

    pass

class Library(ObservableObject):
    """
    A library is a suite of data and programming code that is used to develop
    software programs and applications. [based on
    https://www.techopedia.com/definition/3828/software-library]
    """

    pass

class GeoLocationTrack(ObservableObject):
    """
    A geolocation track is a set of contiguous geolocation entries representing
    a path/track taken.
    """

    pass

class Memory(ObservableObject):
    """
    Memory is a particular region of temporary information storage (e.g., RAM
    (random access memory), ROM (read only memory)) on a digital device.
    """

    pass

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

    pass

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

    pass

class RasterPictureFacet(core.Facet):
    """
    A raster picture facet is a grouping of characteristics unique to a raster
    (or bitmap) image.
    """

    camera: Optional[ObservableObject] = None
    bitsPerPixel: Optional[int] = None
    pictureHeight: Optional[int] = None
    pictureWidth: Optional[int] = None
    imageCompressionMethod: Optional[str] = None
    pictureType: Optional[str] = None

class WindowsPrefetchFacet(core.Facet):
    """
    A Windows prefetch facet is a grouping of characteristics unique to entries
    in the Windows prefetch file (used to speed up application startup starting
    with Windows XP).
    """

    volume: Optional[ObservableObject] = None
    accessedDirectory: Optional[ObservableObject] = None
    accessedFile: Optional[ObservableObject] = None
    firstRun: Optional[str] = None
    lastRun: Optional[str] = None
    timesExecuted: Optional[int] = None
    applicationFileName: Optional[str] = None
    prefetchHash: Optional[str] = None

class ContactListFacet(core.Facet):
    """
    A contact list facet is a grouping of characteristics unique to a set of
    multiple individual contacts such as that found in a digital address book.
    """

    sourceApplication: Optional[ObservableObject] = None
    contact: Optional[ObservableObject] = None

class ComputerSpecification(ObservableObject):
    """
    A computer specification is the hardware and software of a programmable
    electronic device that can store, retrieve, and process data. {based on
    merriam-webster.com/dictionary/computer]
    """

    pass

class BrowserCookie(ObservableObject):
    """
    A browser cookie is a piece of of data sent from a website and stored on the
    user's computer by the user's web browser while the user is browsing. [based
    on https://en.wikipedia.org/wiki/HTTP_cookie]
    """

    pass

class Pipe(ObservableObject):
    """
    A pipe is a mechanism for one-way inter-process communication using message
    passing where data written by one process is buffered by the operating
    system until it is read by the next process, and this uni-directional
    channel disappears when the processes are completed. [based on
    https://en.wikipedia.org/wiki/Pipeline_(Unix) ;
    https://en.wikipedia.org/wiki/Anonymous_pipe]
    """

    pass

class AutonomousSystem(ObservableObject):
    """
    An autonomous system is a collection of connected Internet Protocol (IP)
    routing prefixes under the control of one or more network operators on
    behalf of a single administrative entity or domain that presents a common,
    clearly defined routing policy to the Internet. [based on
    https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]
    """

    pass

class ContactPhone(core.UcoInherentCharacterizationThing):
    """
    A contact phone is a grouping of characteristics unique to details for
    contacting a contact entity by telephone.
    """

    contactPhoneNumber: Optional[ObservableObject] = None
    contactPhoneScope: Optional[str] = None
    contactPhoneScope: Optional[Any] = None
    contactPhoneScope: Optional[Any] = None

class UserSessionFacet(core.Facet):
    """
    A user session facet is a grouping of characteristics unique to a temporary
    and interactive information interchange between two or more communicating
    devices within the managed scope of a single user. [based on
    https://en.wikipedia.org/wiki/Session_(computer_science)]
    """

    effectiveUser: Optional[ObservableObject] = None
    loginTime: Optional[str] = None
    logoutTime: Optional[str] = None
    effectiveGroup: Optional[str] = None
    effectiveGroupID: Optional[str] = None

class WindowsRegistryKey(ObservableObject):
    """
    A Windows registry key is a particular key within a Windows registry (a
    hierarchical database that stores low-level settings for the Microsoft
    Windows operating system and for applications that opt to use the registry).
    [based on https://en.wikipedia.org/wiki/Windows_Registry]
    """

    pass

class NetworkSubnet(ObservableObject):
    """
    A network subnet is a logical subdivision of an IP network. [based on
    https://en.wikipedia.org/wiki/Subnetwork]
    """

    pass

class WhoIs(ObservableObject):
    """
    WhoIs is a response record conformant to the WHOIS protocol standard (RFC
    3912). [based on https://en.wikipedia.org/wiki/WHOIS]
    """

    pass

class WhoisRegistrarInfoType(core.UcoInherentCharacterizationThing):
    """
    A Whois registrar info type is a grouping of characteristics unique to
    registrar-related information present in a response record conformant to the
    WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]
    """

    geolocationAddress: Optional[location.Location] = None
    contactPhoneNumber: Optional[ObservableObject] = None
    emailAddress: Optional[ObservableObject] = None
    referralURL: Optional[ObservableObject] = None
    whoisServer: Optional[ObservableObject] = None
    registrarGUID: Optional[str] = None
    registrarID: Optional[str] = None
    registrarName: Optional[str] = None

class Call(ObservableObject):
    """
    A call is a connection as part of a realtime cyber communication between one
    or more parties.
    """

    pass

class BotConfiguration(ObservableObject):
    """
    A bot configuration is a set of contextual settings for a software
    application that runs automated tasks (scripts) over the Internet at a much
    higher rate than would be possible for a human alone.
    """

    pass

class Credential(ObservableObject):
    """
    A credential is a single specific login and password combination for
    authorization of access to a digital account or system.
    """

    pass

class ContactMessaging(core.UcoInherentCharacterizationThing):
    """
    A contact messaging is a grouping of characteristics unique to details for
    contacting a contact entity by digital messaging.
    """

    contactMessagingPlatform: Optional[ObservableObject] = None
    messagingAddress: Optional[ObservableObject] = None

class FileSystemObject(ObservableObject):
    """
    A file system object is an informational object represented and managed
    within a file system.
    """

    pass

class SQLiteBlob(ObservableObject):
    """
    An SQLite blob is a blob (binary large object) of data within an SQLite
    database. [based on https://en.wikipedia.org/wiki/SQLite]
    """

    pass

class Profile(ObservableObject):
    """
    A profile is an explicit digital representation of identity and
    characteristics of the owner of a single user account associated with an
    online service or application. [based on
    https://en.wikipedia.org/wiki/User_profile]
    """

    pass

class MessageThread(ObservableObject):
    """
    A message thread is a running commentary of electronic messages pertaining
    to one topic or question.
    """

    pass

class ContentData(ObservableObject):
    """
    Content data is a block of digital data.
    """

    pass

class DigitalSignatureInfo(ObservableObject):
    """
    A digital signature info is a value calculated via a mathematical scheme for
    demonstrating the authenticity of an electronic message or document.
    """

    pass

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

    pass

class URLVisitFacet(core.Facet):
    """
    A URL visit facet is a grouping of characteristics unique to the properties
    of a visit of a URL within a particular browser.
    """

    browserInformation: Optional[ObservableObject] = None
    fromURLVisit: Optional[ObservableObject] = None
    url: Optional[ObservableObject] = None
    visitTime: Optional[str] = None
    visitDuration: Optional[str] = None
    urlTransitionType: Optional[str] = None
    urlTransitionType: Optional[Any] = None
    urlTransitionType: Optional[Any] = None

class DNSCache(ObservableObject):
    """
    An DNS cache is a temporary locally stored collection of previous Domain
    Name System (DNS) query results (created when an domain name is resolved to
    a IP address) for a particular computer.
    """

    pass

class X509Certificate(ObservableObject):
    """
    A X.509 certificate is a public key digital identity certificate conformant
    to the X.509 PKI (Public Key Infrastructure) standard.
    """

    pass

class Contact(ObservableObject):
    """
    A contact is a set of identification and communication related details for a
    single entity.
    """

    pass

class DiskPartition(ObservableObject):
    """
    A disk partition is a particular managed region on a storage mechanism where
    data is recorded by various electronic, magnetic, optical, or mechanical
    changes to a surface layer of one or more rotating disks. [based on
    https://en.wikipedia.org/wiki/Disk_storage]
    """

    pass

class WindowsSystemRestore(ObservableObject):
    """
    A Windows system restore is a capture of a Windows computer's state
    (including system files, installed applications, Windows Registry, and
    system settings) at a particular point in time such that the computer can be
    reverted to that state in the event of system malfunctions or other
    problems. [based on https://en.wikipedia.org/wiki/System_Restore]
    """

    pass

class WindowsHook(ObservableObject):
    """
    A Windows hook is a mechanism by which an application can intercept events,
    such as messages, mouse actions, and keystrokes within the Windows operating
    system. A function that intercepts a particular type of event is known as a
    hook procedure. A hook procedure can act on each event it receives, and then
    modify or discard the event. [based on
    https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks]
    """

    pass

class ProcessFacet(core.Facet):
    """
    A process facet is a grouping of characteristics unique to an instance of a
    computer program executed on an operating system.
    """

    binary: Optional[ObservableObject] = None
    creatorUser: Optional[ObservableObject] = None
    parent: Optional[ObservableObject] = None
    environmentVariables: Optional[types.Dictionary] = None
    isHidden: Optional[bool] = None
    exitTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    exitStatus: Optional[int] = None
    pid: Optional[int] = None
    currentWorkingDirectory: Optional[str] = None
    status: Optional[str] = None
    arguments: Optional[str] = None

class WebPage(ObservableObject):
    """
    A web page is a specific collection of information provided by a website and
    displayed to a user in a web browser. A website typically consists of many
    web pages linked together in a coherent fashion. [based on
    https://en.wikipedia.org/wiki/Web_page]
    """

    pass

class CallFacet(core.Facet):
    """
    A call facet is a grouping of characteristics unique to a connection as part
    of a realtime cyber communication between one or more parties.
    """

    application: Optional[ObservableObject] = None
    from_: Optional[ObservableObject] = None
    participant: Optional[ObservableObject] = None
    to: Optional[ObservableObject] = None
    endTime: Optional[str] = None
    startTime: Optional[str] = None
    duration: Optional[int] = None
    callType: Optional[str] = None

class ApplicationAccountFacet(core.Facet):
    """
    An application account facet is a grouping of characteristics unique to an
    account within a particular software program designed for end users.
    """

    application: Optional[ObservableObject] = None

class MimePartType(core.UcoInherentCharacterizationThing):
    """
    A mime part type is a grouping of characteristics unique to a component of a
    multi-part email body.
    """

    bodyRaw: Optional[ObservableObject] = None
    body: Optional[str] = None
    contentDisposition: Optional[str] = None
    contentType: Optional[str] = None

class GeoLocationLogFacet(core.Facet):
    """
    A geolocation log facet is a grouping of characteristics unique to a record
    containing geolocation tracks and/or geolocation entries.
    """

    application: Optional[ObservableObject] = None
    observableCreatedTime: Optional[str] = None

class X509V3Certificate(ObservableObject):
    """
    An X.509 v3 certificate is a public key digital identity certificate
    conformant to the X.509 v3 PKI (Public Key Infrastructure) standard.
    """

    pass

class OnlineServiceFacet(core.Facet):
    """
    An online service facet is a grouping of characteristics unique to a
    particular provision mechanism of information access, distribution or
    manipulation over the Internet.
    """

    location_: Optional[location.Location] = None
    inetLocation: Optional[ObservableObject] = None
    name: Optional[str] = None

class NetworkConnection(ObservableObject):
    """
    A network connection is a connection (completed or attempted) across a
    digital network (a group of two or more computer systems linked together).
    [based on https://www.webopedia.com/TERM/N/network.html]
    """

    pass

class URLFacet(core.Facet):
    """
    A URL facet is a grouping of characteristics unique to a uniform resource
    locator (URL) acting as a resolvable address to a particular WWW (World Wide
    Web) accessible resource.
    """

    host: Optional[ObservableObject] = None
    port: Optional[int] = None
    fragment: Optional[str] = None
    fullValue: Optional[str] = None
    password: Optional[str] = None
    path: Optional[str] = None
    query: Optional[str] = None
    scheme: Optional[str] = None
    userName: Optional[str] = None

class GeoLocationLog(ObservableObject):
    """
    A geolocation log is a record containing geolocation tracks and/or
    geolocation entries.
    """

    pass

class Address(ObservableObject):
    """
    An address is an identifier assigned to enable routing and management of
    information.
    """

    pass

class PaymentCard(ObservableObject):
    """
    A payment card is a physical token that is part of a payment system issued
    by financial institutions, such as a bank, to a customer that enables its
    owner (the cardholder) to access the funds in the customer's designated bank
    accounts, or through a credit account and make payments by electronic funds
    transfer and access automated teller machines (ATMs). [based on
    https://en.wikipedia.org/wiki/Payment_card]
    """

    pass

class Account(ObservableObject):
    """
    An account is an arrangement with an entity to enable and control the
    provision of some capability or service.
    """

    pass

class GeoLocationEntryFacet(core.Facet):
    """
    A geolocation entry facet is a grouping of characteristics unique to a
    single application-specific geolocation entry.
    """

    location_: Optional[location.Location] = None
    application: Optional[ObservableObject] = None
    observableCreatedTime: Optional[str] = None

class OnlineService(ObservableObject):
    """
    An online service is a particular provision mechanism of information access,
    distribution or manipulation over the Internet.
    """

    pass

class MessageFacet(core.Facet):
    """
    A message facet is a grouping of characteristics unique to a discrete unit
    of electronic communication intended by the source for consumption by some
    recipient or group of recipients. [based on
    https://en.wikipedia.org/wiki/Message]
    """

    application: Optional[ObservableObject] = None
    from_: Optional[ObservableObject] = None
    to: Optional[ObservableObject] = None
    sentTime: Optional[str] = None
    messageID: Optional[str] = None
    messageText: Optional[str] = None
    messageType: Optional[str] = None
    sessionID: Optional[str] = None

class NetworkRoute(ObservableObject):
    """
    A network route is a specific path (of specific network nodes, connections
    and protocols) for traffic in a network or between or across multiple
    networks.
    """

    pass

class DomainName(ObservableObject):
    """
    A domain name is an identification string that defines a realm of
    administrative autonomy, authority or control within the Internet. [based on
    https://en.wikipedia.org/wiki/Domain_name]
    """

    pass

class EventRecordFacet(core.Facet):
    """
    An event record facet is a grouping of characteristics unique to something
    that happens in a digital context (e.g., operating system events).
    """

    cyberAction: Optional[ObservableAction] = None
    account: Optional[ObservableObject] = None
    application: Optional[ObservableObject] = None
    eventRecordDevice: Optional[ObservableObject] = None
    endTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    startTime: Optional[str] = None
    eventID: Optional[str] = None
    eventRecordID: Optional[str] = None
    eventRecordRaw: Optional[str] = None
    eventRecordServiceName: Optional[str] = None
    eventRecordText: Optional[str] = None
    eventType: Optional[str] = None

class IPv6AddressFacet(IPAddressFacet):
    """
    An IPv6 (Internet Protocol version 6) address facet is a grouping of
    characteristics unique to an IPv6 standards conformant identifier assigned
    to a device to enable routing and management of IPv6 standards conformant
    communication to or from that device.
    """

    pass

class IPv4AddressFacet(IPAddressFacet):
    """
    An IPv4 (Internet Protocol version 4) address facet is a grouping of
    characteristics unique to an IPv4 standards conformant identifier assigned
    to a device to enable routing and management of IPv4 standards conformant
    communication to or from that device.
    """

    pass

class BluetoothAddressFacet(MACAddressFacet):
    """
    A Bluetooth address facet is a grouping of characteristics unique to a
    Bluetooth standard conformant identifier assigned to a Bluetooth device to
    enable routing and management of Bluetooth standards conformant
    communication to or from that device.
    """

    pass

class WifiAddressFacet(MACAddressFacet):
    """
    A Wi-Fi address facet is a grouping of characteristics unique to a media
    access control (MAC) standards conformant identifier assigned to a device
    network interface to enable routing and management of IEEE 802.11
    standards-conformant communications to and from that device.
    """

    pass

class WindowsTaskFacet(core.Facet):
    """
    A Windows Task facet is a grouping of characteristics unique to a Windows
    Task (a process that is scheduled to execute on a Windows operating system
    by the Windows Task Scheduler). [based on
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]
    """

    account: Optional[ObservableObject] = None
    application: Optional[ObservableObject] = None
    workItemData: Optional[ObservableObject] = None
    workingDirectory: Optional[ObservableObject] = None
    actionList: Optional[TaskActionType] = None
    triggerList: Optional[TriggerType] = None
    mostRecentRunTime: Optional[str] = None
    nextRunTime: Optional[str] = None
    observableCreatedTime: Optional[str] = None
    exitCode: Optional[int] = None
    maxRunTime: Optional[int] = None
    accountLogonType: Optional[str] = None
    accountRunLevel: Optional[str] = None
    imageName: Optional[str] = None
    parameters: Optional[str] = None
    taskComment: Optional[str] = None
    taskCreator: Optional[str] = None
    flags: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[Any] = None
    status: Optional[Any] = None
    flags: Optional[Any] = None
    priority: Optional[Any] = None
    status: Optional[Any] = None
    flags: Optional[Any] = None

class ConfiguredSoftware(Software):
    """
    A ConfiguredSoftware is a Software that is known to be configured to run in
    a more specified manner than some unconfigured or less-configured Software.
    """

    usesConfiguration: Optional[configuration.Configuration] = None
    isConfigurationOf: Optional[Software] = None

class OperatingSystem(Software):
    """
    An operating system is the software that manages computer hardware, software
    resources, and provides common services for computer programs. [based on
    https://en.wikipedia.org/wiki/Operating_system]
    """

    pass

class ForumPost(Message):
    """
    A forum post is message submitted by a user account to an online forum where
    the message content (and typically metadata including who posted it and
    when) is viewable by any party with viewing permissions on the forum.
    """

    pass

class EmailMessage(Message):
    """
    An email message is a message that is an instance of an electronic mail
    correspondence conformant to the internet message format described in RFC
    5322 and related RFCs.
    """

    pass

class Post(Message):
    """
    A post is message submitted to an online discussion/publishing site (forum,
    blog, etc.).
    """

    pass

class Tweet(Message):
    """
    A tweet is message submitted by a Twitter user account to the Twitter
    microblogging platform.
    """

    pass

class ForumPrivateMessage(Message):
    """
    A forum private message (aka PM or DM (direct message)) is a one-to-one
    message from one specific user account to another specific user account on
    an online form where transmission is managed by the online forum platform
    and the message is only viewable by the parties directly involved.
    """

    pass

class SMSMessage(Message):
    """
    An SMS message is a message conformant to the short message service (SMS)
    communication protocol standards.
    """

    pass

class MessageThreadFacet(core.Facet):
    """
    A message thread facet is a grouping of characteristics unique to a running
    commentary of electronic messages pertaining to one topic or question.
    """

    nb3a51a6df83c458aaba1a1700f93ae93b463: Optional[Message] = None
    nb3a51a6df83c458aaba1a1700f93ae93b467: Optional[Message] = None
    nb3a51a6df83c458aaba1a1700f93ae93b471: Optional[Message] = None
    nb3a51a6df83c458aaba1a1700f93ae93b475: Optional[Message] = None
    participant: Optional[ObservableObject] = None
    messageThread: Optional[types.Thread] = None
    visibility: Optional[bool] = None

class UNIXProcess(Process):
    """
    A UNIX process is an instance of a computer program executed on a UNIX
    operating system.
    """

    pass

class WindowsProcess(Process):
    """
    A Windows process is a program running on a Windows operating system.
    """

    pass

class Adaptor(Device):
    """
    An adaptor is a device that physically converts the pin outputs but does not
    alter the underlying protocol (e.g. uSD to SD, CF to ATA, etc.)
    """

    pass

class DigitalCamera(Device):
    """
    A digital camera is a camera that captures photographs in digital memory as
    opposed to capturing images on photographic film.
    """

    pass

class SIMCard(Device):
    """
    A SIM card is a subscriber identification module card intended to securely
    store the international mobile subscriber identity (IMSI) number and its
    related key, which are used to identify and authenticate subscribers on
    mobile telephony. [based on https://en.wikipedia.org/wiki/SIM_card]
    """

    pass

class MobileDevice(Device):
    """
    A mobile device is a portable computing device. [based on
    https://www.lexico.com.definition/mobile_device]
    """

    pass

class SmartDevice(Device):
    """
    A smart device is a microprocessor IoT device that is expected to be
    connected directly to cloud-based networks or via smartphone
    """

    pass

class ProtocolConverter(Device):
    """
    A protocol converter is a device that converts from one protocol to another
    (e.g. SD to USB, SATA to USB, etc.
    """

    pass

class AndroidDevice(Device):
    """
    An Android device is a device running the Android operating system. [based
    on https://en.wikipedia.org/wiki/Android_(operating_system)]
    """

    pass

class GamingConsole(Device):
    """
    A gaming console (video game console or game console) is an electronic
    system that connects to a display, typically a TV or computer monitor, for
    the primary purpose of playing video games.
    """

    pass

class EmbeddedDevice(Device):
    """
    An embedded device is a highly specialized microprocessor device meant for
    one or very few specific purposes and is usually embedded or included within
    another object or as part of a larger system. Examples include answer
    machine, door access logger, card scanner, etc.
    """

    pass

class AppleDevice(Device):
    """
    An apple device is a smart device that applies either the MacOS or iOS
    operating system.
    """

    pass

class WriteBlocker(Device):
    """
    A write blocker is a device that allows read-only access to storage mediums
    in order to preserve the integrity of the data being analyzed. Examples
    include Tableau, Cellibrite, Talon, etc.
    """

    pass

class Appliance(Device):
    """
    An appliance is a purpose-built computer with software or firmware that is
    designed to provide a specific computing capability or resource. [based on
    https://en.wikipedia.org/wiki/Computer_appliance]
    """

    pass

class Computer(Device):
    """
    A computer is an electronic device for storing and processing data,
    typically in binary, according to instructions given to it in a variable
    program. [based on 'Computer.' Oxford English Dictionary, Oxford University
    Press, 2022.]
    """

    pass

class StorageMedium(Device):
    """
    A storage medium is any digital storage device that applies electromagnetic
    or optical surfaces, or depends solely on electronic circuits as solid state
    storage, for storing digital data. Examples include HDD (PATA), SATA, SSD,
    Optical, Memory_Card, Tape, etc
    """

    pass

class URLHistoryFacet(core.Facet):
    """
    A URL history facet is a grouping of characteristics unique to the stored
    URL history for a particular web browser
    """

    browserInformation: Optional[ObservableObject] = None
    urlHistoryEntry: Optional[URLHistoryEntry] = None

class CapturedTelecommunicationsInformationFacet(core.Facet):
    """
    A captured telecommunications information facet represents certain
    information within captured or intercepted telecommunications data.
    """

    captureCellSite: CellSite
    endTime: Optional[str] = None
    startTime: Optional[str] = None
    interceptedCallState: Optional[str] = None

class WhoIsFacet(core.Facet):
    """
    A whois facet is a grouping of characteristics unique to a response record
    conformant to the WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]
    """

    regionalInternetRegistry: Optional[Any] = None
    regionalInternetRegistry: Optional[str] = None
    domainName: Optional[ObservableObject] = None
    ipAddress: Optional[ObservableObject] = None
    registrantContactInfo: Optional[ObservableObject] = None
    serverName: Optional[ObservableObject] = None
    nameServer: Optional[ObservableObject] = None
    registrarInfo: Optional[WhoisRegistrarInfoType] = None
    creationDate: Optional[str] = None
    expirationDate: Optional[str] = None
    lookupDate: Optional[str] = None
    updatedDate: Optional[str] = None
    domainID: Optional[str] = None
    remarks: Optional[str] = None
    sponsoringRegistrar: Optional[str] = None
    registrantIDs: Optional[str] = None
    dnssec: Optional[str] = None
    status: Optional[str] = None
    regionalInternetRegistry: Optional[Any] = None
    status: Optional[Any] = None
    status: Optional[Any] = None

class ContactAffiliation(core.UcoInherentCharacterizationThing):
    """
    A contact affiliation is a grouping of characteristics unique to details of
    an organizational affiliation for a single contact entity.
    """

    contactOrganization: Optional[identity.Organization] = None
    organizationLocation: Optional[ContactAddress] = None
    contactEmail: Optional[ContactEmail] = None
    contactMessaging: Optional[ContactMessaging] = None
    contactPhone: Optional[ContactPhone] = None
    contactProfile: Optional[ContactProfile] = None
    contactURL: Optional[ContactURL] = None
    organizationDepartment: Optional[str] = None
    organizationPosition: Optional[str] = None

class ProfileFacet(core.Facet):
    """
    A profile facet is a grouping of characteristics unique to an explicit
    digital representation of identity and characteristics of the owner of a
    single user account associated with an online service or application. [based
    on https://en.wikipedia.org/wiki/User_profile]
    """

    profileIdentity: Optional[identity.Identity] = None
    contactAddress: Optional[ContactAddress] = None
    contactEmail: Optional[ContactEmail] = None
    contactMessaging: Optional[ContactMessaging] = None
    contactPhone: Optional[ContactPhone] = None
    contactURL: Optional[ContactURL] = None
    profileAccount: Optional[ObservableObject] = None
    profileService: Optional[ObservableObject] = None
    profileWebsite: Optional[ObservableObject] = None
    profileCreated: Optional[str] = None
    name: Optional[str] = None
    displayName: Optional[str] = None
    profileLanguage: Optional[str] = None

class SymbolicLink(FileSystemObject):
    """
    A symbolic link is a file that contains a reference to another file or
    directory in the form of an absolute or relative path and that affects
    pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]
    """

    pass

class CharacterDeviceNode(FileSystemObject):
    """
    A character device node is a UNIX filesystem special file that serves as a
    conduit to communicate with devices, providing only a serial stream of input
    or accepting a serial stream of output. Character device nodes are used to
    apply access rights to the devices and to direct operations on the files to
    the appropriate device drivers. [based on
    https://en.wikipedia.org/wiki/Unix_file_types]
    """

    pass

class Socket(FileSystemObject):
    """
    A socket is a special file used for inter-process communication, which
    enables communication between two processes. In addition to sending data,
    processes can send file descriptors across a Unix domain socket connection
    using the sendmsg() and recvmsg() system calls. Unlike named pipes which
    allow only unidirectional data flow, sockets are fully duplex-capable.
    [based on https://en.wikipedia.org/wiki/Unix_file_types]
    """

    pass

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

    pass

class Snapshot(FileSystemObject):
    """
    A snapshot is a file system object representing a snapshot of the contents
    of a part of a file system at a point in time.
    """

    pass

class Directory(FileSystemObject):
    """
    A directory is a file system cataloging structure which contains references
    to other computer files, and possibly other directories. On many computers,
    directories are known as folders, or drawers, analogous to a workbench or
    the traditional office filing cabinet. In UNIX a directory is implemented as
    a special file. [based on
    https://en.wikipedia.org/wiki/Directory_(computing)]
    """

    pass

class File(FileSystemObject):
    """
    A file is a computer resource for recording data discretely on a computer
    storage device.
    """

    pass

class AlternateDataStream(FileSystemObject):
    """
    An alternate data stream is data content stored within an NTFS file that is
    independent of the standard content stream of the file and is hidden from
    access by default NTFS file viewing mechanisms.
    """

    pass

class BlockDeviceNode(FileSystemObject):
    """
    A block device node is a UNIX filesystem special file that serves as a
    conduit to communicate with devices, providing buffered randomly accesible
    input and output. Block device nodes are used to apply access rights to the
    devices and to direct operations on the files to the appropriate device
    drivers. [based on https://en.wikipedia.org/wiki/Unix_file_types]
    """

    pass

class NamedPipe(FileSystemObject):
    """
    A named pipe is a mechanism for FIFO (first-in-first-out) inter-process
    communication. It is persisted as a filesystem object (that can be deleted
    like any other file), can be written to or read from by any process and
    exists beyond the lifespan of any process interacting with it (unlike simple
    anonymous pipes). [based on https://en.wikipedia.org/wiki/Named_pipe]
    """

    pass

class Junction(FileSystemObject):
    """
    A junction is a specific NTFS (New Technology File System) reparse point to
    redirect a directory access to another directory which can be on the same
    volume or another volume. A junction is similar to a directory symbolic link
    but may differ on whether they are processed on the local system or on the
    remote file server. [based on
    https://jp-andre.pagesperso-orange.fr/junctions.html]
    """

    pass

class WindowsThread(ProcessThread):
    """
    A Windows thread is a single thread of execution within a Windows process.
    """

    pass

class EmailMessageFacet(core.Facet):
    """
    An email message facet is a grouping of characteristics unique to a message
    that is an instance of an electronic mail correspondence conformant to the
    internet message format described in RFC 5322 and related RFCs.
    """

    bodyMultipart: Optional[MimePartType] = None
    application: Optional[ObservableObject] = None
    bodyRaw: Optional[ObservableObject] = None
    from_: Optional[ObservableObject] = None
    headerRaw: Optional[ObservableObject] = None
    sender: Optional[ObservableObject] = None
    xOriginatingIP: Optional[ObservableObject] = None
    bcc: Optional[ObservableObject] = None
    cc: Optional[ObservableObject] = None
    references: Optional[ObservableObject] = None
    to: Optional[ObservableObject] = None
    otherHeaders: Optional[types.Dictionary] = None
    isMimeEncoded: Optional[bool] = None
    isMultipart: Optional[bool] = None
    isRead: Optional[bool] = None
    modifiedTime: Optional[str] = None
    receivedTime: Optional[str] = None
    sentTime: Optional[str] = None
    body: Optional[str] = None
    contentDisposition: Optional[str] = None
    contentType: Optional[str] = None
    inReplyTo: Optional[str] = None
    messageID: Optional[str] = None
    priority: Optional[str] = None
    subject: Optional[str] = None
    xMailer: Optional[str] = None
    categories: Optional[str] = None
    labels: Optional[str] = None
    receivedLines: Optional[str] = None

class WirelessNetworkConnection(NetworkConnection):
    """
    A wireless network connection is a connection (completed or attempted)
    across an IEEE 802.11 standards-confromant digital network (a group of two
    or more computer systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]
    """

    pass

class HTTPConnection(NetworkConnection):
    """
    An HTTP connection is network connection that is conformant to the Hypertext
    Transfer Protocol (HTTP) standard.
    """

    pass

class ICMPConnection(NetworkConnection):
    """
    An ICMP connection is a network connection that is conformant to the
    Internet Control Message Protocol (ICMP) standard.
    """

    pass

class TCPConnection(NetworkConnection):
    """
    A TCP connection is a network connection that is conformant to the Transfer
    """

    pass

class DigitalAddress(Address):
    """
    A digital address is an identifier assigned to enable routing and management
    of digital communication.
    """

    pass

class SocketAddress(Address):
    """
    A socket address (combining and IP address and a port number) is a composite
    identifier for a network socket endpoint supporting internet protocol
    communications.
    """

    pass

class DigitalAccount(Account):
    """
    A digital account is an arrangement with an entity to enable and control the
    provision of some capability or service within the digital domain.
    """

    pass

class Drone(MobileDevice):
    """
    A drone, unmanned aerial vehicle (UAV), is an aircraft without a human
    pilot, crew, or passengers that typically involve a ground-based controller
    and a system for communications with the UAV.
    """

    pass

class MobilePhone(MobileDevice):
    """
    A mobile phone is a portable telephone that at least can make and receive
    calls over a radio frequency link while the user is moving within a
    telephone service area. This category encompasses all types of mobiles,
    simple and smart and satellite ones all together.
    """

    pass

class WearableDevice(SmartDevice):
    """
    A wearable device is an electronic device that is designed to be worn on a
    person's body.
    """

    pass

class AndroidPhone(AndroidDevice):
    """
    An android phone is a smart phone that applies the Android mobile operating
    system.
    """

    pass

class IPhone(AppleDevice):
    """
    An iPhone is a smart phone that applies the iOS mobile operating system.
    """

    pass

class NetworkAppliance(Appliance):
    """
    A network appliance is a purpose-built computer with software or firmware
    that is designed to provide a specific network management function.
    """

    pass

class SecurityAppliance(Appliance):
    """
    A security appliance is a purpose-built computer with software or firmware
    that is designed to provide a specific security function to protect computer
    networks.
    """

    pass

class Tablet(Computer):
    """
    A tablet is a mobile computer that is primarily operated by touching the
    screen. (Devices categorized by their manufacturer as a Tablet)
    """

    pass

class Laptop(Computer):
    """
    A laptop, laptop computer, or notebook computer is a small, portable
    personal computer with a screen and alphanumeric keyboard. These typically
    have a clam shell form factor with the screen mounted on the inside of the
    upper lid and the keyboard on the inside of the lower lid, although 2-in-1
    PCs with a detachable keyboard are often marketed as laptops or as having a
    laptop mode. (Devices categorized by their manufacturer as a Laptop)
    """

    pass

class SmartPhone(Computer):
    """
    A smartphone is a portable device that combines mobile telephone and
    computing functions into one unit. Examples include iPhone, Samsung Galaxy,
    Huawei, Blackberry. (Inferred by model and OperatingSystemFacet)
    """

    pass

class Server(Computer):
    """
    A server is a server rack-mount based computer, minicomputer, supercomputer,
    etc.
    """

    pass

class Disk(StorageMedium):
    """
    A disk is a storage mechanism where data is recorded by various electronic,
    magnetic, optical, or mechanical changes to a surface layer of one or more
    rotating disks.
    """

    pass

class ContactFacet(core.Facet):
    """
    A contact facet is a grouping of characteristics unique to a set of
    identification and communication related details for a single entity.
    """

    contactAddress: Optional[ContactAddress] = None
    contactAffiliation: Optional[ContactAffiliation] = None
    contactEmail: Optional[ContactEmail] = None
    contactMessaging: Optional[ContactMessaging] = None
    contactPhone: Optional[ContactPhone] = None
    contactProfile: Optional[ContactProfile] = None
    contactSIP: Optional[ContactSIP] = None
    contactURL: Optional[ContactURL] = None
    sourceApplication: Optional[ObservableObject] = None
    birthdate: Optional[str] = None
    lastTimeContacted: Optional[str] = None
    numberTimesContacted: Optional[int] = None
    contactID: Optional[str] = None
    displayName: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    namePhonetic: Optional[str] = None
    namePrefix: Optional[str] = None
    nameSuffix: Optional[str] = None
    contactGroup: Optional[str] = None
    contactNote: Optional[str] = None
    nickname: Optional[str] = None

class PDFFile(File):
    """
    A PDF file is a Portable Document Format (PDF) file.
    """

    pass

class WindowsPEBinaryFile(File):
    """
    A Windows PE binary file is a Windows portable executable (PE) file.
    """

    pass

class ArchiveFile(File):
    """
    An archive file is a file that is composed of one or more computer files
    along with metadata.
    """

    pass

class RasterPicture(File):
    """
    A raster picture is a raster (or bitmap) image.
    """

    pass

class UNIXFile(File):
    """
    A UNIX file is a file pertaining to the UNIX operating system.
    """

    pass

class NTFSFile(File):
    """
    An NTFS file is a New Technology File System (NTFS) file.
    """

    pass

class NTFSFileFacet(core.Facet):
    """
    An NTFS file facet is a grouping of characteristics unique to a file on an
    NTFS (new technology filesystem) file system.
    """

    alternateDataStreams: Optional[AlternateDataStream] = None
    entryID: Optional[int] = None
    sid: Optional[str] = None

class MACAddress(DigitalAddress):
    """
    A MAC address is a media access control standards conformant identifier
    assigned to a network interface to enable routing and management of
    communications at the data link layer of a network segment.
    """

    pass

class IPAddress(DigitalAddress):
    """
    An IP address is an Internet Protocol (IP) standards conformant identifier
    assigned to a device to enable routing and management of IP standards
    conformant communication to or from that device.
    """

    pass

class SIPAddress(DigitalAddress):
    """
    A SIP address is an identifier for Session Initiation Protocol (SIP)
    communication.
    """

    pass

class InstantMessagingAddress(DigitalAddress):

    pass

class EmailAddress(DigitalAddress):
    """
    An email address is an identifier for an electronic mailbox to which
    electronic mail messages (conformant to the Simple Mail Transfer Protocol
    (SMTP)) are sent from and delivered to.
    """

    pass

class UNIXAccount(DigitalAccount):
    """
    A UNIX account is an account on a UNIX operating system.
    """

    pass

class UserAccount(DigitalAccount):
    """
    A user account is an account controlling a user's access to a network,
    system or platform.
    """

    pass

class WindowsAccount(DigitalAccount):
    """
    A Windows account is a user account on a Windows operating system.
    """

    pass

class PhoneAccount(DigitalAccount):
    """
    A phone account is an arrangement with an entity to enable and control the
    provision of a telephony capability or service.
    """

    pass

class WindowsActiveDirectoryAccount(DigitalAccount):
    """
    A Windows Active Directory account is an account managed by directory-based
    identity-related services of a Windows operating system.
    """

    pass

class ApplicationAccount(DigitalAccount):
    """
    An application account is an account within a particular software program
    designed for end users.
    """

    pass

class EmailAccount(DigitalAccount):
    """
    An email account is an arrangement with an entity to enable and control the
    provision of electronic mail (email) capabilities or services.
    """

    pass

class MobileAccount(DigitalAccount):
    """
    A mobile account is an arrangement with an entity to enable and control the
    provision of some capability or service on a portable computing device.
    [based on https://www.lexico.com/definition/mobile_device]
    """

    pass

class BlackberryPhone(SmartPhone):
    """
    A blackberry phone is a smart phone that applies the Blackberry OS mobile
    operating system. (Blackberry 10 re-introduces Blackberry OS, prior to that
    the OS was Android.)
    """

    pass

class WhoisContactFacet(ContactFacet):
    """
    A Whois contact type is a grouping of characteristics unique to
    contact-related information present in a response record conformant to the
    WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]
    """

    whoisContactType: Optional[str] = None
    whoisContactType: Optional[Any] = None
    whoisContactType: Optional[Any] = None

class WifiAddress(MACAddress):
    """
    A Wi-Fi address is a media access control (MAC) standards-conformant
    identifier assigned to a device network interface to enable routing and
    management of IEEE 802.11 standards-conformant communications to and from
    that device.
    """

    pass

class BluetoothAddress(MACAddress):
    """
    A Bluetooth address is a Bluetooth standard conformant identifier assigned
    to a Bluetooth device to enable routing and management of Bluetooth
    standards conformant communication to or from that device.
    """

    pass

class IPv6Address(IPAddress):
    """
    An IPv6 (Internet Protocol version 6) address is an IPv6 standards
    conformant identifier assigned to a device to enable routing and management
    of IPv6 standards conformant communication to or from that device.
    """

    pass

class IPv4Address(IPAddress):
    """
    An IPv4 (Internet Protocol version 4) address is an IPv4 standards
    conformant identifier assigned to a device to enable routing and management
    of IPv4 standards conformant communication to or from that device.
    """

    pass

