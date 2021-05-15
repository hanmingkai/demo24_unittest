import unittest

#生成套件、
# suite = unittest.TestLoader().discover(start_dir= '.',pattern = 'demo*.py')
#
# runner = unittest.TextTestRunner()
# runner.run(suite)
from demoa import TestDemoAdd
suite = unittest.TestSuite()
suite.addTest(TestDemoAdd('test_add01'))
runner = unittest.TextTestRunner()
runner.run(suite)