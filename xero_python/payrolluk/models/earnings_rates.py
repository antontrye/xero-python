# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EarningsRates(BaseModel):
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
        "pagination": "Pagination",
        "problem": "Problem",
        "earnings_rates": "list[EarningsRate]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "earnings_rates": "earningsRates",
    }

    def __init__(
        self, pagination=None, problem=None, earnings_rates=None
    ):  # noqa: E501
        """EarningsRates - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._earnings_rates = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if earnings_rates is not None:
            self.earnings_rates = earnings_rates

    @property
    def pagination(self):
        """Gets the pagination of this EarningsRates.  # noqa: E501


        :return: The pagination of this EarningsRates.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EarningsRates.


        :param pagination: The pagination of this EarningsRates.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EarningsRates.  # noqa: E501


        :return: The problem of this EarningsRates.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EarningsRates.


        :param problem: The problem of this EarningsRates.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def earnings_rates(self):
        """Gets the earnings_rates of this EarningsRates.  # noqa: E501


        :return: The earnings_rates of this EarningsRates.  # noqa: E501
        :rtype: list[EarningsRate]
        """
        return self._earnings_rates

    @earnings_rates.setter
    def earnings_rates(self, earnings_rates):
        """Sets the earnings_rates of this EarningsRates.


        :param earnings_rates: The earnings_rates of this EarningsRates.  # noqa: E501
        :type: list[EarningsRate]
        """

        self._earnings_rates = earnings_rates
