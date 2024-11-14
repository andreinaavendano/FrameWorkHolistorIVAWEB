import time

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver: object, base_url: object, datos_usuario: object) -> object:
        self.driver = driver
        self.base_url = base_url
        print(f"Datos de usuario: {datos_usuario} ")
        self.datos_usuario = datos_usuario

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=12):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait_for_element(locator).click()

    def type_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def select_from_dropdown_by_visible_text(self, locator, text):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)

    def select_from_dropdown_by_index(self, locator, index):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_index(index)

    def get_select_options(self, locator):
        dropdown = Select(self.wait_for_element(locator))
        return [option.text for option in dropdown.options]

    def select_element(self, locator):
        element = self.wait_for_element(locator)
        if not element.is_selected():
            element.click()

    def unselect_checkbox(self, locator):
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()

    def hover_over_element(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def reload_page(self):
        self.driver.refresh()

    def is_disabled(self, locator):
        try:
            element = self.wait_for_element(locator)
            return 'disabled' in element.get_attribute('class').split()
        except TimeoutException:
            return False

    def get_name_handle(self, driver):
        return self.driver.current_window_handle

    def swtich_page(self, ventana_original, driver):

        time.sleep(20)
        ventanas = self.driver.window_handles
        for ventana in ventanas:
            if ventana != ventana_original:
                return self.driver.switch_to.window(ventana)

    def title_page(self):
        return self.driver.title

    # Método para obtener la URL actual
    def get_current_url(self):
        return self.driver.current_url

    def close(self):
        ventana_original = self.get_name_handle(self.driver)
        self.driver.close()
        self.swtich_page(ventana_original, self.driver)

    def move_to_element(self, element, timeout=5):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().pause(timeout).perform()
    def hover_element_clic(self, locator):
        element = self.wait_for_element(locator)
        self.move_to_element(element)
        #actions = ActionChains(self.driver)
        #actions.move_to_element(element).click().pause(10).perform()

    def wait_for_presente(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    def hover_element_clic_presente(self, locator):
        element = self.wait_for_presente(locator)
        self.move_to_element(element)

        #actions = ActionChains(self.driver)
        #actions.move_to_element(element).click().pause(10).perform()
