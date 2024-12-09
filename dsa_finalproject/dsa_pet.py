import sqlite3

# Create a SQL connection to our SQLite database
class dataBase():
    
    def sorted_ascending(self, num):

        con = sqlite3.connect('admin3.db')
        cur = con.cursor()
        lst =[]

        for row in cur.execute('SELECT * FROM pet_info_ver2;'):
            ele = row[num]  
            lst.append(ele)
            
    
        self.sorted_lst = lst
        self.sorted_lst.sort()
        #print(self.sorted_lst)

        con.close()
        return self.sorted_lst
 
    def sorted_descending(self, num):

        con = sqlite3.connect('admin3.db')
        cur = con.cursor()
        lst1 =[]
      
        for row in cur.execute('SELECT * FROM pet_info_ver2;'):
            ele = row[num]  
            lst1.append(ele)
        
        self.des_sorted_lst = lst1
        self.des_sorted_lst.sort(reverse=True)
        
        con.close()
        return self.des_sorted_lst
        
    def gathered(self, num):
        conn = sqlite3.connect('admin3.db') 
        cursor = conn.cursor() 

        statement = '''SELECT * FROM pet_info_ver2'''
    
        cursor.execute(statement) 
    
        output = cursor.fetchall() 
        
        for row in output: 
            row
        
        conn.commit() 
        conn.close()
        
        return output[num]
    
    
    def gathered_user(self):
        conn = sqlite3.connect('admin3.db') 
        cursor = conn.cursor() 

        statement = '''SELECT * FROM user_adopt2'''
    
        cursor.execute(statement) 
    
        output = cursor.fetchall() 
        
        for row in output: 
            row
        
        conn.commit() 
        conn.close()
        
        return output
    #try0---------------------
    def ascending_index(self, num):
        con = sqlite3.connect('admin3.db')
        cur = con.cursor()
        lst1 =[]
        lst2 =[]
      
        for row in cur.execute('SELECT * FROM pet_info_ver2;'):
            ele = row[num]  
            lst1.append(ele)
            #-----------------------------
            element = row[num]  
            lst2.append(element)
        
        self.sorted_list = lst1   
        self.asc_sorted_lst = lst2
        self.asc_sorted_lst.sort()
        
        lst_3 = []
        for i, element in enumerate(self.asc_sorted_lst):
            if element in self.sorted_list:
                index_in_list2 = self.sorted_list.index(element)
                lst_3.append(index_in_list2)
                
        self.ascending = lst_3
        con.close()
        return self.ascending
    
    def descending_index(self, num):
        
        con = sqlite3.connect('admin3.db')
        cur = con.cursor()
        lst1 =[]
        lst2 =[]
      
        for row in cur.execute('SELECT * FROM pet_info_ver2;'):
            ele = row[num]  
            lst1.append(ele)
            #-----------------------------
            element = row[num]  
            lst2.append(element)
        
        self.sorted_list = lst1
        self.des_sorted_lst = lst2
        self.des_sorted_lst.sort(reverse=True)
        
        lst_3 = []
        for i, element in enumerate(self.des_sorted_lst):
            if element in self.sorted_list:
                index_in_list2 = self.sorted_list.index(element)
                lst_3.append(index_in_list2)
                
        self.descending = lst_3
        con.close()
        return self.descending
    #try------------------

#same =  len(name)
#print(same)