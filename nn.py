def kSmallestPair(a,b,k):
    M = len(a)
    N = len(b)

    (ia,ib) = 0,0 #0 based arrays
    # we need this for lookback
    nottakenindices = (0,0) # could be any value
    nottakensum = float('inf')
    for i in range(k-1):
        optionone = a[ia+1]+b[ib]
        optiontwo = a[ia]+b[ib+1]
        biggest = min((optionone,optiontwo))
        #first deal with look behind
        if nottakensum < biggest:
           if optionone == biggest:
               newnottakenindices = (ia+1,ib)
           else: newnottakenindices = (ia,ib+1)
           ia,ib = nottakenindices
           nottakensum = biggest
           nottakenindices = newnottakenindices
        #deal with case where indices hit 0
        elif ia >= M and ib >= N:
             ia = ib = 0
        elif ia <= 0:
            ib-=1
            ia = 0
            nottakensum = float('-inf')
        elif ib <= 0:
            ia-=1
            ib = 0
            nottakensum = float('-inf')
        #lookahead cases
        elif optionone > optiontwo:
           #then choose the first option as our next pair
           nottakensum,nottakenindices = optiontwo,(ia-1,ib)
           ib-=1
        elif optionone < optiontwo:

           #then choose the first option as our next pair
           nottakensum,nottakenindices = optiontwo,(ia-1,ib)
           ib-=1
        elif optionone < optiontwo: # choose the second
           nottakensum,nottakenindices = optionone,(ia,ib-1)
           ia-=1
        #next two cases apply if options are equal
        elif a[ia] > b[ib]:# drop the smallest
           nottakensum,nottakenindices = optiontwo,(ia-1,ib)
           ib-=1
        else: # might be equal or not - we can choose arbitrarily if equal
           nottakensum,nottakenindices = optionone,(ia,ib-1)
           ia-=1
        #+2 - one for zero-based, one for skipping the 1st largest
        data = (i+2,a[ia],b[ib],a[ia]+b[ib],ia,ib)
        narrative = "%sth largest pair is %s+%s=%s, with indices (%s,%s)" % data
        print (narrative) #this will work in both versions of python
        if ia <= 0 and ib <= 0:
           raise ValueError("Both arrays exhausted before Kth (%sth) pair reached"%data[0])
    return data, narrative


def main():
    A= [1,2,3,5,7]
    B= [3,4,5,9,12]
    print
    n=kth(A,B,6)
    print n


if __name__ == "__main__":
    main()
