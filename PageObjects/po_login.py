"""
This module is used for login page objects.
"""

from PageObjects.po_base import BasePageObjects
from ResourceFiles.constants import Identifiers


class LoginPageObjects(BasePageObjects):
    """
    This class defines the element identifiers and methods for login page.
    """

    # Locators
    signup_button = {"com.fampay.in.debug:id/sign_up_button": Identifiers.ID.value}
    phone_number_input = {"com.fampay.in.debug:id/phone_number_input": Identifiers.ID.value}
    continue_button = {"com.fampay.in.debug:id/verify_number_button": Identifiers.ID.value}
    permission_grant_button = {"com.fampay.in.debug:id/grant_permissions_button": Identifiers.ID.value}

    def navigate_to_login_screen(self):
        """
        This test verifies the navigation to login screen
        :return: boolean value for navigation to login screen
        """
        self.mouse_click_action(self.get_locator(self.signup_button)[0])
        return self.is_element_displayed(
            self.get_locator(self.phone_number_input)[0])

    def enter_phone_number(self, phone_number):
        """
        This method fills the phone number field & clicks on the CTA
        :param phone_number: registered user phone number
        :return:
        """
        self.enter_text_action(phone_number,
                               self.get_locator(self.phone_number_input)[0])
        self.mouse_click_action(self.get_locator(self.continue_button)[0])

    def verify_successful_login(self):
        """
        This function is used to verify successful login functionality
        :return: this function returns boolean status of element located
        """
        return self.is_element_displayed(self.get_locator(self.permission_grant_button)[0],
                                         max_time_out=20)


class AndLoginPageObjects(LoginPageObjects):
    # Locators
    pass


class IOSLoginPageObjects(LoginPageObjects):
    # Locators
    pass


LoginPageObjects._ANDROID = AndLoginPageObjects
LoginPageObjects._IOS = IOSLoginPageObjects
