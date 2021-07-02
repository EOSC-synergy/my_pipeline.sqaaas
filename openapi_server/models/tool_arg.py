# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ToolArg(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, description: str=None, value: object=None, option: str=None, summary: str=None, format: str=None, selectable: bool=True, repeatable: bool=False, args: List['ToolArg']=None):
        """ToolArg - a model defined in OpenAPI

        :param type: The type of this ToolArg.
        :param description: The description of this ToolArg.
        :param value: The value of this ToolArg.
        :param option: The option of this ToolArg.
        :param summary: The summary of this ToolArg.
        :param format: The format of this ToolArg.
        :param selectable: The selectable of this ToolArg.
        :param repeatable: The repeatable of this ToolArg.
        :param args: The args of this ToolArg.
        """
        self.openapi_types = {
            'type': str,
            'description': str,
            'value': object,
            'option': str,
            'summary': str,
            'format': str,
            'selectable': bool,
            'repeatable': bool,
            'args': List[ToolArg]
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'value': 'value',
            'option': 'option',
            'summary': 'summary',
            'format': 'format',
            'selectable': 'selectable',
            'repeatable': 'repeatable',
            'args': 'args'
        }

        self._type = type
        self._description = description
        self._value = value
        self._option = option
        self._summary = summary
        self._format = format
        self._selectable = selectable
        self._repeatable = repeatable
        self._args = args

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ToolArg':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ToolArg of this ToolArg.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this ToolArg.

        type of argument

        :return: The type of this ToolArg.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ToolArg.

        type of argument

        :param type: The type of this ToolArg.
        :type type: str
        """
        allowed_values = ["subcommand", "positional", "optional"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self):
        """Gets the description of this ToolArg.

        hint about what the command does

        :return: The description of this ToolArg.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ToolArg.

        hint about what the command does

        :param description: The description of this ToolArg.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def value(self):
        """Gets the value of this ToolArg.

        Value for the argument (can be of any type)

        :return: The value of this ToolArg.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ToolArg.

        Value for the argument (can be of any type)

        :param value: The value of this ToolArg.
        :type value: object
        """

        self._value = value

    @property
    def option(self):
        """Gets the option of this ToolArg.

        Name of the option, in the event of optional arguments

        :return: The option of this ToolArg.
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this ToolArg.

        Name of the option, in the event of optional arguments

        :param option: The option of this ToolArg.
        :type option: str
        """

        self._option = option

    @property
    def summary(self):
        """Gets the summary of this ToolArg.

        very brief (2/3 words) description (to be rendered by web clients)

        :return: The summary of this ToolArg.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ToolArg.

        very brief (2/3 words) description (to be rendered by web clients)

        :param summary: The summary of this ToolArg.
        :type summary: str
        """

        self._summary = summary

    @property
    def format(self):
        """Gets the format of this ToolArg.

        The value format (to be rendered by web clients)

        :return: The format of this ToolArg.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ToolArg.

        The value format (to be rendered by web clients)

        :param format: The format of this ToolArg.
        :type format: str
        """
        allowed_values = ["string", "array"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def selectable(self):
        """Gets the selectable of this ToolArg.

        Whether the argument can be selected by the user (to be rendered by web clients)

        :return: The selectable of this ToolArg.
        :rtype: bool
        """
        return self._selectable

    @selectable.setter
    def selectable(self, selectable):
        """Sets the selectable of this ToolArg.

        Whether the argument can be selected by the user (to be rendered by web clients)

        :param selectable: The selectable of this ToolArg.
        :type selectable: bool
        """

        self._selectable = selectable

    @property
    def repeatable(self):
        """Gets the repeatable of this ToolArg.

        Whether the argument can be repeated (to be rendered by web clients)

        :return: The repeatable of this ToolArg.
        :rtype: bool
        """
        return self._repeatable

    @repeatable.setter
    def repeatable(self, repeatable):
        """Sets the repeatable of this ToolArg.

        Whether the argument can be repeated (to be rendered by web clients)

        :param repeatable: The repeatable of this ToolArg.
        :type repeatable: bool
        """

        self._repeatable = repeatable

    @property
    def args(self):
        """Gets the args of this ToolArg.


        :return: The args of this ToolArg.
        :rtype: List[ToolArg]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ToolArg.


        :param args: The args of this ToolArg.
        :type args: List[ToolArg]
        """

        self._args = args
