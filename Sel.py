from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
actions = ActionChains(driver)
f=open("data.csv","w+")
cities=['chennai','ahmedabad','pune']
for r in range(0,len(cities)):
    f.writelines(cities[r]+"\n")
    print('Details for City :'+cities[r])
    url="https://www.urbanclap.com/"
    a=url+cities[r]
    driver.get(a)
    source = driver.page_source
    soup1 = BeautifulSoup(source,"lxml")
    username =driver.find_element_by_xpath('/html/body/div[2]/div/div/div/  section/section/div[2]/div[2]/div/div/div/input')
    username.send_keys('pest control')
    time.sleep(3)
    us = driver.find_element_by_xpath('//*[@id="homepageContainer"]/section/section[1]/div[2]/div[2]/div/div[2]/ul/li[1]/div/div/div').click()
    time.sleep(3)
    a='//*[@id="qaSingleSelect"]/ul/li[i]/label/div[1]'
    b=a.split('li[i]')
    aa=[]
    bb=[]
    cc=[]
    for i in range(1,5):
        f.writelines(str(i)+" BHK\n")
        c=b[0]+'li['+str(i)+']'+b[1]
        us1=driver.find_element_by_xpath(c).click()
        us2=driver.find_element_by_xpath('//*[@id="qaNext"]/div/span[2]').click()
        source=driver.page_source
        soup1=BeautifulSoup(source,'lxml')
        soup2=soup1.find_all('div',{'class':'_2_zFy-1lucSUR_Du1Q018L'})
        soup3=soup1.find_all('div',{'class':'U7DStEWrPcwr-0_rYHtNO'})
        soup4=soup1.find_all('div',{'class':'_2YHu5ZJmJ55peKBM4TTngU clearfix'})
        for j in range(0,len(soup2)):
            x=((soup2[j].find('p').string))
            y=((soup3[j].find('span').string))
            z=((soup4[j].find('p').string))
            f.writelines(x+","+y+",\""+z+"\"\n")
        print(str(i)+" BHK over\n\n")
        us3=driver.find_element_by_xpath('//*[@id="qaBack"]/span').click()
        time.sleep(0.2)
f.close()