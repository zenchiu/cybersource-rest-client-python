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


class Ptsv2paymentsidcapturesOrderInformationShipTo(object):
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
        'administrative_area': 'str',
        'country': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'administrative_area': 'administrativeArea',
        'country': 'country',
        'postal_code': 'postalCode'
    }

    def __init__(self, administrative_area=None, country=None, postal_code=None):
        """
        Ptsv2paymentsidcapturesOrderInformationShipTo - a model defined in Swagger
        """

        self._administrative_area = None
        self._country = None
        self._postal_code = None

        if administrative_area is not None:
          self.administrative_area = administrative_area
        if country is not None:
          self.country = country
        if postal_code is not None:
          self.postal_code = postal_code

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        State or province of the shipping address. Use the State, Province, and Territory Codes for the United States and Canada. 

        :return: The administrative_area of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        State or province of the shipping address. Use the State, Province, and Territory Codes for the United States and Canada. 

        :param administrative_area: The administrative_area of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 2:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `2`")

        self._administrative_area = administrative_area

    @property
    def country(self):
        """
        Gets the country of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        Country of the shipping address. Use the two character ISO Standard Country Codes.

        :return: The country of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        Country of the shipping address. Use the two character ISO Standard Country Codes.

        :param country: The country of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        :type: str
        """
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")

        self._country = country

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        Postal code for the shipping address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  **American Express Direct**\\ Before sending the postal code to the processor, CyberSource removes all nonalphanumeric characters and, if the remaining value is longer than nine characters, truncates the value starting from the right side. 

        :return: The postal_code of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        Postal code for the shipping address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  **American Express Direct**\\ Before sending the postal code to the processor, CyberSource removes all nonalphanumeric characters and, if the remaining value is longer than nine characters, truncates the value starting from the right side. 

        :param postal_code: The postal_code of this Ptsv2paymentsidcapturesOrderInformationShipTo.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 10:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `10`")

        self._postal_code = postal_code

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
        if not isinstance(other, Ptsv2paymentsidcapturesOrderInformationShipTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
