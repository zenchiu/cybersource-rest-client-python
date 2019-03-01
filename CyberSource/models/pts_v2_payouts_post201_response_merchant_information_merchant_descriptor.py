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


class PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor(object):
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
        'name': 'str',
        'locality': 'str',
        'country': 'str'
    }

    attribute_map = {
        'name': 'name',
        'locality': 'locality',
        'country': 'country'
    }

    def __init__(self, name=None, locality=None, country=None):
        """
        PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor - a model defined in Swagger
        """

        self._name = None
        self._locality = None
        self._country = None

        if name is not None:
          self.name = name
        if locality is not None:
          self.locality = locality
        if country is not None:
          self.country = country

    @property
    def name(self):
        """
        Gets the name of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see Merchant Descriptors in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  For Payouts: * Paymentech (22) 

        :return: The name of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see Merchant Descriptors in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  For Payouts: * Paymentech (22) 

        :param name: The name of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._name = name

    @property
    def locality(self):
        """
        Gets the locality of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        Merchant City. For the descriptions, used-by information, data types, and lengths for these fields, see Merchant Descriptors in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The locality of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        Merchant City. For the descriptions, used-by information, data types, and lengths for these fields, see Merchant Descriptors in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param locality: The locality of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        :type: str
        """
        if locality is not None and len(locality) > 13:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `13`")

        self._locality = locality

    @property
    def country(self):
        """
        Gets the country of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see Merchant Descriptors in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The country of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see Merchant Descriptors in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param country: The country of this PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor.
        :type: str
        """
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")

        self._country = country

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
        if not isinstance(other, PtsV2PayoutsPost201ResponseMerchantInformationMerchantDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
