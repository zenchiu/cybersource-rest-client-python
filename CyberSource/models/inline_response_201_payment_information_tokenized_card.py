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


class InlineResponse201PaymentInformationTokenizedCard(object):
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
        'prefix': 'str',
        'suffix': 'str',
        'type': 'str',
        'assurance_level': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'requestor_id': 'str'
    }

    attribute_map = {
        'prefix': 'prefix',
        'suffix': 'suffix',
        'type': 'type',
        'assurance_level': 'assuranceLevel',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'requestor_id': 'requestorId'
    }

    def __init__(self, prefix=None, suffix=None, type=None, assurance_level=None, expiration_month=None, expiration_year=None, requestor_id=None):
        """
        InlineResponse201PaymentInformationTokenizedCard - a model defined in Swagger
        """

        self._prefix = None
        self._suffix = None
        self._type = None
        self._assurance_level = None
        self._expiration_month = None
        self._expiration_year = None
        self._requestor_id = None

        if prefix is not None:
          self.prefix = prefix
        if suffix is not None:
          self.suffix = suffix
        if type is not None:
          self.type = type
        if assurance_level is not None:
          self.assurance_level = assurance_level
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if requestor_id is not None:
          self.requestor_id = requestor_id

    @property
    def prefix(self):
        """
        Gets the prefix of this InlineResponse201PaymentInformationTokenizedCard.
        First six digits of token. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction. 

        :return: The prefix of this InlineResponse201PaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this InlineResponse201PaymentInformationTokenizedCard.
        First six digits of token. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction. 

        :param prefix: The prefix of this InlineResponse201PaymentInformationTokenizedCard.
        :type: str
        """
        if prefix is not None and len(prefix) > 6:
            raise ValueError("Invalid value for `prefix`, length must be less than or equal to `6`")

        self._prefix = prefix

    @property
    def suffix(self):
        """
        Gets the suffix of this InlineResponse201PaymentInformationTokenizedCard.
        Last four digits of token. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction. 

        :return: The suffix of this InlineResponse201PaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this InlineResponse201PaymentInformationTokenizedCard.
        Last four digits of token. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction. 

        :param suffix: The suffix of this InlineResponse201PaymentInformationTokenizedCard.
        :type: str
        """
        if suffix is not None and len(suffix) > 4:
            raise ValueError("Invalid value for `suffix`, length must be less than or equal to `4`")

        self._suffix = suffix

    @property
    def type(self):
        """
        Gets the type of this InlineResponse201PaymentInformationTokenizedCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover 

        :return: The type of this InlineResponse201PaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InlineResponse201PaymentInformationTokenizedCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover 

        :param type: The type of this InlineResponse201PaymentInformationTokenizedCard.
        :type: str
        """
        if type is not None and len(type) > 3:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `3`")

        self._type = type

    @property
    def assurance_level(self):
        """
        Gets the assurance_level of this InlineResponse201PaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  `Note` This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :return: The assurance_level of this InlineResponse201PaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._assurance_level

    @assurance_level.setter
    def assurance_level(self, assurance_level):
        """
        Sets the assurance_level of this InlineResponse201PaymentInformationTokenizedCard.
        Confidence level of the tokenization. This value is assigned by the token service provider.  `Note` This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :param assurance_level: The assurance_level of this InlineResponse201PaymentInformationTokenizedCard.
        :type: str
        """
        if assurance_level is not None and len(assurance_level) > 2:
            raise ValueError("Invalid value for `assurance_level`, length must be less than or equal to `2`")

        self._assurance_level = assurance_level

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this InlineResponse201PaymentInformationTokenizedCard.
        Two-digit month in which the payment network token expires. `Format: MM`. Possible values: 01 through 12. 

        :return: The expiration_month of this InlineResponse201PaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this InlineResponse201PaymentInformationTokenizedCard.
        Two-digit month in which the payment network token expires. `Format: MM`. Possible values: 01 through 12. 

        :param expiration_month: The expiration_month of this InlineResponse201PaymentInformationTokenizedCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this InlineResponse201PaymentInformationTokenizedCard.
        Four-digit year in which the payment network token expires. `Format: YYYY`. 

        :return: The expiration_year of this InlineResponse201PaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this InlineResponse201PaymentInformationTokenizedCard.
        Four-digit year in which the payment network token expires. `Format: YYYY`. 

        :param expiration_year: The expiration_year of this InlineResponse201PaymentInformationTokenizedCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def requestor_id(self):
        """
        Gets the requestor_id of this InlineResponse201PaymentInformationTokenizedCard.
        Value that identifies your business and indicates that the cardholder’s account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider’s database.  `Note` This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :return: The requestor_id of this InlineResponse201PaymentInformationTokenizedCard.
        :rtype: str
        """
        return self._requestor_id

    @requestor_id.setter
    def requestor_id(self, requestor_id):
        """
        Sets the requestor_id of this InlineResponse201PaymentInformationTokenizedCard.
        Value that identifies your business and indicates that the cardholder’s account number is tokenized. This value is assigned by the token service provider and is unique within the token service provider’s database.  `Note` This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**. 

        :param requestor_id: The requestor_id of this InlineResponse201PaymentInformationTokenizedCard.
        :type: str
        """
        if requestor_id is not None and len(requestor_id) > 11:
            raise ValueError("Invalid value for `requestor_id`, length must be less than or equal to `11`")

        self._requestor_id = requestor_id

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
        if not isinstance(other, InlineResponse201PaymentInformationTokenizedCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
