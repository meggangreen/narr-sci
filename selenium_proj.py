""" Modified from docs boilerplate code """

import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import page

class NSPatentSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = Firefox(options=options)
        self.driver.get('https://narrativescience.com')


    def test_find_specific_patents_in_about_page(self):
        """ Accepts cookie policy on the main ('/') page.
            Navigates from the main page to About Us using the first found element.
            Looks for specific patents listed on About Us.
        """

        # Load the main page and check title
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_match(), "Main Page title doesn't match."

        # Accept cookie policy
        main_page.accept_cookie_policy()

        # Navigate to about us page
        main_page.navigate_to('About Us')

        # Convert to about page and check title
        about_page = page.AboutUsPage(self.driver)
        assert about_page.is_title_match(), "About Page title doesn't match."
        patents = ["8,630,844","9,576,009"]
        assert about_page.has_specific_patents(patents), "Patent(s) not found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
