from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import wget

DRIVER_PATH = '../pdf_scraper/chromedriver_win32/chromedriver.exe'
download_dir = '../pdf_scraper'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.bnpparibas-am.fr/investisseur-prive-particulier/fundsheet/actions/bnp-paribas-euro-valeurs-durables-classic-d-fr0010137174/?tab=documents')
action = ActionChains(driver) 

print('getting here')
time.sleep(6)
        
link_to_pdf = driver.find_element_by_xpath('//div[@class="sc-paZra cxvMSq"]/div[1]/div[@class="sc-pjTqr jJFvBj"]/section/div[@class="section"][1]/div[@class="rows-container"][1]/div[@class="sc-qOvHb dprCAs"]/div[@class="sc-pJurq fphCxn"]/div[@class="cell"]/a[@class="link"]')

action.click(driver.find_element_by_xpath('//div[@class="bnp-disclaimer-buttons"]/a[@class="bnp-btn bnp-btn-round bnp-lightbox-btn bnp-btn-accept bnp-btn-type-green"]'))
time.sleep(3)
driver.execute_script("window.scrollTo(0, 300)") 
time.sleep(3)
#action.move_to_element(to_element=link_to_pdf).context_click(on_element = link_to_pdf).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()
filename = wget.download(link_to_pdf.get_attribute('href'))
