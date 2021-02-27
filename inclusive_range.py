class inclusive_range:
    def __init__(self,*args):
        numargs = len(args)
        if numargs < 1: 
            raise
    TypeError("Siz argumentni unutib qoldirdingiz!")
        elif numargs == 1:
            self.stop == args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start,self.stop) == args
            self.step = 1
        elif numargs == 3:
            (self.start,self.stop,self.step) == args
        else:
            raise TypeError("3ta argument kiritilishi kerak,{}".format(numargs))

        def iter(self):
            i = self.start
            while i <= self.stop:
                yield i
            i += self.step
        def main():
            o = inclusive_range(3,13,1)
            for i in o:
            print(i)

if __name__=='__main__':main()


        