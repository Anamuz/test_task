from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By




# 1. Товар можно добавить в корзину из списка товаров
#3. Конкретный товар появляется в корзине в обоих случаях
def test_add_from_list(driver_setup): 
    driver = driver_setup
    driver.get('https://selenium1py.pythonanywhere.com/ru/catalogue/')
    element = driver.find_element(By.XPATH, "(//*[contains(@class, 'btn btn-primary btn-block')])[1]")
    title = driver.find_element(By.XPATH, '(//*/h3)[1]').text
    element.click()
    driver.find_element(By.XPATH, '//div/p/a[contains(text(), "Посмотреть корзину")]').click()
    check = driver.find_element(By.XPATH, '(//*/h3)[1]').text
    assert title == check




#2. Товар можно добавить в корзину из карточки товара
#3. Конкретный товар появляется в корзине в обоих случаях    
def test_add_from_cart(driver_setup):
    driver = driver_setup
    driver.get('https://selenium1py.pythonanywhere.com/ru/catalogue/')
    driver.find_element(By.XPATH, "(//div[@class = 'image_container']/a)[3]").click()
    title = driver.find_element(By.XPATH, "//div/h1").text
    driver.find_element(By.XPATH, "//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']").click()
    driver.find_element(By.LINK_TEXT, "Посмотреть корзину").click()
    check = driver.find_element(By.XPATH, '(//div/h3)[2]/a').text
    assert title == check




def find_numbers(price):
    price_numbers = ''
    for item_price in price:
        if ('0' <= item_price <= '9'): 
            price_numbers += item_price
        elif (item_price == ','): 
            price_numbers += '.'
        else: 
            continue
    return price_numbers




#4. Сумма в корзине считается корректно
def test_sum(driver_setup): 
    driver = driver_setup
    driver.get('https://selenium1py.pythonanywhere.com/ru/catalogue/')
    driver.find_element(By.XPATH, "(//*[contains(@class, 'btn btn-primary btn-block')])[1]").click()
    driver.find_element(By.XPATH, "(//*[contains(@class, 'btn btn-primary btn-block')])[2]").click()
    driver.find_element(By.XPATH, '//div/p/a[contains(text(), "Посмотреть корзину")]').click()

    first_price = driver.find_element(By.XPATH, '(//div/p[@class="price_color align-right"])[2]').text
    first_price_numbers = find_numbers(first_price)
    first_price = float(first_price_numbers)

    second_price = driver.find_element(By.XPATH, '(//div/p[@class="price_color align-right"])[4]').text
    second_price_numbers = find_numbers(second_price)
    second_price = float(second_price_numbers)

    total_price = driver.find_element(By.CSS_SELECTOR, "#basket_totals th[class = 'total align-right']").text
    total_numbers = find_numbers(total_price)
    total_price = float(total_numbers)

    check_total = first_price + second_price
    assert total_price == check_total
    return total_price




#5. После попытки оформления выскакивает окно с предложением зарегистрироваться
def test_window(driver_setup):
    driver = driver_setup
    driver.get('https://selenium1py.pythonanywhere.com/ru/catalogue/')
    driver.find_element(By.XPATH, "(//*[contains(@class, 'btn btn-primary btn-block')])[1]").click()
    driver.find_element(By.XPATH, "(//*[contains(@class, 'btn btn-primary btn-block')])[2]").click()
    driver.find_element(By.XPATH, '//div/p/a[contains(text(), "Посмотреть корзину")]').click()
    driver.find_element(By.XPATH, '//div/a[contains(text(), "Перейти к оформлению")]').click()
    register = driver.find_element(By.NAME, 'registration_submit')
    assert register is True




#6. После клика на лого сайта есть кнопка корзины с корректной суммой
def test_logo(driver_setup): 
    driver = driver_setup
    driver.get('https://selenium1py.pythonanywhere.com/ru/catalogue/')
    driver.find_element(By.LINK_TEXT, 'Oscar').click()
    card = driver.find_element(By.XPATH, '//div/p/a[contains(text(), "Посмотреть корзину")]')
    price = driver.find_element(By.XPATH, '//div[@class = "basket-mini pull-right hidden-xs"]').text
    assert card is True
    assert price == total_price


total_price = 0