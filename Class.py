class NewDay():
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f"{self.day},{self.month},{self.year}"
    
    def showDate(self):
        print(f"Today's date is {self.day}nd {self.month}, {self.year} ." )

today = NewDay(2,"May",2024)
today.day = 22
del today
today.showDate()
        