__author__ = 'm.esmaeili'


def smallest (A,B,k):
    res=set()

    aind=bind=counter=0
    sofarSum=A[0]+B[0]
    res.add((A[0],B[0]))
    print "sofarSum",sofarSum
    while counter<k:
        S1=A[aind+1]+B[bind]
        print "S1",S1
        S2=A[aind+1]+B[0]
        print "S2",S2
        S3=A[aind]+B[bind+1]
        print "S3",S3
        S4=A[0]+B[bind+1]
        print "S4",S4
        print"sofar",sofarSum

        if ((S1<=sofarSum)  and (aind+1<len(A)) and S2>=sofarSum and S3>=sofarSum and S4>=sofarSum):
            print"11111"
            aind+=1
        elif ((S2<=sofarSum) and  (aind+1<len(A)) and S1>=sofarSum and S3>=sofarSum and S4>=sofarSum):
            print "2222"
            aind+=1
            bind=0
        elif ((S3<=sofarSum and bind+1<len(B) and S1>=sofarSum and S2>= sofarSum and S4>=sofarSum)):
            print "3333"
            bind+=1
        elif ((S4<=sofarSum and bind+1<len(B) and S1>=sofarSum and S2>=sofarSum and S3>=sofarSum)):
            print "4444"
            bind+=1
            aind=0
        elif A[aind]<B[bind]:
            aind+=1
        else:
            if aind+1 >= len(A):
                if bind+1 >= len(B):
                    return
                else:
                    bind+=1
            else:
                aind+=1

        print aind
        print bind
        sofarSum=A[aind]+B[bind]
        res.add((A[aind],B[bind]))
        counter=len(res)
    return res





def main():
    A= [1,2,3,5,7,8,9]
    B= [3,4,5,9,12,13,15]
    print
    n=smallest(A,B,6)
    print n


if __name__ == "__main__":
    main()





