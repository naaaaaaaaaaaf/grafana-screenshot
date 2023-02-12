import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs

def is_visible(driver,locator, timeout = 20):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

def getPanelImage(url,filename):
    driver.get(url)
    driver.set_window_size(900,500)
    driver.implicitly_wait(0.5)
    xpath='//*[@id="reactRoot"]/div/main/div[3]/div[1]/section/div[2]/div/div[1]/div/div[1]/div/div/div[4]'

    try:
        is_visible(driver,xpath)
    except:
        driver.quit()

    driver.get_screenshot_as_file(filename+".png")
    
def dologin(baseurl,user,password):
    driver.get(f'{baseurl}/login')
    driver.maximize_window()
    driver.find_element(By.NAME, "user").send_keys(user)
    driver.find_element(By.ID, "current-password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".css-14g7ilz-button > .css-1mhnkuh").click()
    


if __name__ == "__main__":
    f_in = open("config/config.json", "r")
    config = json.load(f_in)

    baseurl = config['grafana']['base_url']
    user = config['grafana']['user']
    password = config['grafana']['password']

    chrome_service = fs.Service(executable_path=config['driver_path']) 
    driver = webdriver.Chrome(service=chrome_service)
    dologin(config['grafana']['base_url'],user,password)
    time.sleep(1)

    for i in config['grafana']['panel']:
        getPanelImage(i['url'],i['name'])
    
    driver.quit()