import time
import configparser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def is_visible(driver,locator, timeout = 20):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

def getPanelImage(url):
    driver.get(url)
    driver.set_window_size(900,500)
    driver.implicitly_wait(0.5)
    xpath='//*[@id="reactRoot"]/div/main/div[3]/div[1]/section/div[2]/div/div[1]/div/div[1]/div/div/div[4]'

    try:
        is_visible(driver,xpath)
    except:
        driver.quit()

    driver.get_screenshot_as_file(f'aaa.png')
    driver.quit()
    
def dologin(baseurl,user,password):
    driver.get(f'{baseurl}/login')
    driver.maximize_window()
    driver.find_element(By.NAME, "user").send_keys(user)
    driver.find_element(By.ID, "current-password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".css-14g7ilz-button > .css-1mhnkuh").click()
    


if __name__ == "__main__":
    config = configparser.ConfigParser(interpolation=None)
    config.read('config/config.ini')

    baseurl = config['grafana']['base_url']
    user = config['grafana']['user']
    password = config['grafana']['password']

    driver = webdriver.Chrome(executable_path=config['driver']['driver_path'])
    dologin('https://grafana.hostdon.jp',user,password)
    time.sleep(1)
    getPanelImage(config['grafana']['panel_url'])