"""
Auto-generated classes from the .tkape files for the Compound category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class MessagingClientsIRCClients0(KapeTarget):
    name: ClassVar[str] = "IRC Clients"
    base_path: ClassVar[Path] = Path("IRCClients.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsCiscoJabber1(KapeTarget):
    name: ClassVar[str] = "Cisco Jabber"
    base_path: ClassVar[Path] = Path("CiscoJabber.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsDiscord2(KapeTarget):
    name: ClassVar[str] = "Discord"
    base_path: ClassVar[Path] = Path("Discord.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsMattermost3(KapeTarget):
    name: ClassVar[str] = "Mattermost"
    base_path: ClassVar[Path] = Path("Mattermost.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsMicrosoftTeams4(KapeTarget):
    name: ClassVar[str] = "Microsoft Teams"
    base_path: ClassVar[Path] = Path("MicrosoftTeams.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsSignal5(KapeTarget):
    name: ClassVar[str] = "Signal"
    base_path: ClassVar[Path] = Path("Signal.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsSkype6(KapeTarget):
    name: ClassVar[str] = "Skype"
    base_path: ClassVar[Path] = Path("Skype.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsSlack7(KapeTarget):
    name: ClassVar[str] = "Slack"
    base_path: ClassVar[Path] = Path("Slack.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsTelegram8(KapeTarget):
    name: ClassVar[str] = "Telegram"
    base_path: ClassVar[Path] = Path("Telegram.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsViber9(KapeTarget):
    name: ClassVar[str] = "Viber"
    base_path: ClassVar[Path] = Path("Viber.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClientsWhatsApp10(KapeTarget):
    name: ClassVar[str] = "WhatsApp"
    base_path: ClassVar[Path] = Path("WhatsApp.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MessagingClients(KapeTargetConfiguration):
    """
    Author: Gregor Wegberg

    Version: 1.0

    ID: c6d3b238-0be7-4764-afa7-9224e46097c0

    Messaging and communication apps
    """

    name: ClassVar[str] = "MessagingClients"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MessagingClientsIRCClients0,
        MessagingClientsCiscoJabber1,
        MessagingClientsDiscord2,
        MessagingClientsMattermost3,
        MessagingClientsMicrosoftTeams4,
        MessagingClientsSignal5,
        MessagingClientsSkype6,
        MessagingClientsSlack7,
        MessagingClientsTelegram8,
        MessagingClientsViber9,
        MessagingClientsWhatsApp10,
    ]


class ServerTriageWebServers0(KapeTarget):
    name: ClassVar[str] = "WebServers"
    base_path: ClassVar[Path] = Path("WebServers.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ServerTriageExchange1(KapeTarget):
    name: ClassVar[str] = "Exchange"
    base_path: ClassVar[Path] = Path("Exchange.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ServerTriageConfluence2(KapeTarget):
    name: ClassVar[str] = "Confluence"
    base_path: ClassVar[Path] = Path("ConfluenceLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ServerTriageFileZillaServer3(KapeTarget):
    name: ClassVar[str] = "FileZilla Server"
    base_path: ClassVar[Path] = Path("FileZillaServer.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ServerTriageOpenSSHServer4(KapeTarget):
    name: ClassVar[str] = "OpenSSH Server"
    base_path: ClassVar[Path] = Path("OpenSSHServer.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ServerTriageManageEngine5(KapeTarget):
    name: ClassVar[str] = "ManageEngine"
    base_path: ClassVar[Path] = Path("ManageEngineLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ServerTriage(KapeTargetConfiguration):
    """
    Author: Eric Capuano

    Version: 1.0

    ID: 9bea625c-00bd-4389-a0a5-f648e8e267ce

    A compound target for gathering artifacts common to servers.
    """

    name: ClassVar[str] = "ServerTriage"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ServerTriageWebServers0,
        ServerTriageExchange1,
        ServerTriageConfluence2,
        ServerTriageFileZillaServer3,
        ServerTriageOpenSSHServer4,
        ServerTriageManageEngine5,
    ]
