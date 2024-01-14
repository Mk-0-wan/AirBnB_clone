"""
Create a FileStorages object and reload all object from
the json file
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
