# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_express_route_circuit_show_peering_stat
from .example_steps import step_express_route_circuit
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    # STEP NOT FOUND: /ExpressRouteCircuits/put/Create ExpressRouteCircuit
    # STEP NOT FOUND: /ExpressRouteCircuitPeerings/put/Create ExpressRouteCircuit Peerings
    # STEP NOT FOUND: /ExpressRouteCircuits/put/Create ExpressRouteCircuit on ExpressRoutePort
    step_express_route_circuit_show_peering_stat(test, checks=[])
    # STEP NOT FOUND: /ExpressRouteCircuits/get/Get ExpressRoute Circuit Traffic Stats
    # STEP NOT FOUND: /ExpressRouteCircuits/get/Get ExpressRouteCircuit
    # STEP NOT FOUND: /ExpressRouteCircuits/get/List ExpressRouteCircuits in a resource group
    # STEP NOT FOUND: /ExpressRouteCircuits/get/List ExpressRouteCircuits in a subscription
    step_express_route_circuit(test, checks=[])
    # STEP NOT FOUND: /ExpressRouteCircuits/post/List Route Tables
    # STEP NOT FOUND: /ExpressRouteCircuits/post/List ARP Table
    # STEP NOT FOUND: /ExpressRouteCircuits/patch/Update Express Route Circuit Tags
    # STEP NOT FOUND: /ExpressRouteCircuits/delete/Delete ExpressRouteCircuit
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class ExpressroutecircuitsScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(ExpressroutecircuitsScenarioTest, self).__init__(*args, **kwargs)

    @ResourceGroupPreparer(name_prefix='clitestnetwork_rg1'[:7], key='rg', parameter_name='rg')
    def test_expressroutecircuits_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()