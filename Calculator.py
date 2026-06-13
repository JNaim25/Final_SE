import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
try:
    driver = webdriver.Chrome()
    driver.get("https://testsheepnz.github.io/BasicCalculator.html")
    driver.maximize_window()
    time.sleep(2)

    first_number = driver.find_element(By.ID, "number1Field")
    second_number = driver.find_element(By.ID, "number2Field")
    operation_dropdown = driver.find_element(By.ID, "selectOperationDropdown")
    calculate_button = driver.find_element(By.ID, "calculateButton")
    answer_field = driver.find_element(By.ID, "numberAnswerField")

    print("Scenarion 1: Success")

    first_number.clear()
    first_number.send_keys("10")

    second_number.clear()
    second_number.send_keys("5")

    operation_dropdown.send_keys("2")
    calculate_button.click()
    time.sleep(2)

    result = answer_field.get_attribute("value")
    assert result == "50", f"Expected 50 but got {result}"

    print(f"Test passed! Result: {result}")

    print("Scenarion 2: Failure")

    first_number.clear()
    second_number.clear()
    second_number.send_keys("5")

    operation_dropdown.send_keys("2")
    calculate_button.click()
    time.sleep(2)

    error_result = answer_field.get_attribute("value")
    print(f"✅ Fail Case Executed. Answer field shows: '{error_result}'")

finally:
    driver.quit()