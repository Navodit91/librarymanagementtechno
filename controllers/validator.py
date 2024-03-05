import csv


class bookValidate : 

    '''This class intends to validate the book information inputted by the user is in correct format'''

    def __init__(self) :
        pass

    def validate(self,args,file_path) :
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)
        rs = []
        for ele in data :
            rs.append(ele[2])
        for i in range(len(args)) :            
            if args[i] in rs :
                return False
                break
            elif len(args[i]) == 0 :
                return False
                break
        return True
    

class userValidate : 
    
    
    '''This class intends to validate the user information inputted by the user is in correct format'''

    def __init__(self) :
        pass

    def uservalidate(self,args,file_path) :
        return True
