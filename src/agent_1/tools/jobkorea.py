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
        print("로그인 시작")
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
        
        print("잡 검색 시작")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "stext")))

        search_input = driver.find_element(By.ID, "stext")
        search_input.send_keys("파이썬")
        search_input.send_keys(Keys.ENTER)
        print("잡 검색 완료")

        print("직무 선택 시작")
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='jobtype']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='개발·데이터']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='백엔드개발자']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='웹개발자']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='앱개발자']")
        jobtype_button.click()
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-submit'][data-name='직무']")
        submit_button.click()
        
        print("지역 선택 시작")
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='location']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='서울']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='경기']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='경기 > 성남시 분당구']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='경기 > 성남시 수정구']")
        jobtype_button.click()
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='경기 > 성남시 중원구']")
        jobtype_button.click()
        submit_button_location = driver.find_element(By.CSS_SELECTOR, "button[class='button-submit'][data-name='지역']")
        submit_button_location.click()

        print("경력 선택 시작")
        jobtype_button = driver.find_element(By.CSS_SELECTOR, "button[data-name='career']")
        jobtype_button.click()
        checkbox_label = driver.find_element(By.CSS_SELECTOR, "label[for='careertype1']")
        checkbox_label.click()
        checkbox_label = driver.find_element(By.CSS_SELECTOR, "label[for='careertype4']")
        checkbox_label.click()
        checkbox_label = driver.find_element(By.CSS_SELECTOR, "label[for='expYear_1_3']")
        checkbox_label.click()
        submit_button_career = driver.find_element(By.CSS_SELECTOR, "button[class='button-submit'][data-name='경력']")
        submit_button_career.click()


    except Exception as e:
        print(f"오류 발생: {e}")
        traceback.print_exc()

    

    # 종료 대기
    input("브라우저를 닫으려면 Enter 키를 누르세요.")
    # driver.quit()  # 주석 처리하여 크롬이 닫히지 않도록 함

if __name__ == "__main__":
    login_and_search() 