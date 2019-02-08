import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

url='http://reddit.com'

driver.get(url)

def assert_element_is_dropdown(element):

	if element.get_attribute('type') not in ['select-one', 'select-multi']:
		raise AssertionError('The element is not a dropdown')
	return


def select_from_dropdown_by_visible_text(element, select_text)

reddit_search = driver.find_element('id', 'header-search-bar')

reddit_search.send_keys('tarot')
reddit_search.send_keys(Keys.ENTER)

driver.find_element('id', 'search-results-sort')

# why can't it find this obvious element?

# more dropdowns later