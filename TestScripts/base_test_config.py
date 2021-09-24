import logging

import pytest

import FrameworkUtilities.logger_utility as log_utils
from FrameworkUtilities.data_reader_utility import DataReader
from FrameworkUtilities.execution_status_utility import ExecutionStatus
from PageObjects.po_login import LoginPageObjects
from PageObjects.po_registration import RegistrationPageObjects


@pytest.mark.usefixtures("driver")
class BaseTestConfig:
    log = log_utils.custom_logger(logging.INFO)

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.exe_status = ExecutionStatus(self.driver)
        self.data_reader = DataReader()
        self.reg_page = RegistrationPageObjects.instance(self.driver)
        self.login_page = LoginPageObjects.instance(self.driver)
        self.phone_number = self.reg_page.generate_random_phone_number()
        yield "resource"
        self.driver.reset()
