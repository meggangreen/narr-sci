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
