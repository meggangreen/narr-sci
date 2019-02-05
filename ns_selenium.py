""" Please write a selenium test that goes to Narrative Science homepage and
    navigates the site to find the patents we have.  The test should check that
    the following patents (8,630,844 & 9,576,009) are listed on the About Us page.
    Please use the page object model.

"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
ff = Firefox(options=options)
# do stuff with browser 'ff'
ff.get('https://narrativescience.com/')

# accept cookie policy
cookie_ok_button = ff.find_element_by_id('catapultCookie')
cookie_ok_button.click()

# follow (first) link to about us page
about_us_link = ff.find_element_by_link_text('About Us')
about_us_link.click()

# verify we're on about us
if 'About Us' not in ff.title:
    print("oops!")

# find first patent
try:
    patent_1_link = ff.find_element_by_link_text('8,630,844')
    patent_2_link = ff.find_element_by_link_text('9,576,009')
except:
    print("not all patents found")
else:
    print("yay! all patents found")

ff.close()
