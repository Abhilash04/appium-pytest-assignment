""" This module contains the home screen test cases."""

import sys

import allure
import pytest

from TestScripts.base_test_config import BaseTestConfig


@allure.story('[FamPay] - Verify common functionalities for the mobile apps')
@allure.feature('Sanity Tests')
class TestSanityChecks(BaseTestConfig):
    """ This class contains the sanity test cases."""

    @pytest.mark.sanity
    @pytest.mark.registration
    @allure.testcase("Verify Registration Scenarios")
    def test_sanity_101(self, setup_teardown):
        """
        This test is validating the navigation to registration page & successful
        user registration functionality
        :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step("verify navigation to registration page"):
            self.exe_status.mark_final(test_step="verify navigation to registration page",
                                       result=self.reg_page.navigate_to_registration_form_page(self.phone_number))

        with allure.step("verify successful user registration"):
            user = self.reg_page.get_valid_user()
            self.reg_page.enter_form_details(user)
            self.exe_status.mark_final(test_step="verify successful user registration",
                                       result=self.reg_page.verify_successful_registration())

    @pytest.mark.sanity
    @pytest.mark.login
    @allure.testcase("Verify Login Scenarios")
    def test_sanity_102(self, setup_teardown):
        """
        This test is validating the navigation to login page & successful
        user login functionality
        :return: return test status
        """
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        registered_num = self.data_reader.get_data(test_name, "phone_number")

        with allure.step("verify navigation to login page"):
            self.login_page.navigate_to_login_screen()
            self.login_page.enter_phone_number(registered_num)
            self.exe_status.mark_final(test_step="verify navigation to login page",
                                       result=self.login_page.verify_successful_login())
