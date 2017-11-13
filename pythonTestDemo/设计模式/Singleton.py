#!coding:utf-8

class Singleton(object):
    """
    单例模式
    """
    class _A(object):
        """
        真正干活的类，对外隐藏
        """
        def __init__(self):
            pass

        def display(self):
            """返回当前的实例的id,是全局唯一的"""
            return id(self)

    _instance = None

    def __init__(self):
        """先判断类变量中是否已经保存了_A的实例，如果没有则创建一个返回"""
        if Singleton._instance is None:
            Singleton._instance = Singleton._A()

    def __getattr__(self,attr):
        """所有属性都应该直接从Singleton._instance"""
        return getattr(self._instance,attr)

if __name__ == "__main__":
    #创建两个实例
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1),s1.display())
    print(id(s2),s2.display())
