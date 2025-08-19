import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 时区处理（北京时间）
beijing_time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
print(f"当前北京时间: {beijing_time}")

# 配置 Chrome 无头模式
options = Options()
options.add_argument("--headless")  # 无界面运行
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 初始化 WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Step 1: 登录页面
    driver.get("https://minekuai.com/index/login")
    print("已打开登录页面")

    # 输入用户名和密码
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("tzyleo")
    password.send_keys("1q2w3e4r5t")
    print("已输入账号密码")

    # 点击登录按钮
    login_button = driver.find_element(
        By.CSS_SELECTOR, 
        "button.w-full.bg-gradient-to-r.from-blue-500.to-purple-600"
    )
    login_button.click()
    print("已点击登录按钮")
    time.sleep(5)  # 等待登录完成

    # Step 2: 跳转到目标页面
    driver.get("https://minekuai.com/server/9978681d")
    print("已进入服务器页面")

    # 点击“跳过”按钮
    skip_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.absolute.top-4.right-4.w-8.h-8")
        )
    )
    skip_button.click()
    print("已点击跳过按钮")
    time.sleep(2)

    # Step 3: 持续点击“启动”按钮（5分钟）
    start_time = time.time()
    while time.time() - start_time < 300:  # 5分钟 = 300秒
        start_button = driver.find_element(
            By.CSS_SELECTOR, 
            "button.style-module_4LBM1DKx.style-module_3kBDV_wo.flex-1"
        )
        start_button.click()
        print(f"已点击启动按钮 - 剩余时间: {300 - (time.time() - start_time):.0f}秒")
        time.sleep(1)  # 每秒点击一次

except Exception as e:
    print(f"发生错误: {e}")
finally:
    driver.quit()
    print("脚本执行完毕")
