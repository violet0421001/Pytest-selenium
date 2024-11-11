激活python虚拟环境 source .venv/bin/activate
安装全部依赖 pip install -r requirements.txt
运行测试 pytest --alluredir ./report/result
查看测试报告 allure serve ./report/result
