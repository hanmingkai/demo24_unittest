import unittest
from parameterized import parameterized
def add(x,y):
    z = x + y
    return z

#print(add(3,4) == 7)
#print(add(3,4) == 8)
#print(add(1.2,4.5) == 5.7)





class TestDemoAdd(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('fafadf')
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('sdfsfsd')
    # def setUp(self) -> None:
    #     print('fdsafd')
    # def tearDown(self) -> None:
    #     print('dfsdf')
    date = [(7,3,4),(5,3,2),(9,5,4)]
    @parameterized.expand(date)

    def test_add(self,c,b,a):
        res = add(a,b)
        self.assertEqual(c,res)


    @unittest.skip('失效用例')
    def test_add01(self):
        res1 = add(3,4)
        self.assertEqual(7,res1)

    def test_add02(self):
        res2 = add(0,1)
        self.assertEqual(1,res2)

    def test_add03(self):
        res3 = add(-1,3)
        self.assertEqual(2,res3)

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemoAdd('test_add01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
