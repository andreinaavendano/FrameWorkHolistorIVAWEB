import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.PDE.home_page_holistor_pde import HomePageHolistorPDE


class ABM_Dependencia_DGI(BasePage):
    MENU_PPAL_BUTTON = (By.ID, "BTNTOGGLEMENU_MPAGE")

    MENU_ARCHIVO_BUTTON = (By.XPATH, "//span[@class='sidebar-nav-item' and (text()='Archivo')]")

    MENU_DATOS_GENERALES = (By.XPATH, "//span [@class='sidebar-nav-item' and (text()='Datos Generales')]")

    MENU_DEP_DGI = (By.XPATH, "//span [@class='sidebar-nav-item' and (text()='Dependencias DGI')]")

    URL = "https://pde-qa.holistorsaas.com.ar/agenda.wwdepdgi.aspx"
    TITULO_DEP_DGI = (By.XPATH, "//span[@id='PGMDESCRIPTORTEXTBLOCK']")

    ADD_BUTTON = (By.XPATH, "// *[@id = 'INSERT']")
    CODIGO_DGI_TEXT = (By.XPATH, "//*[@type = 'text' and @id='W0041W0029DEPDGICOD']")
    DESCRIPCION_DGI_TEXT = (By.XPATH, "//*[@type = 'text' and @id='W0041W0029DEPDGIDESC']")
    ACEPTAR_BUTTON = (By.XPATH, "//* [@type='button' and @id = 'W0041W0029ENTER']")

    BUSCAR_TEXT = (By.ID, "vK2BTOOLSGENERICSEARCHFIELD")
    ITEM1_GRID = (By.XPATH, "// span[ @ id = 'span_DEPDGICOD_0001']")

    IMG_ACTUALIZAR_GRID = (By.XPATH, "// img[@id = 'vUPDATE_0001']")
    TITULO_TABLA = (By.XPATH, "//span[@class='PopupTitle' and @id = 'COMPONENTTITLE']")
    ACT_DESCRIPCION_DGI_TEXT = (By.XPATH, "//*[@type = 'text' and @id='W0067DEPDGIDESC']")
    MODIFICAR_BUTTON = (By.XPATH, "//input[@type='button' and @id = 'W0067ENTER']")

    IMG_ELIMINAR_GRID = (By.XPATH, "// img[@id = 'vDELETE_0001']")
    ELIMINAR_BUTTON = (By.XPATH, "//input[@type='button' and @id = 'W0067ENTER']")

    IMG_VISUALIZAR_GRID = (By.XPATH, "// img[@id = 'vDISPLAY_0001']")
    VIS_CODIGO_DGI_TEXTGRID = (By.XPATH, "// span[@id = 'span_W0041W0029DEPDGICOD']")
    VIS_DESCRIPCION_DGI_TEXTGRID = (By.XPATH, "// span[@id = 'span_W0041W0029DEPDGIDESC']")
    VOLVER_HREF = (By.XPATH, "// *[@id = 'BACKTOWORKWITH']/a")

    #datos prueba insert
    codigo_dgi = "TST"
    descripcion = "TSTCRUD"
    # datos prueba actualziar
    act_descripcion = "TSTCRUD_ACTUALIZADA"

    def iniciar(self):
        home = HomePageHolistorPDE(self.driver, self.base_url, self.datos_usuario)
        home.navegar_pde()

    def selected_item_menu_dgi(self):
        self.move_to_element(self.wait_for_element(self.MENU_PPAL_BUTTON))
        self.move_to_element(self.wait_for_element(self.MENU_ARCHIVO_BUTTON))
        self.move_to_element(self.wait_for_element(self.MENU_DATOS_GENERALES))
        self.move_to_element(self.wait_for_element(self.MENU_DEP_DGI))
        if self.get_current_url() == self.URL:
            return True
        else:
            return False

    def get_titulo(self):
        return self.wait_for_element(self.TITULO_DEP_DGI).text

    def add_item(self):
        self.click(self.ADD_BUTTON)
        self.type_text(self.CODIGO_DGI_TEXT, self.codigo_dgi)
        self.type_text(self.DESCRIPCION_DGI_TEXT, self.descripcion)
        self.click(self.ACEPTAR_BUTTON)
        self.wait_for_element(self.ADD_BUTTON)
        if self.get_current_url() == self.URL:
            return True
        else:
            return False

    def search_item(self):
        self.type_text(self.BUSCAR_TEXT,self.codigo_dgi)
        time.sleep(10)
        resultado = self.wait_for_element(self.ITEM1_GRID).text
        if resultado == self.codigo_dgi:
            return True
        else:
            return False

    def visualizar_item(self):
        self.hover_element_clic_presente(self.IMG_VISUALIZAR_GRID)
        ban = True
        codigo_obtenido = self.wait_for_element(self.VIS_CODIGO_DGI_TEXTGRID).text
        descripcion_obtenido = self.wait_for_element(self.VIS_DESCRIPCION_DGI_TEXTGRID).text
        if codigo_obtenido == self.codigo_dgi:
            print("Codigo correcto")
        elif descripcion_obtenido == self.descripcion:
            print("Descripcion correcto")
        else:
            ban = False

        self.click(self.VOLVER_HREF)
        self.wait_for_element(self.ADD_BUTTON)
        if self.get_current_url() == self.URL and ban:
            return True
        else:
            return False

    def modificar_item(self):
        self.hover_element_clic_presente(self.IMG_ACTUALIZAR_GRID)
        #self.move_to_element(self.IMG_ACTUALIZAR_GRID)
        self.wait_for_element(self.TITULO_TABLA)

        self.type_text(self.ACT_DESCRIPCION_DGI_TEXT, self.act_descripcion)
        self.click(self.MODIFICAR_BUTTON)
        self.wait_for_element(self.ADD_BUTTON)
        if self.get_current_url() == self.URL:
            return True
        else:
            return False

    def eliminar_item(self):
        self.hover_element_clic_presente(self.IMG_ELIMINAR_GRID)
        self.wait_for_element(self.TITULO_TABLA)
        self.click(self.ELIMINAR_BUTTON)
        self.wait_for_element(self.ADD_BUTTON)
        if self.get_current_url() == self.URL:
            return True
        else:
            return False

