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


class Tmsv1paymentinstrumentsBillTo(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'company': 'str',
        'address1': 'str',
        'address2': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'country': 'str',
        'email': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company': 'company',
        'address1': 'address1',
        'address2': 'address2',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'country': 'country',
        'email': 'email',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, first_name=None, last_name=None, company=None, address1=None, address2=None, locality=None, administrative_area=None, postal_code=None, country=None, email=None, phone_number=None):
        """
        Tmsv1paymentinstrumentsBillTo - a model defined in Swagger
        """

        self._first_name = None
        self._last_name = None
        self._company = None
        self._address1 = None
        self._address2 = None
        self._locality = None
        self._administrative_area = None
        self._postal_code = None
        self._country = None
        self._email = None
        self._phone_number = None

        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if company is not None:
          self.company = company
        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if country is not None:
          self.country = country
        if email is not None:
          self.email = email
        if phone_number is not None:
          self.phone_number = phone_number

    @property
    def first_name(self):
        """
        Gets the first_name of this Tmsv1paymentinstrumentsBillTo.
        Bill to First Name.

        :return: The first_name of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Tmsv1paymentinstrumentsBillTo.
        Bill to First Name.

        :param first_name: The first_name of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if first_name is not None and len(first_name) > 60:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `60`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Tmsv1paymentinstrumentsBillTo.
        Bill to Last Name.

        :return: The last_name of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Tmsv1paymentinstrumentsBillTo.
        Bill to Last Name.

        :param last_name: The last_name of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if last_name is not None and len(last_name) > 60:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `60`")

        self._last_name = last_name

    @property
    def company(self):
        """
        Gets the company of this Tmsv1paymentinstrumentsBillTo.
        Bill to Company.

        :return: The company of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Tmsv1paymentinstrumentsBillTo.
        Bill to Company.

        :param company: The company of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if company is not None and len(company) > 60:
            raise ValueError("Invalid value for `company`, length must be less than or equal to `60`")

        self._company = company

    @property
    def address1(self):
        """
        Gets the address1 of this Tmsv1paymentinstrumentsBillTo.
        Bill to Address Line 1.

        :return: The address1 of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Tmsv1paymentinstrumentsBillTo.
        Bill to Address Line 1.

        :param address1: The address1 of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if address1 is not None and len(address1) > 60:
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `60`")

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Tmsv1paymentinstrumentsBillTo.
        Bill to Address Line 2.

        :return: The address2 of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Tmsv1paymentinstrumentsBillTo.
        Bill to Address Line 2.

        :param address2: The address2 of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if address2 is not None and len(address2) > 60:
            raise ValueError("Invalid value for `address2`, length must be less than or equal to `60`")

        self._address2 = address2

    @property
    def locality(self):
        """
        Gets the locality of this Tmsv1paymentinstrumentsBillTo.
        Bill to City.

        :return: The locality of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Tmsv1paymentinstrumentsBillTo.
        Bill to City.

        :param locality: The locality of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if locality is not None and len(locality) > 50:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `50`")

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Tmsv1paymentinstrumentsBillTo.
        Bill to State.

        :return: The administrative_area of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Tmsv1paymentinstrumentsBillTo.
        Bill to State.

        :param administrative_area: The administrative_area of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 20:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `20`")

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Tmsv1paymentinstrumentsBillTo.
        Bill to Postal Code.

        :return: The postal_code of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Tmsv1paymentinstrumentsBillTo.
        Bill to Postal Code.

        :param postal_code: The postal_code of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 10:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `10`")

        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Tmsv1paymentinstrumentsBillTo.
        Bill to Country. Accepts input in the ISO 3166-1 standard, stores as ISO 3166-1-Alpha-2

        :return: The country of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Tmsv1paymentinstrumentsBillTo.
        Bill to Country. Accepts input in the ISO 3166-1 standard, stores as ISO 3166-1-Alpha-2

        :param country: The country of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if country is not None and len(country) > 3:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `3`")
        if country is not None and len(country) < 2:
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `2`")

        self._country = country

    @property
    def email(self):
        """
        Gets the email of this Tmsv1paymentinstrumentsBillTo.
        Valid Bill to Email.

        :return: The email of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Tmsv1paymentinstrumentsBillTo.
        Valid Bill to Email.

        :param email: The email of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if email is not None and len(email) > 320:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `320`")

        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Tmsv1paymentinstrumentsBillTo.
        Bill to Phone Number.

        :return: The phone_number of this Tmsv1paymentinstrumentsBillTo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Tmsv1paymentinstrumentsBillTo.
        Bill to Phone Number.

        :param phone_number: The phone_number of this Tmsv1paymentinstrumentsBillTo.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 32:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `32`")
        if phone_number is not None and len(phone_number) < 6:
            raise ValueError("Invalid value for `phone_number`, length must be greater than or equal to `6`")

        self._phone_number = phone_number

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
        if not isinstance(other, Tmsv1paymentinstrumentsBillTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
