# this program is more likely based on pomotriod fo 4 times  every 35 minutes give 5 minuter break and last give 20 minutes.
a=input("please name this task")
import time as tm
#import os
#print(tm.time())
#print(tm.ctime())
#print(tm.localtime())
for g in range(4):
	for i in range(2100):
		# using sleep() to hault execution
		tm.sleep(300)
		print(i)
	#file = "(SpaceAdbentureIntroduction)DavidFrsliyan.mp3"
	#os.system("mpg123 " + file)
	print(tm.sleep(2))
print(tm.sleep(900))

Print ("Finished",a)