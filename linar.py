#训练数据
dots = [[1,1] , [2,2] , [3,3] , [4,4]]
#计算

sumX = 0
sumY = 0
cnt = 0
for x,y in dots:
	sumX += x
	sumY += y
	cnt +=1
xAve = sumX / cnt
yAve = sumY / cnt
b = 0
for x,y in dots:
	b += (x - xAve) * (y - yAve)

bt = 0
for x,y in dots:
	bt += ((x - xAve) * (x - xAve))

b /= bt
a = sumY - sumX * b

def predict(x):
	return x * b + a

print(predict(5))
print(predict(666))

