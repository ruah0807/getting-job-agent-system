from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import traceback
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

def login_and_search():
    # 환경 변수에서 로그인 정보 가져오기
    USER_NAME = os.getenv("JOBKOREA_USERNAME")
    PASSWORD = os.getenv("JOBKOREA_PASSWORD")

    if USER_NAME is None or PASSWORD is None:
        print("환경 변수 'JOBKOREA_USERNAME' 또는 'JOBKOREA_PASSWORD'가 설정되지 않았습니다.")
        return

    # 웹 드라이버 설정
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.jobkorea.co.kr/Login/Login_Tot.asp")

    try:
        # 페이지 로딩 대기
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "M_ID")))

        # 아이디 입력 필드 찾기
        id_input = driver.find_element(By.ID, "M_ID")
        id_input.send_keys(USER_NAME)
        print("아이디 입력 완료")

        # 비밀번호 입력 필드 찾기
        password_input = driver.find_element(By.ID, "M_PWD")
        password_input.send_keys(PASSWORD)
        print("비밀번호 입력 완료")

        # 로그인 버튼 찾기
        login_button = driver.find_element(By.CLASS_NAME, "login-button")
        login_button.click()
        print("로그인 버튼 클릭 완료")

    except Exception as e:
        print(f"오류 발생: {e}")
        traceback.print_exc()

    # 종료 대기
    input("브라우저를 닫으려면 Enter 키를 누르세요.")
    # driver.quit()  # 주석 처리하여 크롬이 닫히지 않도록 함

if __name__ == "__main__":
    login_and_search() 