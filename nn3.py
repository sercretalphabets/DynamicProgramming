__author__ = 'm.esmaeili'


def ksmallest(A,B,k):
    res=set()
    indA=0
    indB=0
    counter=0
    while counter<k and indA<len(A) and indB<len(B):
        #print indA,indB
        res.add((A[indA],B[indB]))
        counter+=1
        if A[indA] <= B[indB]:
            primindB=indB
            if A[indA]+B[indB+1]<A[indA+1]+B[indB]:
                while A[indA]+B[indB+1]<A[indA+1]+B[indB] and counter<k and indA<len(A)-1 and indB<len(B)-1:
                    currentsum=A[indA]+B[indB+1]
                    res.add((A[indA],B[indB+1]))
                    counter+=1
                    indB+=1
                indB=primindB
            while A[indA+1]<=B[indB] and counter < k:

                indA+=1
                currentsum=A[indA]+B[indB]
                res.add((A[indA],B[indB]))
                #print res
                counter+=1
            indB+=1
            if B[indB]<=currentsum:
                indA=0
            else:
                indA+=1
                indB=0
        else:
            primindA=indA
            if B[indB]+A[indA+1]<A[indB+1]+B[indA]:
                while B[indB]+A[indA+1]<A[indB+1]+B[indA] and counter<k and indA<len(A)-1 and indB<len(B)-1:
                    currentsum=A[indA+1]+B[indB]
                    res.add((A[indA],B[indB]))
                    counter+=1
                    indA+=1
                indA=primindA

            while A[indA]>=B[indB+1] and counter <k:
                indB+=1
                currentsum=A[indA]+B[indB]
                res.add((A[indA],B[indB]))
                #print res
                counter+=1
            indA+=1
            if A[indA]<=currentsum:
                indB=0
            else:
                indB+=1
                indA=0


    return res
def main():
    A= [1,2,3,5,7,8,9]
    B= [2,4,5,9,12,13,15]
    #print
    n=ksmallest(A,B,4)
    print n

    B= [  1,   50,  100, 1000, 6000, 6002, 6004, 6006, 6008, 6010 ]
    A=[100,  200,  300, 2000, 3000, 4000, 5000, 6000, 7000, 8000 ]
    n=ksmallest(A,B,4)
    print n


    A=[1,5,7,35,42]
    B=[6,8,9,35,37]
    n=ksmallest(A,B,3)
    print n
    n=ksmallest(A,B,4)
    print n



if __name__ == "__main__":
    main()
