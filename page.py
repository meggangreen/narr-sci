""" Modified from docs boilerplate code https://selenium-python.readthedocs.io/page-objects.html """

import re
from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def is_title_match(self):
        """Verifies that the supplied text appears in page title"""
        text = ""
        return text in self.driver.title


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()

    def is_title_match(self):
        """Verifies that the hardcoded text "Narrative Science" appears in page title"""
        super().is_title_match()
        text="Narrative Science"
        return text in self.driver.title

    def accept_cookie_policy(self):
        """ Gets the cookie banner out of our way. """
        element = self.driver.find_element(*MainPageLocators.COOKIES_OK_BUTTON)
        element.click()

    def navigate_to(self, link_text):
        """ There is more than one link to the desired destination, could use first or a specific.
            Tried to make dynamic naming; didn't work and didn't want to spend
            time troubleshooting before test was complete.

        """
        # link_text = f"NAV_{link_text.upper().replace(' ', '_')}"
        # locator = f"*MainPageLocators.{link_text}"
        # element = self.driver.find_element(locator)
        if link_text == 'About Us':
            element = self.driver.find_element(*MainPageLocators.NAV_ABOUT_US)
        element.click()


class AboutUsPage(BasePage):
    """ About Us page action methods come here """

    def is_title_match(self):
        """Verifies that the hardcoded text "About Us" appears in page title"""
        super().is_title_match()
        text="About Us"
        return text in self.driver.title

    def has_specific_patents(self, patents):
        LINK_FILL = r'Patent <a href[=\s\w\.\"\-\?\:/,&;%]+>'
        for patent in patents:
            if not re.search(f"{LINK_FILL}{patent}", self.driver.page_source):
                return False

        return True


################################################################################

# 6.4. Locators
# One of the practices is to separate the locator strings from the place where they are being used.
# In this example, locators of the same page belong to same class.
# The locators.py will look like this:

# from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    COOKIES_OK_BUTTON = (By.ID, 'catapultCookie')

    NAV_ABOUT_US = (By.LINK_TEXT, 'About Us')


class AboutUsPageLocators(object):
    """A class for About Us locators. All About Us locators should come here"""
    pass

