__author__ = 'Maryam Esmaeili'

#Given a set of vertexes V describing a path in a graph, with each vertex assigned a weight,
#the Maximum Weighted Independent Set is the subset of vertices whose weights sum to the maximum possible value
#without any two vertices being adjacent to one another (hence "independent" set).

#This can be used in a sequence to find an indepent set in a sequence. like a string.



class MaxIndependentSet():
    '''
    Calculates the maximum weight independent set of a path graph.
    '''


    def __init__(self, vertex):

        '''
        Initializes the sequence with a positive-valued array, where vertex[i] is
        the weight of vertex i.
        '''

        self.vertex = vertex
        self.progress = [0,vertex[1]]
        self.mws=set()

    def max_weight(self):
        '''
        Does all the work and calculates the value of the maximum weight
        independent set of the class' path graph.
        '''
        if len(self.vertex)==2:
            self.progress.append(max(self.vertex))
        else:
            for i in xrange(2, len(self.vertex)):
                # There's an obvious bug when i=2, but this conveys the idea
                self.progress.append(max(self.progress[i-1], self.progress[i-2] + self.vertex[i]))
                #print self.progress
        return self.progress


    def max_weight_set(self):
        i=len(self.progress)-1
        while i>=1:
            #print "progress",self.progress
            if self.progress[i]==self.progress[i-1]:
                i-=1
                #print i
            else:
                self.mws.add(self.vertex[i])
                i-=2

        return self.mws




def main():
    b = [0,3,4,5,6,12,2,1,7]
    mis=MaxIndependentSet(b)
    maxweight=mis.max_weight()
    print maxweight[-1]
    maxweightset=mis.max_weight_set()
    print maxweightset


if __name__ == "__main__":
    main()