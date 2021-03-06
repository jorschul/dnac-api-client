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


class SAVAMappingSyncResultSyncList(object):
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
        'device_sn_list': 'list[str]',
        'sync_type': 'str'
    }

    attribute_map = {
        'device_sn_list': 'deviceSnList',
        'sync_type': 'syncType'
    }

    def __init__(self, device_sn_list=None, sync_type=None):  # noqa: E501
        """SAVAMappingSyncResultSyncList - a model defined in OpenAPI"""  # noqa: E501

        self._device_sn_list = None
        self._sync_type = None
        self.discriminator = None

        if device_sn_list is not None:
            self.device_sn_list = device_sn_list
        if sync_type is not None:
            self.sync_type = sync_type

    @property
    def device_sn_list(self):
        """Gets the device_sn_list of this SAVAMappingSyncResultSyncList.  # noqa: E501


        :return: The device_sn_list of this SAVAMappingSyncResultSyncList.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_sn_list

    @device_sn_list.setter
    def device_sn_list(self, device_sn_list):
        """Sets the device_sn_list of this SAVAMappingSyncResultSyncList.


        :param device_sn_list: The device_sn_list of this SAVAMappingSyncResultSyncList.  # noqa: E501
        :type: list[str]
        """

        self._device_sn_list = device_sn_list

    @property
    def sync_type(self):
        """Gets the sync_type of this SAVAMappingSyncResultSyncList.  # noqa: E501


        :return: The sync_type of this SAVAMappingSyncResultSyncList.  # noqa: E501
        :rtype: str
        """
        return self._sync_type

    @sync_type.setter
    def sync_type(self, sync_type):
        """Sets the sync_type of this SAVAMappingSyncResultSyncList.


        :param sync_type: The sync_type of this SAVAMappingSyncResultSyncList.  # noqa: E501
        :type: str
        """
        allowed_values = ["Add", "Update", "Delete", "MismatchError"]  # noqa: E501
        if sync_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sync_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sync_type, allowed_values)
            )

        self._sync_type = sync_type

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
        if not isinstance(other, SAVAMappingSyncResultSyncList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
