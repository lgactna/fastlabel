"""
Auto-generated classes from the .tkape files for the Text Editor category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class NotepadNotepadUnsavedEdits0(KapeTarget):
    """
    Locates non-saved Notepad++ files and copies them.
    """

    name: ClassVar[str] = "Notepad++ Unsaved Edits"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Notepad++\\backup\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NotepadNotepadConfig1(KapeTarget):
    """
    Retrieves config.xml which contains recently searched terms, replaced terms
    and recently opened documents
    """

    name: ClassVar[str] = "Notepad++ Config"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Notepad++\\")
    file_mask: ClassVar[str] = "config.xml"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NotepadNotepadSession2(KapeTarget):
    """
    Retrieves session.xml which contains session date
    """

    name: ClassVar[str] = "Notepad++ Session"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Notepad++\\")
    file_mask: ClassVar[str] = "session.xml"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Notepad(KapeTargetConfiguration):
    """
    Author: Banaanhangwagen and Matt Dawson

    Version: 2.0

    ID: dc6c1009-2d0a-4ead-99f0-d1f3a5380751

    Notepad++ Backups, recently searched/replaced terms and recently opened
    documents
    """

    name: ClassVar[str] = "Notepad++"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        NotepadNotepadUnsavedEdits0,
        NotepadNotepadConfig1,
        NotepadNotepadSession2,
    ]


class SublimeTextSublimeText23AutoSaveSession0(KapeTarget):
    """
    Sublime Text 2/3 stores unsaved (temporary) files and its content in its
    Session.sublime_session file
    """

    name: ClassVar[str] = "SublimeText 2/3 Auto Save Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Sublime Text*\\Settings"
    )
    file_mask: ClassVar[str] = "Session.sublime_session"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SublimeText(KapeTargetConfiguration):
    """
    Author: Mathias Frank

    Version: 1.0

    ID: c1a64d12-bdf3-4ebe-a715-719bd6f2ddad

    Sublime Text 2/3 Auto Save Session
    """

    name: ClassVar[str] = "SublimeText"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SublimeTextSublimeText23AutoSaveSession0
    ]
