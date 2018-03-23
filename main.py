import models
import store

def create_members():
	member1=models.Member("Ali", 20)
	member2 = models.Member("Mohammed ", 30)
	member3=models.Member("Ahmed", 22)

	print("*" * 20)
	print member1
	print member2
	print member3
	print("*" *20 )

	return member1, member2, member3

def store_should_add_models(members_instances, member_store):
	for member in members_instances:
		member_store.add(member)

def store_should_be_similar():
	mem_store1 = store.MemberStore()
	mem_store2 = store.MemberStore()
	if mem_store1.get_all() is mem_store2.get_all():
		print ("Same stores elements !")

def prnit_all_members(mem_store):
	print ("-" * 30)
	for member in mem_store.get_all():
		print (member)
	print ("-" * 30)

def get_by_id_should_retrieve_same_object(member_store, member2):
	member2_retrieved = member_store.get_by_id(member2.id)
	if member2 is member2_retrieved:
		print ("member2 and member2_retrieved are maching !")
		
def update_should_modify_object(mem_store, member3):
	member3_copy = models.Member(member3.name, member3.age)
	member3_copy.id = 3

	if member3_copy is not member3:
		print ("member3 and member3_copy are not the Same !")
	print (member3_copy)
	member3_copy.name = "john"
	mem_store.update(member3_copy)
	print (mem_store.get_by_id(member3.id))

def catch_exception_when_delete():
    try:
        mem_store.delete(5)
    except ValueError:
        print("It shoude be an existence entity befere deleting !")

members_instances = create_members()
member1, member2, member3 = members_instances

mem_store = store.MemberStore()
store_should_add_models(members_instances, mem_store)
store_should_be_similar()

prnit_all_members(mem_store)
get_by_id_should_retrieve_same_object(mem_store, member2)	
update_should_modify_object(mem_store, member3)

catch_exception_when_delete()

prnit_all_members(mem_store)



post1 = models.Post("the first title ", "this is the first post")
post2 = models.Post("the secend title ", "this is the second post")
post3 = models.Post("the third title ", "this is the third post")



#all_models=[member1, member2, post1, post2, post3]


print "~"*5, "-"*5, "~"*10
print post1
print post2
print post3
print "~"*5, "-"*5, "~"*10