import sqlite3

# Create a SQL connection to our SQLite database
class dataBase():

    def sorted_ascending(self, num):

        con = sqlite3.connect('admin2.db')
        cur = con.cursor()
        lst =[]

        for row in cur.execute('SELECT * FROM dog_info;'):
            ele = row[num]  
            lst.append(ele)
            print(row[num])
    
        sorted_lst = lst
        sorted_lst.sort()
        print(sorted_lst)

        con.close()
 
    def sorted_descending(self, num):

        con = sqlite3.connect('admin2.db')
        cur = con.cursor()
        lst =[]

        for row in cur.execute('SELECT * FROM dog_info;'):
            ele = row[num]  
            lst.append(ele)
            print(row[num])
    
        des_sorted_lst = lst
        des_sorted_lst.sort(reverse=True)
        print(des_sorted_lst)

        con.close()
 
 
 
        
access = dataBase()
access.sorted_ascending(1)
access.sorted_descending(1)
