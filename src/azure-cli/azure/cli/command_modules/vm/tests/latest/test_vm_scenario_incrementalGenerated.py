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
from .example_steps import step_disk_access_list_private_endpoint_connection
from .example_steps import step_disk_access_show_private_link_resource
from .example_steps import step_disk_access_delete
from .example_steps import step_disk_restore_point_show
from .example_steps import step_create
from .example_steps import step_show
from .example_steps import step_install_patch
from .example_steps import step_reimage
from .example_steps import step_vm_extension_create
from .example_steps import step_vm_extension_show
from .example_steps import step_vm_extension_list
from .example_steps import step_vm_run_list
from .example_steps import step_v_ms_retrieve_boot_diagnostic_data
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
    step_disk_access_list_private_endpoint_connection(test, checks=[])
    step_disk_access_show_private_link_resource(test, checks=[])
    step_disk_access_delete(test, checks=[])
    step_disk_restore_point_show(test, checks=[])
    step_create(test, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("publicKey", "{{ssh-rsa public key}}", case_sensitive=False),
        test.check("name", "{mySshPublicKey}", case_sensitive=False),
    ])
    step_show(test, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("publicKey", "{{ssh-rsa public key}}", case_sensitive=False),
        test.check("name", "{mySshPublicKey}", case_sensitive=False),
    ])
    step_install_patch(test, checks=[])
    step_reimage(test, checks=[])
    step_vm_extension_create(test, checks=[])
    step_vm_extension_show(test, checks=[])
    step_vm_extension_list(test, checks=[])
    step_vm_run_list(test, checks=[])
    step_v_ms_retrieve_boot_diagnostic_data(test, checks=[])
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class VmScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(VmScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'mySshPublicKey': 'mySshPublicKeyName',
            'myDiskAccess': 'myDiskAccess',
            'myDiskRestorePoint': 'TestDisk45ceb03433006d1baee0_b70cd924-3362-4a80-93c2-9415eaa12745',
        })

    @ResourceGroupPreparer(name_prefix='clitestvm_myResourceGroup'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestvm_myResourceGroupName'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestvm_ResourceGroup'[:7], key='rg_3', parameter_name='rg_3')
    def test_vm_Scenario(self, rg, rg_2, rg_3):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
