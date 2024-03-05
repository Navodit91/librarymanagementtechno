import csv

def is_convertible_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Book_Addition :
    '''This class adds a new book info in the library'''
    def init(self) :
        pass
    
    def book_add(self, data, file_path) :
        with open(file_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(data)
        print("Hurray! Book added successfully")


class Book_Deletion :
    '''This class removes an existing book info from the library'''

    def __init__(self):
        pass
    
    def book_delete(self, isbn, file_path) :
              
        data = []
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            for row in csv_reader:
                data.append(row)

        ls = []
        for row in data:
            ls.append(row[2])
        

        if is_convertible_to_int(isbn) :
            if isbn in ls :

                row_index = ls.index(isbn) + 1

                with open(file_path, 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    data = list(csv_reader)
                
                del data[row_index]
                # Write the updated data back to the CSV file
                with open(file_path, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(data)
                print("Book deleted successfully")
            else :
                print("Oops! Invalid ISBN ")

        else :
            print("Oops! Invalid ISBN ")

class Listing_by_Search :
    '''This class helps user search a book by any keyword in the library'''
    def __init__(self):
        pass

    def show(self,keyword , file_path) :

        if len(keyword)>0 :

            with open(file_path, 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    data = list(csv_reader)
                    
            res = []
            for i in range(1, len(data)):

                if keyword in data[i] :
                    res.append(data[i])
            rows_as_string = '\n'.join(','.join(row) for row in res)

            if len(rows_as_string) == 0 :
                print("No matches found")
            else :
                print(rows_as_string)

    

class User_Addition :
    '''This class adds a new user info in the library'''
    def init(self) :
        pass
    
    def user_add(self, data, file_path) :
        with open(file_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(data)
        print("Hurray! User added successfully")

class User_Deletion :
    '''This class removes an existing user info from the library'''
    def __init__(self):
        pass
    
    def user_delete(self, empid, file_path) :
              
        data = []
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            for row in csv_reader:
                data.append(row)

        ls = []
        for row in data:
            ls.append(row[2])
        
        if is_convertible_to_int(empid) :
            if empid in ls :

                row_index = ls.index(empid) + 1

                with open(file_path, 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    data = list(csv_reader)
                
                del data[row_index]
                # Write the updated data back to the CSV file
                with open(file_path, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(data)
                print("User deleted successfully")
            else :
                print(" User not found. ")

        else :
            print("Oops! Invalid Emp Id ")

class User_checkin :
    '''This class lets the user issue an existing book from the library'''
    def __init__(self) :
        pass

    def check_in(self, empid, isbn, file_path, bookfliepath):

        bookdata = []
        with open(bookfliepath, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            bookheader = next(csv_reader)
            for row in csv_reader:
                bookdata.append(row)
        
        fp = True
        for i in range(len(bookdata)):
            if bookdata[i][2]== isbn :
                idx = i
                if bookdata[i][3] == "1" :
                    fp = False
                    break

        ls = []
        for row in bookdata:
            ls.append(row[2])
        data = []
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            for row in csv_reader:
                data.append(row)
        
        
        if fp :
            if str(isbn) in ls :
                fl = False
                for i in range(len(data)) :
                    print(data[i][2])
                    if data[i][2]== empid :
                        fl = True
                        
                        if data[i][3] == "NIL" :
                            data[i][3] = str(isbn)
                            bookdata[idx][3] = "1"
                            
                        else :
                            data[i][3]= data[i][3] + "," + str(isbn)
                            bookdata[idx][3] = "1"
                        print("Book issued to user successfully")
                        break
                if not fl :
                    print("Invalid Emp Id")

            else :
                print("Book isbn not found")
        
        else :
            print("Book already issued")
        
        with open(file_path, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(header)
                    csv_writer.writerows(data)

        with open(bookfliepath, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(bookheader)
                    csv_writer.writerows(bookdata)         



class User_checkout :

    '''This class lets the user return a issued book from the library'''

    def __init__(self) :
        pass

    def check_out(self, empid, isbn, file_path, bookfliepath):

        bookdata = []
        with open(bookfliepath, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            bookheader = next(csv_reader)
            for row in csv_reader:
                bookdata.append(row)
        
        ls = []
        for row in bookdata:
            ls.append(row[2])

        fo = True
        for i in range(len(bookdata)):
            if bookdata[i][2]== isbn :
                idx = i
                if bookdata[i][3] == "0" :
                    fo = False
                    break
        
        data = []
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            for row in csv_reader:
                data.append(row)


        if fo :
            if str(isbn) in ls :
                fl = False
                for i in range(len(data)) :
                    print(data[i][2])
                    if data[i][2]== empid :
                        fl = True
                        
                        if data[i][3] == "NIL" :
                            print("Not a single book was issued by user")
                        elif isbn not in data[i][3].split(",") :
                            print("This book was not issued by the user")
                        else :
                            data[i][3].remove(isbn)
                            bookdata[idx][3] = "0"
                            print("Book checked-out by user successfully")
                        break
                if not fl :
                    print("Invalid Emp Id")
            else :
                print("Book isbn not found")
        
        else :
            print("This book was not issued by the user")
            