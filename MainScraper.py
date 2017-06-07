from selenium import webdriver
import Config

# replace with .Firefox(), or with the browser of your choice
browser = webdriver.Chrome()
browser.implicitly_wait(10)
url = "https://my.wealthsimple.com/app/login"
browser.get(url)  # navigate to the page

emailForm = browser.find_element_by_name("email")
passForm = browser.find_element_by_name("password")

emailForm.send_keys(Config.User)
passForm.send_keys(Config.Pass)

submitButton = browser.find_element_by_css_selector(
    ".button.primary-action.size-md.base-margin-top-x3.ladda-button.no-mask")
submitButton.click()

# navigate to page behind login
browser.get("https://my.wealthsimple.com/app/portfolio")
balanceSpan = browser.find_element_by_css_selector(".value.ng-binding")

print balanceSpan.text

browser.quit()
