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
title_label = tkinter.Label(text="Join the Pawsome Community and \nConnect with Dog Lovers!", bg="#e5cd6c", font=("Times", "24", "bold italic"))
title_label.place(x = 700, y= 40)

design = tkinter.Label(background="#f9f3b9", height="35", width="115")
design.place(x=525, y=150)
#---------------------------LABEL

dog_name_label = info.dog_label(540, 250, "DOG NAME", "#f9f3b9", "Times", 14, "bold italic") 
dog_weight_label = info.dog_label(540, 330, "DOG WEIGHT", "#f9f3b9", "Times", 14, "bold italic") 
dog_birth_label = info.dog_label(540, 410, "DOG BIRTH DATE", "#f9f3b9", "Times", 14, "bold italic") 
any_msg_label = info.dog_label(540, 490, "ANY OTHER MESSAGE", "#f9f3b9", "Times", 14, "bold italic") 

dog_breed_label= info.dog_label(960, 250, "DOG BREED", "#f9f3b9", "Times", 14, "bold italic") 
dog_gender_label = info.dog_label(960, 330, "DOG GENDER", "#f9f3b9", "Times", 14, "bold italic") 
dog_id  =  info.dog_label(960, 410, "DOG ID", "#f9f3b9", "Times", 14, "bold italic") 


#---------------------ENTRY

dog_name_entry =info.dog_entry(540, 280, 30, "white")
dog_weight_entry =info.dog_entry(540, 360, 30, "white")
dog_birth_date = info.dog_date(540, 440, 42)
any_msg_txt =info.dog_entry(540, 520, 80,"white")


price_entry = info.dog_entry(990, 205, 30, "white")
dog_breed_entry =info.dog_entry(960, 280, 30, "white")
dog_gender_combobox =info.dog_combobox(960, 360,["Male", "Female"], 28)     
dog_id_entry =info.dog_entry(960, 440, 30, "white")

#-----------------------PICTURE
path_entry = info.new_label_entry("Picture path", 540, 175, 50)


#--------------FUNCTION FOR BUTTON
def search_img():
    filepath1 = path_entry.get()
    filepath1 = filepath1.replace('"', "")
    info.new_image(filepath1, 0, 0, 500, 1000)
    
    
def print_l():
    dog_id = dog_id_entry.get()
    dog_name = dog_name_entry.get()
    dog_weight = dog_weight_entry.get()
    dog_b_day = dog_birth_date.get()
    dog_breed = dog_breed_entry.get()
    dog_gender = dog_gender_combobox.get()
    pic_link = path_entry.get()
    msg = any_msg_txt.get()
    price  =  price_entry.get()
    
    val = [dog_id, dog_name, dog_weight, dog_b_day, dog_breed, dog_gender, pic_link, msg]
     
    
def add():
    dog_id = dog_id_entry.get()
    dog_name = dog_name_entry.get()
    dog_weight = dog_weight_entry.get()
    dog_b_day = dog_birth_date.get()
    dog_breed = dog_breed_entry.get()
    dog_gender = dog_gender_combobox.get()
    pic_link = path_entry.get()
    msg = any_msg_txt.get()
    price  =  price_entry.get()
    
   
    
    conn = sqlite3.connect('admin2.db')
    
    table_create = '''CREATE TABLE IF NOT EXISTS dog_info2
    (dog_id INTEGER, dog_name TEXT, dog_weight INTEGER, dog_b_day INTEGER,
    dog_breed TEXT, dog_gender TEXT, pic_link TEXT, msg TEXT, price INTEGER)
    '''
    conn.execute(table_create)
    
    Data_insert = ''' INSERT INTO dog_info2
    (dog_id, dog_name, dog_weight, dog_b_day, dog_breed, dog_gender, pic_link, msg, price)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    Data_insert_tuple = (dog_id, dog_name, dog_weight, dog_b_day, dog_breed, dog_gender, pic_link, msg, price)
    
    conn.execute(Data_insert, Data_insert_tuple)
    conn.commit()
    conn.close()
    
def update():
    conn = sqlite3.connect('admin2.db')
    cur = conn.cursor()
    
    dog_id = dog_id_entry.get()
    dog_name = dog_name_entry.get()
    dog_weight = dog_weight_entry.get()
    dog_b_day = dog_birth_date.get()
    dog_breed = dog_breed_entry.get()
    dog_gender = dog_gender_combobox.get()
    pic_link = path_entry.get()
    msg = any_msg_txt.get()
    price  =  price_entry.get()
    
    update_val = '''UPDATE dog_info2 SET
    dog_name = ?, dog_weight = ?, dog_b_day = ?, 
    dog_breed = ?, dog_gender = ?, pic_link = ?, msg = ?, price = ?
    WHERE dog_id = ?
    '''
    update_data = (dog_name, dog_weight, dog_b_day, dog_breed, dog_gender, pic_link, msg, price, dog_id)
     
    cur.execute(update_val, update_data)
    
    conn.commit()
    conn.close()
    
def search():
    dog_id = dog_id_entry.get()
    conn = sqlite3.connect('admin2.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dog_info2 WHERE dog_id=?", (dog_id))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        
        dog_name_entry.delete(0, tkinter.END)
        dog_name_entry.insert(0, row[1])
        
        dog_weight_entry.delete(0, tkinter.END)
        dog_weight_entry.insert(0, row[2])
        
        dog_birth_date.delete(0, tkinter.END)
        dog_birth_date.insert(0, row[3])
        
        dog_breed_entry.delete(0, tkinter.END)
        dog_breed_entry.insert(0, row[4])
        
        dog_gender_combobox.delete(0, tkinter.END)
        dog_gender_combobox.insert(0, row[5])
        
        path_entry.delete(0, tkinter.END)
        path_entry.insert(0, row[6])
        
        any_msg_txt.delete(0, tkinter.END)
        any_msg_txt.insert( 0, row[7])
        
        
        
        search_img()
    
#BUTTON#
#https://www.figma.com/design/FuKDQSmponloFqIwjtcZ38/Pawsome---Dog-Community-(Community)?node-id=1-26&node-type=frame&t=U0Gol1cinUAVGnwJ-0
#https://www.figma.com/design/GK21UqtppgKmqSZiQrjhb2/Dash-UI---Admin-Dashboard-Template-(Community)?node-id=1602-6181&node-type=frame&t=Bp3AzvdGTDcf4L6O-0
search_img_button = info.button_a(870, 205, "SEARCH IMAGE","gray", search_img)
add_button = info.button_a(1190, 600, "Add Record","gray", add)
update_button = info.button_a(1120, 600, "Update","gray", update)
search_button = info.button_a(1045, 600, "Search","gray", search)

#https://www.figma.com/design/5hqLVgCEovapmWWWQy7RqD/Simple-admin-panel-UI-(Community)?node-id=239-2279&node-type=canvas&t=GdmE8iFL7ueQjrgj-0
back_button = info.button_a(540, 600, "Admin Page","gray", search_img)
print_but = info.button_a(700, 600, "Admin Page","gray", print_l)


 

root.mainloop()

#date of bitrh
#anny other message
#button