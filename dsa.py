class solution:
    def getMonthName(self, monthNumber):
        #Write your code here...
        if monthNumber==1:
            print("January")
        if monthNumber==2:
            print("February")
        if monthNumber==3:
            print("March")
        if monthNumber==4:
            print("April")
        if monthNumber==5:
            print("May")
        if monthNumber==6:
            print("June")
        if monthNumber==7:
            print("July")
        if monthNumber==8:
            print("August")
        if monthNumber==9:
            print("September")
        if monthNumber==10:
            print("October")
        if monthNumber==11:
            print("November")
        if monthNumber==12:
            print("December")
        else:
            print("Invalid input!")

if __name__=="__main__":
    monthNumber=int(input())
    sol=solution()
    sol.getMonthName(monthNumber)