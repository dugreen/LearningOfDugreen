#coding:utf-8

"""
过滤器简单实现
"""

class Filter():
    def __init__(self,list=[]):
        self.blocked = list
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def __init__(self,list=[]):
        self.blocked = list


s = SPAMFilter()
s.__init__(['SPAM','eggs'])

print(s.filter(["SPAM","SPAM" ,"eggs","bacon", "SPAM","SPAM"]))
f= Filter()
f.__init__([10])

print(f.filter([10,20,30,50,10]))
