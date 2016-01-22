#bloom filter By Radish

__MAX__ = 10000

tmp = [1 for x in range(1,__MAX__)] #create array

def bloomHash(string):
	count = 0
	for i in string:
		count += ord(i)
	return count

def bloomSet(string):

	num = abs(bloomHash(string)%__MAX__)
	tmp[num] = 0
	return num

def bloomCheck(string):
	num = abs(bloomHash(string)%__MAX__)
	if tmp[num] == 0 :
		return True
	else :
		return False

print(bloomSet("12345666"))
print(bloomCheck("12345666"))