class Member:
	"""docstring for member"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return  "Name: {}, Age: {}".format(self.name, self.age)



class Post:
	"""docstring for ClassName"""
	def __init__(self, title, content):
		self.title = title
		self.content = content

	def __str__(self):
		return "POST title: {},  POST content :{}".format(self.title, self.content)

		
		
		