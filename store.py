class MemberStore:
	"""docstring for MemberStore"""
	members = []
	last_id = 1

	def get_all(self):
		return MemberStore.members

	def add(self, member):
		member.id = MemberStore.last_id
		self.members.append(member)
		MemberStore.last_id += 1

	def get_by_id(self, id):
		all_mem = self.get_all()
		res = None
		for member in all_mem :
			if member.id == id:
				res = member
				break
		return res

	def entity_exists(self, member):
		res = True
		if self.get_by_id(member.id) is None:
			res = False

		return res

	def delete(self, id):
		member = self.get_by_id(id)
		MemberStore.members.remove(member)

	def update(self, member):
		all_mem = self.get_all()
		for i, me in enumerate(all_mem):
			if member.id == me.id:
				all_mem[i] = member
				break
				





class PostStore:
	"""docstring for PostStore"""
	postsS = []
	last_id = 1
	def get_all(self):
		return PostStore.postsS

	def add(self, post):
		post.id = PostStore.last_id
		PostStore.postsS.append(post)
		PostStore.last_id += 1

	def get_by_id(self, id):
		all_pos = self.get_all()
		res = None
		for post in all_pos:
			if post.id == id :
				res = post
				break
		return res

	def entity_exists(self, post):
		res = True
		if self.get_by_id(post.id) is None :
			res = False
		return res

	def delete(self, id):
		post = self.get_by_id(id)
		PostStore.postsS.remove(post)
		


		

		



		
	
		