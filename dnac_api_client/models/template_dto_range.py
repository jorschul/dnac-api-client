# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TemplateDTORange(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'min_value': 'int',
        'max_value': 'int',
        'id': 'str'
    }

    attribute_map = {
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'id': 'id'
    }

    def __init__(self, min_value=None, max_value=None, id=None):  # noqa: E501
        """TemplateDTORange - a model defined in OpenAPI"""  # noqa: E501

        self._min_value = None
        self._max_value = None
        self._id = None
        self.discriminator = None

        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if id is not None:
            self.id = id

    @property
    def min_value(self):
        """Gets the min_value of this TemplateDTORange.  # noqa: E501


        :return: The min_value of this TemplateDTORange.  # noqa: E501
        :rtype: int
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this TemplateDTORange.


        :param min_value: The min_value of this TemplateDTORange.  # noqa: E501
        :type: int
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this TemplateDTORange.  # noqa: E501


        :return: The max_value of this TemplateDTORange.  # noqa: E501
        :rtype: int
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this TemplateDTORange.


        :param max_value: The max_value of this TemplateDTORange.  # noqa: E501
        :type: int
        """

        self._max_value = max_value

    @property
    def id(self):
        """Gets the id of this TemplateDTORange.  # noqa: E501


        :return: The id of this TemplateDTORange.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateDTORange.


        :param id: The id of this TemplateDTORange.  # noqa: E501
        :type: str
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplateDTORange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
