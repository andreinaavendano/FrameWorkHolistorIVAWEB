from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPlataformaPage(BasePage):
    TENANT_BOX = (By.NAME, "tenancyName")
    USERNAME_BOX = (By.NAME, "userNameOrEmailAddress")
    PASSWORD_BOX = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Iniciar sesión' and @type='submit']")

    RECUERDAME_CHEKBOX = (By.XPATH, "//span[@class ='ng-tns-c3-1']")
    RECUERDAME_LABEL = (By.XPATH, "//label[contains(., 'Recuérdame')]")

    # Localizadores de los enlaces de recuperación Password
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Olvidó la contraseña?']")

    # Localizadores de los enlaces de recuperación Tenant
    FORGOT_TENANT_LINK = (By.XPATH, "//a[text()='Olvidó su espacio de trabajo?']")

    # Localizador que indica que la página de login ha cargado
    TENANT_TEXTO = (By.XPATH, "//*[@id='kt_header']/topbar/div/div[3]/div/div/span/span")
    USUARIO_TEXTO = (By.XPATH, "//*[@id='kt_header']/topbar/div/div[3]/div/div/span")
    SALIR_BUTTON = (By.XPATH, "//a[text()='Salir']")

    # Localizadores de Credenciales Incorrectas
    ERROR_LOGIN_TITLE = (By.XPATH, "// *[@id = 'swal2-title']")
    ERROR_LOGIN_MSG = (By.XPATH, "// *[@id = 'swal2-content']")
    ERROR_LOGIN_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'swal2-confirm swal2-styled')]")

    # Localizadores de Tenant No existe
    ERROR_LOGIN_TENANT_MSG = (By.XPATH, "//*[@id = 'swal2-title']")



    def navegar_login_plataforma(self):
        url = self.base_url + "/account/login"
        self.navigate_to(url)

    def get_tenant_input(self):
        return self.wait_for_element(self.TENANT_BOX)

    def get_username_input(self):
        return self.wait_for_element(self.USERNAME_BOX)

    def get_password_input(self):
        return self.wait_for_element(self.PASSWORD_BOX)

    def get_recuerdame_checkbox(self):
        return self.wait_for_element(self.RECUERDAME_CHEKBOX)

    def get_recuerdame_label_checkbox(self):
        return self.wait_for_element(self.RECUERDAME_LABEL)

    def get_login_button(self):
        return self.wait_for_element(self.LOGIN_BUTTON)

    def get_olvido_pass_link(self):
        return self.wait_for_element(self.FORGOT_PASSWORD_LINK)

    def olvido_pass_link_clic(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    def get_olvido_tenant_link(self):
        return self.wait_for_element(self.FORGOT_TENANT_LINK)

    def olvido_tenant_link_clic(self):
        return self.click(self.FORGOT_TENANT_LINK)

    def get_tenant_login_ok(self):
        return self.wait_for_element(self.TENANT_TEXTO)

    def get_usuario_login_ok(self):
        return self.wait_for_element(self.USUARIO_TEXTO)

    def get_error_login_title(self):
        return self.wait_for_element(self.ERROR_LOGIN_TITLE)

    def get_error_login_msg(self):
        return self.wait_for_element(self.ERROR_LOGIN_MSG)

    def get_error_login_tenant_msg(self):
        return self.wait_for_element(self.ERROR_LOGIN_TENANT_MSG).text

    def get_error_login_button_clic(self):
        return self.click(self.ERROR_LOGIN_BUTTON)

    def set_user_inputs(self, tenant, usuario, password):
        self.type_text(self.TENANT_BOX, tenant)
        self.type_text(self.USERNAME_BOX, usuario)
        self.type_text(self.PASSWORD_BOX, password)

    def iniciar_sesion_button(self):
        self.click(self.LOGIN_BUTTON)

    def usuario_clic(self):
        self.click(self.USUARIO_TEXTO)

    def log_out(self):
        self.click(self.SALIR_BUTTON)

    def login(self):
        self.navegar_login_plataforma()
        self.set_user_inputs(self.datos_usuario["tenan"], self.datos_usuario["usuario"], self.datos_usuario["clave"])
        self.iniciar_sesion_button()
