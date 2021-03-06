# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class GalleryImage(Model):
    """A gallery image.

    :param author: The author of the gallery image.
    :type author: str
    :param created_date: The creation date of the gallery image.
    :type created_date: datetime
    :param description: The description of the gallery image.
    :type description: str
    :param image_reference: The image reference of the gallery image.
    :type image_reference: :class:`GalleryImageReference
     <azure.mgmt.devtestlabs.models.GalleryImageReference>`
    :param icon: The icon of the gallery image.
    :type icon: str
    :param enabled: Indicates whether this gallery image is enabled.
    :type enabled: bool
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    """

    _attribute_map = {
        'author': {'key': 'properties.author', 'type': 'str'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'image_reference': {'key': 'properties.imageReference', 'type': 'GalleryImageReference'},
        'icon': {'key': 'properties.icon', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, author=None, created_date=None, description=None, image_reference=None, icon=None, enabled=None, id=None, name=None, type=None, location=None, tags=None):
        self.author = author
        self.created_date = created_date
        self.description = description
        self.image_reference = image_reference
        self.icon = icon
        self.enabled = enabled
        self.id = id
        self.name = name
        self.type = type
        self.location = location
        self.tags = tags
