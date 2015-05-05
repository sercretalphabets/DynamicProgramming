__author__ = 'Maryam Esmaeili'




class Knapsack():


    def __init__(self, items,c):
        self.items=items
        self.progress=[(0,0)]
        self.c=c

    def knapsack(self):

        table = [[0 for w in range(self.c + 1)] for j in xrange(len(self.items) + 1)]

        for j in xrange(1, len(self.items) + 1):
            item, wt, val = self.items[j-1]
            for w in xrange(1, self.c + 1):
                if wt > w:
                    table[j][w] = table[j-1][w]
                else:
                    table[j][w] = max(table[j-1][w],table[j-1][w-wt] + val)
        print "This  is the value of the bag", table[len(self.items)][self.c]

        bag = []
        w = self.c
        for j in range(len(self.items), 0, -1):
            if (table[j][w] != table[j-1][w]):
                item, wt, val = self.items[j-1]
                bag.append(self.items[j-1])
                w -= wt

        return bag




def main():
    items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )

    a=Knapsack(items,400 )
    bag=a.knapsack()
    print bag


if __name__ == "__main__":
    main()


