def sort(Nums):
    for i in range(len(Nums), -1, -1):
        for j in range(0,i-1,1):
            if Nums[j] > Nums[j+1]:
                Nums[j],Nums[j+1] = Nums[j+1],Nums[j]
    return Nums

ls = [2, 3, 4,1,7,6,5]
print(sort(ls))
        
