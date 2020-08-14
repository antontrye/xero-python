# coding: utf-8

"""
    Xero oAuth 2 identity service

    This specifing endpoints related to managing authentication tokens and identity for Xero API  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Connection(BaseModel):
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
        "id": "str",
        "tenant_id": "str",
        "auth_event_id": "str",
        "tenant_type": "str",
        "tenant_name": "str",
        "created_date_utc": "datetime",
        "updated_date_utc": "datetime",
    }

    attribute_map = {
        "id": "id",
        "tenant_id": "tenantId",
        "auth_event_id": "authEventId",
        "tenant_type": "tenantType",
        "tenant_name": "tenantName",
        "created_date_utc": "createdDateUtc",
        "updated_date_utc": "updatedDateUtc",
    }

    def __init__(
        self,
        id=None,
        tenant_id=None,
        auth_event_id=None,
        tenant_type=None,
        tenant_name=None,
        created_date_utc=None,
        updated_date_utc=None,
    ):  # noqa: E501
        """Connection - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._tenant_id = None
        self._auth_event_id = None
        self._tenant_type = None
        self._tenant_name = None
        self._created_date_utc = None
        self._updated_date_utc = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if auth_event_id is not None:
            self.auth_event_id = auth_event_id
        if tenant_type is not None:
            self.tenant_type = tenant_type
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def id(self):
        """Gets the id of this Connection.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Connection.

        Xero identifier  # noqa: E501

        :param id: The id of this Connection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Connection.  # noqa: E501

        Xero identifier of organisation  # noqa: E501

        :return: The tenant_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Connection.

        Xero identifier of organisation  # noqa: E501

        :param tenant_id: The tenant_id of this Connection.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def auth_event_id(self):
        """Gets the auth_event_id of this Connection.  # noqa: E501

        Identifier shared across connections authorised at the same time  # noqa: E501

        :return: The auth_event_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._auth_event_id

    @auth_event_id.setter
    def auth_event_id(self, auth_event_id):
        """Sets the auth_event_id of this Connection.

        Identifier shared across connections authorised at the same time  # noqa: E501

        :param auth_event_id: The auth_event_id of this Connection.  # noqa: E501
        :type: str
        """

        self._auth_event_id = auth_event_id

    @property
    def tenant_type(self):
        """Gets the tenant_type of this Connection.  # noqa: E501

        Xero tenant type (i.e. ORGANISATION, PRACTICE)  # noqa: E501

        :return: The tenant_type of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._tenant_type

    @tenant_type.setter
    def tenant_type(self, tenant_type):
        """Sets the tenant_type of this Connection.

        Xero tenant type (i.e. ORGANISATION, PRACTICE)  # noqa: E501

        :param tenant_type: The tenant_type of this Connection.  # noqa: E501
        :type: str
        """

        self._tenant_type = tenant_type

    @property
    def tenant_name(self):
        """Gets the tenant_name of this Connection.  # noqa: E501

        Xero tenant name  # noqa: E501

        :return: The tenant_name of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this Connection.

        Xero tenant name  # noqa: E501

        :param tenant_name: The tenant_name of this Connection.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def created_date_utc(self):
        """Gets the created_date_utc of this Connection.  # noqa: E501

        The date when the user connected this tenant to your app  # noqa: E501

        :return: The created_date_utc of this Connection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        """Sets the created_date_utc of this Connection.

        The date when the user connected this tenant to your app  # noqa: E501

        :param created_date_utc: The created_date_utc of this Connection.  # noqa: E501
        :type: datetime
        """

        self._created_date_utc = created_date_utc

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Connection.  # noqa: E501

        The date when the user most recently connected this tenant to your app. May differ to the created date if the user has disconnected and subsequently reconnected this tenant to your app.  # noqa: E501

        :return: The updated_date_utc of this Connection.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Connection.

        The date when the user most recently connected this tenant to your app. May differ to the created date if the user has disconnected and subsequently reconnected this tenant to your app.  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Connection.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc
