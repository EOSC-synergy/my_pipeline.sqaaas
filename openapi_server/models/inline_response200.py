# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_name: str=None, content: Dict[str, object]=None):
        """InlineResponse200 - a model defined in OpenAPI

        :param file_name: The file_name of this InlineResponse200.
        :param content: The content of this InlineResponse200.
        """
        self.openapi_types = {
            'file_name': str,
            'content': Dict[str, object]
        }

        self.attribute_map = {
            'file_name': 'file_name',
            'content': 'content'
        }

        self._file_name = file_name
        self._content = content

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inline_response_200 of this InlineResponse200.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_name(self):
        """Gets the file_name of this InlineResponse200.


        :return: The file_name of this InlineResponse200.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this InlineResponse200.


        :param file_name: The file_name of this InlineResponse200.
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def content(self):
        """Gets the content of this InlineResponse200.


        :return: The content of this InlineResponse200.
        :rtype: Dict[str, object]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InlineResponse200.


        :param content: The content of this InlineResponse200.
        :type content: Dict[str, object]
        """

        self._content = content