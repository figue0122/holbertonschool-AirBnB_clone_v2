#!/usr/bin/python3
"""
This module initializes the appropriate storage engine
based on the environment variable HBNB_TYPE_STORAGE.
"""

import os

# Determine the storage type from the environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    # If storage type is 'db', use the DBStorage engine
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    # Default to FileStorage if the storage type is not 'db'
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage to either populate from the database or from the JSON file
storage.reload()
