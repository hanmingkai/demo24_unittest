

#  导入HTMLTestRunner
import unittest

from HTMLTestRunner import HTMLTestRunner


#  定义一个测试报告文件夹
report_file = 'test_report.html'

# 创建套件

suite = unittest.TestLoader().discover('.',pattern="demo*.py")

# 生成一个runner

with open(report_file,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='V12测试报告')
    runner.run(suite)