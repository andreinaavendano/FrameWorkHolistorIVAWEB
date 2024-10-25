import pytest
import allure
from pages.recuperar_clave import RecuperarClave
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def recuperar_clave(browser, base_url):
    return RecuperarClave(browser, base_url)


@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Credenciales para el ingreso a Plataforma ")
@allure.testcase("TC - 0001")
@allure.title("Campo tenant ok")
@allure.description("Este test verifica que se encuentra el input text Tenant")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion

def test_campo_tenant_ok(recuperar_clave):
    with allure.step("Al navegar en la pagina de recuperar contraseña"):
        recuperar_clave.navegar_recuperar_contrasena()

    with allure.step("Se debe mostrar el campo Tenant"):
        resultado = recuperar_clave.get_tenant_input().get_attribute('placeholder')

    with allure.step("Puedo verificar que se encuentra con el texto Nombre de espacio de trabajo *"):
        texto_tenant_esperado = 'Nombre de espacio de trabajo *'
        assert (texto_tenant_esperado in resultado
                ), "El texto esperado no coincide con el texto encontrado"


@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Credenciales para el ingreso a Plataforma ")
@allure.testcase("TC - 0002")
@allure.title("Campo Email ok")
@allure.description("Este test verifica que se encuentra el input text Email")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion
def test_campo_email_ok(recuperar_clave):
    with allure.step("Al navegar en la pagina de recuperar contraseña"):
        recuperar_clave.navegar_recuperar_contrasena()

    with allure.step("Se debe mostrar el campo Email"):
        resultado = recuperar_clave.get_email_input().get_attribute('placeholder')

    with allure.step("Puedo verificar que se encuentra con el texto Dirección de email *"):
        texto_tenant_esperado = 'Dirección de email *'
        assert (texto_tenant_esperado in resultado
                ), "El texto esperado no coincide con el texto encontrado"


@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Credenciales para el ingreso a Plataforma ")
@allure.testcase("TC - 0003")
@allure.title("Botón Enviar OK")
@allure.description("Este test verifica que se encuentra el botón Enviar")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion
def test_boton_enviar_ok(recuperar_clave):
    with allure.step("Al navegar en la pagina de recuperar contraseña"):
        recuperar_clave.navegar_recuperar_contrasena()

    with allure.step("Se debe mostrar el botón Enviar"):
        resultado = recuperar_clave.wait_for_element(recuperar_clave.ENVIAR_BUTTON)
        resultado_text = recuperar_clave.get_enviar_button().text

    with allure.step("Puedo verificar que se encuentra el botón con el texto Enviar"):
        texto_boton_esperado = 'Enviar'
        assert (texto_boton_esperado in resultado_text
                ), "El texto esperado no coincide con el texto encontrado"
        assert resultado.is_displayed(), "El botón no esta visible"
        assert not resultado.is_enabled(), "El botón esta habilitado para click"


@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Credenciales para el ingreso a Plataforma ")
@allure.testcase("TC - 0004")
@allure.title("Botón Atrás OK")
@allure.description("Este test verifica que se encuentra el botón Atrás")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion
def test_boton_atras_ok(recuperar_clave):
    with allure.step("Al navegar en la pagina de recuperar contraseña"):
        recuperar_clave.navegar_recuperar_contrasena()

    with allure.step("Se debe mostrar el botón Atrás"):
        resultado_text = recuperar_clave.get_atras_button().text
        resultado = recuperar_clave.get_atras_button()
        resultado_link_href = recuperar_clave.get_atras_button().get_attribute('routerlink')

    with allure.step("Puedo verificar que se encuentra el botón con el texto Atrás"):
        text_boton_esperado = "Atrás"
        href_esperado = "/account/login"
        assert text_boton_esperado in resultado_text
        assert resultado.is_displayed(), "El botón no esta visible"
        assert resultado.is_enabled(), "El botón no esta habilitado para click"
        assert (href_esperado == resultado_link_href), f"El href {resultado_link_href}  no es el esperado"

@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Credenciales para el ingreso a Plataforma ")
@allure.testcase("TC - 0005")
@allure.title("Ingresar un Tenant que no existe")
@allure.description("Este test verifica que se muestre el mensaje correcto cuando se ingresa un tenant no existe")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion
def test_tenant_no_valido(recuperar_clave):
    # declaracion
    tenant = "novalido"
    email = "aavendano@holistor.com.ar"
    with allure.step("Al navegar en la pagina de recuperar contraseña"):
        recuperar_clave.navegar_recuperar_contrasena()

    with allure.step("Ingreso los datos requeridos y se ingresa un tenant no existe"):
        recuperar_clave.set_input_datos(tenant, email)
        recuperar_clave.enviar_button()
        resultado = recuperar_clave.get_error_tenant_email_novalido_msg().text

    with allure.step(f"Puedo veririfar que se muestra el mensaje No existe un Espacio de Trabajo con nombre {tenant}"):
        text_esperado = "No existe un Espacio de Trabajo con nombre novalido"
        assert (text_esperado in resultado), "El texto esperado no coincide con el texto encontrado"

@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Credenciales para el ingreso a Plataforma ")
@allure.testcase("TC - 0006")
@allure.title("Ingresar un Email que no existe")
@allure.description("Este test verifica que se muestre el mensjae correcto cuando se ingresa un email no existe")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion
def test_email_no_valido(recuperar_clave):
    # declaracion
    tenant = "Agenda22022022"
    email = "aavendano@holistor.com"

    with allure.step("Al navegar en la pagina de recuperar contraseña"):
        recuperar_clave.navegar_recuperar_contrasena()

    with allure.step("Ingreso los datos requeridos y se ingresa un email no valido"):
        recuperar_clave.set_input_datos(tenant, email)
        recuperar_clave.enviar_button()
        resultado = recuperar_clave.get_error_tenant_email_novalido_msg().text

    with allure.step(f"Puedo veririfar que se muestra el mensaje dirección {email} no valida"):
        text_esperado = "Dirección de correo inválida"
        assert (text_esperado in resultado), "El texto esperado no coincide con el texto encontrado"


@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Credenciales para el ingreso a Plataforma ")
@allure.testcase("TC - 0007")
@allure.title("Ingresar un set de datos que existe para recuperar contraseña")
@allure.description("Este test verifica que se hace el preceso de eviar el email para recuperar constraseña")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion
def test_recuperar_contrasena_datos_validos(recuperar_clave):
    # declaracion
    tenant = "Agenda22022022"
    email = "aavendano@holistor.com.ar"

    with allure.step("Al navegar en la pagina de recuperar contraseña"):
        recuperar_clave.navegar_recuperar_contrasena()

    with allure.step("Ingreso los datos requeridos y que existen"):
        recuperar_clave.set_input_datos(tenant, email)
        recuperar_clave.enviar_button()
        resultado = recuperar_clave.get_error_tenant_email_novalido_msg().text
    with allure.step(f"Puedo verificar que se muestra que se envio el email a la dirección {email} porporciona "):
        # comprobacion
        text_esperado = "Correo enviado"
        assert text_esperado in resultado

@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Credenciales para el ingreso a Plataforma ")
@allure.testcase("TC - 0008")
@allure.title("Ingresar un set de datos que existe para recuperar contraseña")
@allure.description("Este test verifica que se hace el preceso de eviar el email para recuperar constraseña")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion
def test_atras_ok(recuperar_clave):
    # declaracion
    tenant = "espaciosoporte"
    email = "aavendano@holistor.com.ar"
    with allure.step("Al navegar en la pagina de recuperar contraseña"):
        recuperar_clave.navegar_recuperar_contrasena()
    # Ejecución
    with allure.step("AL hacer clic en atras regresa la pagina de inicio"):
        recuperar_clave.atras_button()
        url_resultado = recuperar_clave.get_current_url()
        url_esperado = recuperar_clave.get_base_url()+"/account/login"
        assert url_resultado in url_esperado, "La URL esperado no coincide con URL encontrado"
