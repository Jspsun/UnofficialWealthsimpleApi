from selenium import webdriver
import os

class Scraper(object):

    def __init__(self):

        if os.environp['GOOGLE_CHROME_SHIM']:
            self.browser = webdriver.Chrome(os.environp['GOOGLE_CHROME_SHIM'])
        else:
            self.browser = webdriver.Chrome()

        self.browser.implicitly_wait(5)

    def getBalance(self, username, password, attemptsLeft):
        if attemptsLeft <= 0:
            return None
        try:
            # navigate to the page
            self.browser.get("https://my.wealthsimple.com/app/login")

            emailForm = self.browser.find_element_by_name("email")
            passForm = self.browser.find_element_by_name("password")

            emailForm.send_keys(username)
            passForm.send_keys(password)

            submitButton = self.browser.find_element_by_css_selector(
                ".button.primary-action.size-md.base-margin-top-x3.ladda-button.no-mask")
            submitButton.click()

            # navigate to page behind login
            balanceSpan = self.browser.find_element_by_css_selector(".value.ng-binding")

            if balanceSpan.text == "":
                return self.getBalance(username, password, attemptsLeft - 1)
            temp = balanceSpan.text.replace(',', '')
            return temp
        except:
            print "caught exception"
            return self.getBalance(username, password, attemptsLeft - 1)

    def cleanup(self):
        self.browser.quit()

# if __name__ == "__main__":
#     s = Scraper()
#     print s.getBalance(Config.User, Config.Pass)
#     s.cleanup()
