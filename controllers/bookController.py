import csv
from .validator import bookValidate
from .storage import Book_Addition, Book_Deletion, Listing_by_Search


class BookControl :

    '''This class controls all the functionalites related to book database'''
    
    def __init__(self) :
        self.header = ['Title', 'Author', 'isbn','Issued']
        self.file_path = 'books.csv'    
        with open(self.file_path, 'w', newline='') as csvfile :
                # Create a CSV writer object
            csv_writer = csv.writer(csvfile)
                # Write the header to the CSV file
            csv_writer.writerow(self.header)

    def takebookinputsforadd(self) :
        
        self.bookinfo = []
        for i in range(len(self.header)):
            if i!=3 :
                user_input = input("Enter "+ str(self.header[i])+":  " )
                self.bookinfo.append(user_input)
            else :
                self.bookinfo.append("0")
            
        val = bookValidate()
        if val.validate(self.bookinfo, self.file_path) :
            appnd = Book_Addition()
            appnd.book_add(self.bookinfo, self.file_path)
            
        else:
            print("Incorrect Credentials. Try again")

    def takeisbnfordel(self):
        
        self.isbn = input("Enter ISBN :")
        delt = Book_Deletion()
        delt.book_delete(self.isbn, self.file_path)

    def getsearchinput(self) :

        self.keyword = input("Enter keyword :")
        keyy = Listing_by_Search()
        keyy.show(self.keyword, self.file_path)



         


     

    
