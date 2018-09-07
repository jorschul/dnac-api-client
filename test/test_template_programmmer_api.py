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
from dnac_api_client.api.template_programmmer_api import TemplateProgrammmerApi  # noqa: E501
from dnac_api_client.rest import ApiException


class TestTemplateProgrammmerApi(unittest.TestCase):
    """TemplateProgrammmerApi unit test stubs"""

    def setUp(self):
        self.api = dnac_api_client.api.template_programmmer_api.TemplateProgrammmerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_template_programmer_project_get(self):
        """Test case for api_v1_template_programmer_project_get

        Gets a list of projects  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_project_post(self):
        """Test case for api_v1_template_programmer_project_post

        Create Project  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_project_project_id_delete(self):
        """Test case for api_v1_template_programmer_project_project_id_delete

        Deletes the project  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_project_project_id_template_post(self):
        """Test case for api_v1_template_programmer_project_project_id_template_post

        Create Template  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_project_put(self):
        """Test case for api_v1_template_programmer_project_put

        Update Project  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_deploy_post(self):
        """Test case for api_v1_template_programmer_template_deploy_post

        Deploy Template  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_deploy_status_deployment_id_get(self):
        """Test case for api_v1_template_programmer_template_deploy_status_deployment_id_get

        Status of template deployment  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_get(self):
        """Test case for api_v1_template_programmer_template_get

        Gets the templates available depending on the criteria  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_preview_put(self):
        """Test case for api_v1_template_programmer_template_preview_put

        Preview Template  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_put(self):
        """Test case for api_v1_template_programmer_template_put

        Update Template  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_template_id_delete(self):
        """Test case for api_v1_template_programmer_template_template_id_delete

        Deletes the template  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_template_id_get(self):
        """Test case for api_v1_template_programmer_template_template_id_get

        Gets details of a given template  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_version_post(self):
        """Test case for api_v1_template_programmer_template_version_post

        Version Template  # noqa: E501
        """
        pass

    def test_api_v1_template_programmer_template_version_template_id_get(self):
        """Test case for api_v1_template_programmer_template_version_template_id_get

        Gets all the versions of a given template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()