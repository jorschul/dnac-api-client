# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TaskDTOListResponseResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'additional_status_url': 'str',
        'data': 'str',
        'end_time': 'str',
        'error_code': 'str',
        'error_key': 'str',
        'failure_reason': 'str',
        'id': 'str',
        'instance_tenant_id': 'str',
        'is_error': 'bool',
        'last_update': 'str',
        'operation_id_list': 'object',
        'parent_id': 'str',
        'progress': 'str',
        'root_id': 'str',
        'service_type': 'str',
        'start_time': 'str',
        'username': 'str',
        'version': 'int'
    }

    attribute_map = {
        'additional_status_url': 'additionalStatusURL',
        'data': 'data',
        'end_time': 'endTime',
        'error_code': 'errorCode',
        'error_key': 'errorKey',
        'failure_reason': 'failureReason',
        'id': 'id',
        'instance_tenant_id': 'instanceTenantId',
        'is_error': 'isError',
        'last_update': 'lastUpdate',
        'operation_id_list': 'operationIdList',
        'parent_id': 'parentId',
        'progress': 'progress',
        'root_id': 'rootId',
        'service_type': 'serviceType',
        'start_time': 'startTime',
        'username': 'username',
        'version': 'version'
    }

    def __init__(self, additional_status_url=None, data=None, end_time=None, error_code=None, error_key=None, failure_reason=None, id=None, instance_tenant_id=None, is_error=None, last_update=None, operation_id_list=None, parent_id=None, progress=None, root_id=None, service_type=None, start_time=None, username=None, version=None):  # noqa: E501
        """TaskDTOListResponseResponse - a model defined in Swagger"""  # noqa: E501

        self._additional_status_url = None
        self._data = None
        self._end_time = None
        self._error_code = None
        self._error_key = None
        self._failure_reason = None
        self._id = None
        self._instance_tenant_id = None
        self._is_error = None
        self._last_update = None
        self._operation_id_list = None
        self._parent_id = None
        self._progress = None
        self._root_id = None
        self._service_type = None
        self._start_time = None
        self._username = None
        self._version = None
        self.discriminator = None

        if additional_status_url is not None:
            self.additional_status_url = additional_status_url
        if data is not None:
            self.data = data
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if error_key is not None:
            self.error_key = error_key
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if id is not None:
            self.id = id
        if instance_tenant_id is not None:
            self.instance_tenant_id = instance_tenant_id
        if is_error is not None:
            self.is_error = is_error
        if last_update is not None:
            self.last_update = last_update
        if operation_id_list is not None:
            self.operation_id_list = operation_id_list
        if parent_id is not None:
            self.parent_id = parent_id
        if progress is not None:
            self.progress = progress
        if root_id is not None:
            self.root_id = root_id
        if service_type is not None:
            self.service_type = service_type
        if start_time is not None:
            self.start_time = start_time
        if username is not None:
            self.username = username
        if version is not None:
            self.version = version

    @property
    def additional_status_url(self):
        """Gets the additional_status_url of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The additional_status_url of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._additional_status_url

    @additional_status_url.setter
    def additional_status_url(self, additional_status_url):
        """Sets the additional_status_url of this TaskDTOListResponseResponse.


        :param additional_status_url: The additional_status_url of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._additional_status_url = additional_status_url

    @property
    def data(self):
        """Gets the data of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The data of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskDTOListResponseResponse.


        :param data: The data of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def end_time(self):
        """Gets the end_time of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The end_time of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskDTOListResponseResponse.


        :param end_time: The end_time of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def error_code(self):
        """Gets the error_code of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The error_code of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this TaskDTOListResponseResponse.


        :param error_code: The error_code of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_key(self):
        """Gets the error_key of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The error_key of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_key

    @error_key.setter
    def error_key(self, error_key):
        """Sets the error_key of this TaskDTOListResponseResponse.


        :param error_key: The error_key of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._error_key = error_key

    @property
    def failure_reason(self):
        """Gets the failure_reason of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The failure_reason of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this TaskDTOListResponseResponse.


        :param failure_reason: The failure_reason of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def id(self):
        """Gets the id of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The id of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskDTOListResponseResponse.


        :param id: The id of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instance_tenant_id(self):
        """Gets the instance_tenant_id of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The instance_tenant_id of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_tenant_id

    @instance_tenant_id.setter
    def instance_tenant_id(self, instance_tenant_id):
        """Sets the instance_tenant_id of this TaskDTOListResponseResponse.


        :param instance_tenant_id: The instance_tenant_id of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._instance_tenant_id = instance_tenant_id

    @property
    def is_error(self):
        """Gets the is_error of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The is_error of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        """Sets the is_error of this TaskDTOListResponseResponse.


        :param is_error: The is_error of this TaskDTOListResponseResponse.  # noqa: E501
        :type: bool
        """

        self._is_error = is_error

    @property
    def last_update(self):
        """Gets the last_update of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The last_update of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this TaskDTOListResponseResponse.


        :param last_update: The last_update of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def operation_id_list(self):
        """Gets the operation_id_list of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The operation_id_list of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: object
        """
        return self._operation_id_list

    @operation_id_list.setter
    def operation_id_list(self, operation_id_list):
        """Sets the operation_id_list of this TaskDTOListResponseResponse.


        :param operation_id_list: The operation_id_list of this TaskDTOListResponseResponse.  # noqa: E501
        :type: object
        """

        self._operation_id_list = operation_id_list

    @property
    def parent_id(self):
        """Gets the parent_id of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The parent_id of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this TaskDTOListResponseResponse.


        :param parent_id: The parent_id of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def progress(self):
        """Gets the progress of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The progress of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this TaskDTOListResponseResponse.


        :param progress: The progress of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._progress = progress

    @property
    def root_id(self):
        """Gets the root_id of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The root_id of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this TaskDTOListResponseResponse.


        :param root_id: The root_id of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._root_id = root_id

    @property
    def service_type(self):
        """Gets the service_type of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The service_type of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this TaskDTOListResponseResponse.


        :param service_type: The service_type of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def start_time(self):
        """Gets the start_time of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The start_time of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskDTOListResponseResponse.


        :param start_time: The start_time of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def username(self):
        """Gets the username of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The username of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TaskDTOListResponseResponse.


        :param username: The username of this TaskDTOListResponseResponse.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def version(self):
        """Gets the version of this TaskDTOListResponseResponse.  # noqa: E501


        :return: The version of this TaskDTOListResponseResponse.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TaskDTOListResponseResponse.


        :param version: The version of this TaskDTOListResponseResponse.  # noqa: E501
        :type: int
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, TaskDTOListResponseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other