#Divide and Conquer Algorithm
#Time Complexity - O(nlogn)
def merge(l,low,mid,high,a):
    l=[]
    start1=low
    start2=mid+1
    while start1<=mid and start2<=high:
        if a[start1]<a[start2]:
            l.append(a[start1])
            start1=start1+1
        else:
            l.append(a[start2])
            start2+=1
    while start1<=mid:
        l.append(a[start1])
        start1=start1+1
    while start2<=high:
        l.append(a[start2])
        start2=start2+1
a=[12,54,78,43,9,72,0,45,23]
