from plus import count
#测试两个数相加
class TestCount:
    def test_add(self):
        try:
            j=count(5,10)
            add=j.add()
            assert (add==14),'you are foolish'

        except AssertionError as msg:
            print(msg)
        else:
            print('test pass')
# 执行测试类的测试方法
mytest=TestCount()
mytest.test_add()