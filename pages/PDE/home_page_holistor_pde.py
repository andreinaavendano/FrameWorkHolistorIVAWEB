from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.Plataforma.login_plataforma_page import LoginPlataformaPage


class HomePageHolistorPDE(BasePage):
    PDE_IMAGEN_BUTTON = (By.XPATH, "//img[@src='/assets/common/images/holistor/planificacion-estudios-logo.png']")
    GES_IMAGEN_BUTTON = (By.XPATH, "//img[@src='/assets/common/images/holistor/gestionERP-logo.png']")

    #Locator imagen de SYJ Home page baner principal.
    PDE_IMAGEN_LOGO_HP = (By.ID, "K2BAPPLICATIONICON_MPAGE")

    #Lupa para seleccionar empresa
    IMG_LUPA_SELECT_EMPRESA = (By.XPATH, "//img[@id='IMAGE1_MPAGE']")
    #Seleccionar la empresa de la fila 1
    ROW1_SELECT_EMPRESA = (By.XPATH, "//img[@id='vACTION_ACTION_0001' and @class='Image_Action']")
    BUSCADOR_TYPE_TEXT = (By.ID, "vGENERICFILTER_GRID")

    EMPRESA_SELECCIONADA = (By.XPATH, "//span[@id='EMPRESA_MPAGE']")

    def navegar_plataforma(self):
        login_plataforma = LoginPlataformaPage(self.driver, self.base_url, self.datos_usuario)
        login_plataforma.login()

    def navegar_pde(self):
        self.navegar_plataforma()
        self.open_pde()
    def get_current_url(self):
        return self.driver.current_url

    def is_pde_tenant(self):
        if self.wait_for_element(self.PDE_IMAGEN_BUTTON).is_displayed():
            return True
        else:
            return False

    def is_pde_user_enabled(self):
        return self.is_disabled(self.PDE_IMAGEN_BUTTON)

    def open_pde(self):
        ventana_plataforma = self.get_name_handle(self.driver)
        self.click(self.PDE_IMAGEN_BUTTON)
        self.swtich_page(ventana_plataforma, self.driver)
        return self.wait_for_element(self.PDE_IMAGEN_LOGO_HP).is_displayed()

    def open_select_empresa(self):
        #posiciona y hace clic en la lupa
        self.hover_element_clic(self.IMG_LUPA_SELECT_EMPRESA)
        #cambio al iframe seleccionar empresa
        self.driver.switch_to.frame(self.driver.find_elements(By.XPATH, "//iframe[@id='gxp0_ifrm']")[0])

        """if "Seleccionar Empresa" in self.driver.page_source:
            print("Cambio exitoso al iframe.")
        else:
            print("Puede que aún estés en el contexto principal.")
        """
        # posiciona y hace clic en la empresa fila 1
        self.hover_element_clic_presente(self.ROW1_SELECT_EMPRESA)
        #Volver a la HP 0o salir del iframe
        self.driver.switch_to.default_content()
        #trae el nombre de la empresa seleccionada.
        text = self.wait_for_element(self.EMPRESA_SELECCIONADA).text
        return text






