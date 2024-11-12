from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RecuperarClave(BasePage):
    TENANT_BOX = (By.NAME, "tenancyName")
    EMAIL_BOX = (By.NAME, "emailAddress")

    ENVIAR_BUTTON = (By.XPATH,
                     "//button[@type='submit' and contains (@class, 'btn btn-primary btn-elevate "
                     "kt-login__btn-primary')]")
    ATRAS_BUTTON = (By.XPATH, "//*[@id='kt_login']/div/div[2]/div[2]/ng-component/div/form/div[3]/button[1]")

    ERROR_MSG = (By.XPATH, "//*[@id = 'swal2-title']")

    def navegar_recuperar_contrasena(self):
        url = self.base_url + "/account/forgot-password"
        self.navigate_to(url)
    def get_current_url(self):
        return self.driver.current_url
    def get_base_url(self):
        return self.base_url
    def get_tenant_input(self):
        return self.wait_for_element(self.TENANT_BOX)

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

    def set_input_datos(self, tenant, email):
        # Limpia los campos de texto
        self.type_text(self.TENANT_BOX, tenant)
        self.type_text(self.EMAIL_BOX, email)

    def set_input_tenant(self, tenant):
        # Limpia los campos de texto
        self.type_text(self.TENANT_BOX, tenant)

    def set_input_email(self, email):
        self.type_text(self.EMAIL_BOX, email)

    def get_error_tenant_email_novalido_msg(self):
        return self.wait_for_element(self.ERROR_MSG)

