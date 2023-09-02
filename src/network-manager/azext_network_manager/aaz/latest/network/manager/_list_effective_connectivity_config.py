# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network manager list-effective-connectivity-config",
)
class ListEffectiveConnectivityConfig(AAZCommand):
    """List all effective connectivity configurations applied on a virtual network.

    :example: List Azure Virtual Network Manager Effective Configuration
        az network manager list-effective-connectivity-config --virtual-network-name "myVirtualNetwork" --resource-group "myResourceGroup"
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworks/{}/listnetworkmanagereffectiveconnectivityconfigurations", "2022-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.virtual_network_name = AAZStrArg(
            options=["--vnet-name", "--virtual-network-name"],
            help="The name of the virtual network.",
            required=True,
            id_part="name",
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.skip_token = AAZStrArg(
            options=["--skip-token"],
            arg_group="Parameters",
            help="When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ListNetworkManagerEffectiveConnectivityConfigurations(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ListNetworkManagerEffectiveConnectivityConfigurations(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/listNetworkManagerEffectiveConnectivityConfigurations",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkName", self.ctx.args.virtual_network_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("skipToken", AAZStrType, ".skip_token")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.skip_token = AAZStrType(
                serialized_name="skipToken",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.configuration_groups = AAZListType(
                serialized_name="configurationGroups",
            )
            _element.id = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            configuration_groups = cls._schema_on_200.value.Element.configuration_groups
            configuration_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.configuration_groups.Element
            _element.id = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.configuration_groups.Element.properties
            properties.description = AAZStrType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.applies_to_groups = AAZListType(
                serialized_name="appliesToGroups",
                flags={"required": True},
            )
            properties.connectivity_topology = AAZStrType(
                serialized_name="connectivityTopology",
                flags={"required": True},
            )
            properties.delete_existing_peering = AAZStrType(
                serialized_name="deleteExistingPeering",
            )
            properties.description = AAZStrType()
            properties.hubs = AAZListType()
            properties.is_global = AAZStrType(
                serialized_name="isGlobal",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            applies_to_groups = cls._schema_on_200.value.Element.properties.applies_to_groups
            applies_to_groups.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.applies_to_groups.Element
            _element.group_connectivity = AAZStrType(
                serialized_name="groupConnectivity",
                flags={"required": True},
            )
            _element.is_global = AAZStrType(
                serialized_name="isGlobal",
            )
            _element.network_group_id = AAZStrType(
                serialized_name="networkGroupId",
                flags={"required": True},
            )
            _element.use_hub_gateway = AAZStrType(
                serialized_name="useHubGateway",
            )

            hubs = cls._schema_on_200.value.Element.properties.hubs
            hubs.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.hubs.Element
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
            )
            _element.resource_type = AAZStrType(
                serialized_name="resourceType",
            )

            return cls._schema_on_200


class _ListEffectiveConnectivityConfigHelper:
    """Helper class for ListEffectiveConnectivityConfig"""


__all__ = ["ListEffectiveConnectivityConfig"]