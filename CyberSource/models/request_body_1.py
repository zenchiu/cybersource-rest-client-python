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


class RequestBody1(object):
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
        'organization_id': 'str',
        'report_definition_name': 'str',
        'report_fields': 'list[str]',
        'report_mime_type': 'str',
        'report_name': 'str',
        'timezone': 'str',
        'report_start_time': 'datetime',
        'report_end_time': 'datetime',
        'report_filters': 'dict(str, list[str])',
        'report_preferences': 'InlineResponse2006ReportPreferences',
        'selected_merchant_group_name': 'str'
    }

    attribute_map = {
        'organization_id': 'organizationId',
        'report_definition_name': 'reportDefinitionName',
        'report_fields': 'reportFields',
        'report_mime_type': 'reportMimeType',
        'report_name': 'reportName',
        'timezone': 'timezone',
        'report_start_time': 'reportStartTime',
        'report_end_time': 'reportEndTime',
        'report_filters': 'reportFilters',
        'report_preferences': 'reportPreferences',
        'selected_merchant_group_name': 'selectedMerchantGroupName'
    }

    def __init__(self, organization_id=None, report_definition_name=None, report_fields=None, report_mime_type=None, report_name=None, timezone=None, report_start_time=None, report_end_time=None, report_filters=None, report_preferences=None, selected_merchant_group_name=None):
        """
        RequestBody1 - a model defined in Swagger
        """

        self._organization_id = None
        self._report_definition_name = None
        self._report_fields = None
        self._report_mime_type = None
        self._report_name = None
        self._timezone = None
        self._report_start_time = None
        self._report_end_time = None
        self._report_filters = None
        self._report_preferences = None
        self._selected_merchant_group_name = None

        if organization_id is not None:
          self.organization_id = organization_id
        if report_definition_name is not None:
          self.report_definition_name = report_definition_name
        if report_fields is not None:
          self.report_fields = report_fields
        if report_mime_type is not None:
          self.report_mime_type = report_mime_type
        if report_name is not None:
          self.report_name = report_name
        if timezone is not None:
          self.timezone = timezone
        if report_start_time is not None:
          self.report_start_time = report_start_time
        if report_end_time is not None:
          self.report_end_time = report_end_time
        if report_filters is not None:
          self.report_filters = report_filters
        if report_preferences is not None:
          self.report_preferences = report_preferences
        if selected_merchant_group_name is not None:
          self.selected_merchant_group_name = selected_merchant_group_name

    @property
    def organization_id(self):
        """
        Gets the organization_id of this RequestBody1.
        Valid CyberSource Organization Id

        :return: The organization_id of this RequestBody1.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this RequestBody1.
        Valid CyberSource Organization Id

        :param organization_id: The organization_id of this RequestBody1.
        :type: str
        """
        if organization_id is not None and not re.search('[a-zA-Z0-9-_]+', organization_id):
            raise ValueError("Invalid value for `organization_id`, must be a follow pattern or equal to `/[a-zA-Z0-9-_]+/`")

        self._organization_id = organization_id

    @property
    def report_definition_name(self):
        """
        Gets the report_definition_name of this RequestBody1.

        :return: The report_definition_name of this RequestBody1.
        :rtype: str
        """
        return self._report_definition_name

    @report_definition_name.setter
    def report_definition_name(self, report_definition_name):
        """
        Sets the report_definition_name of this RequestBody1.

        :param report_definition_name: The report_definition_name of this RequestBody1.
        :type: str
        """
        if report_definition_name is not None and len(report_definition_name) > 80:
            raise ValueError("Invalid value for `report_definition_name`, length must be less than or equal to `80`")
        if report_definition_name is not None and len(report_definition_name) < 1:
            raise ValueError("Invalid value for `report_definition_name`, length must be greater than or equal to `1`")
        if report_definition_name is not None and not re.search('[a-zA-Z0-9-]+', report_definition_name):
            raise ValueError("Invalid value for `report_definition_name`, must be a follow pattern or equal to `/[a-zA-Z0-9-]+/`")

        self._report_definition_name = report_definition_name

    @property
    def report_fields(self):
        """
        Gets the report_fields of this RequestBody1.
        List of fields which needs to get included in a report

        :return: The report_fields of this RequestBody1.
        :rtype: list[str]
        """
        return self._report_fields

    @report_fields.setter
    def report_fields(self, report_fields):
        """
        Sets the report_fields of this RequestBody1.
        List of fields which needs to get included in a report

        :param report_fields: The report_fields of this RequestBody1.
        :type: list[str]
        """

        self._report_fields = report_fields

    @property
    def report_mime_type(self):
        """
        Gets the report_mime_type of this RequestBody1.
         Format of the report

        :return: The report_mime_type of this RequestBody1.
        :rtype: str
        """
        return self._report_mime_type

    @report_mime_type.setter
    def report_mime_type(self, report_mime_type):
        """
        Sets the report_mime_type of this RequestBody1.
         Format of the report

        :param report_mime_type: The report_mime_type of this RequestBody1.
        :type: str
        """
        allowed_values = ["application/xml", "text/csv"]
        if report_mime_type not in allowed_values:
            raise ValueError(
                "Invalid value for `report_mime_type` ({0}), must be one of {1}"
                .format(report_mime_type, allowed_values)
            )

        self._report_mime_type = report_mime_type

    @property
    def report_name(self):
        """
        Gets the report_name of this RequestBody1.
        Name of the report

        :return: The report_name of this RequestBody1.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """
        Sets the report_name of this RequestBody1.
        Name of the report

        :param report_name: The report_name of this RequestBody1.
        :type: str
        """
        if report_name is not None and len(report_name) > 128:
            raise ValueError("Invalid value for `report_name`, length must be less than or equal to `128`")
        if report_name is not None and len(report_name) < 1:
            raise ValueError("Invalid value for `report_name`, length must be greater than or equal to `1`")
        if report_name is not None and not re.search('[a-zA-Z0-9-_ ]+', report_name):
            raise ValueError("Invalid value for `report_name`, must be a follow pattern or equal to `/[a-zA-Z0-9-_ ]+/`")

        self._report_name = report_name

    @property
    def timezone(self):
        """
        Gets the timezone of this RequestBody1.
        Timezone of the report

        :return: The timezone of this RequestBody1.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this RequestBody1.
        Timezone of the report

        :param timezone: The timezone of this RequestBody1.
        :type: str
        """

        self._timezone = timezone

    @property
    def report_start_time(self):
        """
        Gets the report_start_time of this RequestBody1.
        Start time of the report

        :return: The report_start_time of this RequestBody1.
        :rtype: datetime
        """
        return self._report_start_time

    @report_start_time.setter
    def report_start_time(self, report_start_time):
        """
        Sets the report_start_time of this RequestBody1.
        Start time of the report

        :param report_start_time: The report_start_time of this RequestBody1.
        :type: datetime
        """

        self._report_start_time = report_start_time

    @property
    def report_end_time(self):
        """
        Gets the report_end_time of this RequestBody1.
        End time of the report

        :return: The report_end_time of this RequestBody1.
        :rtype: datetime
        """
        return self._report_end_time

    @report_end_time.setter
    def report_end_time(self, report_end_time):
        """
        Sets the report_end_time of this RequestBody1.
        End time of the report

        :param report_end_time: The report_end_time of this RequestBody1.
        :type: datetime
        """

        self._report_end_time = report_end_time

    @property
    def report_filters(self):
        """
        Gets the report_filters of this RequestBody1.

        :return: The report_filters of this RequestBody1.
        :rtype: dict(str, list[str])
        """
        return self._report_filters

    @report_filters.setter
    def report_filters(self, report_filters):
        """
        Sets the report_filters of this RequestBody1.

        :param report_filters: The report_filters of this RequestBody1.
        :type: dict(str, list[str])
        """

        self._report_filters = report_filters

    @property
    def report_preferences(self):
        """
        Gets the report_preferences of this RequestBody1.

        :return: The report_preferences of this RequestBody1.
        :rtype: InlineResponse2006ReportPreferences
        """
        return self._report_preferences

    @report_preferences.setter
    def report_preferences(self, report_preferences):
        """
        Sets the report_preferences of this RequestBody1.

        :param report_preferences: The report_preferences of this RequestBody1.
        :type: InlineResponse2006ReportPreferences
        """

        self._report_preferences = report_preferences

    @property
    def selected_merchant_group_name(self):
        """
        Gets the selected_merchant_group_name of this RequestBody1.
        Specifies the group name

        :return: The selected_merchant_group_name of this RequestBody1.
        :rtype: str
        """
        return self._selected_merchant_group_name

    @selected_merchant_group_name.setter
    def selected_merchant_group_name(self, selected_merchant_group_name):
        """
        Sets the selected_merchant_group_name of this RequestBody1.
        Specifies the group name

        :param selected_merchant_group_name: The selected_merchant_group_name of this RequestBody1.
        :type: str
        """
        if selected_merchant_group_name is not None and not re.search('[0-9]*', selected_merchant_group_name):
            raise ValueError("Invalid value for `selected_merchant_group_name`, must be a follow pattern or equal to `/[0-9]*/`")

        self._selected_merchant_group_name = selected_merchant_group_name

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
        if not isinstance(other, RequestBody1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
