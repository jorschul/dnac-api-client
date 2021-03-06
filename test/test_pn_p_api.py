# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dnac_api_client
from dnac_api_client.api.pn_p_api import PnPApi  # noqa: E501
from dnac_api_client.rest import ApiException


class TestPnPApi(unittest.TestCase):
    """PnPApi unit test stubs"""

    def setUp(self):
        self.api = dnac_api_client.api.pn_p_api.PnPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_onboarding_pnp_device_claim_post(self):
        """Test case for api_v1_onboarding_pnp_device_claim_post

        Claim Device(s)  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_count_get(self):
        """Test case for api_v1_onboarding_pnp_device_count_get

        Get Device Count  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_dashboard_count_get(self):
        """Test case for api_v1_onboarding_pnp_device_dashboard_count_get

        Get Categorized Device Count  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_get(self):
        """Test case for api_v1_onboarding_pnp_device_get

        List devices  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_history_get(self):
        """Test case for api_v1_onboarding_pnp_device_history_get

        Get Device History  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_id_delete(self):
        """Test case for api_v1_onboarding_pnp_device_id_delete

        Delete Device  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_id_get(self):
        """Test case for api_v1_onboarding_pnp_device_id_get

        Get Device by ID  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_id_put(self):
        """Test case for api_v1_onboarding_pnp_device_id_put

        Update Device  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_import_post(self):
        """Test case for api_v1_onboarding_pnp_device_import_post

        Import Many Devices  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_post(self):
        """Test case for api_v1_onboarding_pnp_device_post

        Create Device  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_provision_post(self):
        """Test case for api_v1_onboarding_pnp_device_provision_post

        Provision Device  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_reset_post(self):
        """Test case for api_v1_onboarding_pnp_device_reset_post

        Reset Device  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_sacct_domain_vacct_name_sync_result_get(self):
        """Test case for api_v1_onboarding_pnp_device_sacct_domain_vacct_name_sync_result_get

        Get Sync Result for Virtual Account  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_unclaim_post(self):
        """Test case for api_v1_onboarding_pnp_device_unclaim_post

        Un-Claim Device  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_device_vacct_sync_post(self):
        """Test case for api_v1_onboarding_pnp_device_vacct_sync_post

        Sync Virtual Account Devices  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_settings_get(self):
        """Test case for api_v1_onboarding_pnp_settings_get

        View Settings  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_settings_put(self):
        """Test case for api_v1_onboarding_pnp_settings_put

        Update Settings  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_settings_sacct_domain_vacct_get(self):
        """Test case for api_v1_onboarding_pnp_settings_sacct_domain_vacct_get

        Get Virtual Account List  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_settings_sacct_get(self):
        """Test case for api_v1_onboarding_pnp_settings_sacct_get

        Get Smart Account List  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_settings_savacct_post(self):
        """Test case for api_v1_onboarding_pnp_settings_savacct_post

        Add Virtual Account  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_settings_savacct_put(self):
        """Test case for api_v1_onboarding_pnp_settings_savacct_put

        Edit PnP Server Profile  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_settings_vacct_delete(self):
        """Test case for api_v1_onboarding_pnp_settings_vacct_delete

        Deregister Virtual Account  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_workflow_count_get(self):
        """Test case for api_v1_onboarding_pnp_workflow_count_get

        Get Workflow Count  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_workflow_get(self):
        """Test case for api_v1_onboarding_pnp_workflow_get

        List Workflows  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_workflow_id_delete(self):
        """Test case for api_v1_onboarding_pnp_workflow_id_delete

        Delete Workflow  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_workflow_id_get(self):
        """Test case for api_v1_onboarding_pnp_workflow_id_get

        Get Workflow  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_workflow_id_put(self):
        """Test case for api_v1_onboarding_pnp_workflow_id_put

        Update Workflow  # noqa: E501
        """
        pass

    def test_api_v1_onboarding_pnp_workflow_post(self):
        """Test case for api_v1_onboarding_pnp_workflow_post

        Create Workflow  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
