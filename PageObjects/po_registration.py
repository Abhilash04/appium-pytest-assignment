"""
This module is used for registration page objects.
"""

from PageObjects.po_base import BasePageObjects
from ResourceFiles.constants import Identifiers


class RegistrationPageObjects(BasePageObjects):
    """
    This class defines the element identifiers and methods.
    """

    # Locators
    signup_button = {"com.fampay.in.debug:id/sign_up_button": Identifiers.ID.value}
    phone_number_input = {"com.fampay.in.debug:id/phone_number_input": Identifiers.ID.value}
    continue_button = {"com.fampay.in.debug:id/verify_number_button": Identifiers.ID.value}
    card_link = {"com.fampay.in.debug:id/card_front": Identifiers.ID.value}
    first_name_input = {"com.fampay.in.debug:id/first_name": Identifiers.ID.value}
    last_name_input = {"com.fampay.in.debug:id/last_name": Identifiers.ID.value}
    dob_input = {"com.fampay.in.debug:id/dob": Identifiers.ID.value}
    next_button = {"com.fampay.in.debug:id/next_button_fab": Identifiers.ID.value}
    submit_button = {"com.fampay.in.debug:id/continue_button": Identifiers.ID.value}
    permission_grant_button = {"com.fampay.in.debug:id/grant_permissions_button": Identifiers.ID.value}

    def navigate_to_registration_form_page(self, phone_number):
        """
        This test verifies the navigation to registration form screen
        :param phone_number: user registered phone number
        :return: boolean value for navigation to registration form screen
        """

        signup_button_prop = self.get_locator(self.signup_button)
        phone_number_prop = self.get_locator(self.phone_number_input)
        continue_button_prop = self.get_locator(self.continue_button)
        card_link_prop = self.get_locator(self.card_link)

        self.mouse_click_action(signup_button_prop[0])
        if self.is_element_displayed(phone_number_prop[0]):
            self.enter_text_action(phone_number, phone_number_prop[0])
            self.mouse_click_action(continue_button_prop[0])
            if self.is_element_displayed(card_link_prop[0], max_time_out=20):
                self.mouse_click_action(card_link_prop[0])
                return True
            else:
                self.log.error("Main registration screen is not visible.")
                return False
        else:
            self.log.error("Phone number screen is not visible.")
            return False

    def enter_form_details(self, user):
        """
        This method fills the form details required for registration.
        :param user: accepts user object
        :return:
        """
        try:
            self.enter_text_action(user["first_name"], self.get_locator(self.first_name_input)[0])
            self.enter_text_action(user["last_name"], self.get_locator(self.last_name_input)[0])
            self.enter_text_action(user["dob"], self.get_locator(self.dob_input)[0])
            if self.is_element_displayed(self.get_locator(self.next_button)[0], max_time_out=3):
                self.mouse_click_action(self.get_locator(self.next_button)[0])
            self.mouse_click_action(self.get_locator(self.submit_button)[0])

        except Exception as ex:
            self.log.error("Failed to fill the form details:\n", ex)

    def verify_successful_registration(self):
        """
        This method verifies the successful registration.
        :return:
        """
        return self.is_element_displayed(self.get_locator(self.permission_grant_button)[0],
                                         max_time_out=20)


class AndRegistrationPageObjects(RegistrationPageObjects):
    pass


class IOSRegistrationPageObjects(RegistrationPageObjects):
    pass


RegistrationPageObjects._ANDROID = AndRegistrationPageObjects
RegistrationPageObjects._IOS = IOSRegistrationPageObjects
