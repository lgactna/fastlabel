"""
Auto-generated classes from the SHACL graph in vocabulary.ttl.

This file was generated using the `case_models.py` script.
"""

from enum import Enum


class AccountTypeVocab(str, Enum):
    LDAP = "ldap"
    NIS = "nis"
    OPENID = "openid"
    RADIUS = "radius"
    TACACS = "tacacs"
    UNIX = "unix"
    WINDOWS_DOMAIN = "windows_domain"
    WINDOWS_LOCAL = "windows_local"


class ActionArgumentNameVocab(str, Enum):
    """
    Defines an open-vocabulary for common arguments of cyber actions.
    """

    APC_ADDRESS = "APC Address"
    APC_MODE = "APC Mode"
    API = "API"
    ACCESS_MODE = "Access Mode"
    APPLICATION_NAME = "Application Name"
    BASE_ADDRESS = "Base Address"
    CALLBACK_ADDRESS = "Callback Address"
    CODE_ADDRESS = "Code Address"
    COMMAND = "Command"
    CONTROL_CODE = "Control Code"
    CONTROL_PARAMETER = "Control Parameter"
    CREATION_FLAGS = "Creation Flags"
    DATABASE_NAME = "Database Name"
    DELAY_TIME__MS_ = "Delay Time (ms)"
    DESTINATION_ADDRESS = "Destination Address"
    ERROR_CONTROL = "Error Control"
    FILE_INFORMATION_CLASS = "File Information Class"
    FLAGS = "Flags"
    FUNCTION_ADDRESS = "Function Address"
    FUNCTION_NAME = "Function Name"
    FUNCTION_ORDINAL = "Function Ordinal"
    HOOK_TYPE = "Hook Type"
    HOST_NAME = "Host Name"
    HOSTNAME = "Hostname"
    INITIAL_OWNER = "Initial Owner"
    MAPPING_OFFSET = "Mapping Offset"
    NUMBER_OF_BYTES_PER_SEND = "Number of Bytes Per Send"
    OPTIONS = "Options"
    PARAMETER_ADDRESS = "Parameter Address"
    PASSWORD = "Password"
    PRIVILEGE_NAME = "Privilege Name"
    PROTECTION = "Protection"
    PROXY_BYPASS = "Proxy Bypass"
    PROXY_NAME = "Proxy Name"
    REASON = "Reason"
    REQUEST_SIZE = "Request Size"
    REQUESTED_VERSION = "Requested Version"
    SERVER = "Server"
    SERVICE_NAME = "Service Name"
    SERVICE_STATE = "Service State"
    SERVICE_TYPE = "Service Type"
    SHARE_MODE = "Share Mode"
    SHUTDOWN_FLAG = "Shutdown Flag"
    SIZE__BYTES_ = "Size (bytes)"
    SLEEP_TIME__MS_ = "Sleep Time (ms)"
    SOURCE_ADDRESS = "Source Address"
    STARTING_ADDRESS = "Starting Address"
    SYSTEM_METRIC_INDEX = "System Metric Index"
    TARGET_PID = "Target PID"
    TRANSFER_FLAGS = "Transfer Flags"
    USERNAME = "Username"


class ActionNameVocab(str, Enum):
    """
    Defines an open-vocabulary of common specific cyber action names.
    """

    ACCEPT_SOCKET_CONNECTION = "Accept Socket Connection"
    ADD_CONNECTION_TO_NETWORK_SHARE = "Add Connection to Network Share"
    ADD_NETWORK_SHARE = "Add Network Share"
    ADD_SCHEDULED_TASK = "Add Scheduled Task"
    ADD_SYSTEM_CALL_HOOK = "Add System Call Hook"
    ADD_USER = "Add User"
    ADD_WINDOWS_HOOK = "Add Windows Hook"
    ALLOCATE_VIRTUAL_MEMORY_IN_PROCESS = "Allocate Virtual Memory in Process"
    BIND_ADDRESS_TO_SOCKET = "Bind Address to Socket"
    CHANGE_SERVICE_CONFIGURATION = "Change Service Configuration"
    CHECK_FOR_REMOTE_DEBUGGER = "Check for Remote Debugger"
    CLOSE_PORT = "Close Port"
    CLOSE_REGISTRY_KEY = "Close Registry Key"
    CLOSE_SOCKET = "Close Socket"
    CONFIGURE_SERVICE = "Configure Service"
    CONNECT_TO_IP = "Connect to IP"
    CONNECT_TO_NAMED_PIPE = "Connect to Named Pipe"
    CONNECT_TO_NETWORK_SHARE = "Connect to Network Share"
    CONNECT_TO_SOCKET = "Connect to Socket"
    CONNECT_TO_URL = "Connect to URL"
    CONTROL_DRIVER = "Control Driver"
    CONTROL_SERVICE = "Control Service"
    COPY_FILE = "Copy File"
    CREATE_DIALOG_BOX = "Create Dialog Box"
    CREATE_DIRECTORY = "Create Directory"
    CREATE_EVENT = "Create Event"
    CREATE_FILE = "Create File"
    CREATE_FILE_ALTERNATE_DATA_STREAM = "Create File Alternate Data Stream"
    CREATE_FILE_MAPPING = "Create File Mapping"
    CREATE_FILE_SYMBOLIC_LINK = "Create File Symbolic Link"
    CREATE_HIDDEN_FILE = "Create Hidden File"
    CREATE_MAILSLOT = "Create Mailslot"
    CREATE_MODULE = "Create Module"
    CREATE_MUTEX = "Create Mutex"
    CREATE_NAMED_PIPE = "Create Named Pipe"
    CREATE_PROCESS = "Create Process"
    CREATE_PROCESS_AS_USER = "Create Process as User"
    CREATE_REGISTRY_KEY = "Create Registry Key"
    CREATE_REGISTRY_KEY_VALUE = "Create Registry Key Value"
    CREATE_REMOTE_THREAD_IN_PROCESS = "Create Remote Thread in Process"
    CREATE_SERVICE = "Create Service"
    CREATE_SOCKET = "Create Socket"
    CREATE_SYMBOLIC_LINK = "Create Symbolic Link"
    CREATE_THREAD = "Create Thread"
    CREATE_WINDOW = "Create Window"
    DELETE_DIRECTORY = "Delete Directory"
    DELETE_FILE = "Delete File"
    DELETE_NAMED_PIPE = "Delete Named Pipe"
    DELETE_NETWORK_SHARE = "Delete Network Share"
    DELETE_REGISTRY_KEY = "Delete Registry Key"
    DELETE_REGISTRY_KEY_VALUE = "Delete Registry Key Value"
    DELETE_SERVICE = "Delete Service"
    DELETE_USER = "Delete User"
    DISCONNECT_FROM_NAMED_PIPE = "Disconnect from Named Pipe"
    DISCONNECT_FROM_NETWORK_SHARE = "Disconnect from Network Share"
    DISCONNECT_FROM_SOCKET = "Disconnect from Socket"
    DOWNLOAD_FILE = "Download File"
    ENUMERATE_DLLS = "Enumerate DLLs"
    ENUMERATE_NETWORK_SHARES = "Enumerate Network Shares"
    ENUMERATE_PROCESSES = "Enumerate Processes"
    ENUMERATE_PROTOCOLS = "Enumerate Protocols"
    ENUMERATE_REGISTRY_KEY_SUBKEYS = "Enumerate Registry Key Subkeys"
    ENUMERATE_REGISTRY_KEY_VALUES = "Enumerate Registry Key Values"
    ENUMERATE_SERVICES = "Enumerate Services"
    ENUMERATE_SYSTEM_HANDLES = "Enumerate System Handles"
    ENUMERATE_THREADS = "Enumerate Threads"
    ENUMERATE_THREADS_IN_PROCESS = "Enumerate Threads in Process"
    ENUMERATE_USERS = "Enumerate Users"
    ENUMERATE_WINDOWS = "Enumerate Windows"
    FIND_FILE = "Find File"
    FIND_WINDOW = "Find Window"
    FLUSH_PROCESS_INSTRUCTION_CACHE = "Flush Process Instruction Cache"
    FREE_LIBRARY = "Free Library"
    FREE_PROCESS_VIRTUAL_MEMORY = "Free Process Virtual Memory"
    GET_DISK_FREE_SPACE = "Get Disk Free Space"
    GET_DISK_TYPE = "Get Disk Type"
    GET_ELAPSED_SYSTEM_UP_TIME = "Get Elapsed System Up Time"
    GET_FILE_ATTRIBUTES = "Get File Attributes"
    GET_FUNCTION_ADDRESS = "Get Function Address"
    GET_HOST_BY_ADDRESS = "Get Host By Address"
    GET_HOST_BY_NAME = "Get Host By Name"
    GET_HOST_NAME = "Get Host Name"
    GET_LIBRARY_FILE_NAME = "Get Library File Name"
    GET_LIBRARY_HANDLE = "Get Library Handle"
    GET_NETBIOS_NAME = "Get NetBIOS Name"
    GET_PROCESS_CURRENT_DIRECTORY = "Get Process Current Directory"
    GET_PROCESS_ENVIRONMENT_VARIABLE = "Get Process Environment Variable"
    GET_PROCESS_STARTUP_INFORMATION = "Get Process Startup Information"
    GET_PROCESSES_SNAPSHOT = "Get Processes Snapshot"
    GET_REGISTRY_KEY_ATTRIBUTES = "Get Registry Key Attributes"
    GET_SERVICE_STATUS = "Get Service Status"
    GET_SYSTEM_GLOBAL_FLAGS = "Get System Global Flags"
    GET_SYSTEM_HOST_NAME = "Get System Host Name"
    GET_SYSTEM_LOCAL_TIME = "Get System Local Time"
    GET_SYSTEM_NETBIOS_NAME = "Get System NetBIOS Name"
    GET_SYSTEM_NETWORK_PARAMETERS = "Get System Network Parameters"
    GET_SYSTEM_TIME = "Get System Time"
    GET_THREAD_CONTEXT = "Get Thread Context"
    GET_THREAD_USERNAME = "Get Thread Username"
    GET_USER_ATTRIBUTES = "Get User Attributes"
    GET_USERNAME = "Get Username"
    GET_WINDOWS_DIRECTORY = "Get Windows Directory"
    GET_WINDOWS_SYSTEM_DIRECTORY = "Get Windows System Directory"
    GET_WINDOWS_TEMPORARY_FILES_DIRECTORY = "Get Windows Temporary Files Directory"
    HIDE_WINDOW = "Hide Window"
    IMPERSONATE_PROCESS = "Impersonate Process"
    IMPERSONATE_THREAD = "Impersonate Thread"
    INJECT_MEMORY_PAGE = "Inject Memory Page"
    KILL_PROCESS = "Kill Process"
    KILL_THREAD = "Kill Thread"
    KILL_WINDOW = "Kill Window"
    LISTEN_ON_PORT = "Listen on Port"
    LISTEN_ON_SOCKET = "Listen on Socket"
    LOAD_DRIVER = "Load Driver"
    LOAD_LIBRARY = "Load Library"
    LOAD_MODULE = "Load Module"
    LOAD_AND_CALL_DRIVER = "Load and Call Driver"
    LOCK_FILE = "Lock File"
    LOGON_AS_USER = "Logon as User"
    MAP_FILE = "Map File"
    MAP_LIBRARY = "Map Library"
    MAP_VIEW_OF_FILE = "Map View of File"
    MODIFY_FILE = "Modify File"
    MODIFY_NAMED_PIPE = "Modify Named Pipe"
    MODIFY_PROCESS = "Modify Process"
    MODIFY_REGISTRY_KEY = "Modify Registry Key"
    MODIFY_REGISTRY_KEY_VALUE = "Modify Registry Key Value"
    MODIFY_SERVICE = "Modify Service"
    MONITOR_REGISTRY_KEY = "Monitor Registry Key"
    MOVE_FILE = "Move File"
    OPEN_FILE = "Open File"
    OPEN_FILE_MAPPING = "Open File Mapping"
    OPEN_MUTEX = "Open Mutex"
    OPEN_PORT = "Open Port"
    OPEN_PROCESS = "Open Process"
    OPEN_REGISTRY_KEY = "Open Registry Key"
    OPEN_SERVICE = "Open Service"
    OPEN_SERVICE_CONTROL_MANAGER = "Open Service Control Manager"
    PROTECT_VIRTUAL_MEMORY = "Protect Virtual Memory"
    QUERY_DNS = "Query DNS"
    QUERY_DISK_ATTRIBUTES = "Query Disk Attributes"
    QUERY_PROCESS_VIRTUAL_MEMORY = "Query Process Virtual Memory"
    QUEUE_APC_IN_THREAD = "Queue APC in Thread"
    READ_FILE = "Read File"
    READ_FROM_NAMED_PIPE = "Read From Named Pipe"
    READ_FROM_PROCESS_MEMORY = "Read From Process Memory"
    READ_REGISTRY_KEY_VALUE = "Read Registry Key Value"
    RECEIVE_DATA_ON_SOCKET = "Receive Data on Socket"
    RECEIVE_EMAIL_MESSAGE = "Receive Email Message"
    RELEASE_MUTEX = "Release Mutex"
    RENAME_FILE = "Rename File"
    REVERT_THREAD_TO_SELF = "Revert Thread to Self"
    SEND_CONTROL_CODE_TO_FILE = "Send Control Code to File"
    SEND_CONTROL_CODE_TO_PIPE = "Send Control Code to Pipe"
    SEND_CONTROL_CODE_TO_SERVICE = "Send Control Code to Service"
    SEND_DNS_QUERY = "Send DNS Query"
    SEND_DATA_ON_SOCKET = "Send Data on Socket"
    SEND_DATA_TO_ADDRESS_ON_SOCKET = "Send Data to Address on Socket"
    SEND_EMAIL_MESSAGE = "Send Email Message"
    SEND_ICMP_REQUEST = "Send ICMP Request"
    SEND_REVERSE_DNS_QUERY = "Send Reverse DNS Query"
    SET_FILE_ATTRIBUTES = "Set File Attributes"
    SET_NETBIOS_NAME = "Set NetBIOS Name"
    SET_PROCESS_CURRENT_DIRECTORY = "Set Process Current Directory"
    SET_PROCESS_ENVIRONMENT_VARIABLE = "Set Process Environment Variable"
    SET_SYSTEM_GLOBAL_FLAGS = "Set System Global Flags"
    SET_SYSTEM_HOST_NAME = "Set System Host Name"
    SET_SYSTEM_TIME = "Set System Time"
    SET_THREAD_CONTEXT = "Set Thread Context"
    SHOW_WINDOW = "Show Window"
    SHUTDOWN_SYSTEM = "Shutdown System"
    SLEEP_PROCESS = "Sleep Process"
    SLEEP_SYSTEM = "Sleep System"
    START_SERVICE = "Start Service"
    UNLOAD_DRIVER = "Unload Driver"
    UNLOAD_MODULE = "Unload Module"
    UNLOCK_FILE = "Unlock File"
    UNMAP_FILE = "Unmap File"
    UPLOAD_FILE = "Upload File"
    WRITE_TO_FILE = "Write to File"
    WRITE_TO_PROCESS_VIRTUAL_MEMORY = "Write to Process Virtual Memory"


class ActionRelationshipTypeVocab(str, Enum):
    """
    Defines an open-vocabulary for capturing types of relationships between
    actions.
    """

    DEPENDENT_ON = "Dependent_On"
    EQUIVALENT_TO = "Equivalent_To"
    FOLLOWED_BY = "Followed_By"
    INITIATED = "Initiated"
    INITIATED_BY = "Initiated_By"
    PRECEDED_BY = "Preceded_By"
    RELATED_TO = "Related_To"


class ActionStatusTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of action status types.
    """

    COMPLETE_FINISH = "Complete/Finish"
    ERROR = "Error"
    FAIL = "Fail"
    ONGOING = "Ongoing"
    PENDING = "Pending"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"


class ActionTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of common general action types.
    """

    ACCEPT = "Accept"
    ACCESS = "Access"
    ADD = "Add"
    ALERT = "Alert"
    ALLOCATE = "Allocate"
    ARCHIVE = "Archive"
    ASSIGN = "Assign"
    AUDIT = "Audit"
    BACKUP = "Backup"
    BIND = "Bind"
    BLOCK = "Block"
    CALL = "Call"
    CHANGE = "Change"
    CHECK = "Check"
    CLEAN = "Clean"
    CLICK = "Click"
    CLOSE = "Close"
    COMPARE = "Compare"
    COMPRESS = "Compress"
    CONFIGURE = "Configure"
    CONNECT = "Connect"
    CONTROL = "Control"
    COPY_DUPLICATE = "Copy/Duplicate"
    CREATE = "Create"
    DECODE = "Decode"
    DECOMPRESS = "Decompress"
    DECRYPT = "Decrypt"
    DENY = "Deny"
    DEPRESS = "Depress"
    DETECT = "Detect"
    DISCONNECT = "Disconnect"
    DOWNLOAD = "Download"
    DRAW = "Draw"
    DROP = "Drop"
    ENCODE = "Encode"
    ENCRYPT = "Encrypt"
    ENUMERATE = "Enumerate"
    EXECUTE = "Execute"
    EXTRACT = "Extract"
    FILTER = "Filter"
    FIND = "Find"
    FLUSH = "Flush"
    FORK = "Fork"
    FREE = "Free"
    GET = "Get"
    HIDE = "Hide"
    HOOK = "Hook"
    IMPERSONATE = "Impersonate"
    INITIALIZE = "Initialize"
    INJECT = "Inject"
    INSTALL = "Install"
    INTERLEAVE = "Interleave"
    JOIN = "Join"
    KILL = "Kill"
    LISTEN = "Listen"
    LOAD = "Load"
    LOCK = "Lock"
    LOGIN_LOGON = "Login/Logon"
    LOGOUT_LOGOFF = "Logout/Logoff"
    MAP = "Map"
    MERGE = "Merge"
    MODIFY = "Modify"
    MONITOR = "Monitor"
    MOVE = "Move"
    OPEN = "Open"
    PACK = "Pack"
    PAUSE = "Pause"
    PRESS = "Press"
    PROTECT = "Protect"
    QUARANTINE = "Quarantine"
    QUERY = "Query"
    QUEUE = "Queue"
    RAISE = "Raise"
    READ = "Read"
    RECEIVE = "Receive"
    RELEASE = "Release"
    REMOVE_DELETE = "Remove/Delete"
    RENAME = "Rename"
    REPLICATE = "Replicate"
    RESTORE = "Restore"
    RESUME = "Resume"
    REVERT = "Revert"
    RUN = "Run"
    SAVE = "Save"
    SCAN = "Scan"
    SCHEDULE = "Schedule"
    SEARCH = "Search"
    SEND = "Send"
    SET = "Set"
    SHUTDOWN = "Shutdown"
    SLEEP = "Sleep"
    SNAPSHOT = "Snapshot"
    START = "Start"
    STOP = "Stop"
    SUSPEND = "Suspend"
    SYNCHRONIZE = "Synchronize"
    THROW = "Throw"
    TRANSMIT = "Transmit"
    UNBLOCK = "Unblock"
    UNHIDE = "Unhide"
    UNHOOK = "Unhook"
    UNINSTALL = "Uninstall"
    UNLOAD = "Unload"
    UNLOCK = "Unlock"
    UNMAP = "Unmap"
    UNPACK = "Unpack"
    UPDATE = "Update"
    UPGRADE = "Upgrade"
    UPLOAD = "Upload"
    WIPE_DESTROY_PURGE = "Wipe/Destroy/Purge"
    WRITE = "Write"


class BitnessVocab(str, Enum):
    """
    Defines an open-vocabulary of word sizes that define classes of operating
    systems.
    """

    _32 = "32"
    _64 = "64"


class CharacterEncodingVocab(str, Enum):
    """
    Defines an open-vocabulary of character encodings.
    """

    ASCII = "ASCII"
    UTF_16 = "UTF-16"
    UTF_32 = "UTF-32"
    UTF_8 = "UTF-8"
    WINDOWS_1250 = "Windows-1250"
    WINDOWS_1251 = "Windows-1251"
    WINDOWS_1252 = "Windows-1252"
    WINDOWS_1253 = "Windows-1253"
    WINDOWS_1254 = "Windows-1254"
    WINDOWS_1255 = "Windows-1255"
    WINDOWS_1256 = "Windows-1256"
    WINDOWS_1257 = "Windows-1257"
    WINDOWS_1258 = "Windows-1258"


class ContactAddressScopeVocab(str, Enum):
    """
    Defines an open-vocabulary of scopes for address entries of digital
    contacts.
    """

    HOME = "home"
    WORK = "work"
    SCHOOL = "school"


class ContactEmailScopeVocab(str, Enum):
    """
    Defines an open-vocabulary of scopes for email entries of digital contacts.
    """

    HOME = "home"
    WORK = "work"
    SCHOOL = "school"
    CLOUD = "cloud"


class ContactPhoneScopeVocab(str, Enum):
    """
    Defines an open-vocabulary of scopes for phone entries of digital contacts.
    """

    HOME = "home"
    WORK = "work"
    SCHOOL = "school"
    MOBILE = "mobile"
    MAIN = "main"
    HOME_FAX = "home fax"
    WORK_FAX = "work fax"
    PAGER = "pager"


class ContactSIPScopeVocab(str, Enum):
    """
    Defines an open-vocabulary of scopes for Session Initiation Protocol (SIP)
    entries of digital contacts.
    """

    HOME = "home"
    WORK = "work"
    SCHOOL = "school"


class ContactURLScopeVocab(str, Enum):
    """
    Defines an open-vocabulary of scopes for URL entries of digital contacts.
    """

    HOME = "home"
    WORK = "work"
    SCHOOL = "school"
    HOMEPAGE = "homepage"


class DiskTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of disk types.
    """

    CDROM = "CDRom"
    FIXED = "Fixed"
    RAMDISK = "RAMDisk"
    REMOTE = "Remote"
    REMOVABLE = "Removable"


class EndiannessTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of byte ordering methods.
    """

    BIG_ENDIAN = "Big-endian"
    LITTLE_ENDIAN = "Little-endian"
    MIDDLE_ENDIAN = "Middle-endian"


class HashNameVocab(str, Enum):
    """
    Defines an open-vocabulary of hashing algorithm names.
    """

    MD5 = "MD5"
    MD6 = "MD6"
    SHA1 = "SHA1"
    SHA224 = "SHA224"
    SHA256 = "SHA256"
    SHA3_224 = "SHA3-224"
    SHA3_256 = "SHA3-256"
    SHA3_384 = "SHA3-384"
    SHA3_512 = "SHA3-512"
    SHA384 = "SHA384"
    SHA512 = "SHA512"
    SSDEEP = "SSDEEP"


class LibraryTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of library types.
    """

    DYNAMIC = "Dynamic"
    OTHER = "Other"
    REMOTE = "Remote"
    SHARED = "Shared"
    STATIC = "Static"


class MemoryBlockTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of types of memory blocks.
    """

    BIT_MAPPED = "Bit-mapped"
    BYTE_MAPPED = "Byte-mapped"
    INITIALIZED = "Initialized"
    OVERLAY = "Overlay"
    UNINITIALIZED = "Uninitialized"


class ObservableObjectRelationshipVocab(str, Enum):
    """
    Defines an open-vocabulary of inter-observable object relationships.
    """

    ALLOCATED = "Allocated"
    ALLOCATED_BY = "Allocated_By"
    ATTACHMENT_OF = "Attachment_Of"
    BOUND = "Bound"
    BOUND_BY = "Bound_By"
    CHARACTERIZED_BY = "Characterized_By"
    CHARACTERIZES = "Characterizes"
    CHILD_OF = "Child_Of"
    CLOSED = "Closed"
    CLOSED_BY = "Closed_By"
    COMPRESSED = "Compressed"
    COMPRESSED_BY = "Compressed_By"
    COMPRESSED_FROM = "Compressed_From"
    COMPRESSED_INTO = "Compressed_Into"
    CONNECTED_FROM = "Connected_From"
    CONNECTED_TO = "Connected_To"
    CONTAINED_WITHIN = "Contained_Within"
    CONTAINS = "Contains"
    COPIED = "Copied"
    COPIED_BY = "Copied_By"
    COPIED_FROM = "Copied_From"
    COPIED_TO = "Copied_To"
    CREATED = "Created"
    CREATED_BY = "Created_By"
    DECODED = "Decoded"
    DECODED_BY = "Decoded_By"
    DECOMPRESSED = "Decompressed"
    DECOMPRESSED_BY = "Decompressed_By"
    DECRYPTED = "Decrypted"
    DECRYPTED_BY = "Decrypted_By"
    DELETED = "Deleted"
    DELETED_BY = "Deleted_By"
    DELETED_FROM = "Deleted_From"
    DOWNLOADED = "Downloaded"
    DOWNLOADED_BY = "Downloaded_By"
    DOWNLOADED_FROM = "Downloaded_From"
    DOWNLOADED_TO = "Downloaded_To"
    DROPPED = "Dropped"
    DROPPED_BY = "Dropped_By"
    ENCODED = "Encoded"
    ENCODED_BY = "Encoded_By"
    ENCRYPTED = "Encrypted"
    ENCRYPTED_BY = "Encrypted_By"
    ENCRYPTED_FROM = "Encrypted_From"
    ENCRYPTED_TO = "Encrypted_To"
    EXTRACTED_FROM = "Extracted_From"
    FQDN_OF = "FQDN_Of"
    FREED = "Freed"
    FREED_BY = "Freed_By"
    HAD_ATTACHMENT = "Had_Attachment"
    HOOKED = "Hooked"
    HOOKED_BY = "Hooked_By"
    INITIALIZED_BY = "Initialized_By"
    INITIALIZED_TO = "Initialized_To"
    INJECTED = "Injected"
    INJECTED_AS = "Injected_As"
    INJECTED_BY = "Injected_By"
    INJECTED_INTO = "Injected_Into"
    INSTALLED = "Installed"
    INSTALLED_BY = "Installed_By"
    JOINED = "Joined"
    JOINED_BY = "Joined_By"
    KILLED = "Killed"
    KILLED_BY = "Killed_By"
    LISTENED_ON = "Listened_On"
    LISTENED_ON_BY = "Listened_On_By"
    LOADED_FROM = "Loaded_From"
    LOADED_INTO = "Loaded_Into"
    LOCKED = "Locked"
    LOCKED_BY = "Locked_By"
    MAPPED_BY = "Mapped_By"
    MAPPED_INTO = "Mapped_Into"
    MERGED = "Merged"
    MERGED_BY = "Merged_By"
    MODIFIED_PROPERTIES_OF = "Modified_Properties_Of"
    MONITORED = "Monitored"
    MONITORED_BY = "Monitored_By"
    MOVED = "Moved"
    MOVED_BY = "Moved_By"
    MOVED_FROM = "Moved_From"
    MOVED_TO = "Moved_To"
    OPENED = "Opened"
    OPENED_BY = "Opened_By"
    PACKED = "Packed"
    PACKED_BY = "Packed_By"
    PACKED_FROM = "Packed_From"
    PACKED_INTO = "Packed_Into"
    PARENT_OF = "Parent_Of"
    PAUSED = "Paused"
    PAUSED_BY = "Paused_By"
    PREVIOUSLY_CONTAINED = "Previously_Contained"
    PROPERTIES_MODIFIED_BY = "Properties_Modified_By"
    PROPERTIES_QUERIED = "Properties_Queried"
    PROPERTIES_QUERIED_BY = "Properties_Queried_By"
    READ_FROM = "Read_From"
    READ_FROM_BY = "Read_From_By"
    RECEIVED = "Received"
    RECEIVED_BY = "Received_By"
    RECEIVED_FROM = "Received_From"
    RECEIVED_VIA_UPLOAD = "Received_Via_Upload"
    REDIRECTS_TO = "Redirects_To"
    RELATED_TO = "Related_To"
    RENAMED = "Renamed"
    RENAMED_BY = "Renamed_By"
    RENAMED_FROM = "Renamed_From"
    RENAMED_TO = "Renamed_To"
    RESOLVED_TO = "Resolved_To"
    RESUMED = "Resumed"
    RESUMED_BY = "Resumed_By"
    ROOT_DOMAIN_OF = "Root_Domain_Of"
    SEARCHED_FOR = "Searched_For"
    SEARCHED_FOR_BY = "Searched_For_By"
    SENT = "Sent"
    SENT_BY = "Sent_By"
    SENT_TO = "Sent_To"
    SENT_VIA_UPLOAD = "Sent_Via_Upload"
    SET_FROM = "Set_From"
    SET_TO = "Set_To"
    SIGNED_BY = "Signed_By"
    SUB_DOMAIN_OF = "Sub-domain_Of"
    SUPRA_DOMAIN_OF = "Supra-domain_Of"
    SUSPENDED = "Suspended"
    SUSPENDED_BY = "Suspended_By"
    UNHOOKED = "Unhooked"
    UNHOOKED_BY = "Unhooked_By"
    UNLOCKED = "Unlocked"
    UNLOCKED_BY = "Unlocked_By"
    UNPACKED = "Unpacked"
    UNPACKED_BY = "Unpacked_By"
    UPLOADED = "Uploaded"
    UPLOADED_BY = "Uploaded_By"
    UPLOADED_FROM = "Uploaded_From"
    UPLOADED_TO = "Uploaded_To"
    USED = "Used"
    USED_BY = "Used_By"
    VALUES_ENUMERATED = "Values_Enumerated"
    VALUES_ENUMERATED_BY = "Values_Enumerated_By"
    WRITTEN_TO_BY = "Written_To_By"
    WROTE_TO = "Wrote_To"


class ObservableObjectStateVocab(str, Enum):
    """
    Defines an open-vocabulary of observable object states.
    """

    ACTIVE = "Active"
    CLOSED = "Closed"
    DOES_NOT_EXIST = "Does Not Exist"
    EXISTS = "Exists"
    INACTIVE = "Inactive"
    LOCKED = "Locked"
    OPEN = "Open"
    STARTED = "Started"
    STOPPED = "Stopped"
    UNLOCKED = "Unlocked"


class PartitionTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of partition types. See
    http://www.win.tue.nl/~aeb/partitions/partition_types-1.html for more
    information about the various partition types.
    """

    PARTITION_ENTRY_UNUSED = "PARTITION_ENTRY_UNUSED"
    PARTITION_EXTENDED = "PARTITION_EXTENDED"
    PARTITION_FAT32 = "PARTITION_FAT32"
    PARTITION_FAT32_XINT13 = "PARTITION_FAT32_XINT13"
    PARTITION_FAT_12 = "PARTITION_FAT_12"
    PARTITION_FAT_16 = "PARTITION_FAT_16"
    PARTITION_HUGE = "PARTITION_HUGE"
    PARTITION_IFS = "PARTITION_IFS"
    PARTITION_LDM = "PARTITION_LDM"
    PARTITION_NTFT = "PARTITION_NTFT"
    PARTITION_OS2BOOTMGR = "PARTITION_OS2BOOTMGR"
    PARTITION_PREP = "PARTITION_PREP"
    PARTITION_UNIX = "PARTITION_UNIX"
    PARTITION_XENIX_1 = "PARTITION_XENIX_1"
    PARTITION_XENIX_2 = "PARTITION_XENIX_2"
    PARTITION_XINT13 = "PARTITION_XINT13"
    PARTITION_XINT13_EXTENDED = "PARTITION_XINT13_EXTENDED"
    UNKNOWN = "UNKNOWN"
    VALID_NTFT = "VALID_NTFT"


class ProcessorArchVocab(str, Enum):
    """
    Defines an open-vocabulary of computer processor architectures.
    """

    ARM = "ARM"
    ALPHA = "Alpha"
    IA_64 = "IA-64"
    MIPS = "MIPS"
    MOTOROLA_68K = "Motorola 68k"
    OTHER = "Other"
    POWERPC = "PowerPC"
    SPARC = "SPARC"
    ESI_RISC = "eSi-RISC"
    X86_32 = "x86-32"
    X86_64 = "x86-64"
    Z_ARCHITECTURE = "z/Architecture"


class RecoveredObjectStatusVocab(str, Enum):
    """
    Defines the vocabulary for Recovered Object status of data.
    """

    RECOVERED = "recovered"
    PARTIALLY_RECOVERED = "partially recovered"
    OVERWRITTEN = "overwritten"
    UNKNOWN = "unknown"


class RegionalRegistryTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of Regional Internet Registries (RIRs) names,
    represented via their respective acronyms.
    """

    APNIC = "APNIC"
    ARIN = "ARIN"
    AFRINIC = "AfriNIC"
    LACNIC = "LACNIC"
    RIPE_NCC = "RIPE NCC"


class RegistryDatatypeVocab(str, Enum):
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


class SIMFormVocab(str, Enum):
    """
    Defines an open-vocabulary of common SIM card form factors.
    """

    FULL_SIZE_SIM = "Full-size SIM"
    MICRO_SIM = "Micro SIM"
    NANO_SIM = "Nano SIM"


class SIMTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of common SIM card types.
    """

    SIM = "SIM"
    UICC = "UICC"
    USIM = "USIM"


class TaskActionTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of task action types. See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa380596(v=vs.85).aspx.
    """

    TASK_ACTION_COM_HANDLER = "TASK_ACTION_COM_HANDLER"
    TASK_ACTION_EXEC = "TASK_ACTION_EXEC"
    TASK_ACTION_SEND_EMAIL = "TASK_ACTION_SEND_EMAIL"
    TASK_ACTION_SHOW_MESSAGE = "TASK_ACTION_SHOW_MESSAGE"


class TaskFlagVocab(str, Enum):
    """
    Defines an open-vocabulary of the run flags for a task scheduler task. See
    also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381283(v=vs.85).aspx
    See Also:
    http://msdn.microsoft.com/en-us/library/microsoft.office.excel.server.addins.computecluster.taskscheduler.taskflags(v=office.12).aspx.
    """

    TASK_FLAG_DELETE_WHEN_DONE = "TASK_FLAG_DELETE_WHEN_DONE"
    TASK_FLAG_DISABLED = "TASK_FLAG_DISABLED"
    TASK_FLAG_DONT_START_IF_ON_BATTERIES = "TASK_FLAG_DONT_START_IF_ON_BATTERIES"
    TASK_FLAG_HIDDEN = "TASK_FLAG_HIDDEN"
    TASK_FLAG_INTERACTIVE = "TASK_FLAG_INTERACTIVE"
    TASK_FLAG_KILL_IF_GOING_ON_BATTERIES = "TASK_FLAG_KILL_IF_GOING_ON_BATTERIES"
    TASK_FLAG_KILL_ON_IDLE_END = "TASK_FLAG_KILL_ON_IDLE_END"
    TASK_FLAG_RESTART_ON_IDLE_RESUME = "TASK_FLAG_RESTART_ON_IDLE_RESUME"
    TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET = "TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET"
    TASK_FLAG_RUN_ONLY_IF_LOGGED_ON = "TASK_FLAG_RUN_ONLY_IF_LOGGED_ON"
    TASK_FLAG_START_ONLY_IF_IDLE = "TASK_FLAG_START_ONLY_IF_IDLE"
    TASK_FLAG_SYSTEM_REQUIRED = "TASK_FLAG_SYSTEM_REQUIRED"
    TASK_FLAG_ZERO = "TASK_FLAG_ZERO"


class TaskPriorityVocab(str, Enum):
    """
    Defines an open-vocabulary of the priority levels of task scheduler tasks.
    See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383512(v=vs.85).aspx.
    """

    ABOVE_NORMAL_PRIORITY_CLASS = "ABOVE_NORMAL_PRIORITY_CLASS"
    BELOW_NORMAL_PRIORITY_CLASS = "BELOW_NORMAL_PRIORITY_CLASS"
    HIGH_PRIORITY_CLASS = "HIGH_PRIORITY_CLASS"
    IDLE_PRIORITY_CLASS = "IDLE_PRIORITY_CLASS"
    NORMAL_PRIORITY_CLASS = "NORMAL_PRIORITY_CLASS"
    REALTIME_PRIORITY_CLASS = "REALTIME_PRIORITY_CLASS"


class TaskStatusVocab(str, Enum):
    """
    Defines an open-vocabulary of the possible statuses of a scheduled task. See
    also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383604(v=vs.85).aspx
    See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381263(v=vs.85).aspx
    See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381833(v=vs.85).aspx
    See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383617(v=vs.85).aspx.
    """

    SCHED_E_ACCOUNT_DBASE_CORRUPT = "SCHED_E_ACCOUNT_DBASE_CORRUPT"
    SCHED_E_ACCOUNT_INFORMATION_NOT_SET = "SCHED_E_ACCOUNT_INFORMATION_NOT_SET"
    SCHED_E_ACCOUNT_NAME_NOT_FOUND = "SCHED_E_ACCOUNT_NAME_NOT_FOUND"
    SCHED_E_CANNOT_OPEN_TASK = "SCHED_E_CANNOT_OPEN_TASK"
    SCHED_E_INVALID_TASK = "SCHED_E_INVALID_TASK"
    SCHED_E_NO_SECURITY_SERVICES = "SCHED_E_NO_SECURITY_SERVICES"
    SCHED_E_SERVICE_NOT_INSTALLED = "SCHED_E_SERVICE_NOT_INSTALLED"
    SCHED_E_SERVICE_NOT_RUNNING = "SCHED_E_SERVICE_NOT_RUNNING"
    SCHED_E_TASK_NOT_READY = "SCHED_E_TASK_NOT_READY"
    SCHED_E_TASK_NOT_RUNNING = "SCHED_E_TASK_NOT_RUNNING"
    SCHED_E_TRIGGER_NOT_FOUND = "SCHED_E_TRIGGER_NOT_FOUND"
    SCHED_E_UNKNOWN_OBJECT_VERSION = "SCHED_E_UNKNOWN_OBJECT_VERSION"
    SCHED_E_UNSUPPORTED_ACCOUNT_OPTION = "SCHED_E_UNSUPPORTED_ACCOUNT_OPTION"
    SCHED_S_EVENT_TRIGGER = "SCHED_S_EVENT_TRIGGER"
    SCHED_S_TASK_DISABLED = "SCHED_S_TASK_DISABLED"
    SCHED_S_TASK_HAS_NOT_RUN = "SCHED_S_TASK_HAS_NOT_RUN"
    SCHED_S_TASK_NOT_SCHEDULED = "SCHED_S_TASK_NOT_SCHEDULED"
    SCHED_S_TASK_NO_MORE_RUNS = "SCHED_S_TASK_NO_MORE_RUNS"
    SCHED_S_TASK_NO_VALID_TRIGGERS = "SCHED_S_TASK_NO_VALID_TRIGGERS"
    SCHED_S_TASK_READY = "SCHED_S_TASK_READY"
    SCHED_S_TASK_RUNNING = "SCHED_S_TASK_RUNNING"
    SCHED_S_TASK_TERMINATED = "SCHED_S_TASK_TERMINATED"
    TASK_STATE_QUEUED = "TASK_STATE_QUEUED"
    TASK_STATE_UNKNOWN = "TASK_STATE_UNKNOWN"


class ThreadRunningStatusVocab(str, Enum):
    """
    Defines an open-vocabulary of the various states that a thread may be in
    before, during, or after execution. See
    http://msdn.microsoft.com/en-us/library/system.diagnostics.threadstate(v=vs.110).aspx.
    """

    INITIALIZED = "Initialized"
    READY = "Ready"
    RUNNING = "Running"
    STANDBY = "Standby"
    TERMINATED = "Terminated"
    TRANSITION = "Transition"
    UNKNOWN = "Unknown"
    WAITING = "Waiting"


class TimestampPrecisionVocab(str, Enum):
    """
    Defines an open-vocabulary of timestamp precision granularities.
    """

    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    MONTH = "month"
    SECOND = "second"
    YEAR = "year"


class TrendVocab(str, Enum):
    """
    Defines an open-vocabulary of trend values.
    """

    DECREASING = "Decreasing"
    INCREASING = "Increasing"


class TriggerFrequencyVocab(str, Enum):
    """
    Defines an open-vocabulary of the frequency types that a trigger may use.
    See also:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383620(v=vs.85).aspx
    and
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa383987(v=vs.85).aspx.
    """

    TASK_EVENT_TRIGGER_AT_LOGON = "TASK_EVENT_TRIGGER_AT_LOGON"
    TASK_EVENT_TRIGGER_AT_SYSTEMSTART = "TASK_EVENT_TRIGGER_AT_SYSTEMSTART"
    TASK_EVENT_TRIGGER_ON_IDLE = "TASK_EVENT_TRIGGER_ON_IDLE"
    TASK_TIME_TRIGGER_DAILY = "TASK_TIME_TRIGGER_DAILY"
    TASK_TIME_TRIGGER_MONTHLYDATE = "TASK_TIME_TRIGGER_MONTHLYDATE"
    TASK_TIME_TRIGGER_MONTHLYDOW = "TASK_TIME_TRIGGER_MONTHLYDOW"
    TASK_TIME_TRIGGER_ONCE = "TASK_TIME_TRIGGER_ONCE"
    TASK_TIME_TRIGGER_WEEKLY = "TASK_TIME_TRIGGER_WEEKLY"


class TriggerTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of the types of triggers associated with a task.
    """

    TASK_TRIGGER_BOOT = "TASK_TRIGGER_BOOT"
    TASK_TRIGGER_EVENT = "TASK_TRIGGER_EVENT"
    TASK_TRIGGER_IDLE = "TASK_TRIGGER_IDLE"
    TASK_TRIGGER_LOGON = "TASK_TRIGGER_LOGON"
    TASK_TRIGGER_REGISTRATION = "TASK_TRIGGER_REGISTRATION"
    TASK_TRIGGER_SESSION_STATE_CHANGE = "TASK_TRIGGER_SESSION_STATE_CHANGE"
    TASK_TRIGGER_TIME = "TASK_TRIGGER_TIME"


class URLTransitionTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of types of URL transitions.
    """

    LINK = "link"
    TYPED = "typed"
    AUTO_BOOKMARK = "auto_bookmark"
    AUTO_SUBFRAME = "auto_subframe"
    MANUAL_SUBFRAME = "manual_subframe"
    GENERATED = "generated"
    AUTO_TOPLEVEL = "auto_toplevel"
    FORM_SUBMIT = "form_submit"
    RELOAD = "reload"
    KEYWORD = "keyword"
    KEYWORD_GENERATED = "keyword_generated"


class UnixProcessStateVocab(str, Enum):
    """
    Defines an open-vocabulary of Unix process states
    """

    DEAD = "Dead"
    INTERRUPTIBLESLEEP = "InterruptibleSleep"
    PAGING = "Paging"
    RUNNING = "Running"
    STOPPED = "Stopped"
    UNINTERRUPTIBLESLEEP = "UninterruptibleSleep"
    ZOMBIE = "Zombie"


class WhoisContactTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of types of registrar contacts listed in a whois
    entry.
    """

    ADMIN = "ADMIN"
    BILLING = "BILLING"
    TECHNICAL = "TECHNICAL"


class WhoisDNSSECTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of acceptable values for the DNSSEC field in a
    Whois entry.
    """

    SIGNED = "Signed"
    UNSIGNED = "Unsigned"


class WhoisStatusTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of all valid statuses for a domain within a whois
    entry.
    """

    ADD_PERIOD = "ADD_PERIOD"
    AUTO_RENEW_PERIOD = "AUTO_RENEW_PERIOD"
    CLIENT_DELETE_PROHIBITED = "CLIENT_DELETE_PROHIBITED"
    CLIENT_HOLD = "CLIENT_HOLD"
    CLIENT_RENEW_PROHIBITED = "CLIENT_RENEW_PROHIBITED"
    CLIENT_TRANSFER_PROHIBITED = "CLIENT_TRANSFER_PROHIBITED"
    CLIENT_UPDATE_PROHIBITED = "CLIENT_UPDATE_PROHIBITED"
    DELETE_PROHIBITED = "DELETE_PROHIBITED"
    HOLD = "HOLD"
    INACTIVE = "INACTIVE"
    OK = "OK"
    PENDING_DELETE_RESTORABLE = "PENDING_DELETE_RESTORABLE"
    PENDING_DELETE_SCHEDULED_FOR_RELEASE = "PENDING_DELETE_SCHEDULED_FOR_RELEASE"
    PENDING_RESTORE = "PENDING_RESTORE"
    RENEW_PERIOD = "RENEW_PERIOD"
    RENEW_PROHIBITED = "RENEW_PROHIBITED"
    TRANSFER_PERIOD = "TRANSFER_PERIOD"
    TRANSFER_PROHIBITED = "TRANSFER_PROHIBITED"
    UPDATE_PROHIBITED = "UPDATE_PROHIBITED"


class WindowsDriveTypeVocab(str, Enum):
    """
    Defines an open-vocabulary of possible drive types, as enumerated by the
    WINAPI GetDriveType function:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa364939(v=vs.85).aspx.
    """

    DRIVE_CDROM = "DRIVE_CDROM"
    DRIVE_FIXED = "DRIVE_FIXED"
    DRIVE_NO_ROOT_DIR = "DRIVE_NO_ROOT_DIR"
    DRIVE_RAMDISK = "DRIVE_RAMDISK"
    DRIVE_REMOTE = "DRIVE_REMOTE"
    DRIVE_REMOVABLE = "DRIVE_REMOVABLE"
    DRIVE_UNKNOWN = "DRIVE_UNKNOWN"


class WindowsVolumeAttributeVocab(str, Enum):
    """
    Defines an open-vocabulary of attributes that may be returned by the
    diskpart attributes command:
    http://technet.microsoft.com/en-us/library/cc766465(v=ws.10).aspx.
    """

    HIDDEN = "Hidden"
    NODEFAULTDRIVELETTER = "NoDefaultDriveLetter"
    READONLY = "ReadOnly"
    SHADOWCOPY = "ShadowCopy"


class WirelessNetworkSecurityModeVocab(str, Enum):
    """
    Defines an open-vocabulary of security modes that may be configured for
    wireless network connections.
    """

    NONE = "None"
    WEP = "WEP"
    WPA = "WPA"
    WPA2_PSK = "WPA2-PSK"
    WPA2_ENTERPRISE = "WPA2-Enterprise"
    WPA3_PSK = "WPA3-PSK"
    WPA3_ENTERPRISE = "WPA3-Enterprise"
