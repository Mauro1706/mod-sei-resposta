# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test02SEIMREnviarResposta():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://seleniumhub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_00EnviarRespostaDefinitiva(self):
    self.driver.get("http://sei4.resposta.nuvem.gov.br//sip/login.php?sigla_orgao_sistema=ABC&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    self.driver.find_element(By.LINK_TEXT, "Iniciar Processo").click()
    self.vars["error"] = len(self.driver.find_elements(By.XPATH, "//a[contains(text(), \'Protocolização de documentos para o Protocolo Central do ME\')]"))
    if self.driver.execute_script("return (arguments[0]==0)", self.vars["error"]):
      self.driver.find_element(By.ID, "imgExibirTiposProcedimento").click()
    self.driver.find_element(By.LINK_TEXT, "Protocolização de documentos para o Protocolo Central do ME").click()
    self.driver.find_element(By.ID, "txtDescricao").send_keys("teste arquivo")
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Incluir Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Incluir Documento\']").click()
    self.driver.find_element(By.LINK_TEXT, "Despacho").click()
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.vars["win5785"] = self.wait_for_window(30000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win5785"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Assinar Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Assinar Documento\']").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    WebDriverWait(self.driver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "selCargoFuncao")))
    dropdown = self.driver.find_element(By.ID, "selCargoFuncao")
    dropdown.find_element(By.XPATH, "//option[. = 'Corregedor']").click()
    self.driver.find_element(By.ID, "selCargoFuncao").click()
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "btnAssinar").click()
    time.sleep(20000)
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.XPATH, "//div[@id=\'topmenu\']/a[2]").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Enviar Resposta\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Enviar Resposta\']").click()
    self.driver.find_element(By.ID, "txaMensagem").click()
    self.driver.find_element(By.ID, "txaMensagem").send_keys("teste")
    self.driver.find_element(By.ID, "imgInfraCheck").click()
    self.driver.find_element(By.ID, "lblDefinitiva").click()
    self.driver.find_element(By.NAME, "btnEnviar").click()
    assert self.driver.switch_to.alert.text == "Confirma o envio da resposta? \nEssa ação  não poderá ser desfeita."
    self.driver.switch_to.alert.accept()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(0)
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(.,\'Resposta ao Protocolo Digital\')]")))
    elements = self.driver.find_elements(By.XPATH, "//span[contains(.,\'Resposta ao Protocolo Digital\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Resposta ao Protocolo Digital\')]").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.ID, "ifrArvoreHtml")))
    print(str("o index abaixo deve ser zero para rodar corretamente no python. Caso deseje rodar pelo IDE use 1"))
    self.driver.switch_to.frame(0)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[contains(.,\'Resposta ao Protocolo Digital\')]")))
    elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Anexos\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(text(),\'Despacho\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//label[contains(.,\'Resposta ao Protocolo Digital\')]")
    assert len(elements) > 0
  
  def test_01EnviarRespostaAjuste(self):
    self.driver.get("http://sei4.resposta.nuvem.gov.br//sip/login.php?sigla_orgao_sistema=ABC&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    self.driver.find_element(By.LINK_TEXT, "Iniciar Processo").click()
    self.vars["error"] = len(self.driver.find_elements(By.XPATH, "//a[contains(text(), \'Protocolização de documentos para o Protocolo Central do ME\')]"))
    if self.driver.execute_script("return (arguments[0]==0)", self.vars["error"]):
      self.driver.find_element(By.ID, "imgExibirTiposProcedimento").click()
    self.driver.find_element(By.LINK_TEXT, "Protocolização de documentos para o Protocolo Central do ME").click()
    self.driver.find_element(By.ID, "txtDescricao").send_keys("teste arquivo")
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Incluir Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Incluir Documento\']").click()
    self.driver.find_element(By.LINK_TEXT, "Despacho").click()
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.vars["win5785"] = self.wait_for_window(30000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win5785"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Assinar Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Assinar Documento\']").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    WebDriverWait(self.driver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "selCargoFuncao")))
    dropdown = self.driver.find_element(By.ID, "selCargoFuncao")
    dropdown.find_element(By.XPATH, "//option[. = 'Corregedor']").click()
    self.driver.find_element(By.ID, "selCargoFuncao").click()
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "btnAssinar").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.XPATH, "//div[@id=\'topmenu\']/a[2]").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Enviar Resposta\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Enviar Resposta\']").click()
    self.driver.find_element(By.ID, "txaMensagem").click()
    self.driver.find_element(By.ID, "txaMensagem").send_keys("teste")
    self.driver.find_element(By.ID, "imgInfraCheck").click()
    self.driver.find_element(By.ID, "lblParcial").click()
    self.driver.find_element(By.NAME, "btnEnviar").click()
    self.driver.switch_to.alert.accept()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(0)
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(.,\'Resposta ao Protocolo Digital\')]")))
    elements = self.driver.find_elements(By.XPATH, "//span[contains(.,\'Resposta ao Protocolo Digital\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Resposta ao Protocolo Digital\')]").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.ID, "ifrArvoreHtml")))
    self.driver.switch_to.frame(0)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[contains(.,\'Resposta ao Protocolo Digital\')]")))
    elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Anexos\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//a[contains(text(),\'Despacho\')]")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.XPATH, "//label[contains(.,\'Resposta ao Protocolo Digital\')]")
    assert len(elements) > 0
  
  def test_02EnviarRespostaValidacaoMensagem(self):
    self.driver.get("http://sei4.resposta.nuvem.gov.br//sip/login.php?sigla_orgao_sistema=ABC&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    self.driver.find_element(By.LINK_TEXT, "Iniciar Processo").click()
    self.vars["error"] = len(self.driver.find_elements(By.XPATH, "//a[contains(text(), \'Protocolização de documentos para o Protocolo Central do ME\')]"))
    if self.driver.execute_script("return (arguments[0]==0)", self.vars["error"]):
      self.driver.find_element(By.ID, "imgExibirTiposProcedimento").click()
    self.driver.find_element(By.LINK_TEXT, "Protocolização de documentos para o Protocolo Central do ME").click()
    self.driver.find_element(By.ID, "txtDescricao").send_keys("teste arquivo")
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Enviar Resposta\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Enviar Resposta\']").click()
    self.driver.find_element(By.NAME, "btnEnviar").click()
    assert self.driver.switch_to.alert.text == "Informe a Mensagem."
    self.driver.switch_to.alert.accept()
  
  def test_03EnviarRespostaValidacaoDoc(self):
    self.driver.get("http://sei4.resposta.nuvem.gov.br//sip/login.php?sigla_orgao_sistema=ABC&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    self.driver.find_element(By.LINK_TEXT, "Iniciar Processo").click()
    self.vars["error"] = len(self.driver.find_elements(By.XPATH, "//a[contains(text(), \'Protocolização de documentos para o Protocolo Central do ME\')]"))
    if self.driver.execute_script("return (arguments[0]==0)", self.vars["error"]):
      self.driver.find_element(By.ID, "imgExibirTiposProcedimento").click()
    self.driver.find_element(By.LINK_TEXT, "Protocolização de documentos para o Protocolo Central do ME").click()
    self.driver.find_element(By.ID, "txtDescricao").send_keys("teste arquivo")
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Enviar Resposta\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Enviar Resposta\']").click()
    self.driver.find_element(By.ID, "txaMensagem").click()
    self.driver.find_element(By.ID, "txaMensagem").send_keys("teste")
    self.driver.find_element(By.NAME, "btnEnviar").click()
    assert self.driver.switch_to.alert.text == "Não há documento(s) no processo."
    self.driver.switch_to.alert.accept()
  
  def test_04EnviarRespostaValidacaoDocNAssinado(self):
    self.driver.get("http://sei4.resposta.nuvem.gov.br//sip/login.php?sigla_orgao_sistema=ABC&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    self.driver.find_element(By.LINK_TEXT, "Iniciar Processo").click()
    self.vars["error"] = len(self.driver.find_elements(By.XPATH, "//a[contains(text(), \'Protocolização de documentos para o Protocolo Central do ME\')]"))
    if self.driver.execute_script("return (arguments[0]==0)", self.vars["error"]):
      self.driver.find_element(By.ID, "imgExibirTiposProcedimento").click()
    self.driver.find_element(By.LINK_TEXT, "Protocolização de documentos para o Protocolo Central do ME").click()
    self.driver.find_element(By.ID, "txtDescricao").send_keys("teste arquivo")
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Incluir Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Incluir Documento\']").click()
    self.driver.find_element(By.LINK_TEXT, "Despacho").click()
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.vars["win5785"] = self.wait_for_window(30000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win5785"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.XPATH, "//span").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Enviar Resposta\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Enviar Resposta\']").click()
    self.driver.find_element(By.ID, "txaMensagem").click()
    self.driver.find_element(By.ID, "txaMensagem").send_keys("teste")
    self.driver.find_element(By.NAME, "btnEnviar").click()
    assert self.driver.switch_to.alert.text == "Nenhum documento selecionado."
    self.driver.switch_to.alert.accept()
  
  def test_05EnviarRespostaValidacaoDocAssinado(self):
    self.driver.get("http://sei4.resposta.nuvem.gov.br//sip/login.php?sigla_orgao_sistema=ABC&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    self.driver.find_element(By.LINK_TEXT, "Iniciar Processo").click()
    self.vars["error"] = len(self.driver.find_elements(By.XPATH, "//a[contains(text(), \'Protocolização de documentos para o Protocolo Central do ME\')]"))
    if self.driver.execute_script("return (arguments[0]==0)", self.vars["error"]):
      self.driver.find_element(By.ID, "imgExibirTiposProcedimento").click()
    self.driver.find_element(By.LINK_TEXT, "Protocolização de documentos para o Protocolo Central do ME").click()
    self.driver.find_element(By.ID, "txtDescricao").send_keys("teste arquivo")
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Incluir Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Incluir Documento\']").click()
    self.driver.find_element(By.LINK_TEXT, "Despacho").click()
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.vars["win5785"] = self.wait_for_window(30000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win5785"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Assinar Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Assinar Documento\']").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    WebDriverWait(self.driver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "selCargoFuncao")))
    dropdown = self.driver.find_element(By.ID, "selCargoFuncao")
    dropdown.find_element(By.XPATH, "//option[. = 'Corregedor']").click()
    self.driver.find_element(By.ID, "selCargoFuncao").click()
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "btnAssinar").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.XPATH, "//div[@id=\'topmenu\']/a[2]").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Enviar Resposta\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Enviar Resposta\']").click()
    self.driver.find_element(By.ID, "txaMensagem").click()
    self.driver.find_element(By.ID, "txaMensagem").send_keys("teste")
    self.driver.find_element(By.ID, "lblParcial").click()
    self.driver.find_element(By.NAME, "btnEnviar").click()
    assert self.driver.switch_to.alert.text == "Nenhum documento selecionado."
    self.driver.switch_to.alert.accept()
  
  def test_06EnviarRespostaValidacaoConclusivo(self):
    self.driver.get("http://sei4.resposta.nuvem.gov.br//sip/login.php?sigla_orgao_sistema=ABC&sigla_sistema=SEI")
    self.driver.find_element(By.ID, "txtUsuario").send_keys("teste")
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "Acessar").click()
    self.driver.find_element(By.LINK_TEXT, "Iniciar Processo").click()
    self.vars["error"] = len(self.driver.find_elements(By.XPATH, "//a[contains(text(), \'Protocolização de documentos para o Protocolo Central do ME\')]"))
    if self.driver.execute_script("return (arguments[0]==0)", self.vars["error"]):
      self.driver.find_element(By.ID, "imgExibirTiposProcedimento").click()
    self.driver.find_element(By.LINK_TEXT, "Protocolização de documentos para o Protocolo Central do ME").click()
    self.driver.find_element(By.ID, "txtDescricao").send_keys("teste arquivo")
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Incluir Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Incluir Documento\']").click()
    self.driver.find_element(By.LINK_TEXT, "Despacho").click()
    self.driver.find_element(By.CSS_SELECTOR, "#divOptPublico .infraRadioLabel").click()
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar")))
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#divInfraBarraComandosInferior > #btnSalvar").click()
    self.vars["win5785"] = self.wait_for_window(30000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win5785"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Assinar Documento\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Assinar Documento\']").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    WebDriverWait(self.driver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "selCargoFuncao")))
    dropdown = self.driver.find_element(By.ID, "selCargoFuncao")
    dropdown.find_element(By.XPATH, "//option[. = 'Corregedor']").click()
    self.driver.find_element(By.ID, "selCargoFuncao").click()
    self.driver.find_element(By.ID, "pwdSenha").click()
    self.driver.find_element(By.ID, "pwdSenha").send_keys("teste")
    self.driver.find_element(By.ID, "btnAssinar").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.XPATH, "//div[@id=\'topmenu\']/a[2]").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(1)
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt=\'Enviar Resposta\']")))
    self.driver.find_element(By.XPATH, "//img[@alt=\'Enviar Resposta\']").click()
    self.driver.find_element(By.ID, "txaMensagem").click()
    self.driver.find_element(By.ID, "txaMensagem").send_keys("teste")
    self.driver.find_element(By.ID, "imgInfraCheck").click()
    self.driver.find_element(By.NAME, "btnEnviar").click()
    assert self.driver.switch_to.alert.text == "Selecione o Tipo de resposta."
    self.driver.switch_to.alert.accept()
  
