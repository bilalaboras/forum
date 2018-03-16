import models

member1=models.Member("Ali", 20)
member2 = models.Member("Mohammed ", 30)

post1 = models.Post("the first title ", "this is the first post")
post2 = models.Post("the secend title ", "this is the second post")
post3 = models.Post("the third title ", "this is the third post")

#all_models=[member1, member2, post1, post2, post3]
print("*" * 20)
print member1
print  member2
print("*" *20 )

print "~"*5, "-"*5, "~"*10
print post1
print post2
print post3
print "~"*5, "-"*5, "~"*10