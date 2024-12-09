#adopt pet aplication form -  name, age, nationality, address, cellphone num, email add, ocupation
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
#----------------color palete
#0D1E4C
#C48CB3
#E5C9D7
#83A6CE
#26415E
#0B1B32
root = tkinter.Tk()
root.title("USER_dashboard")
root.config(bg="#0D1E4C")
root.geometry("1400x700")

info = admin_dog_input_class.admin()
dsa = dsa_pet.dataBase()

image_user = info.button_pic(770, 580, "image\\user_frontpage.png")


img_about_us_button = info.button_pic(100, 40, "image_ver2\\about_us.png")
img_gallery_button = info.button_pic(100, 40, "image_ver2\\pet_gallery.png")
img_wishlist_button = info.button_pic(100, 40, "image_ver2\\wishlist.png")
img_toKnow_button = info.button_pic(100, 40, "image_ver2\\get_to_know.png")
img_signout_button = info.button_pic(100, 40, "image\\sign_out.png")
def about():
    about_us()
#---------------------------------------------------------------------------
def gallery():
    design = tkinter.Label(background="#0D1E4C", height="40", width="200")
    design.place(x=0, y=110)
    
    id_ascending_access_image()
   
def id_ascending_access_image(): 
    high_des = tkinter.Label(background="#E5C9D7", height=5, width=250)
    high_des.place(x=0, y=110)

    low_des = tkinter.Label(background="#83A6CE", height=50, width=200)
    low_des.place(x=0, y=190)
    # Get the ascending IDs (ensure `dsa.ascending_index` works as expected)
    id_ascending = dsa.ascending_index(0)
    x = 50
    y = 230
    lst = []
    image_references = []  # Store references to all images to avoid garbage collection

    for i in id_ascending:
        # Get data for each ID (ensure `dsa.gathered` works as expected)
        sample_1 = dsa.gathered(i)
        lst.append(sample_1)

        # Create and place a text label
        #data_label1 = info.dog_label(x, y, sample_1[6], "#E5C9D7", "Helvetica", 10, "bold italic")

        # Process and load the image
        filepath1 = sample_1[6].replace('"', "").strip()  # Clean up the file path

        try:
            # Open and resize the image using Pillow
            img = Image.open(filepath1)
            img = img.resize((130, 130))  # Resize the image to the desired dimensions
            tk_img = ImageTk.PhotoImage(img)  # Convert to PhotoImage
            
            # Store a reference to avoid garbage collection
            image_references.append(tk_img)
            #button functionality
            def button_callback(i=i):  # Capture the current `i` value
                root = tkinter.Tk()
                root.title("USER_dashboard")
                root.config(bg="#0D1E4C")
                root.geometry("400x300")
                root.mainloop()

            # Display the image
            info.button_b(x, y, "Add Pet","gray",5, 10, button_callback, tk_img)
            
            
            #img_label = tkinter.Label(image=tk_img, background="#E5C9D7")
            #img_label.place(x=x, y=y)
        except Exception as e:
            print(f"Error loading image {filepath1}: {e}")

        # Update x and y for the next image
        x += 250
        if(i==4):
            y += 230
            x-=1250
        
            
    low_des.image_refs = image_references  
    #button()      
#--------------------------------------------------------------------------  
def prim():
    print("Haaha")
def wishlist():
    design = tkinter.Label(background="#0D1E4C", height="40", width="200")
    design.place(x=0, y=110)
    
def toknow():
    design = tkinter.Label(background="#0D1E4C", height="40", width="200")
    design.place(x=0, y=110)
    
    
def sign_out():
    print("Hahaha")






def about_us():
    
    design = tkinter.Label(background="#0D1E4C", height="40", width="200")
    design.place(x=0, y=110)
    
    
    user_des = tkinter.Label(image=image_user)
    user_des.place(x=600,y= 110)
    #---------------------------------------
    design = tkinter.Label(background="#26415E", height="7", width="200")
    design.place(x=0, y=0)

    #button-----------
    info.button_b(600, 35, "Add Pet","gray",5, 10, about, img_about_us_button)
    info.button_b(750, 35, "Add Pet","gray",5, 10, gallery, img_gallery_button)  
    info.button_b(900, 35, "Add Pet","gray",5, 10, wishlist, img_wishlist_button) 
    info.button_b(1050, 35, "Add Pet","gray",5, 10, toknow, img_toKnow_button)  
    signout_button = info.button_b(1200, 35, "SIGN OUT","gray",5, 10, sign_out, img_signout_button)
    #label----------------------------
    animals_label = info.dog_label(50, 35, "ADU PET", "#26415E", "Helvetica", 25, "bold italic")
    info.dog_label(50, 175, "ABOUT US", "#0D1E4C", "Helvetica", 10, "bold italic")
    info.dog_label(50, 195, "BRING HOME\nA NEW BEST\nFRIEND BY\nADOPTING", "#0D1E4C", "Helvetica", 50, "bold")
    info.dog_label(100, 600, "ADOPT A FURRY COMPANION AND ADD THEM TO\nYOUR FAMILY AS YOUR NEW BEST FRIEND", "#0D1E4C", "Helvetica", 10, "bold italic")
    
about_us()


root.mainloop()

