import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
import sqlite3
import admin_dog_input_class
import dsa_pet

# Color Palette
# 0D1E4C, C48CB3, E5C9D7, 83A6CE, 26415E, 0B1B32

root = tkinter.Tk()
root.title("User Dashboard")
root.config(bg="#0D1E4C")
root.geometry("1400x700")

# Initialize required instances
info = admin_dog_input_class.admin()
dsa = dsa_pet.dataBase()
# Load images
image_user = info.button_pic(770, 580, "image\\user_frontpage.png")
img_about_us_button = info.button_pic(100, 40, "image_ver2\\about_us.png")
img_gallery_button = info.button_pic(100, 40, "image_ver2\\pet_gallery.png")
img_wishlist_button = info.button_pic(100, 40, "image_ver2\\wishlist.png")
img_toKnow_button = info.button_pic(100, 40, "image_ver2\\get_to_know.png")
img_signout_button = info.button_pic(100, 40, "image\\sign_out.png")

# About function to show about information
def about():
    about_us()

# Gallery function to display the pet gallery
def gallery():
    design = tkinter.Label(background="#0D1E4C", height="40", width="200")
    design.place(x=0, y=110)
    
    id_ascending_access_image()

# Function to display the pet images in ascending order
def id_ascending_access_image(): 
    high_des = tkinter.Label(background="#E5C9D7", height=5, width=250)
    high_des.place(x=0, y=110)

    low_des = tkinter.Label(background="#83A6CE", height=50, width=200)
    low_des.place(x=0, y=190)

    # Get ascending pet IDs from the database
    id_ascending = dsa.ascending_index(0)
    x = 50
    y = 230
    image_references = []  # Store references to images to avoid garbage collection

    for i in id_ascending:
        sample_1 = dsa.gathered(i)
        filepath1 = sample_1[6].replace('"', "").strip()  # Clean up the file path

        try:
            # Load and resize the image using Pillow
            img = Image.open(filepath1)
            img = img.resize((130, 130))  # Resize the image
            tk_img = ImageTk.PhotoImage(img)  # Convert to PhotoImage
            
            # Store the image reference to avoid garbage collection
            image_references.append(tk_img)

            # Button callback for each pet image
            def button_callback(i=i):  # Capture the current index `i`
                
                pet_window = tkinter.Toplevel(root)  
                pet_window.title(f"Pet Details - {i+1}")
                pet_window.config(bg="#0D1E4C")
                pet_window.geometry("550x450")
                
                
                # Design for the pet details window
                design = tkinter.Label(pet_window, background="#0D1E4C", height=40, width=200)
                design.place(x=0, y=110)
                
                # Add specific widgets here for pet details
                pet_id_label = tkinter.Label(pet_window, text=f"Pet {i + 1}", font=("Helvetica", 20), bg="#0D1E4C", fg="#E5C9D7")
                pet_id_label.place(x=175, y=0)
                
                def button1():
                    design = tkinter.Label(pet_window, background="#e5cd6c", height=40, width=200)
                    design.place(x=0, y=0)

                    Value = dsa.gathered(i)

                    # Adopt pet application form
                    namelabel = info.label_classes(pet_window, 5, 40, "FULL NAME", "#e5cd6c", "Times", 14, "bold italic")
                    user_id = info.label_classes(pet_window, 425, 40, "USER ID", "#e5cd6c", "Times", 14, "bold italic")
                    nationalitylabel = info.label_classes(pet_window, 5, 110, "NATIONALITY", "#e5cd6c", "Times", 14, "bold italic")
                    cellphone_numlabel = info.label_classes(pet_window, 300, 110, "CELLPHONE NUMBER", "#e5cd6c", "Times", 14, "bold italic")
                    Addresslabel = info.label_classes(pet_window, 5, 180, "COMPLETE ADDRESS", "#e5cd6c", "Times", 14, "bold italic")
                    emaillabel = info.label_classes(pet_window, 5, 250, "COMPLETE E-MAIL", "#e5cd6c", "Times", 14, "bold italic")
                    occupationlabel = info.label_classes(pet_window, 5, 320, "OCCUPATION", "#e5cd6c", "Times", 14, "bold italic")

                    # Entry fields
                    f_name_entry = info.entry_classes(pet_window, 5, 70, 43, "white")
                    user_id_entry = info.entry_classes(pet_window, 425, 70, 10, "white")
                    nationality_entry = info.entry_classes(pet_window, 5, 140, 30, "white")
                    cellphone_num_entry = info.entry_classes(pet_window, 300, 140, 24, "white")
                    address_entry = info.entry_classes(pet_window, 5, 210, 57, "white")
                    email_entry = info.entry_classes(pet_window, 5, 280, 57, "white")
                    occupation_entry = info.entry_classes(pet_window, 5, 350, 57, "white")

                    def adopt():
                        # Gather data from entry fields
                        
                        f_name = f_name_entry.get()
                        user_id = user_id_entry.get()
                        nationality = nationality_entry.get()
                        cellphone_num = cellphone_num_entry.get()
                        address = address_entry.get()
                        email = email_entry.get()
                        occupation = occupation_entry.get()
                        dog_id = Value[0]
                        dog_name = Value[1]
                        dog_price = Value[9]
                        # Process or print the data
                        conn = sqlite3.connect('admin3.db')
                        
                        table_create =  '''CREATE TABLE IF NOT EXISTS user_adopt2
                        (f_name TEXT, user_id INTEGER, nationality TEXT, cellphone_num INTEGER, address INTEGER, 
                        email TEXT, occupation TEXT, dog_id INTEGER, dog_name TEXT, dog_price INTEGER)
                        
                        '''
                        conn.execute(table_create)
                        
                        Data_insert = ''' INSERT INTO user_adopt2
                        (f_name, user_id, nationality, cellphone_num, address, email, occupation, dog_id, dog_name, dog_price)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        '''
                        
                        Data_insert_tuple  =  (f_name, user_id, nationality, cellphone_num, address, email, occupation, dog_id, dog_name, dog_price)
                        conn.execute(Data_insert, Data_insert_tuple)
                        conn.commit()
                        conn.close()
                        
                        
                    adopt_button = info.button_c(pet_window, 210, 400, "ENTER", "white", adopt)
                    
                button2 = tkinter.Button(pet_window, text="    APPLY    ", command=button1)
                button2.place(x = 210, y = 400)
               
             
                lst = []
                lst2 = []
                
                sample_2 = dsa.gathered(i)
                a = 50
                b = 100    
                c = 0   
                    
                for k in sample_2:
                   
                        element = k
                        lst.append(element) 
                        #c1 c2 c8 c9
                        name_label = tkinter.Label(pet_window, text="Name", font=("Helvetica", 20), bg="#C48CB3", fg="#E5C9D7")
                        name_label.place(x=250, y=60)
                        
                        weight_label = tkinter.Label(pet_window, text="Weight", font=("Helvetica", 20), bg="#C48CB3", fg="#E5C9D7")
                        weight_label.place(x=440, y=60)
                        
                        species_label = tkinter.Label(pet_window, text="Species", font=("Helvetica", 20), bg="#C48CB3", fg="#E5C9D7")
                        species_label.place(x=210, y=260)
                        
                        price_label = tkinter.Label(pet_window, text="Price", font=("Helvetica", 20), bg="#C48CB3", fg="#E5C9D7")
                        price_label.place(x=420, y=260)
                        
                        
                        if (c == 0 or c == 6):
                            c+=1
                          
                        elif c == 3:
                            a -= 430
                            b +=110
                            name_id_label = tkinter.Label(pet_window, text=element, font=("Helvetica", 20), bg="#0D1E4C", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b)
                            
                            name_id_label = tkinter.Label(pet_window, text="Birth Date", font=("Helvetica", 20), bg="#C48CB3", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b - 40)
                            c+=1
                        elif c == 4:
                            a += 180
                            name_id_label = tkinter.Label(pet_window, text=element, font=("Helvetica", 20), bg="#0D1E4C", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b)
                            
                            name_id_label = tkinter.Label(pet_window, text="Breed", font=("Helvetica", 20), bg="#C48CB3", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b - 40)
                            c+=1
                            
                        elif c == 5:
                            a += 240
                            name_id_label = tkinter.Label(pet_window, text=element, font=("Helvetica", 20), bg="#0D1E4C", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b)
                            
                            name_id_label = tkinter.Label(pet_window, text="Gender", font=("Helvetica", 20), bg="#C48CB3", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b - 40)
                            
                            c+=1
                        elif c == 7:
                            a -= 420
                            b +=100
                            name_id_label = tkinter.Label(pet_window, text=element, font=("Helvetica", 20), bg="#0D1E4C", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b)
                            
                            name_id_label = tkinter.Label(pet_window, text="Message", font=("Helvetica", 20), bg="#C48CB3", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b - 50)
                            
                            c+=1                     
                        else:
                            a += 200
                            name_id_label = tkinter.Label(pet_window, text=element, font=("Helvetica", 20), bg="#0D1E4C", fg="#E5C9D7")
                            name_id_label.place(x=a, y=b)
                
                            
                            c+=1
                           
                            
                # Add more details for the pet if needed (e.g., image, info)
                # Example image display (assuming pet images are available)
                try:
                    filepath1 = dsa.gathered(i)[6].replace('"', "").strip()  # Get the image path
                    img = Image.open(filepath1)
                    img = img.resize((160, 160))
                    tk_img = ImageTk.PhotoImage(img)
                    
                    img_label = tkinter.Label(pet_window, image=tk_img)
                    img_label.place(x=0, y=0)  # Adjust placement as needed
                    img_label.image = tk_img  # Keep a reference to prevent garbage collection
                    
                except Exception as e:
                    print(f"Error loading image for Pet {i}: {e}")
                    
                    
                #---------------------------
                
                #----------------------
                
                pet_window.mainloop()

            # Display the pet image with a button#-----------------------------------------------
            info.button_b(x, y, "Add Pet", "gray", 5, 10, button_callback, tk_img)
            
        except Exception as e:
            print(f"Error loading image {filepath1}: {e}")

        # Update x and y for the next image
        x += 250
        if i == 4:
            y += 230
            x -= 1250

    # Keep references to the images to prevent garbage collection
    low_des.image_refs = image_references
    

# Wishlist function
def wishlist():
    design = tkinter.Label(background="#0D1E4C", height="40", width="200")
    design.place(x=0, y=110)

# To Know function
def toknow():
    design = tkinter.Label(background="#0D1E4C", height="40", width="200")
    design.place(x=0, y=110)

# Sign-out function
def sign_out():
    print("Hahaha")

# Function to display about us page
def about_us():
    design = tkinter.Label(background="#0D1E4C", height="40", width="200")
    design.place(x=0, y=110)
    
    user_des = tkinter.Label(image=image_user)
    user_des.place(x=600, y=110)

    design = tkinter.Label(background="#26415E", height="7", width="200")
    design.place(x=0, y=0)

    # Buttons
    info.button_b(600, 35, "Add Pet", "gray", 5, 10, about, img_about_us_button)
    info.button_b(750, 35, "Pet Gallery", "gray", 5, 10, gallery, img_gallery_button)  
    #info.button_b(900, 35, "Wishlist", "gray", 5, 10, wishlist, img_wishlist_button) 
    #info.button_b(1050, 35, "To Know", "gray", 5, 10, toknow, img_toKnow_button)  
    #info.button_b(1200, 35, "Sign Out", "gray", 5, 10, sign_out, img_signout_button)

    # Labels
    animals_label = info.dog_label(50, 35, "ADOPT PET", "#26415E", "Helvetica", 25, "bold italic")
    info.dog_label(50, 175, "ABOUT US", "#0D1E4C", "Helvetica", 10, "bold italic")
    info.dog_label(50, 195, "BRING HOME\nA NEW BEST\nFRIEND BY\nADOPTING", "#0D1E4C", "Helvetica", 50, "bold")
    info.dog_label(100, 600, "ADOPT A FURRY COMPANION AND ADD THEM TO\nYOUR FAMILY AS YOUR NEW BEST FRIEND", "#0D1E4C", "Helvetica", 10, "bold italic")

# Initialize the About Us page
about_us()


root.mainloop()
