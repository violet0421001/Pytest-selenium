import pytest
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome import service as chrome_fs
from selenium.webdriver.edge import service as edge_fs
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import pytest
def pytest_configure(config):
   project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
   os.environ['PYTHONPATH'] = project_root
   sys.path.insert(0, project_root)  # 动态添加项目根目录到 sys.path


@pytest.fixture(scope="session")
def driver():
   load_dotenv("../config.env")
   print("Start loading driver...")

   DRIVER_PATH = os.getenv("DRIVER_PATH")
   BROWSER_TYPE = os.getenv("BROWSER_TYPE", "chrome")  # 默认浏览器类型为 chrome

   print(f"Using browser: {BROWSER_TYPE}")
   options = ChromeOptions()

   # 设置浏览器界面语言为日语（ja-JP）
   options.add_argument('--locale=ja-JP')

   # 自动安装 ChromeDriver
   service = ChromeService(ChromeDriverManager().install())

   # 创建 Chrome 浏览器的实例
   driver = webdriver.Chrome(service=service, options=options)

   # if BROWSER_TYPE == "chrome":

   # elif BROWSER_TYPE == "edge":
   #    options = EdgeOptions()
   #    driver = webdriver.Edge(service=edge_fs.Service(executable_path=DRIVER_PATH), options=options)
   # else:
   #    print("Warning: Unsupported BROWSER_TYPE, continuing with Chrome driver.")
   #    options = webdriver.ChromeOptions()
   #    options.add_argument('--lang=ja')
   #    options.add_argument('--locale=ja-JP')
   #    service = ChromeService(ChromeDriverManager().install())
   #    driver = webdriver.Chrome(service=service, options=options)

   yield driver
   print("Driver closed.")
   driver.quit()

@pytest.fixture(scope="session")
def url():
   load_dotenv()
   BASE_URL = os.getenv("BASE_URL")
   assert BASE_URL is not None, "base url is not given."
   yield BASE_URL