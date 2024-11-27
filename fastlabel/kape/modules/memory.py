"""
Auto-generated classes from the .mkape files for the Memory category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class DumpItMemory(KapeModule):
    """
    Author: Doug Metz

    Version: 1.1

    ID: 7504551a-41b6-4287-ad8a-ee0a10a66f7d

    DumpIt Memory Acquisition
    """

    name: ClassVar[str] = "DumpIt_Memory"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.DMP]


class MagnetForensicsRAMCapture(KapeModule):
    """
    Author: Doug Metz

    Version: 1.1

    ID: 23a35c17-15a8-4d7e-9029-083bc70bd4ef

    Magnet RAM Capture Memory Acquisition
    """

    name: ClassVar[str] = "MagnetForensics_RAMCapture"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.RAW]


class VelocidexWinPmem(KapeModule):
    """
    Author: Eric Capuano

    Version: 3.0

    ID: 1d284835-417b-459e-a396-d228edea3808

    WinPmem Memory Dump
    """

    name: ClassVar[str] = "Velocidex_WinPmem"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.RAW]


class Volatilityamcache(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: df9c3a2d-bea4-4a86-808e-08bbe712fcb1

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_amcache"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityclipboard(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 3d64e6ad-e574-49e7-b227-6ae787e871ae

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_clipboard"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitycmdline(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: a22fbcf0-c0d3-40b1-8df7-26169c265e58

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_cmdline"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitycmdscan(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: e6bffba9-e023-48e3-9355-997175da0d37

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_cmdscan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityconnections(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 5620ba3d-7d23-4670-b765-be00cdf11274

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_connections"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityconnscan(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: da81007a-5a63-4fa8-aa74-f958893d1a83

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_connscan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityconsoles(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: cdc796f3-6627-496c-9636-d51db65f636c

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_consoles"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitydlllist(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: d311a46f-113d-4274-81e2-c4f536f85bfa

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_dlllist"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitydriverirp(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 65418efa-cae6-40c0-8e9c-a15ac32e5a8a

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_driverirp"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityhollowfind(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 2d966a97-a950-48b1-8219-e784ffb3a552

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_hollowfind"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityidt(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: efc76bc6-2c27-492f-be24-fb532bf20d10

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_idt"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitymalfind(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 5afeec46-890c-4510-8a95-f36c7ddf2fde

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_malfind"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitymodscan(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 62658f4a-9ca1-498d-81b8-85f61e18e8ab

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_modscan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitymodules(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: e68cd71f-074f-470d-a7ce-8196bdd21ee4

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_modules"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitynetscan(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: dfa01514-aaba-41f3-a60c-74a3d2952bf7

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_netscan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitynotepad(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: abdb5baa-9693-4742-9444-7bd6f7f08942

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_notepad"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitypslist(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: de03554f-fe9f-4bd6-ac3b-8920be4ff609

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_pslist"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitypsscan(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 6485072f-9ba9-4538-b713-d5dcf93ffdf9

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_psscan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitypstree(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 750ea28d-1b96-4cd2-8399-eee4245eb6be

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_pstree"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitypsxview(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 0e25fb2e-a197-4c2f-a839-6b2128a4ef2b

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_psxview"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityshimcache(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: ca3f78e2-98b1-4099-8b00-0912e64ce616

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_shimcache"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitysockets(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 5b5a957d-8c2d-4790-ad19-d6101903f8de

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_sockets"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilitysockscan(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 3915788a-4513-4951-ac3d-02daaf6a46a9

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_sockscan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityssdt(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: b4c02e2f-5223-4c3a-9f8a-9022e40ae1d5

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_ssdt"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityuserassist(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: bbcd1c2c-6802-4b1d-8c35-2856f8ce3bb6

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_userassist"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]


class Volatilityuserhandles(KapeModule):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: 65ddfd53-f445-49a5-bc58-82e85f6c2cfb

    Post-Process memory images with Volatility
    """

    name: ClassVar[str] = "Volatility_userhandles"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.GREPTEXT]
