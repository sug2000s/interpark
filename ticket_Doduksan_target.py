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

schedule_time = datetime(2023, 2, 23, 13, 0, 0)

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 1)

set_schedule = True

### CONFIG ###
userID = 'sug4000s'
userPW = 'dlstoddms31!'

async def sendTelegram(day): #실행시킬 함수명 임의지정
    token = "텔레그램 봇 API"
    bot = telegram.Bot( chat_token)
    await bot.send_message(bot_id, day + ' 도덕산 캠핑장 예약하세요.')


def move_to_ticket_page():
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
                asyncio.run(sendTelegram('4월' ))  # 봇 실행하는 코드


        move_to_ticket_page()


    except Exception as e:
        print(e)
        print("got exception(move_to_ticket_page)")
        asyncio.run(sendTelegram('오류가 발생 하였습니다.'))  # 봇 실행하는 코드


##log_in()
move_to_ticket_page()