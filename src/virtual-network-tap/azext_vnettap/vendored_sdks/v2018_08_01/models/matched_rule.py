# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MatchedRule(Model):
    """Matched rule.

    :param rule_name: Name of the matched network security rule.
    :type rule_name: str
    :param action: The network traffic is allowed or denied. Possible values
     are 'Allow' and 'Deny'.
    :type action: str
    """

    _attribute_map = {
        'rule_name': {'key': 'ruleName', 'type': 'str'},
        'action': {'key': 'action', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MatchedRule, self).__init__(**kwargs)
        self.rule_name = kwargs.get('rule_name', None)
        self.action = kwargs.get('action', None)
