import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from  datetime import date
# which are needed 
import  sqlite3
import admin_dog_input_class


root = tkinter.Tk()
root.title("ADMIN")
root.config(bg="#e5cd6c")
root.geometry("1400x700")

info = admin_dog_input_class.admin()

#picture

e_photo = Image.open("adoption.png")
resized = e_photo.resize((500, 1000))
new_photo = ImageTk.PhotoImage(resized)
my_label = tkinter.Label(image=new_photo, background="#DEB992")
my_label.place(x=0, y=0)

#---------------------------------------------------------------------
#design
title_label = tkinter.Label(text="Join the Pawsome Community and \nConnect with PET Lovers!", bg="#e5cd6c", font=("Times", "24", "bold italic"))
title_label.place(x = 700, y= 40)

design = tkinter.Label(background="#f9f3b9", height="35", width="115")
design.place(x=525, y=150)
#---------------------------LABEL


namelabel = info.dog_label(540, 175, "NAME", "#f9f3b9", "Times", 14, "bold italic") 
userlabel = info.dog_label(540, 250, "USER ID", "#f9f3b9", "Times", 14, "bold italic") 
Nationalitylabel = info.dog_label(540, 330, "NATIONALITY", "#f9f3b9", "Times", 14, "bold italic") 
cellphone_numlabel = info.dog_label(540, 410, "CELLPHONE NUMBER", "#f9f3b9", "Times", 14, "bold italic") 
Addresslabel = info.dog_label(540, 490, "ADDRESS", "#f9f3b9", "Times", 14, "bold italic") 

emaillabel = info.dog_label(960, 175, "EMAIL", "#f9f3b9", "Times", 14, "bold italic")
occupationlabel= info.dog_label(960, 250, "OCCUPATION", "#f9f3b9", "Times", 14, "bold italic") 
dog_id_label = info.dog_label(960, 330, "PET ID", "#f9f3b9", "Times", 14, "bold italic") 
dog_name_label  =  info.dog_label(960, 410, "PET NAME", "#f9f3b9", "Times", 14, "bold italic") 
dog_price_label = info.dog_label(960, 490, "PET PRICE", "#f9f3b9", "Times", 14, "bold italic")


#---------------------ENTRY


f_name_entry = info.dog_entry(540, 200, 30, "white")
user_id_entry =info.dog_entry(540, 280, 30, "white")
nationality_entry =info.dog_entry(540, 360, 30, "white")
cellphone_num_entry = info.dog_entry(540, 440, 30, "white")
address_entry =info.dog_entry(540, 520, 45,"white")

email_entry = info.dog_entry(960, 200, 30, "white")
occupation_entry =info.dog_entry(960, 280, 30, "white")
dog_id_entry =info.dog_entry(960, 360, 30, "white")    
dog_name_entry =info.dog_entry(960, 440, 30, "white")
dog_price_entry =info.dog_entry(960, 520, 30, "white")


#-----------------------PICTURE




#--------------FUNCTION FOR BUTTON

def add():
    f_name = f_name_entry.get()
    user_id = user_id_entry.get()
    nationality = nationality_entry.get()
    cellphone_num = cellphone_num_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    occupation = occupation_entry.get()
    dog_id = dog_id_entry.get()
    dog_name = dog_name_entry.get()
    dog_price = dog_price_entry.get()
   
    
    conn = sqlite3.connect('admin3.db')

    Data_insert = ''' INSERT INTO user_adopt2
    (f_name, user_id, nationality, cellphone_num, address, email, occupation, dog_id, dog_name, dog_price)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
                        
    Data_insert_tuple  =  (f_name, user_id, nationality, cellphone_num, address, email, occupation, dog_id, dog_name, dog_price)
    conn.execute(Data_insert, Data_insert_tuple)
    conn.commit()
    conn.close()
    
def update():
    conn = sqlite3.connect('admin3.db')
    cur = conn.cursor()
    
    f_name = f_name_entry.get()
    user_id = user_id_entry.get()
    nationality = nationality_entry.get()
    cellphone_num = cellphone_num_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    occupation = occupation_entry.get()
    dog_id = dog_id_entry.get()
    dog_name = dog_name_entry.get()
    dog_price = dog_price_entry.get()
    
    update_val = '''UPDATE user_adopt2 SET
    f_name = ?, nationality = ?, cellphone_num = ?, 
    address = ?, email = ?, occupation = ?, dog_id = ?, dog_name = ?, dog_price = ?
    WHERE user_id = ?
    '''
    update_data = (f_name, nationality, cellphone_num, address, email, occupation, dog_id, dog_name, dog_price, user_id)
     
    cur.execute(update_val, update_data)
    
    conn.commit()
    conn.close()
    
def search():
    user_id = user_id_entry.get()
    conn = sqlite3.connect('admin3.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_adopt2 WHERE user_id=?", (user_id))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        
        f_name_entry.delete(0, tkinter.END)
        f_name_entry.insert(0, row[0])
        
        nationality_entry.delete(0, tkinter.END)
        nationality_entry.insert(0, row[2])
        
        cellphone_num_entry.delete(0, tkinter.END)
        cellphone_num_entry.insert(0, row[3])
        
        address_entry.delete(0, tkinter.END)
        address_entry.insert(0, row[4])
        
        email_entry.delete(0, tkinter.END)
        email_entry.insert(0, row[5])
        
        occupation_entry.delete(0, tkinter.END)
        occupation_entry.insert(0, row[6])
        
        dog_id_entry.delete(0, tkinter.END)
        dog_id_entry.insert( 0, row[7])
        
        dog_name_entry.delete(0, tkinter.END)
        dog_name_entry.insert(0, row[8])
        
        dog_price_entry.delete(0, tkinter.END)
        dog_price_entry.insert(0, row[9])
    
#BUTTON#
#https://www.figma.com/design/FuKDQSmponloFqIwjtcZ38/Pawsome---Dog-Community-(Community)?node-id=1-26&node-type=frame&t=U0Gol1cinUAVGnwJ-0
#https://www.figma.com/design/GK21UqtppgKmqSZiQrjhb2/Dash-UI---Admin-Dashboard-Template-(Community)?node-id=1602-6181&node-type=frame&t=Bp3AzvdGTDcf4L6O-0

#button img

add_button = info.button_a(1190, 600, "Add Record","gray", add)
update_button = info.button_a(1120, 600, "Update","gray", update)
search_button = info.button_a(1045, 600, "Search","gray", search)

#https://www.figma.com/design/5hqLVgCEovapmWWWQy7RqD/Simple-admin-panel-UI-(Community)?node-id=239-2279&node-type=canvas&t=GdmE8iFL7ueQjrgj-0



#apointment GUI

#https://www.behance.net/gallery/111756097/Vets-Admin-Dashboard
#https://www.adopets.com/
 

root.mainloop()

#date of bitrh
#anny other message
#button