# coding: utf-8

"""
    Batch Product Details Api

    Retrieve list of product details from list of part numbers  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BatchProductDetailsResponse(object):
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
        'product_details': 'list[ProductDetails]',
        'errors': 'list[str]'
    }

    attribute_map = {
        'product_details': 'ProductDetails',
        'errors': 'Errors'
    }

    def __init__(self, product_details=None, errors=None):  # noqa: E501
        """BatchProductDetailsResponse - a model defined in Swagger"""  # noqa: E501

        self._product_details = None
        self._errors = None
        self.discriminator = None

        if product_details is not None:
            self.product_details = product_details
        if errors is not None:
            self.errors = errors

    @property
    def product_details(self):
        """Gets the product_details of this BatchProductDetailsResponse.  # noqa: E501

        List of ProductDetails  # noqa: E501

        :return: The product_details of this BatchProductDetailsResponse.  # noqa: E501
        :rtype: list[ProductDetails]
        """
        return self._product_details

    @product_details.setter
    def product_details(self, product_details):
        """Sets the product_details of this BatchProductDetailsResponse.

        List of ProductDetails  # noqa: E501

        :param product_details: The product_details of this BatchProductDetailsResponse.  # noqa: E501
        :type: list[ProductDetails]
        """

        self._product_details = product_details

    @property
    def errors(self):
        """Gets the errors of this BatchProductDetailsResponse.  # noqa: E501

        List of Errors  # noqa: E501

        :return: The errors of this BatchProductDetailsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BatchProductDetailsResponse.

        List of Errors  # noqa: E501

        :param errors: The errors of this BatchProductDetailsResponse.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

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
        if issubclass(BatchProductDetailsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchProductDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
