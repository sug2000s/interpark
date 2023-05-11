import threading
from tkinter import *

import schedule as schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

##userID = 'efu1128'
##userPW = 'River1213%i'

async def sendTelegram(day): #실행시킬 함수명 임의지정
    token = "텔레그램 봇 API"
    bot = telegram.Bot( chat_token)
    print(day + " 캠핑장 예약하세요.")
    await bot.send_message(bot_id, day + ' 캠핑장 예약하세요.')
def log_in():
    try:
        login_url = "https://accounts.interpark.com/login/form"
        driver.get(login_url)

        driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(userID)  # ID 입력
        driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(userPW)

        time.sleep(15)
        driver.find_element(By.XPATH, '//*[@id="btn_login"]').click()

    except Exception as e:
        print(e)
        print("got exception(log_in)")

def link_ticket():
    ##직접 링크로 이동(티켓 존재)
    공연코드 = 21012652
    directLink = f"https://poticket.interpark.com/CampingBook/BookSession.asp?GroupCode={공연코드}"
    driver.get(directLink)

def reservation_ticket():
    try:
        labels = [
                     #'//*[@id="BookingDateTime"]/div/table/tbody/tr[1]/td[7]'
                     '//*[@id="BookingDateTime"]/div/table/tbody/tr[3]/td[7]'
                     ,'//*[@id="BookingDateTime"]/div/table/tbody/tr[4]/td[7]'
                     ,'//*[@id="BookingDateTime"]/div/table/tbody/tr[5]/td[1]'
                    ### ,'//*[@id="BookingDateTime"]/div/table/tbody/tr[5]/td[3]'##시현 테스트 용
            ###'//*[@id="BookingDateTime"]/div/table/tbody/tr[3]/td[5]' #테스트용
                  ]

        positionNames = ['[캠핑장] 캠핑사이트-A-1', '[캠핑장] 캠핑사이트-A-2', '[캠핑장] 캠핑사이트-A-3','[캠핑장] 캠핑사이트-A-4'
                         '[캠핑장] 캠핑사이트-A-5','[캠핑장] 캠핑사이트-A-6','[캠핑장] 캠핑사이트-A-7','[캠핑장] 캠핑사이트-A-8'
                         '[캠핑장] 캠핑사이트-A-9','[캠핑장] 캠핑사이트-A-10','[캠핑장] 캠핑사이트-A-11','[캠핑장] 캠핑사이트-A-12'
                         ]
        flag = True;
        while (True):
            for i in range(0, len(labels)):

                try:
                    driver.find_element(By.XPATH, labels[i]).click()
                    time.sleep(0.1)
                    driver.find_element(By.XPATH, '//*[@id="SelectCheckIn"]/option[2]').click()
                except Exception as e:
                    print(e)
                    continue

                time.sleep(0.1)
                driver.find_element(By.XPATH, '//*[@id="ifrmSeat"]').click()

                # 잔여 좌석 카운트 체크
                time.sleep(0.1)
                document = driver.find_element(By.XPATH, '//*[@id="ifrmSeat"]')
                driver.switch_to.frame(document)
                seats = driver.find_elements(By.CLASS_NAME, 'stySeat')

                if len(seats) > 0:
                    for j in range(0, len(seats)):
                        val = seats[j].accessible_name in positionNames

                        if val == False:
                            seats[j].click()
                            driver.find_element(By.XPATH, '//*[@id="NextStepImage"]').click()
                            driver.switch_to.default_content()

                            # 02. 이용요금선택
                            document = driver.find_element(By.XPATH, '//*[@id="ifrmBookStep"]')
                            driver.switch_to.frame(document)
                            driver.find_element(By.XPATH, '//*[@id="NextStepImage"]').click()
                            driver.switch_to.default_content()

                            # 03. 결제하기
                            document = driver.find_element(By.XPATH, '//*[@id="ifrmBookStep"]')
                            driver.switch_to.frame(document)
                            driver.find_element(By.XPATH, '//*[@id="YYMMDD"]').send_keys('861213')
                            driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div/table/tbody/tr[3]/td/label/input').click()
                            driver.find_element(By.XPATH, '//*[@id="BankCode"]').click()
                            driver.find_element(By.XPATH, '//*[@id="BankCode"]/option[6]').click()
                            driver.find_element(By.XPATH, '//*[@id="NextStepImage"]').click()
                            driver.switch_to.default_content()

                            # 03. (최종)결제하기
                            document = driver.find_element(By.XPATH, '//*[@id="ifrmBookStep"]')
                            driver.switch_to.frame(document)
                            driver.find_element(By.XPATH, '//*[@id="checkAll"]').click()

                            time.sleep(1)
                            driver.find_element(By.XPATH, '//*[@id="NextStepImage"]').click()

                            time.sleep(2)
                            #asyncio.run(sendTelegram('예약완료.'))  # 봇 실행하는 코드
                            flag = False

                else:
                    driver.switch_to.default_content()

    except Exception as e:
        print(e)


class App(threading.Thread):
    def __init__(self):
        super().__init__()

        # tkinter
        self.dp = Tk()
        self.dp.geometry("500x500")
        self.dp.title("인터파크 티케팅 프로그램")
        self.object_frame = Frame(self.dp)
        self.object_frame.pack()

        self.id_label = Label(self.object_frame, text="로그인")
        self.id_label.grid(row=1, column=0)

        self.login_btn = Button(self.object_frame, text="로그인", width=10, height=5, command=log_in)
        self.login_btn.grid(row=1, column=1)

        self.reser_lb = Label(self.object_frame, text="직링")
        self.reser_lb.grid(row=2, column=0)
        self.reservation_btn = Button(self.object_frame, text="직링", width=10, height=5, command=link_ticket)
        self.reservation_btn.grid(row=2, column=1)

        self.reser_lb = Label(self.object_frame, text="예약")
        self.reser_lb.grid(row=3, column=0)
        self.reservation_btn = Button(self.object_frame, text="예약", width=10, height=5, command=reservation_ticket)
        self.reservation_btn.grid(row=3, column=1)

        self.dp.mainloop()

    def payment(self):
        print('XXX')



app = App()
app.start()
