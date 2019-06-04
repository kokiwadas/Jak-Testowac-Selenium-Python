from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import time
import allure
from allure_commons.types import AttachmentType


class ScreenshotListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        make_screenshot(driver, exception)


def make_screenshot(driver, producer):
    screenshot_path = rf'testScreenshots\{producer}_exception_{time.time()}.png'
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    print(f'Screenshot saved as {screenshot_path}')
