import tkinter as tk
from tkinter import Entry, Label, ttk
import tkinter.filedialog
from PIL import ImageTk, Image
from tkcalendar import Calendar
from tkcalendar import DateEntry
from  datetime import date
from tkinter import messagebox




class admin:
    def __init__(self):
        # initial parameters for methods
        self.frame1 = self.label1 = self.entry1 = self.calendar1 = self.button1 = self.option1 = None

        # initial parameters for new_image method
        self.length = self.width = self.path = self.image = self.img_thumb = self.label2 = None
    
    
    def dog_label(self, a, b, text_value, bg, f_text, f_size, f_bold) -> tkinter.Label:
        self.dog_label_1 = tkinter.Label(text=text_value,
                                   font=(f_text, f_size, f_bold),
                                   background=bg)
        self.dog_label_1.place(x=a, y=b)
        
    def dog_label2(self, a, b, text_value, bg, f_text, f_size, f_bold, w) -> tkinter.Label:
        self.dog_label_1 = tkinter.Label(text=text_value,
                                   font=(f_text, f_size, f_bold),
                                   background=bg, width=w)
        self.dog_label_1.place(x=a, y=b)
        
    def dog_text(self, a, b, w, h, back):
        
        self.text = tkinter.Text(width=w, height=h,  bg = back, font=("Times", "14"),  cursor ="arrow")
        self.text.place(x=a, y=b)
        return self.text

        
    def dog_entry(self, a, b, w, back) -> tkinter.Entry:
        
        self.dog_entry_1 = tkinter.Entry(width=w, bg = back, font=("Times", "14"),  cursor ="arrow")
        self.dog_entry_1.place(x = a, y = b)
        return self.dog_entry_1
    
    def label_classes(self,canva, a, b, text_value, bg, f_text, f_size, f_bold ):
        self.dog_label_1 = tkinter.Label(canva,text=text_value,
                                   font=(f_text, f_size, f_bold),
                                   background=bg)
        self.dog_label_1.place(x=a, y=b)
        
    def entry_classes(self, canva, a, b, w, back) -> tkinter.Entry:
        
        self.dog_entry_1 = tkinter.Entry(canva,width=w, bg = back, font=("Times", "14"),  cursor ="arrow")
        self.dog_entry_1.place(x = a, y = b)
        return self.dog_entry_1
    
    def dog_date(self, a, b, w):
      
        date_1 = DateEntry(selectmode = 'day', width = w)
        dt=date(2024,4,8)
        date_1.set_date(dt)
        date_1.place(x=a, y=b)
        
        return date_1  
    def dog_combobox(self, a, b, text_value, w):
        
        self.info_combobox = ttk.Combobox(values=text_value, width=w, font=("Times", "14"),  cursor ="arrow")
        self.info_combobox.place(x=a,y=b)
        return self.info_combobox
    #-----------------------
    def new_entry(self, x, y, w):
        #   creates an entry with corresponding width
        self.entry1 = Entry(width=w, fg="black", border=2, bg="white")
        self.entry1.place(x=x, y=y)
        return self.entry1
    
    def new_label(self, text, x, y) -> str:
        #   creates a label with brown text and gray bg
        self.label1 = Label(text=text, bg="#f9f3b9", justify="left", font=("Times", 14, "bold italic"))
        self.label1.place(x=x, y=y)
    
    def new_label_entry(self,text, x, y, w):
        #   creates a label with brown text and gray bg, as well as its corresponding entry
        self.new_label(text, x, y)
        entry1 = self.new_entry(x, y + 30, w)
        return entry1
        
    def new_image(self, path, a, b, length, width) -> str:
       
        self.image = Image.open(path)
        self.img_thumb = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.label2 = Label(image=self.img_thumb)
        self.label2.place(x=a, y=b)
    
    def change_data(self, widget, data):
        widget.configure(state="normal")
        self.clear_data(widget)
        widget.insert(0, str(data))
        widget.configure(state="readonly")
    
    
    def clear_data(self, widget):
        widget.configure(state="normal")
        widget.delete(0, "end")
        
    
    def open_pic(self):
        filetypes = (("JPG", "*.jpg"), ("PNG", "*.png"), ("ALL files", "*.*"))
        filepath = tkinter.filedialog.askopenfile(title="Search Picture Path", initialdir="/", filetypes=filetypes)
        return filepath
    
    def clear_widget(source_frame):
        for child in source_frame.winfo_children():
            child.destroy()
            
#---button------------           
    def button_a(self, x, y, text, color, a) -> tkinter.Button:
        
        self.button = tkinter.Button(text=text, bg=color, command=a)
        self.button.place(x=x, y=y)
        return self.button 
    
    def button_b(self, x, y, text, color, w, h, a, im) -> tkinter.Button:
        
        self.button = tkinter.Button(text=text, bg=color, command=a, image=im)
        self.button.place(x=x, y=y)
        return self.button  
    
    def button_c(self, canva, x, y, text, color, a) -> tkinter.Button:
        
        self.button = tkinter.Button(canva,text=text, bg=color, command=a)
        self.button.place(x=x, y=y)
        return self.button
    
    def button_pic(self, w, h, link) -> ImageTk.PhotoImage:
        self.photo_button = Image.open(link)
        self.resized = self.photo_button.resize((w, h))
        self.user_b = ImageTk.PhotoImage(self.resized)
        return self.user_b
        
        
    
    
