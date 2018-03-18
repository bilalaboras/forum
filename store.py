class MemberStore:
	"""docstring for MemberStore"""
	members = []

	def get_all(self):
		return MemberStore.members

	def add(self, member):

		self.members.append(member)

	def get_by_id(self, id):
		all_mem = self.get_all()

		res = None
		for item in all_mem :
			if member.id == id:

				res = member
			return res


class PostStore:
	"""docstring for PostStore"""
	postsS = []


	def get_all(self):
		return PostStore.postsS

	def add(self, post):
		PostStore.postsS.append(post)

	def get_by_id(self, id):
		all_pos = self.get_all()

		res = None

		for item1 in all_pos:
			if post.id == id :
				res = post

			return res


		

		



		
	
		