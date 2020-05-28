# About the Repo
I applied to be a SDET and submitted this solution to the coding challenge.

The first part of the challenge was to test a 3rd-party API. I found this part
to be particularly straight-forward owing to limited previous experience and 
good Python documentation.
- [lyrics_api.py](https://github.com/meggangreen/narr-sci/blob/master/lyrics_api.py)

The second part of the challenge was to "write a Selenium test that goes to NS 
homepage and navigates the site to find the patents we have. The test should 
check that the following patents (8,630,844 & 9,576,009) are listed on the About 
Us page. Please use the page object model." I knew what Selenium was, but had 
never used it or the page object model. The Selenium docs are excellent.
- I first executed the task without the page object model, so that I could
understand the essentials: [ns_selenium.py](https://github.com/meggangreen/narr-sci/blob/master/ns_selenium.py)
- I then executed the full task: [page.py](https://github.com/meggangreen/narr-sci/blob/master/page.py) and [selenium_proj.py](https://github.com/meggangreen/narr-sci/blob/master/selenium_proj.py)

Everything below this point was part of my original submission.

# About Me
As I stated in my cover letter, I've only recently discovered how interesting
I find testing to be. I'm looking for my first position in Test as a Junior
Engineer. Also, I love writing in Python and I'd like to do more JavaScript.
I've never used Selenium and I had not heard of the Page Object Model, but I
think I did ... not too bad. I hope you think so too.
Thanks!

# Installation
The module 'selenium_proj.py' assumes Python3 is installed.

You will also need Selenium, Firefox, and the Gecko webdriver. Detailed
instructions for those requirements follows in 'Install Requirements'.

To run the test from the command line:
```
$ python3 selenium_proj.py
```

The expected response is:
```
.
----------------------------------------------------------------------
Ran 1 test in 38.831s

OK
```

# Install Requirements
The following examples are to install Selenium, Firefox, and the Gecko webdriver
on Ubuntu 18.04 LTS and ought to work on plenty of other Linux distros and versions.
It still assumes Python3 is installed.

### Selenium
The easiest one.
```
pip install selenium
```

### Firefox
It will be even easier if you know where to get a minified version.
```
sudo apt-get install -y firefox
```

### Gecko webdriver
Not too hairy once you've done it.

Download the webdriver:
```
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
```

Extract the file:
```
$ tar xvzf geckodriver-v0.24.0-linux64.tar.gz
```

Move to a dir that your $PATH knows about:
```
$ mv geckodriver /usr/local/bin/
```
or update $PATH:
```
$ export PATH=$PATH:/path/to/driver/geckodriver
```

### Make sure it runs
Open a python3 REPL.
```
>>> from selenium.webdriver import Firefox
>>> from selenium.webdriver.firefox.options import Options
>>> options = Options()
>>> options.headless = True
>>> ff = Firefox(options=options)
>>> ff.get("http://meggangreen.com")
>>> ff.title
':: meggangreen ::'
>>>ff.close()
```
