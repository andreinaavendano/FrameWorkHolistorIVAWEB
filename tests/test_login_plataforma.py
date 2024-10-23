import pytest
import allure
from pages.login_plataforma_page import LoginPlataformaPage


@pytest.fixture
def login_plataforma_page(browser, base_url):
    return LoginPlataformaPage(browser, base_url)


@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0001")
@allure.title("Campo tenant ok")
@allure.description("Este test verifica que se encuentra el input text Tenant")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
@pytest.mark.ui
def test_campo_tenant_ok(login_plataforma_page):
    with allure.step("Al navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()

    with allure.step("Se debe mostrar el campo Tenant"):
        resultado = login_plataforma_page.get_tenant_input().get_attribute('placeholder')

    with allure.step("Puedo verificar que se encuentra con el texto Nombre de espacio de trabajo *"):
        texto_tenant_esperado = 'Nombre de espacio de trabajo *'
        assert (texto_tenant_esperado in resultado
                ), "El texto esperado no coincide con el texto encontrado"


@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0002")
@allure.title("Campo usuario ok")
@allure.description("Este test verifica que se encuentra el input text Usuario")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
@pytest.mark.ui
def test_campo_nombre_usurio_ok(login_plataforma_page):
    with allure.step("Al navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()

    with allure.step("Se debe mostrar el campo Usuario"):
        resultado = login_plataforma_page.get_username_input().get_attribute('placeholder')

    with allure.step("Puedo verificar que se encuentra con el texto Nombre de espacio de trabajo *"):
        texto_usuario_esperado = 'Nombre de usuario o email *'
        assert (texto_usuario_esperado in resultado
                ), "El texto esperado no coincide con el texto encontrado"


@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0003")
@allure.title("Campo password ok")
@allure.description("Este test verifica que se encuentra el input text Usuario")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
@pytest.mark.ui
def test_campo_nombre_password_ok(login_plataforma_page):
    with allure.step("Al navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()

    with allure.step("Se debe mostrar el campo Password"):
        resultado = login_plataforma_page.get_password_input().get_attribute('placeholder')

    with allure.step("Puedo verificar que se encuentra con el texto Contraseña *"):
        texto_contrasena_esperado = 'Contraseña *'
        assert (texto_contrasena_esperado in resultado
                ), "El texto esperado no coincide con el texto encontrado"


@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0004")
@allure.title("Check box recuerdame existe")
@allure.description("Este test verifica que se encuentra el Check Box Recuérdame")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
@pytest.mark.ui
def test_checkRecuerdame_ok(login_plataforma_page):
    with allure.step("Navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()

    with allure.step("Se debe mostrar el CheckBox Recuérdame"):
        resultado = login_plataforma_page.get_recuerdame_checkbox()
        resultado_label = login_plataforma_page.get_recuerdame_label_checkbox()

    with allure.step("Se puede verificar que se muestra el checkBox con el texto Recuérdame"):
        label_recuerdame_esperado = "Recuérdame"
        # Realizar un assert para comprobar que el checkbox fue encontrado y es visible
        assert (resultado is not None), "El checkbox no se encontró."
        assert (resultado.is_enabled()), "El checkbox no está habilitado en pantalla."
        assert (label_recuerdame_esperado in resultado_label.text
                ), "El texto esperado no coincide con el texto encontrado "


@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0005")
@allure.title("Link Text Ref olvidó la contraseña existe")
@allure.description("Este test verifica que se encuentra el link con el texto correcto y se encuentre habilitado")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.login
@pytest.mark.ui
def test_link_text_olvido_contrasena_ok(login_plataforma_page):
    with allure.step("Navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()
    with allure.step("Se debe mostrar el Link text Olvidó la contraseña?"):
        resultado = login_plataforma_page.get_olvido_pass_link()
        resultado_link_text = login_plataforma_page.get_olvido_pass_link().text
        resultado_link_href = login_plataforma_page.get_olvido_pass_link().get_attribute('href')

    with allure.step("Se puede verificar que se muestra el link, se encuentra habilitado y tiene href esperado"):
        text_OlvidoPass_esperado = "Olvidó la contraseña?"
        href_esperado = "/account/forgot-password"
        # Realizar un assert para comprobar que el link tiene el texto y esta visible y  habilitado para clic
        assert (text_OlvidoPass_esperado in resultado_link_text), (
            "El texto esperado no coincide con el texto encontrado")
        assert (resultado.is_displayed()), "El link no esta visible"
        assert (href_esperado in resultado_link_href), f"El href {resultado_link_href}  no es el esperado"


@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0006")
@allure.title("Link Text Ref olvidó Espcio de trabajo existe")
@allure.description("Este test verifica que se encuentra el link con el texto correcto")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.login
@pytest.mark.ui
def test_link_text_olvido_tenant_ok(login_plataforma_page):
    with allure.step("Navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()

    with allure.step("Se debe mostrar el Link text Olvidó la contraseña?"):
        resultado = login_plataforma_page.get_olvido_tenant_link()
        resultado_link_text = login_plataforma_page.get_olvido_tenant_link().text
        resultado_link_href = login_plataforma_page.get_olvido_tenant_link().get_attribute('href')

    with allure.step("Se puede verificar que se muestra el link y tiene href esperado"):
        text_olvido_tenant_esperado = "Olvidó su espacio de trabajo?"
        href_esperado = "/account/forgot-tenancyName"
        # Realizar un assert para comprobar que el link tiene el texto y esta visible y  habilitado para clic
        assert (text_olvido_tenant_esperado in resultado_link_text
                ), "El texto esperado no coincide con el texto encontrado"
        assert (resultado.is_displayed()), "El link no esta visible"
        assert (href_esperado in resultado_link_href), f"El href {resultado_link_href}  no es el esperado"



@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0008")
@allure.title("Log incorrecto usurio o clave no son validas")
@allure.description("Este test verifica que no se puede loguear con datos usuario clave no validos")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
@pytest.mark.ui
def test_login_plataforma_error_usuario_clave(login_plataforma_page):
    # declaracion
    tenan = "Agenda22022022"
    usuario = "Andre"
    clave = "12qw"
    with allure.step("Navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()

    with allure.step("Setear los datos con credencial incorrectas en los campos Tenant, Usuario, Contraseña"):
        login_plataforma_page.set_user_inputs(tenan, usuario, clave)
        login_plataforma_page.iniciar_sesion_button()

    with ((allure.step("Muestra el pop up con el mensaje de error"))):
        TitleEsperado = "Inicio de sesión fallido!"
        MsgEsperado = "Nombre de usuario o contraseña incorrecta"
        resultado_title = login_plataforma_page.get_error_login_title().text
        resultado_msg = login_plataforma_page.get_error_login_msg().text
        assert (TitleEsperado in resultado_title
                ), "El titulo esperado no coincide con el texto encontrado"
        assert (MsgEsperado in resultado_msg
                ), "El mensaje de error esperado no coincide con el texto encontrado"

    with allure.step("Cerrar el mensaje pop up"):
        login_plataforma_page.get_error_login_button_clic()


@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0009")
@allure.title("Log incorrecto Tenant no existe")
@allure.description("Este test verifica que no se puede loguear en un tenant que no existe")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.login
@pytest.mark.ui
def test_login_plataforma_error_tenant(login_plataforma_page):
    # declaracion
    tenan = "Agenda220220"
    usuario = "Andreina"
    clave = "123qwe"
    with allure.step("Navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()

    with allure.step("Setear los datos correctos en los campos Tenant, Usuario, Contraseña"):
        login_plataforma_page.set_user_inputs(tenan, usuario, clave)
        login_plataforma_page.iniciar_sesion_button()

    with allure.step("Muestra el pop up con el mensaje de error"):
        MsgEsperado = f"No existe un Espacio de Trabajo con nombre {tenan}"
        resultado = login_plataforma_page.get_error_login_tenant_msg()
        assert (resultado in MsgEsperado), "El mensaje de error esperado no coincide con el texto encontrado"

    with allure.step("Muestra el pop up con el mensaje de error"):
        login_plataforma_page.get_error_login_button_clic()

@allure.suite("Casos de prueba de la pagina reports de Plataforma")
@allure.epic("reports")
@allure.feature("Página de reports en Plataforma")
@allure.story("US: reports")
@allure.testcase("TC - 0007")
@allure.title("reports correcto")
@allure.description("Este test verifica que se hace el login con los datos correctos y abre la pagina de Dashboard.")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.login
@pytest.mark.ui
def test_login_plataforma_datos_correctos(login_plataforma_page):
    # declaracion
    tenan = "Agenda22022022"
    usuario = "Andreina"
    clave = "123qwe"
    with allure.step("Navegar en la pagina de inicio de plataforma"):
        login_plataforma_page.navegar_login_plataforma()

    with allure.step("Setear los datos correctos en los campos Tenant, Usuario, Contraseña"):
        login_plataforma_page.set_user_inputs(tenan, usuario, clave)
        login_plataforma_page.iniciar_sesion_button()

    with allure.step("Ingresamos en la pagina Dashboard y se muestran los datos del Tenant y usuario"):
        tenanEsperado = "Agenda22022022"
        usuarioEsperado = "Andreina"
        assert tenanEsperado in login_plataforma_page.get_tenant_login_ok().text
        assert usuarioEsperado in login_plataforma_page.get_usuario_login_ok().text

    with allure.step("Log out de la página Dashboard"):
        login_plataforma_page.usuario_clic()
        login_plataforma_page.log_out()

