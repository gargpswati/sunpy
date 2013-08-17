# Author: Simon Liedtke <liedtke.simon@googlemail.com>
#
# This module was developed with funding provided by
# the Google Summer of Code (2013).

"""
Overview
--------
The database package exports the following classes and exceptions:

    :classes:
        - Database
    :exceptions:
        - EntryAlreadyAddedError
        - NoSuchEntryError
        - EntryAlreadyStarredError
        - EntryAlreadyUnstarredError
        - EntryNotFoundError
        - TagAlreadyAssignedError
        - NoSuchTagError
        - NonRemovableTagError
"""
from __future__ import absolute_import

from sunpy.database.database import Database, EntryAlreadyAddedError,\
    EntryAlreadyStarredError, EntryAlreadyUnstarredError, NoSuchTagError,\
    EntryNotFoundError, TagAlreadyAssignedError
from sunpy.database.commands import NoSuchEntryError, NonRemovableTagError

__all__ = [
    'Database', 'EntryAlreadyAddedError', 'NoSuchEntryError', 'NoSuchTagError',
    'NonRemovableTagError', 'EntryAlreadyStarredError',
    'EntryAlreadyUnstarredError', 'EntryNotFoundError',
    'TagAlreadyAssignedError']
