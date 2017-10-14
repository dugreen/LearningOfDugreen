#coding:utf-8

"""
单链表实现
"""
class Node(object):
	"""节点"""
	def __init__(self,elem):
		self.elem = elem
		self.next = None

class SingleLinkList(object):
	"""单链表"""
	def __init__(self, node = None):
		self.__head = node

	def is_empty(self):
		"""判断链表是否为空"""
		return self.__head == None

	def length(self):
		"""链表长度"""
		current = self.__head
		count = 0
		while current != None:
			count += 1
			current = current.next
		return count

	def travel(self):
		"""遍历链表"""
		current = self.__head
		while current != None:
			print(current.elem)
			current = current.next

	def add(self,item):
		"""链表头部添加元素"""
		node = Node(item)
		node.next = self.__head
		self.__head = node

	def append(self,item):
		"""链表尾部添加元素"""
		node = Node(item)
		#判断链表是否为空
		if self.is_empty():
			self.__head = node
		else:
			current = self.__head
			while current.next != None:
				current = current.next
			current.next = node
	def insert(self,pos,item):
		"""指定位置添加元素"""
		if pos < 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count < pos-1 :
				count += 1
				pre = pre.next
			# 当循环退出后,pre指向pos-1的位置
			node = Node(item)
			node.next = pre.next
			pre.next = node

	def remove(self,item):
		"""删除节点"""
		current = self.__head
		pre = None
		while current != None:
			if current.elem == item:
				#头节点情况
				if current == self.__head:
					self.__head = current.next
				else:
					pre.next = current.next
				break
			else:
				pre = current
				current = current.next

	def search(self,item):
		"""查找结点是否存在"""
		current = self.__head
		while current != None:
			if current.elem == item:
				return True
			else:
				current = current.next
		return False

if __name__ == "__main__":
	single_obj = SingleLinkList()
	print(single_obj.is_empty())
	print(single_obj.length())
	single_obj.append(50)
	single_obj.append(47)
	single_obj.append(58)
	single_obj.add(1)
	single_obj.add(0)
	single_obj.insert(2,100)
	single_obj.insert(9,147)
	single_obj.travel()
	single_obj.remove(100)
	print(single_obj.search(100))
