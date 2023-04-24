from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time, pyautogui
from datetime import datetime
import winsound as sd

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

def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 10000     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

def interval_time():
    n = datetime.now()

    print("interval start - now({}), schedule({})".format(n, schedule_time))

    interval = schedule_time - n
    interval_seconds = interval.seconds + 1

    print("inerval time - {}".format(interval_seconds))

    if (interval.days < 0):
        print("previous time can't interval")
    else:
        time.sleep(interval_seconds)

    print("interval end - {}".format(datetime.now()))


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


def move_to_ticket_page():
    try:
        공연코드 = 21012652
        userSearch = f"https://tickets.interpark.com/goods/{공연코드}#"
        driver.get(userSearch)
        time.sleep(0.7)
        driver.find_element(By.XPATH, '//*[@id="popup-prdGuide"]/div/div[3]/button').click()
        #driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[2]/a[1]/span').click()

        ##driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[1]/div[2]/div/div/div/div/ul[3]/li[35]').click()
        labels = ['//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[35]'
                  , '//*[@id="productSide"]/div/div[1]/div[1]/div[2]/div/div/div/div/ul[3]/li[36]'
                  ]
        for i in labels:
            driver.find_element(By.XPATH, i).click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[1]/ul/li[1]').click()
            result = driver.find_element(By.XPATH,
                                         '//*[@id="productSide"]/div/div[1]/div[2]/div[2]/div[2]/ul/li/span').text
            if result == '매진':

                time.sleep(60)

            else:
                print('XXXXXX')
                beepsound()

        move_to_ticket_page()

        ##driver.find_element_by_xpath("/html/body/div/div[5]/div[1]/div/span[3]").click()
        ### 이 아래 콘피그랑 공연코드는 직접 설정하셔야합니다

        '''
        pyautogui.moveTo(572, 243, 0.5)  # 팝업닫기
        pyautogui.click(clicks=2, interval=1)
        pyautogui.moveTo(534, 671, 0.2)  # 창닫기
        pyautogui.click()
        pyautogui.moveTo(523, 390, 0.2)  # 자리선택
        pyautogui.click()
        pyautogui.moveTo(537, 390, 0.2)  # 자리선택
        pyautogui.click()
        pyautogui.moveTo(545, 390, 0.2)  # 자리선택
        pyautogui.click()

        pyautogui.moveTo(865, 672, 0.2)  # 선택완료
        pyautogui.click()

        pyautogui.moveTo(427, 532, 0.1)  # 문자입력
        pyautogui.click()
        '''

    except Exception as e:
        print(e)
        print("got exception(move_to_ticket_page)")


if (set_schedule):
    interval_time()

log_in()
move_to_ticket_page()