from Helper import properties
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = properties.get_settings()['DEFAULT-TIMEOUT']

def wait_until_presence_of_element_located( driver, locator ):
    return WebDriverWait( driver, TIMEOUT ).until( EC.presence_of_element_located( locator ) )

def wait_until_element_to_be_clickable( driver, locator ):
    return WebDriverWait( driver, TIMEOUT ).until( EC.element_to_be_clickable( locator ) )

def wait_until_text_to_be_present_in_element( driver, locator ):
    return WebDriverWait( driver, TIMEOUT ).until( EC.element_to_be_clickable( locator ) )