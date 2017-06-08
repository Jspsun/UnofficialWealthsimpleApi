from selenium import webdriver
import Config


class Scraper(object):

    def __init__(self):
        # replace with .Firefox(), or with the browser of your choice
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(15)
        self.depth = 0

    def getBalance(self, username, password):
        self.depth += 1
        if self.depth >= 3:
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
            self.browser.get("https://my.wealthsimple.com/app/portfolio")
            balanceSpan = self.browser.find_element_by_css_selector(
                ".value.ng-binding")

            if balanceSpan.text == "":
                return self.getBalance(username, password)

            return '$' + balanceSpan.text
        except:
            print "caught exception"
            return self.getBalance(username, password)

    def cleanup(self):
        self.depth = 0
        self.browser.quit()

# if __name__ == "__main__":
#     s = Scraper()
#     print s.getBalance(Config.User, Config.Pass)
#     s.cleanup()
