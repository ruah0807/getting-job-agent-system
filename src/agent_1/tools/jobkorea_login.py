from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def login_and_search():
    # 환경 변수에서 로그인 정보 가져오기
    USER_NAME = os.getenv("JOBKOREA_USERNAME")
    PASSWORD = os.getenv("JOBKOREA_PASSWORD")

    # 웹 드라이버 설정
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.jobkorea.co.kr/Login/Login_Tot.asp")

    try:
        # 로그인 버튼 클릭
        time.sleep(2)  # 페이지 로딩 대기
        print("로그인 버튼 클릭 시도 중...")
        login_button = driver.find_element(By.ID, "btnGlLogin")
        print("로그인 버튼 찾음")
        login_button.click()
        print("로그인 버튼 클릭 완료")

        # 새로운 창으로 전환
        original_window = driver.current_window_handle
        print("창 전환 대기 중...")
        try:
            WebDriverWait(driver, 10).until(EC.new_window_is_opened(driver.window_handles))
            print("창 핸들 목록:", driver.window_handles)
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    print("새 창으로 전환 완료")
                    print("새 창 URL:", driver.current_url)  # 새 창의 URL 출력
                    break
        except Exception as e:
            print(f"창 전환 중 오류 발생: {e}")

        # 새 창의 요소 확인
        try:
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )
            email_input.send_keys(USER_NAME)
            email_input.send_keys(Keys.RETURN)
            print("이메일 입력 완료")
        except Exception as e:
            print(f"새 창에서 요소를 찾을 수 없습니다: {e}")

    except Exception as e:
        print(f"오류 발생: {e}")

    # 종료 대기
    input("브라우저를 닫으려면 Enter 키를 누르세요.")
    # driver.quit()  # 주석 처리하여 크롬이 닫히지 않도록 함

if __name__ == "__main__":
    login_and_search() 