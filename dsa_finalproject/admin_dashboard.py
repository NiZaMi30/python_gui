import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from  datetime import date
# which are needed 
import  sqlite3
import admin_dog_input_class
import dsa_pet

import subprocess


root = tkinter.Tk()
root.title("ADMIN_dashboard")
root.config(bg="#26415E")
root.geometry("1400x700")

info = admin_dog_input_class.admin()
dsa = dsa_pet.dataBase()

#-----------------------------------------
image_admin = info.button_pic(1200, 700, "image\\admin_page.png")
admin_des = tkinter.Label(image=image_admin)
admin_des.place(x=200,y= 0)
#-----------------------------------------
design = tkinter.Label(background="#C48CB3", height="50", width="30")
design.place(x=0, y=0)

design1 = tkinter.Label(background="#E5C9D7", height="5", width="30")
design1.place(x=0, y=0)
#--------------------
admin_label = info.dog_label(48, 20, "ADMIN", "#E5C9D7", "Times", 27, "bold italic")

#--------------button attributes


#---------------------------------------
count =  dsa.sorted_ascending(0)
count_val = len(count)

#----------------------------------------------
def des_attribute():
    descending = dsa.ascending_index(1)
    x = 230
    for i in descending:
        sample_1 = dsa.gathered(i)
        data_label1 = info.dog_label(280, x, sample_1, "#E5C9D7", "Helvetica", 10, "bold italic")
        x = x + 40

def attribute():
    animals_label = info.dog_label(280, 35, "ANIMALS", "#83A6CE", "Helvetica", 25, "bold italic")
    
    Id_label = info.dog_label(270, 175, "ID", "#C48CB3","Times", 13, "bold italic")  
    Name_label = info.dog_label(330, 175, "NAME", "#C48CB3","Times", 13, "bold italic")
    weight_label = info.dog_label(400, 175, "WEIGHT", "#C48CB3","Times", 13, "bold italic")
    birth_date_label = info.dog_label(500, 165, "BIRTH\nDATE", "#C48CB3","Times", 13, "bold italic")
    breed_label = info.dog_label(600, 175, "BREED", "#C48CB3","Times", 13, "bold italic")
    gender_label = info.dog_label(740, 175, "GENDER", "#C48CB3","Times", 13, "bold italic")
    msg_label = info.dog_label(870, 175, "MESSAGE", "#C48CB3","Times", 13, "bold italic")
    species_label = info.dog_label(1030, 175, "SPECIES", "#C48CB3","Times", 13, "bold italic")
    price_label = info.dog_label(1140, 175, "PRICE", "#C48CB3","Times", 13, "bold italic") 
    
def des_forpet():
    design_ = tkinter.Label(background="#26415E", height="50", width="200")
    design_.place(x=215, y=0)
    
    high_des = tkinter.Label(background="#83A6CE", height="5", width="150")
    high_des.place(x=260, y=20)
    
    low_des = tkinter.Label(background="#C48CB3", height="30", width="150")
    low_des.place(x=260, y=150) 
    
    low_des = tkinter.Label(background="#E5C9D7", height="30", width="150")
    low_des.place(x=260, y=220)

  
    
    
#--------------------------button image
img_addpet_button = info.button_pic(100, 40, "image\\Button_Add_pet.png")
img_id_button = info.button_pic(60, 30, "image\\ID_button.png")
img2_id_button = info.button_pic(60, 30, "image\\ID_2_button.png")

img_name =  info.button_pic(60, 30, "image\\name_1_button.png")
img_name_2  = info.button_pic(60, 30, "image\\name_2_button.png")
image_user  = info.button_pic(100, 40, "image\\manage_user_button.png")
def pet():
    des_forpet()
    attribute()
    id_ascending()
    #--------------------- label
    button_label = info.dog_label(17, 220, "BUTTON FOR\nPET", "#C48CB3", "Times", 22, "bold italic")
    ascending_label = info.dog_label(5, 320, "ASCENDING", "#C48CB3", "Times", 10, "bold italic")
    descending_label = info.dog_label(110, 320, "DESCENDING", "#C48CB3", "Times", 10, "bold italic")
    
    #button 
    add_pet_button =  info.button_b(1170, 35, "Add Pet","gray",5, 10, add_pet, img_addpet_button)
    #----------------------------------
    id_button = info.button_b(15, 350, "SIGN OUT","gray",5, 10, id_ascending, img_id_button)
    id2_button = info.button_b(115, 350, "SIGN OUT","gray",5, 10, id_descending, img2_id_button)

    name_button = info.button_b(15, 390, "SIGN OUT","gray",5, 10, name_ascending, img_name)
    name_2_button = info.button_b(115, 390, "SIGN OUT","gray",5, 10, name_descending, img_name_2)
    
    #img_addpet_button = info.button_pic(100, 40, "image\Button_Add_pet.png")
    #add_pet_button =  info.button_b(1170, 35, "Add Pet","gray",5, 10, add_pet, img_addpet_button)
    
    
def des_for_user():
    design_ = tkinter.Label(background="#26415E", height="50", width="200")
    design_.place(x=215, y=0)
    
    high_des = tkinter.Label(background="#83A6CE", height="5", width="150")
    high_des.place(x=260, y=20)
    
    low_des = tkinter.Label(background="#C48CB3", height="30", width="150")
    low_des.place(x=260, y=150) 
    
    low_des = tkinter.Label(background="#E5C9D7", height="30", width="150")
    low_des.place(x=260, y=220) 
    
    low_des = tkinter.Label(background="#C48CB3", height="15", width="28")
    low_des.place(x=0, y=220) 
    
def attribute_user():
    user_label = info.dog_label(280, 35, "USER", "#83A6CE", "Helvetica", 25, "bold italic")
    
    name_label = info.dog_label(270, 175, "FULL NAME", "#C48CB3","Times", 13, "bold italic")  
    user_ID_label = info.dog_label(330 + 80, 175, "USER ID", "#C48CB3","Times", 13, "bold italic")
  
    cellphone_number_label = info.dog_label(500 + 10, 165, "CELLPHONE\nNUMBER", "#C48CB3","Times", 13, "bold italic")
    email_label = info.dog_label(640 + 90, 175, "EMAIL", "#C48CB3","Times", 13, "bold italic")
    ocupation_label = info.dog_label(770 + 90, 175, "OCCUPATION", "#C48CB3","Times", 13, "bold italic")
    dog_id_label = info.dog_label(930 + 90, 165, "PET\nID", "#C48CB3","Times", 13, "bold italic")
    dog_name_label = info.dog_label(1040 + 90, 165, "PET\nName", "#C48CB3","Times", 13, "bold italic")
    dog_price_label = info.dog_label(1140 + 90, 175, "PRICE", "#C48CB3","Times", 13, "bold italic")
def user():
    
    des_for_user()
    attribute_user()
    user_ascending()
    manage_user_button =  info.button_b(1170, 35, "Add Pet","gray",5, 10, manage_user, image_user)
    
   
def manage_user():
    subprocess.run(["python", "admin_userinput.py"])
 
   
def signout():
    print("HAHHA")
#-------acess newfile    
def add_pet():
    subprocess.run(["python", "admin_petinput.py"])
#---------------------------------------------------------------------------------------------------------------------------------------------------
def user_ascending():
    low_des = tkinter.Label(background="#E5C9D7", height="30", width="150")
    low_des.place(x=260, y=220)

    # Retrieve data sorted by ascending index
    id_ascending_data = dsa.gathered_user()
    x_start = 280
    y_start = 220
    y_increment = 40
    x = x_start
    y = y_start
  
    lst = []
    
    for i in id_ascending_data:
        for j, value in enumerate(i):

            # Set label properties dynamically based on the data type (j)
            if j == 0:  # user name
                x_increment = 160
            elif j == 1:  # id
                x_increment = 80
            elif j == 2:  # nationality
                x_increment = 90
                continue
            elif j == 3:  # contact number
                x_increment = 120
            elif j == 4:  # location
                x_increment = 160
                continue
            elif j == 5:  # email
                x_increment = 240
                
            elif j == 6:  # occupation
                x_increment = 160
            
            elif j == 7:  # dog id
                x_increment = 100
            elif j == 8:  # dog name
                x_increment = 100
            else:  # price
                x_increment = 20

            # Create and place the label for the current data
            info.dog_label(x, y, value, "#E5C9D7", "Helvetica", 10, "bold italic")

            # Update x-coordinate for the next label
            x += x_increment

        # Move to the next row for the next record
        y += y_increment
        x = x_start 
        
    # Initial position for placing labels
    
#-------------------------------------------------------------------------------------------------------------------
def id_ascending():
    low_des = tkinter.Label(background="#E5C9D7", height="30", width="150")
    low_des.place(x=260, y=220)

    # Retrieve data sorted by ascending index
    id_ascending_data = dsa.ascending_index(0)

    # Initial position for placing labels
    x_start = 280
    y_start = 220
    y_increment = 40
    x = x_start
    y = y_start

    # Iterate through sorted data
    for record_id in id_ascending_data:
        record = dsa.gathered(record_id)  # Gather data for the current ID

        # Iterate through each piece of data in the record
        for j, value in enumerate(record):
             # Debugging log for each value in the record

            # Set label properties dynamically based on the data type (j)
            if j == 0:  # ID and name
                x_increment = 50
            elif j == 1:  # Weight
                x_increment = 100
            elif j == 2:  # Weight
                x_increment = 75
            elif j == 3:  # Date
                x_increment = 90
            elif j == 4:  # Breed
                x_increment = 160
            elif j == 5:  # Gender
                x_increment = 120
            elif j == 6:  # Image (skipping label placement)
                x_increment = 20
                continue
            elif j == 7:  # Messages
                x_increment = 170
            else:  # Other data
                x_increment = 100

            # Create and place the label for the current data
            info.dog_label(x, y, value, "#E5C9D7", "Helvetica", 10, "bold italic")

            # Update x-coordinate for the next label
            x += x_increment

        # Move to the next row for the next record
        y += y_increment
        x = x_start  
         
def id_descending():
    low_des = tkinter.Label(background="#E5C9D7", height="30", width="150")
    low_des.place(x=260, y=220)
    id_ascending = dsa.descending_index(0)
    x = 280
    y = 220
    lst = []
    for i in id_ascending:
        sample_1 = dsa.gathered(i)
        lst.append(sample_1)
        
        for j in range(0, 10):
           
            if(1>j):#id and name
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 50 
                
            elif(2 == j):#weight
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 75
            elif(3 == j):#date
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 90  
            elif(4 == j):#breed
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 160 
            elif(5 == j):#gender
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 100 
            elif(6 == j):#image
                x = x + 20 
                
            elif(7 == j):#messages
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 170 
            else:
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic") 
                x = x + 100
        y = y + 40  
        x = 280  
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------       
def name_ascending():
    low_des = tkinter.Label(background="#E5C9D7", height="30", width="150")
    low_des.place(x=260, y=220)
    id_ascending = dsa.ascending_index(1)
    x = 280
    y = 220
    lst = []
    for i in id_ascending:
        sample_1 = dsa.gathered(i)
        lst.append(sample_1)
        for j in range(0, 10):
            if(1>j):#id and name
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 50 
                
            elif(2 == j):#weight
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 75
            elif(3 == j):#date
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 90  
            elif(4 == j):#breed
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 160 
            elif(5 == j):#gender
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 100 
            elif(6 == j):#image
                x = x + 20 
                
            elif(7 == j):#messages
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 170 
            else:
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic") 
                x = x + 100
        y = y + 40  
        x = 280  
         
def name_descending():
    low_des = tkinter.Label(background="#E5C9D7", height="30", width="150")
    low_des.place(x=260, y=220)
    id_ascending = dsa.descending_index(1)
    x = 280
    y = 220
    lst = []
    for i in id_ascending:
        sample_1 = dsa.gathered(i)
        lst.append(sample_1)
        for j in range(0, 10):
            if(1>j):#id and name
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 50 
                
            elif(2 == j):#weight
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 75
            elif(3 == j):#date
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 90  
            elif(4 == j):#breed
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 160 
            elif(5 == j):#gender
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 100 
            elif(6 == j):#image
                x = x + 20 
                
            elif(7 == j):#messages
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic")
                x = x + 170 
            else:
                data_label1 = info.dog_label(x, y, sample_1[j], "#E5C9D7", "Helvetica", 10, "bold italic") 
                x = x + 100
        y = y + 40  
        x = 280
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------      
#pet()
#----------------color palete
#0D1E4C
#C48CB3
#E5C9D7
#83A6CE
#26415E
#0B1B32

#-------------------------Button image
image_user_button = info.button_pic(100, 40, "image\\user_button.png")
img_pet_button = info.button_pic(100, 40, "image\\pet_button.png")
img_signout_button = info.button_pic(100, 40, "image\\sign_out.png")

#---------------------------

#------------------------------

pet_button = info.button_b(55, 100, "GENERAL","gray",5, 10,pet, img_pet_button)
users_button = info.button_b(55, 160, "USERS","gray", 5, 10, user, image_user_button)
#signout_button = info.button_b(50, 600, "SIGN OUT","gray",5, 10, signout, img_signout_button)

#---------------------
root.mainloop()


#https://www.figma.com/design/5hqLVgCEovapmWWWQy7RqD/Simple-admin-panel-UI-(Community)?node-id=239-2279&node-type=canvas&t=oc2uteW55Sq7tOHn-0

