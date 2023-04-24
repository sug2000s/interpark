from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time, pyautogui
from datetime import datetime

import telegram
import asyncio

#텔레그램 토큰
chat_token = "1340164445:AAFGSPa4aKzvJbeDV9Gp6S5DVIm3x03x4j0"
#텔레그램 id
bot_id = '846598578'

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])#불필요한 메세지 제거

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

### CONFIG ###
userID = 'sug4000s'
userPW = 'dlstoddms31!'

async def sendTelegram(day): #실행시킬 함수명 임의지정
    token = "텔레그램 봇 API"
    bot = telegram.Bot( chat_token)
    await bot.send_message(bot_id, day + ' 캠핑장 예약하세요.')

def log_in():
    try:
        login_url = "https://accounts.interpark.com/login/form"
        driver.get(login_url)
        ##time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(userID)  # ID 입력
        driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(userPW)
        driver.find_element(By.XPATH, '//*[@id="btn_login"]').click()
    except Exception as e:
        print(e)
        print("got exception(log_in)")


def move_to_ticket_Cheon_page():
    try:
        공연코드 = 21012652
        userSearch = f"https://tickets.interpark.com/goods/{공연코드}#"
        driver.get(userSearch)
        time.sleep(0.7)
        driver.find_element(By.XPATH, '//*[@id="popup-prdGuide"]/div/div[3]/button').click()

        labels = ['//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[35]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[36]'
                  ]
        for i in labels:
            driver.find_element(By.XPATH, i).click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[1]/ul/li[1]').click()

            result = driver.find_element(By.XPATH,
                                         '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span').text

            if result == '매진':
                time.sleep(2)
            else:
                day = driver.find_element(By.XPATH, i).text
                asyncio.run(sendTelegram('4월' + day + ' 천왕산 '))  # 봇 실행하는 코드

        ##5월 클릭
        driver.find_element(By.XPATH,
                            '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[1]/li[3]').click()
        labels2 = ['//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[6]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[7]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[14]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[21]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[28]'
                   ]

        for i in labels2:
            driver.find_element(By.XPATH, i).click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[1]/ul/li[1]').click()

            result = driver.find_element(By.XPATH,
                                         '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span').text

            if result == '매진':
                time.sleep(2)
            else:
                day = driver.find_element(By.XPATH, i).text
                asyncio.run(sendTelegram('5월' + day + ' 천왕산 '))  # 봇 실행하는 코드


    except Exception as e:
        print(e)
        print("got exception(move_to_ticket_page)")
        asyncio.run(sendTelegram('오류가 발생 하였습니다.'))  # 봇 실행하는 코드


def move_to_ticket_No_page():
    try:
        공연코드 = 22011899
        userSearch = f"https://tickets.interpark.com/goods/{공연코드}#"
        driver.get(userSearch)
        time.sleep(0.7)
        driver.find_element(By.XPATH, '//*[@id="popup-prdGuide"]/div/div[3]/button').click()

        labels = ['//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[35]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[36]'
                  ]
        for i in labels:
            driver.find_element(By.XPATH, i).click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[1]/ul/li[1]').click()

            result = driver.find_element(By.XPATH,
                                         '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span').text

            result2 = driver.find_element(By.XPATH,
                                          '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[2]/ul/li[2]/span').text
            if result == '매진' and result2 == '매진':
                time.sleep(2)
            else:
                day = driver.find_element(By.XPATH, i).text
                asyncio.run(sendTelegram('4월' + day + ' 노을진 '))  # 봇 실행하는 코드

        ##5월 클릭
        driver.find_element(By.XPATH,
                            '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[1]/li[3]').click()
        labels2 = ['//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[6]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[7]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[14]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[21]'
            , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[28]'
                   ]

        for i in labels2:
            driver.find_element(By.XPATH, i).click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[1]/ul/li[1]').click()

            result = driver.find_element(By.XPATH,
                                         '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[2]/ul/li[1]/span').text

            result2 = driver.find_element(By.XPATH,
                                          '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[2]/ul/li[2]/span').text
            if result == '매진' and result2 == '매진':
                time.sleep(2)
            else:
                day = driver.find_element(By.XPATH, i).text
                asyncio.run(sendTelegram('5월' + day+ ' 노을진 '))  # 봇 실행하는 코드

    except Exception as e:
        print(e)
        print("got exception(move_to_ticket_page)")
        asyncio.run(sendTelegram('오류가 발생 하였습니다.'))  # 봇 실행하는 코드


def move_to_ticket_Do_page():
    try:

        userSearch = f"https://reserve.gmuc.co.kr/user/camp/campReservation.do?menu=d&menuFlag=C"
        driver.get(userSearch)
        time.sleep(10)
        labels = ['//*[@id="sub_wrap_full"]/div/table/tbody/tr[6]/td[7]/div[2]/a'
             , '//*[@id="sub_wrap_full"]/div/table/tbody/tr[6]/td[7]/div[3]/a'
             , '//*[@id="sub_wrap_full"]/div/table/tbody/tr[7]/td[1]/div[2]/a'
             , '//*[@id="sub_wrap_full"]/div/table/tbody/tr[7]/td[1]/div[3]/a'
                  ]
        for i in range(0,len(labels)):
            result = driver.find_element(By.XPATH, labels[i]).text

            if i%2 == 0 and result == 'A구역 잔여 데크: 0':
                time.sleep(2)
            elif i%2 == 1 and result == 'B구역 잔여 데크: 0':
                time.sleep(2)
            else:
                asyncio.run(sendTelegram('4월' + ' 도덕산 '))  # 봇 실행하는 코드
    except Exception as e:
        print(e)
        print("got exception(move_to_ticket_page)")
        asyncio.run(sendTelegram('오류가 발생 하였습니다.'))  # 봇 실행하는 코드


log_in()

while (True):
    move_to_ticket_Cheon_page()
    move_to_ticket_No_page()
    move_to_ticket_Do_page()