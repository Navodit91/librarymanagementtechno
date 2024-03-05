import csv

from controllers.bookController import BookControl
from controllers.userController import UserControl
#from controllers.database_handler import Book_Deletion
#from controllers.database_handler import Listing_by_Search


def main_menu():
    
    print("Library Management System")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Search book by keyword")
    print("4. Add user")
    print("5. Delete user")
    print("6. Checkin book")
    print("7. Checkout book")
    print("8. Exit")
    c = input("Enter choice: ") 
    return c


def main() :
    bookcontroller = BookControl()
    usercontroller = UserControl()
    while True :
        
        choice = main_menu()

        if choice == str(1) :
            bookcontroller.takebookinputsforadd()
        
        elif choice == str(2) :           
            bookcontroller.takeisbnfordel()

        elif choice == str(3) :           
            bookcontroller.getsearchinput()

        elif choice == str(4) :
            usercontroller.takeuserinputsforadd()

        elif choice == str(5) :
            usercontroller.takeempidfordel()

        elif choice == str(6) :
            usercontroller.checkin()

        elif choice == str(7) :
            usercontroller.checkout()

        elif  choice == str(8) :
            quit()



if __name__ == "__main__":
    main()

