from re import U
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
from PIL import Image
import time 
import sys
import os

def collect_data(search_term):
  driver.get('https://www.google.com/imghp?hl=FR')
  driver.find_element(By.CLASS_NAME,'QS5gu.sy4vM').click()
  driver.find_element(By.CLASS_NAME,'gLFyf.gsfi').click()
  time.sleep(2)
  test =driver.find_element_by_tag_name("input")
  test.send_keys(search_term+Keys.ENTER)
  selection=driver.find_elements(By.CLASS_NAME, 'rg_i.Q4LuWd')[0:int(sys.argv[2])]
  liste=[image.get_attribute('src') for image in selection]

  return (liste)
  
  

driver = webdriver.Chrome('../chromedriver')
liste=collect_data(sys.argv[1])
basewidth = 500
i=1
for image in liste:
  try:
    os.mkdir(sys.argv[1])
  except:
    pass
  urllib.request.urlretrieve(image,f'./{sys.argv[1]}/{sys.argv[1]}{i}.jpg')
  img=Image.open(f'./{sys.argv[1]}/{sys.argv[1]}{i}.jpg')
  wpercent = (basewidth/float(img.size[0]))
  hsize = int((float(img.size[1])*float(wpercent)))
  img = img.resize((basewidth,hsize), Image.ANTIALIAS)
  img.save(f'./{sys.argv[1]}/{sys.argv[1]}{i}.jpg') 
  i+=1
  img.show()

