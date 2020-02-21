class JustCounter:
    __secretCout = 0

    def count(self):
        self.__secretCout += 1
        print(self.__secretCout)


counter = JustCounter()
counter.count()
#counter.count()
print(counter._JustCounter__secretCout)
#print(counter.__secretCout)




