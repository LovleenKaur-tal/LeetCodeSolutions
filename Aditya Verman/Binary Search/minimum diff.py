

lt = [1,3,8,10,15]
target = 12
l = 0
r = len(lt)-1

while(l<=r):
    mid = (l+r)//2
    if lt[mid]==target:
        print(target)
        break
    elif target >lt[mid]:
        l = mid+1
    else:
        r = mid-1

print(min(lt[l]-target, lt[r]-target))



