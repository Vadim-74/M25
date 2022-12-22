from selenium.webdriver.common.by import By
from settings import base_url, valid_email, valid_pass
from selenium import webdriver


class TestCase:
    def test_case(self):
        # Инициализируем WebDriver
        driver = webdriver.Chrome()

        # Загружаем страницу
        driver.get(f"{base_url}new_user")

        # Переход по ссылке «У меня уже есть аккаунт»
        click_link = driver.find_element(By.CSS_SELECTOR, "form > div:nth-of-type(4) > a")
        click_link.click()

        # Очистка поля email и ввод валидного значения
        email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
        email_input.clear()
        email_input.send_keys(valid_email)

        # Очистка поля pass и ввод валидного значения
        pass_input = driver.find_element(By.CSS_SELECTOR, "input#pass")
        pass_input.clear()
        pass_input.send_keys(valid_pass)

        # Нажимаем на кнопку «Войти» и проверяем карточку
        button_enter = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > button")
        button_enter.click()
        assert driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > div.card")

        # Выход
        driver.quit()
