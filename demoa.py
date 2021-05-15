import unittest
def add(x,y):
    z = x + y
    return z

#print(add(3,4) == 7)
#print(add(3,4) == 8)
#print(add(1.2,4.5) == 5.7)





class TestDemoAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('fafadf')
    @classmethod
    def tearDownClass(cls) -> None:
        print('sdfsfsd')
    def setUp(self) -> None:
        print('fdsafd')
    def tearDown(self) -> None:
        print('dfsdf')




    def test_add01(self):
        self.assertEqual(7,add(3,4))

    def test_add02(self):
        self.assertEqual(None,add(3,4))

    def test_add03(self):
        self.assertEqual(5.7,add(1.2,4.5))

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestDemoAdd('test_add01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)