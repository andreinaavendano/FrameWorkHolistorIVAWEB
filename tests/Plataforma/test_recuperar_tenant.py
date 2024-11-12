import pytest
import allure
from pages.Plataforma.recuperar_tenant import RecuperarTenant


@pytest.fixture
def recuperar_tenant(browser, base_url, datos_usuario):
    return RecuperarTenant(browser, base_url, datos_usuario)

@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar Espacios de trabajo tenant en Plataforma")
@allure.story("US: Recuperar Espacios de trabajo tenant para el ingreso a Plataforma ")
@allure.testcase("TC - 0001")
@allure.title("Campo email ok")
@allure.description("Este test verifica que se encuentra el input text Email")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_tenant
@pytest.mark.regresion

def test_campo_email_ok(recuperar_tenant):
    with allure.step("Al navegar en la pagina de recuperar tenant"):
        recuperar_tenant.navegar_recuperar_tenant()

    with allure.step("Se debe mostrar el campo Email"):
        resultado = recuperar_tenant.get_email_input().get_attribute('placeholder')

    with allure.step("Puedo verificar que se encuentra con el texto Dirección de email *"):
        texto_tenant_esperado = 'Dirección de email *'
        assert (texto_tenant_esperado in resultado
                ), "El texto esperado no coincide con el texto encontrado"


@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Espacios de trabajo tenant para el ingreso a Plataforma ")
@allure.testcase("TC - 0002")
@allure.title("Botón Enviar OK")
@allure.description("Este test verifica que se encuentra el botón Enviar")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_tenant
@pytest.mark.regresion
def test_boton_enviar_ok(recuperar_tenant):
    with allure.step("Al navegar en la pagina de recuperar tenant"):
        recuperar_tenant.navegar_recuperar_tenant()

    with allure.step("Se debe mostrar el botón Enviar"):
        resultado = recuperar_tenant.wait_for_element(recuperar_tenant.ENVIAR_BUTTON)
        resultado_text = recuperar_tenant.get_enviar_button().text

    with allure.step("Puedo verificar que se encuentra el botón con el texto Enviar"):
        texto_boton_esperado = 'Enviar'
        assert (texto_boton_esperado in resultado_text
                ), "El texto esperado no coincide con el texto encontrado"
        assert resultado.is_displayed(), "El botón no esta visible"
        assert not resultado.is_enabled(), "El botón esta habilitado para click"

@allure.suite("Casos de prueba de la pagina Login de Plataforma")
@allure.epic("Login")
@allure.feature("Página de recuperar contraseña en Plataforma")
@allure.story("US: Recuperar Espacios de trabajo tenant para el ingreso a Plataforma ")
@allure.testcase("TC - 0003")
@allure.title("Botón Atrás OK")
@allure.description("Este test verifica que se encuentra el botón Atrás")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_clave
@pytest.mark.regresion
def test_boton_atras_ok(recuperar_tenant):
    with allure.step("Al navegar en la pagina de recuperar tenant"):
        recuperar_tenant.navegar_recuperar_tenant()

    with allure.step("Se debe mostrar el botón Atrás"):
        resultado_text = recuperar_tenant.get_atras_button().text
        resultado = recuperar_tenant.get_atras_button()
        resultado_link_href = recuperar_tenant.get_atras_button().get_attribute('routerlink')

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
@allure.story("US: Recuperar Espacios de trabajo tenant para el ingreso a Plataforma ")
@allure.testcase("TC - 0004")
@allure.title("Ingresar una direccion de correo valida para recuperar los espacios de trabajo")
@allure.description("Este test verifica que se hace el preceso de eviar el email para recuperar los espacios de trabajo")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.recuperar_tenant
@pytest.mark.regresion
def test_recuperar_tenant_datos_validos(recuperar_tenant):
    # declaracion

    email = "aavendano@holistor.com.ar"

    with allure.step("Al navegar en la pagina de recuperar tenant"):
        recuperar_tenant.navegar_recuperar_tenant()

    with allure.step("Ingreso los datos requeridos y que existen"):
        recuperar_tenant.set_input_email(email)
        recuperar_tenant.enviar_button()
        resultado = recuperar_tenant.get_msg().text
    with allure.step(f"Puedo verificar que se muestra que se envio el email a la dirección {email} porporciona "):
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
def test_atras_ok(recuperar_tenant):
    # declaracion

    email = "aavendano@holistor.com.ar"
    with allure.step("Al navegar en la pagina de recuperar tenant"):
        recuperar_tenant.navegar_recuperar_tenant()
    # Ejecución
    with allure.step("AL hacer clic en atras regresa la pagina de inicio"):
        recuperar_tenant.atras_button()
        url_resultado = recuperar_tenant.get_current_url()
        url_esperado = recuperar_tenant.get_base_url()+"/account/login"
        assert url_resultado in url_esperado, "La URL esperado no coincide con URL encontrado"