import pytest
import allure
from pages.PDE.home_page_holistor_pde import HomePageHolistorPDE
from pages.PDE.abm_dependencia_dgi import ABM_Dependencia_DGI


@pytest.fixture
def abm_dependencia_dgi(browser, base_url, datos_usuario):
    return ABM_Dependencia_DGI(browser, base_url, datos_usuario)


@pytest.fixture(scope="function")
def setup(abm_dependencia_dgi):
    return abm_dependencia_dgi.iniciar()


@allure.suite("Casos de Prueba Dependencia DGI")
@allure.epic("Archivos")
@allure.feature("Datos Generales")
@allure.story("US: ABM Dependencia DGI")
@allure.testcase("TC - 0001")
@allure.title("Verificar item de menu")
@allure.description("Este test verifica que se pueda ingresar al item de menu")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dependencia_dgi
@pytest.mark.regresion
def test_ingresar_menu(abm_dependencia_dgi, setup):

    URL = "https://pde-qa.holistorsaas.com.ar/agenda.wwdepdgi.aspx"
    titulo_esperado = 'Dependencias DGI'
    
    with allure.step("Dado que navego al menu Dependencias DGI obtengo el ingreso a la pagina Dep_DGI"):
        resultado = abm_dependencia_dgi.selected_item_menu_dgi()
        assert resultado in URL, "La pagina no corresponde con la esperada"
    with allure.step("Puedo observar el titulo de la pagina principal"):
        titulo = abm_dependencia_dgi.get_titulo()
        assert titulo == titulo_esperado, "El titulo no se corresponde con el esperado"
    abm_dependencia_dgi.close()
    #abm_dependencia_dgi.close()

@allure.suite("Casos de Prueba Dependencia DGI")
@allure.epic("Archivos")
@allure.feature("Datos Generales")
@allure.story("US: ABM Dependencia DGI")
@allure.testcase("TC - 0002")
@allure.title("Circutio Completo ABMC")
@allure.description("Este test verifica que se pueda ingresar, buscar, visualizar, modificar y eliminar un item con "
                    "datos correctos y requeridos")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dependencia_dgi
@pytest.mark.regresion
def test_abmc(abm_dependencia_dgi, setup):

    URL = "https://pde-qa.holistorsaas.com.ar/agenda.wwdepdgi.aspx"
    # datos prueba insert
    codigo_dgi = "TST"
    descripcion = "TSTCRUD"
    # datos prueba actualizar
    act_descripcion = "TSTCRUD_ACTUALIZADA"
    texto_esperado_ingreso = f'La dependencias dgi {descripcion} fue creada'
    texto_esperado_modificar = f'La dependencias dgi {act_descripcion} fue actualizada'
    texto_esperado_eliminar = 'Confirme la eliminación de los datos.'
    texto_esperado_eliminado = f'La dependencias dgi {act_descripcion} fue eliminada'
    with allure.step("Dado que navego al menu Dependencias DGI obtengo el ingreso a la pagina Dep_DGI"):
        abm_dependencia_dgi.navegar_dgi()

    with allure.step("Podemos ingresar un nuevo item"):
        resultado = abm_dependencia_dgi.add_item(codigo_dgi, descripcion)
        assert resultado in texto_esperado_ingreso, "No se muestra el texto de ingreso esperado"
        assert abm_dependencia_dgi.get_current_url() in URL, ("No se pudo agregar el nuevo item y volver a la pagina "
                                                              "principal")
        abm_dependencia_dgi.cerrar_msg_popup()
    with allure.step("Podemos buscar el item recien ingresado"):
        resultado = abm_dependencia_dgi.search_item(codigo_dgi)
        assert resultado == codigo_dgi, "No se pudo buscar el nuevo item"

    with allure.step("Podemos visualizar el item recien ingresado y comprobar que tiene los datos enviados"):
        resultado_visualizar = abm_dependencia_dgi.visualizar_item()
        assert resultado_visualizar["codigo_obtenido"] == codigo_dgi, "El codigo no es el correcto"
        assert resultado_visualizar["descripcion_obtenido"] == descripcion, "La descripcion no es la correcta"

    with allure.step("Volver a la pantalla principal "):
        assert abm_dependencia_dgi.volver_pantalla_principal() in URL, "No pudo volver a la pagina Principal"

    with allure.step("Buscar el item recien ingresado"):
        resultado = abm_dependencia_dgi.search_item(codigo_dgi)
        assert resultado == codigo_dgi, "No se pudo buscar el item actualizado"

    with allure.step("Modificar el item recien ingresado"):
        resultado = abm_dependencia_dgi.modificar_item(act_descripcion)
        assert resultado in texto_esperado_modificar, "No se muestra el texto de ingreso esperado"
        assert abm_dependencia_dgi.get_current_url() in URL, ("No se pudo agregar el nuevo item y volver a la pagina "
                                                              "principal")
        abm_dependencia_dgi.cerrar_msg_popup()

    with allure.step("Buscar el item recien ingresado"):
        resultado = abm_dependencia_dgi.search_item(codigo_dgi)
        assert resultado == codigo_dgi, "No se pudo buscar el item actualizado"

    with allure.step("Eliminar el item recien modificado"):
        resultado = abm_dependencia_dgi.eliminar_item()
        assert resultado["pedir_confirmacion"] in texto_esperado_eliminar, "El mensaje para pedir confirmación de eliminación no es el esperado"
        assert resultado["eliminacion"] in texto_esperado_eliminado, "El mensaje para informar la eliminacion del item no es el esperado"
        assert abm_dependencia_dgi.get_current_url() in URL, ("No se pudo eliminar y volver a la pagina principal")
        abm_dependencia_dgi.cerrar_msg_popup()

@allure.suite("Casos de Prueba Dependencia DGI")
@allure.epic("Archivos")
@allure.feature("Datos Generales")
@allure.story("US: ABM Dependencia DGI")
@allure.testcase("TC - 0003")
@allure.title("Agregar /Cancelar ")
@allure.description("Este test verifica que se pueda cancelar el proceso de alta de un item")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dependencia_dgi
@pytest.mark.regresion
def test_nuevo_cancelar(abm_dependencia_dgi, setup):
    URL = "https://pde-qa.holistorsaas.com.ar/agenda.wwdepdgi.aspx"
    #datos prueba insert
    codigo_dgi = "TST"
    descripcion = "TSTCRUD"
    with allure.step("Dado que navego al menu Dependencias DGI obtengo el ingreso a la pagina Dep_DGI"):
        abm_dependencia_dgi.navegar_dgi()

    with allure.step("Podemos ingresar a dar de alta y cancelar el proceso"):
        resultado = abm_dependencia_dgi.add_item_cancelar(codigo_dgi, descripcion)
        assert resultado in URL, "No se pudo agregar el nuevo item y vovler a la pagina principal"

    with allure.step("Podemos buscar el item para verificar que no se ingresa el nuevo item, "
                     "luego de haber cancelado"):
        resultado = abm_dependencia_dgi.search_no_item(codigo_dgi)
        assert resultado == "No hay resultados", "Ingresó el item nuevo cuando se hizo clic en cancelar"
@allure.suite("Casos de Prueba Dependencia DGI")
@allure.epic("Archivos")
@allure.feature("Datos Generales")
@allure.story("US: ABM Dependencia DGI")
@allure.testcase("TC - 0004")
@allure.title("Agregar/Sin Datos obligatorios")
@allure.description("Este test verifica que no se pueda agregar un item sin los datos obligatorios")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dependencia_dgi
@pytest.mark.regresion
def test_nuevo_sin_datos_obligatorios(abm_dependencia_dgi, setup):

    URL = "https://pde-qa.holistorsaas.com.ar/agenda.entitymanagerdepdgi.aspx"
    with allure.step("Dado que navego al menu Dependencias DGI obtengo el ingreso a la pagina Dep_DGI"):
        abm_dependencia_dgi.navegar_dgi()
    with allure.step("Intento Agregar un item sin los datos obligatorios"):
        resultado = abm_dependencia_dgi.add_item_sin_datos_obligatorios()
    with allure.step("Se puede verificar que el sistema muestra los mensajes de error y no permite la carga"):
        assert resultado["message_visible"] == "Descripción es obligatorio", "El mensaje de error no es el esperado"
        assert resultado["popup_visible"] == "Descripción es obligatorio", "El mensaje popup no es el esperado"
        assert URL in abm_dependencia_dgi.get_current_url(), "El sistema abrio una nueva pagina de forma incorrecta"

@allure.suite("Casos de Prueba Dependencia DGI")
@allure.epic("Archivos")
@allure.feature("Datos Generales")
@allure.story("US: ABM Dependencia DGI")
@allure.testcase("TC - 0005")
@allure.title("Agregar/Item con codigo duplicado")
@allure.description("Este test verifica que no se pueda agregar un item cuyo identificador unico ya existe")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dependencia_dgi
@pytest.mark.regresion
def test_nuevo_cod_existente(abm_dependencia_dgi, setup):
    URL = "https://pde-qa.holistorsaas.com.ar/agenda.wwdepdgi.aspx"
    # datos prueba insert
    codigo_dgi = "TST"
    descripcion = "TSTCRUD"
    texto_esperado_ingreso = f'La dependencias dgi {descripcion} fue creada'
    texto_esperado_duplicado = 'Ya existe el registro'
    with allure.step("Dado que navego al menu Dependencias DGI obtengo el ingreso a la pagina Dep_DGI"):
        abm_dependencia_dgi.navegar_dgi()
    with allure.step("Ingreso el nuevo item"):
        resultado = abm_dependencia_dgi.add_item(codigo_dgi, descripcion)
        assert resultado in texto_esperado_ingreso, "No se muestra el texto de ingreso esperado"
        abm_dependencia_dgi.cerrar_msg_popup()
    with allure.step("Se intenta ingresa un nuevo item con el mismo identificador unico ya ingresado"):
        resultado = abm_dependencia_dgi.add_item_duplicado(codigo_dgi, descripcion)
        assert resultado in texto_esperado_duplicado, "No realizo la validación de codigo duplicado"
        abm_dependencia_dgi.cerrar_msg_popup()

    ##pasos luego de la prueba
    with allure.step("Se regresa a la pagina principal se busca el item y luego se elimina el item."):
        abm_dependencia_dgi.cancelar()
        abm_dependencia_dgi.search_item(codigo_dgi)
        abm_dependencia_dgi.eliminar_item()
