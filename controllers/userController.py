import csv
from .validator import userValidate
from .storage import User_Addition, User_Deletion, User_checkin, User_checkout

class UserControl :

    def __init__(self) :
        self.header = ['Name', 'Age', 'empid','Books issued']
        self.file_path = 'users.csv'
        with open(self.file_path, 'w', newline='') as csvfile :
                # Create a CSV writer object
            csv_writer = csv.writer(csvfile)
                # Write the header to the CSV file
            csv_writer.writerow(self.header) 

    def takeuserinputsforadd(self) :      
        self.userinfo = []
        for i in range(len(self.header)):
            if i!=3 :
                user_input = input("Enter "+ str(self.header[i])+":  " )
                self.userinfo.append(user_input)
            else :
                self.userinfo.append("NIL")

        val = userValidate()
        if val.uservalidate(self.userinfo, self.file_path) :
            appnd = User_Addition()
            appnd.user_add(self.userinfo, self.file_path)
        else:
            print("Incorrect Credentials. Try again")

    def takeempidfordel(self):        
        self.isbn = input("Enter Emp-Id :")
        delt = User_Deletion()
        delt.user_delete(self.isbn, self.file_path)

    def checkin(self):
        self.empid = input("Enter Emp-Id : ")
        self.isbn = input("Enter the book ISBN : ")
        self.bookfilepath = "books.csv"       
        chkin = User_checkin()
        chkin.check_in(self.empid, self.isbn, self.file_path, self.bookfilepath)


    def checkout(self) :
        self.empid = input("Enter Emp-Id : ")
        self.isbn = input("Enter the book ISBN : ")
        self.bookfilepath = "books.csv"
        chkout = User_checkout()
        chkout.check_out(self.empid, self.isbn, self.file_path, self.bookfilepath)
