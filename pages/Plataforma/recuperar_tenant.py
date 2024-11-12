from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RecuperarTenant(BasePage):
    EMAIL_BOX = (By.XPATH, "//input[@name='emailAddress' and @type='text']")

    ENVIAR_BUTTON = (By.XPATH,
                     "//button[@type='submit' and contains (@class, 'btn btn-primary btn-elevate "
                     "kt-login__btn-primary')]")

    ATRAS_BUTTON = (By.XPATH, "//button [text()=' Atrás' and @class='btn btn-light btn-elevate "
                              "kt-login__btn-secondary' ]")

    MSG = (By.XPATH, "//*[@id = 'swal2-title']")

    def navegar_recuperar_tenant(self):
        url = self.base_url + "/account/forgot-tenancyName"
        self.navigate_to(url)

    def get_current_url(self):
        return self.driver.current_url
    def get_base_url(self):
        return self.base_url
    def get_email_input(self):
        return self.wait_for_element(self.EMAIL_BOX)

    def get_enviar_button(self):
        return self.wait_for_element(self.ENVIAR_BUTTON)

    def enviar_button(self):
        self.click(self.ENVIAR_BUTTON)

    def get_atras_button(self):
        return self.wait_for_element(self.ATRAS_BUTTON)

    def atras_button(self):
        self.click(self.ATRAS_BUTTON)

    def set_input_email(self, email):
        self.type_text(self.EMAIL_BOX, email)

    def get_msg(self):
        return self.wait_for_element(self.MSG)
