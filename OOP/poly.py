class Bank:
    __pvt = 5
    pub = 6

    def rateOfInterest(self):
        print (self.__pvt)
        return 0


class SBI(Bank):
    def rateOfInterest(self):
        return 10.5


obj1 = Bank().rateOfInterest()
print(obj1)
