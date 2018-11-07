# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse4007(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'code': 'str',
        'message': 'str',
        'localization_key': 'str',
        'correlation_id': 'str',
        'detail': 'str',
        'fields': 'list[InlineResponse4007Fields]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'localization_key': 'localizationKey',
        'correlation_id': 'correlationId',
        'detail': 'detail',
        'fields': 'fields'
    }

    def __init__(self, code=None, message=None, localization_key=None, correlation_id=None, detail=None, fields=None):
        """
        InlineResponse4007 - a model defined in Swagger
        """

        self._code = None
        self._message = None
        self._localization_key = None
        self._correlation_id = None
        self._detail = None
        self._fields = None

        self.code = code
        self.message = message
        if localization_key is not None:
          self.localization_key = localization_key
        if correlation_id is not None:
          self.correlation_id = correlation_id
        if detail is not None:
          self.detail = detail
        if fields is not None:
          self.fields = fields

    @property
    def code(self):
        """
        Gets the code of this InlineResponse4007.
        Error code

        :return: The code of this InlineResponse4007.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this InlineResponse4007.
        Error code

        :param code: The code of this InlineResponse4007.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this InlineResponse4007.
        Error message

        :return: The message of this InlineResponse4007.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponse4007.
        Error message

        :param message: The message of this InlineResponse4007.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def localization_key(self):
        """
        Gets the localization_key of this InlineResponse4007.
        Localization Key Name

        :return: The localization_key of this InlineResponse4007.
        :rtype: str
        """
        return self._localization_key

    @localization_key.setter
    def localization_key(self, localization_key):
        """
        Sets the localization_key of this InlineResponse4007.
        Localization Key Name

        :param localization_key: The localization_key of this InlineResponse4007.
        :type: str
        """

        self._localization_key = localization_key

    @property
    def correlation_id(self):
        """
        Gets the correlation_id of this InlineResponse4007.
        Correlation Id

        :return: The correlation_id of this InlineResponse4007.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """
        Sets the correlation_id of this InlineResponse4007.
        Correlation Id

        :param correlation_id: The correlation_id of this InlineResponse4007.
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def detail(self):
        """
        Gets the detail of this InlineResponse4007.
        Error Detail

        :return: The detail of this InlineResponse4007.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """
        Sets the detail of this InlineResponse4007.
        Error Detail

        :param detail: The detail of this InlineResponse4007.
        :type: str
        """

        self._detail = detail

    @property
    def fields(self):
        """
        Gets the fields of this InlineResponse4007.
        Error fields List

        :return: The fields of this InlineResponse4007.
        :rtype: list[InlineResponse4007Fields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this InlineResponse4007.
        Error fields List

        :param fields: The fields of this InlineResponse4007.
        :type: list[InlineResponse4007Fields]
        """

        self._fields = fields

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse4007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
