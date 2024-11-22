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

    #Agregar
    ADD_BUTTON = (By.XPATH, "// *[@id = 'INSERT']")
    CODIGO_DGI_TEXT = (By.XPATH, "//*[@type = 'text' and @id='W0041W0029DEPDGICOD']")
    DESCRIPCION_DGI_TEXT = (By.XPATH, "//*[@type = 'text' and @id='W0041W0029DEPDGIDESC']")
    ACEPTAR_BUTTON = (By.XPATH, "//* [@type='button' and @id = 'W0041W0029ENTER']")
    CANCELAR_AGREGAR_BUTTON = (By.XPATH, "//* [@type='button' and @id = 'W0041W0029CANCEL']")

    #Mensajes de error y pop up
    MSG_ERR_DESCRIPCION_OBL = (By.XPATH, "// span[@class='ErrorMessages'  and @id='W0041W0029DEPDGIDESC_Balloon']")
    MSG_POPUP = (By.XPATH, "//div[@class='toast-message']")
    MSG_POPUP_CERRAR = (By.XPATH, "//button[@class='toast-close-button']")
    #MSG_ERR_CODIGO_OBL = (By.XPATH, "// span[@class='ErrorMessages'  and @id='W0041W0029TR_CODIGO_Balloon']")
    #Buscar
    BUSCAR_TEXT = (By.ID, "vK2BTOOLSGENERICSEARCHFIELD")
    GRID_ITEMS = (By.XPATH, "// table[@id = 'GridContainerTbl']")
    GRID_NO_ITEMS = (By.XPATH, "//table[@id= 'NORESULTSFOUNDTABLE']/tbody/tr[1]/td[1]/span")
    ITEM1_GRID = (By.XPATH, "// span[ @ id = 'span_DEPDGICOD_0001']")

    #Actualizar
    IMG_ACTUALIZAR_GRID = (By.XPATH, "// img[@id = 'vUPDATE_0001']")
    TITULO_TABLA = (By.XPATH, "//span[@class='PopupTitle' and @id = 'COMPONENTTITLE']")
    ACT_DESCRIPCION_DGI_TEXT = (By.XPATH, "//*[@type = 'text' and @id='W0067DEPDGIDESC']")
    MODIFICAR_BUTTON = (By.XPATH, "//input[@type='button' and @id = 'W0067ENTER']")
    CANCELAR_MODIFICAR_BUTTON = (By.XPATH, "//input[@type='button' and @id = 'W0067CANCEL']")

    #Eliminar
    IMG_ELIMINAR_GRID = (By.XPATH, "// img[@id = 'vDELETE_0001']")
    ELIMINAR_BUTTON = (By.XPATH, "//input[@type='button' and @id = 'W0067ENTER']")
    CANCELAR_ELIMINAR_BUTTON = (By.XPATH, "//input[@type='button' and @id = 'W0067CANCEL']")

    #Visualizar
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

    def navegar_dgi(self):
        self.driver.get(self.URL)

    def selected_item_menu_dgi(self):
        self.move_to_element(self.wait_for_element(self.MENU_PPAL_BUTTON))
        self.move_to_element(self.wait_for_element(self.MENU_ARCHIVO_BUTTON))
        self.move_to_element(self.wait_for_element(self.MENU_DATOS_GENERALES))
        self.move_to_element(self.wait_for_element(self.MENU_DEP_DGI))
        return self.get_current_url()

    def get_titulo(self):
        return self.wait_for_element(self.TITULO_DEP_DGI).text

    def add_item(self, codigo_dgi, descripcion):
        self.click(self.ADD_BUTTON)
        self.type_text(self.CODIGO_DGI_TEXT, codigo_dgi)
        self.type_text(self.DESCRIPCION_DGI_TEXT, descripcion)
        self.click(self.ACEPTAR_BUTTON)
        self.wait_for_element(self.ADD_BUTTON)
        return self.wait_for_element(self.MSG_POPUP).text

    def add_item_cancelar(self, codigo_dgi, descripcion):
        self.click(self.ADD_BUTTON)
        self.type_text(self.CODIGO_DGI_TEXT, codigo_dgi)
        self.type_text(self.DESCRIPCION_DGI_TEXT, descripcion)
        self.click(self.CANCELAR_AGREGAR_BUTTON)
        self.wait_for_element(self.ADD_BUTTON)
        return self.get_current_url()

    def add_item_sin_datos_obligatorios(self):
        self.click(self.ADD_BUTTON)
        self.type_text(self.CODIGO_DGI_TEXT, 'prueba')
        self.click(self.ACEPTAR_BUTTON)
        popup_visible = self.wait_for_element(self.MSG_ERR_POPUP).text
        message_visible = self.wait_for_element(self.MSG_ERR_DESCRIPCION_OBL).text
        return {
            "popup_visible": popup_visible,
            "message_visible": message_visible
        }

    def add_item_duplicado(self, codigo_dgi, descripcion):
        self.click(self.ADD_BUTTON)
        self.type_text(self.CODIGO_DGI_TEXT, codigo_dgi)
        self.type_text(self.DESCRIPCION_DGI_TEXT, descripcion)
        self.click(self.ACEPTAR_BUTTON)
        popup_visible = self.wait_for_element(self.MSG_POPUP).text
        return popup_visible

    def search_item(self, codigo_dgi):
        self.type_text(self.BUSCAR_TEXT, codigo_dgi)
        time.sleep(10)
        return self.wait_for_element(self.ITEM1_GRID).text

    def search_no_item(self, codigo_dgi):
        self.type_text(self.BUSCAR_TEXT, codigo_dgi)
        time.sleep(10)
        return self.wait_for_element(self.GRID_NO_ITEMS).text

    def visualizar_item(self):
        self.hover_element_clic_presente(self.IMG_VISUALIZAR_GRID)

        codigo_obtenido = self.wait_for_element(self.VIS_CODIGO_DGI_TEXTGRID).text
        descripcion_obtenido = self.wait_for_element(self.VIS_DESCRIPCION_DGI_TEXTGRID).text
        return {"codigo_obtenido": codigo_obtenido
            , "descripcion_obtenido": descripcion_obtenido}

    def volver_pantalla_principal(self):
        self.click(self.VOLVER_HREF)
        self.wait_for_element(self.ADD_BUTTON)
        return self.get_current_url()

    def modificar_item(self, act_descripcion):
        self.hover_element_clic_presente(self.IMG_ACTUALIZAR_GRID)
        #self.move_to_element(self.IMG_ACTUALIZAR_GRID)
        self.wait_for_element(self.TITULO_TABLA)

        self.type_text(self.ACT_DESCRIPCION_DGI_TEXT, act_descripcion)
        self.click(self.MODIFICAR_BUTTON)
        self.wait_for_element(self.ADD_BUTTON)
        return self.wait_for_element(self.MSG_POPUP).text

    def eliminar_item(self):
        self.hover_element_clic_presente(self.IMG_ELIMINAR_GRID)
        self.wait_for_element(self.TITULO_TABLA)
        pop_visible_pedir_confirmacion = self.wait_for_element(self.MSG_POPUP).text
        self.cerrar_msg_popup()
        self.click(self.ELIMINAR_BUTTON)
        self.wait_for_element(self.ADD_BUTTON)
        pop_visible_eliminacion = self.wait_for_element(self.MSG_POPUP).text
        return {"pedir_confirmacion": pop_visible_pedir_confirmacion,
                "eliminacion": pop_visible_eliminacion
                }

    def cerrar_msg_popup(self):
        self.click(self.MSG_POPUP_CERRAR)

    def cancelar(self):
        self.click(self.CANCELAR_AGREGAR_BUTTON)
