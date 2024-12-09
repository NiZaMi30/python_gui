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
adoption_fee_label = info.dog_label(960, 170, "FEE", "#f9f3b9", "Times", 14, "bold italic")


pet_name_label = info.dog_label(540, 250, "PET NAME", "#f9f3b9", "Times", 14, "bold italic") 
pet_weight_label = info.dog_label(540, 330, "PET WEIGHT", "#f9f3b9", "Times", 14, "bold italic") 
pet_birth_label = info.dog_label(540, 410, "PET BIRTH DATE", "#f9f3b9", "Times", 14, "bold italic") 
any_msg_label = info.dog_label(540, 490, "ANY OTHER MESSAGE", "#f9f3b9", "Times", 14, "bold italic") 

pet_breed_label= info.dog_label(960, 250, "PET BREED", "#f9f3b9", "Times", 14, "bold italic") 
pet_gender_label = info.dog_label(960, 330, "PET GENDER", "#f9f3b9", "Times", 14, "bold italic") 
pet_id  =  info.dog_label(960, 410, "PET ID", "#f9f3b9", "Times", 14, "bold italic") 
species_label = info.dog_label(960, 490, "SPECIES", "#f9f3b9", "Times", 14, "bold italic")


#---------------------ENTRY

adoption_fee_entry = info.dog_entry(960, 200, 30, "white")

pet_name_entry =info.dog_entry(540, 280, 30, "white")
pet_weight_entry =info.dog_entry(540, 360, 30, "white")
pet_birth_date = info.dog_date(540, 440, 42)
any_msg_txt =info.dog_entry(540, 520, 45,"white")

pet_breed_entry =info.dog_entry(960, 280, 30, "white")
pet_gender_combobox =info.dog_combobox(960, 360,["Male", "Female"], 28)     
pet_id_entry =info.dog_entry(960, 440, 30, "white")
species_entry =info.dog_entry(960, 520, 30, "white")


#-----------------------PICTURE
path_entry = info.new_label_entry("Picture path", 540, 175, 50)


#--------------FUNCTION FOR BUTTON
def search_img():
    filepath1 = path_entry.get()
    filepath1 = filepath1.replace('"', "")
    info.new_image(filepath1, 0, 0, 500, 1000)
    
def add():
    pet_id = pet_id_entry.get()
    pet_name = pet_name_entry.get()
    pet_weight = pet_weight_entry.get()
    pet_b_day = pet_birth_date.get()
    pet_breed = pet_breed_entry.get()
    pet_gender = pet_gender_combobox.get()
    pic_link = path_entry.get()
    msg = any_msg_txt.get()
    species = species_entry.get()
    fee = adoption_fee_entry.get()
   
    
    conn = sqlite3.connect('admin3.db')
    
    table_create = '''CREATE TABLE IF NOT EXISTS pet_info_ver2
    (pet_id INTEGER, pet_name TEXT, pet_weight INTEGER, pet_b_day INTEGER,
    pet_breed TEXT, pet_gender TEXT, pic_link TEXT, msg TEXT, species TEXT, fee INTEGER)
    '''
    conn.execute(table_create)
    
    Data_insert = ''' INSERT INTO pet_info_ver2
    (pet_id, pet_name, pet_weight, pet_b_day, pet_breed, pet_gender, pic_link, msg, species, fee)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    Data_insert_tuple = (pet_id, pet_name, pet_weight, pet_b_day, pet_breed, pet_gender, pic_link, msg, species, fee)
    
    conn.execute(Data_insert, Data_insert_tuple)
    conn.commit()
    conn.close()
    
def update():
    conn = sqlite3.connect('admin3.db')
    cur = conn.cursor()
    
    pet_id = pet_id_entry.get()
    pet_name = pet_name_entry.get()
    pet_weight = pet_weight_entry.get()
    pet_b_day = pet_birth_date.get()
    pet_breed = pet_breed_entry.get()
    pet_gender = pet_gender_combobox.get()
    pic_link = path_entry.get()
    msg = any_msg_txt.get()
    species = species_entry.get()
    fee = adoption_fee_entry.get()
    
    update_val = '''UPDATE pet_info_ver2 SET
    pet_name = ?, pet_weight = ?, pet_b_day = ?, 
    pet_breed = ?, pet_gender = ?, pic_link = ?, msg = ?, species = ?, fee = ?
    WHERE pet_id = ?
    '''
    update_data = (pet_name, pet_weight, pet_b_day, pet_breed, pet_gender, pic_link, msg, species, fee, pet_id)
     
    cur.execute(update_val, update_data)
    
    conn.commit()
    conn.close()
    
def search():
    pet_id = pet_id_entry.get()
    conn = sqlite3.connect('admin3.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pet_info_ver2 WHERE pet_id=?", (pet_id))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        
        pet_name_entry.delete(0, tkinter.END)
        pet_name_entry.insert(0, row[1])
        
        pet_weight_entry.delete(0, tkinter.END)
        pet_weight_entry.insert(0, row[2])
        
        pet_birth_date.delete(0, tkinter.END)
        pet_birth_date.insert(0, row[3])
        
        pet_breed_entry.delete(0, tkinter.END)
        pet_breed_entry.insert(0, row[4])
        
        pet_gender_combobox.delete(0, tkinter.END)
        pet_gender_combobox.insert(0, row[5])
        
        path_entry.delete(0, tkinter.END)
        path_entry.insert(0, row[6])
        
        any_msg_txt.delete(0, tkinter.END)
        any_msg_txt.insert( 0, row[7])
        
        species_entry.delete(0, tkinter.END)
        species_entry.insert(0, row[8])
        
        adoption_fee_entry.delete(0, tkinter.END)
        adoption_fee_entry.insert(0, row[9])
    
#BUTTON#
#https://www.figma.com/design/FuKDQSmponloFqIwjtcZ38/Pawsome---Dog-Community-(Community)?node-id=1-26&node-type=frame&t=U0Gol1cinUAVGnwJ-0
#https://www.figma.com/design/GK21UqtppgKmqSZiQrjhb2/Dash-UI---Admin-Dashboard-Template-(Community)?node-id=1602-6181&node-type=frame&t=Bp3AzvdGTDcf4L6O-0

#button img
img_search_button = info.button_pic(80, 20, "image\\search_button.png")
#----------------------------------
search_img_button = info.button_b(660, 170, "SEARCH IMAGE","gray",5, 10,search_img, img_search_button)
add_button = info.button_a(1190, 600, "Add Record","gray", add)
update_button = info.button_a(1120, 600, "Update","gray", update)
search_button = info.button_a(1045, 600, "Search","gray", search)

#https://www.figma.com/design/5hqLVgCEovapmWWWQy7RqD/Simple-admin-panel-UI-(Community)?node-id=239-2279&node-type=canvas&t=GdmE8iFL7ueQjrgj-0
back_button = info.button_a(540, 600, "Admin Page","gray", search_img)


#apointment GUI

#https://www.behance.net/gallery/111756097/Vets-Admin-Dashboard
#https://www.adopets.com/
 

root.mainloop()

#date of bitrh
#anny other message
#button