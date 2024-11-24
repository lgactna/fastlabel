"""
Auto-generated classes from the SHACL graph in types.ttl.

This file was generated using the `case_models.py` script.
"""

from enum import Enum
from typing import Any, Optional

from fastlabel.case import co, core


class DictionaryEntry(core.UcoInherentCharacterizationThing):
    """
    A dictionary entry is a single (term/key, value) pair.
    """

    key: str
    value: str


class Hash(core.UcoInherentCharacterizationThing):
    """
    A hash is a grouping of characteristics unique to the result of applying a
    mathematical algorithm that maps data of arbitrary size to a bit string (the
    'hash') and is a one-way function, that is, a function which is practically
    infeasible to invert. This is commonly used for integrity checking of data.
    [based on https://en.wikipedia.org/wiki/Cryptographic_hash_function]
    """

    hashValue: str
    hashMethod: Optional[str] = None
    hashMethod: Any
    hashMethod: Optional[Any] = None


class ThreadItem(co.Item):
    """
    A ThreadItem is a member of a thread.
    """

    itemContent: Optional[core.UcoObject] = None


class ControlledDictionaryEntry(DictionaryEntry):
    """
    A controlled dictionary entry is a single (term/key, value) pair where the
    term/key is constrained to an explicitly defined set of values.
    """

    pass


class Dictionary(core.UcoInherentCharacterizationThing):
    """
    A dictionary is list of (term/key, value) pairs with each term/key having an
    expectation to exist no more than once. types:Dictionary alone does not
    validate this expectation, but validation is available. For use cases where
    this expectation must be validated, the subclass types:ProperDictionary
    should be used instead of types:Dictionary. For instances where this
    expectation has been found to be violated, the subclass
    types:ImproperDictionary should be used instead of types:Dictionary.
    """

    entry: Optional[DictionaryEntry] = None


class Thread(co.Bag):
    """
    A semi-ordered array of items, that can be present in multiple copies.
    Implemetation of a UCO Thread is similar to a Collections Ontology List,
    except a Thread may fork and merge - that is, one of its members may have
    two or more direct successors, and two or more direct predecessors.
    """

    item: Optional[ThreadItem] = None


class ControlledDictionary(Dictionary):
    """
    A controlled dictionary is a list of (term/key, value) pairs where each
    term/key exists no more than once and is constrained to an explicitly
    defined set of values.
    """

    entry: Optional[ControlledDictionaryEntry] = None


class ImproperDictionary(Dictionary):

    repeatsKey: Optional[str] = None


class ProperDictionary(Dictionary):
    """
    A proper dictionary is list of (term/key, value) pairs with each term/key
    existing no more than once.
    """

    pass
