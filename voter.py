from selenium import webdriver

class Voter:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'/Users/ajayraj/Documents/WebDriver/geckodriver')

    def vote(self, email, name, mr_cursors, ms_cursors):
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfyCMOD7nJFfHlScuKuyhUmMc-gpUsK16wKYfGP5kdBcK2Ljg/viewform')
        self.driver.find_element_by_name('emailAddress').send_keys(email)
        self.driver.find_element_by_name('entry.1438007419').send_keys(name)
        self.driver.find_element_by_css_selector(
            ".quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl[data-value='%s']" % (mr_cursors)).click()
        self.driver.find_element_by_css_selector(
            ".quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl[data-value='%s']" % (ms_cursors)).click()

    def submit(self):
        self.driver.find_element_by_css_selector(".quantumWizButtonPaperbuttonLabel.exportLabel").click()

    def __del__(self):
        self.driver.quit()