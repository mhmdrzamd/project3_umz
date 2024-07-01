from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from datetime import datetime
import jdatetime
from tkinter import ttk 
import requests
from bs4 import BeautifulSoup
import csv
import re
from PIL import Image,ImageTk

win=Tk()
win.title("منوی اصلی")
win.geometry("860x410")
win.resizable(width = False , height = False)

Frame1 = LabelFrame(win, text="",width=640,height=400,bg="grey").place(x=2,y=8)
Frame2 = LabelFrame(win, text="",width=314,height=400,bg="white").place(x=544,y=8)

vazir_font = font.Font(family="Vazir", size=18, weight="bold")
Label(Frame2, text="web scraping app", font=vazir_font, fg="black", bg="white").place(x=600, y=360)




#===================================================
#icons

web_scraper= ImageTk.PhotoImage(Image.open("web_scraper.png").resize((220,220)))
confirmation_icon= ImageTk.PhotoImage(Image.open("confirmation_icon.png").resize((20,20)))
remove_icon = ImageTk.PhotoImage(Image.open("remove_icon.png").resize((20,20)))
search_icon = ImageTk.PhotoImage(Image.open("search_icon.png").resize((20,20)))
show_info = ImageTk.PhotoImage(Image.open("show_info.png").resize((20,20)))


#===================================================
Label(Frame2, text="",image=web_scraper).place(x=585, y=130)



#........................................................
# clock and date function
def update_clock():
    global jdate
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    jdate = jdatetime.date.fromgregorian(day=now.day, month=now.month, year=now.year)
    current_date = jdate.strftime("%Y-%m-%d")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    win.after(1000, update_clock)


time_frame = Frame(Frame2, width=80, height=10, bg="gray", bd=4, relief="groove")
time_frame.place(x=650, y=70)

date_frame = Frame(Frame2, width=125, height=10, bg="gray", bd=4, relief="groove")
date_frame.place(x=630, y=20)

#the pady parameters put some space between the widgets
#by setting pady=0 im telling tkinter to add no extra
#space above or below the label
time_label = Label(time_frame, text="", font=("Segoe UI", 15), fg="black", bg="gray")
time_label.pack(pady=0)
date_label = Label(date_frame, text="", font=("Segoe UI", 17), fg="black", bg="gray")
date_label.pack(pady=0)

update_clock()
#.......................................................

Entry_word=Entry(win,justify='right',font=("w",13),width=20, bd=2, highlightbackground='blue', relief='solid')
Entry_word.place(x=210,y=35)
Label(win,text=" : جستجو ",font=(vazir_font, 16),bg='grey').place(x=400,y=30)



group=['game','tecnology','news','etc']
Label(Frame1,text=" : انتخاب گروه",font=(vazir_font,16),bg='grey').place(x=400,y=90)
selected_group = ttk.Combobox(Frame1, values=group)
selected_group.place(x=230, y=95)



def group_check():
    global urls_2 
    check=selected_group.get()
    urls_2=[]
    print('group value stored')
 
    if check == "tecnology":
        urls=['https://en.wikipedia.org/wiki/{}','https://techcrunch.com/?s={}','https://gizmodo.com/search?blogId=4&q={}','https://www.techradar.com/search?searchTerm={}']
        Label(Frame1,text=" : انتخاب سایت",font=(vazir_font,16),bg='grey').place(x=400,y=150)
        selected_urls = ttk.Combobox(Frame1, values=urls)
        selected_urls.place(x=230, y=155)

        def urls_check():
            global urls_2
            print('url stored')
            if selected_urls.get() == '':
                urls_2.extend(urls)
            else:
                for i in urls:
                    if i == selected_urls.get():
                        urls_2.append(i)
        Urls_check=Button(Frame1 , text = "تایید", image=confirmation_icon,compound=TOP,command=urls_check).place(x=190,y=155)


    elif check == "game":    
        urls=['https://en.wikipedia.org/wiki/{}','https://vigiato.net/?s={}','https://www.zoomg.ir/search/{}/','https://www.gamespot.com/search/?header=1&q={}']
        Label(Frame1,text=" : انتخاب سایت",font=(vazir_font,16),bg='grey').place(x=400,y=150)
        selected_urls = ttk.Combobox(Frame1, values=urls)
        selected_urls.place(x=230, y=155 )

        def urls_check():
            global urls_2
            print('url stored')
            if selected_urls.get() == '':
                urls_2.extend(urls)
            else:
                for i in urls:
                    if i == selected_urls.get():
                        urls_2.append(i)
        Urls_check=Button(Frame1 , text = "تایید", image=confirmation_icon,compound=TOP,command=urls_check).place(x=190,y=155)


    elif check == "news":    
        urls=['https://en.wikipedia.org/wiki/{}','https://dig.watch/?s={}','https://www.tehrantimes.com/search?lang=en&l=&a=0&q={}&pageSize=10&alltp=true&allpl=true&allty=true',
                'https://www.khabaronline.ir/search?q={}']
        Label(Frame1,text=" : انتخاب سایت",font=(vazir_font,16),bg='grey').place(x=400,y=150)
        selected_urls = ttk.Combobox(Frame1, values=urls)
        selected_urls.place(x=230, y=155)

        def urls_check():
            global urls_2
            print('url stored')
            if selected_urls.get() == '':
                urls_2.extend(urls)
            else:
                for i in urls:
                    if i == selected_urls.get():
                        urls_2.append(i)
        Urls_check=Button(Frame1 , text = "تایید", image=confirmation_icon,compound=TOP,command=urls_check).place(x=190,y=155)

 
    elif check == 'etc':    
        urls_2.append('https://en.wikipedia.org/wiki/{}')
        print('url stored')


    else:
        if check == '':
            messagebox.showerror("خطا", "گروه مورد نظر خود را انتخاب کنید!!")
        
        
Group_check=Button(Frame1 , text = "تایید",image=confirmation_icon ,compound=TOP,command=group_check).place(x=190,y=95)

#===============================================================

def script_search():

    window_group = Toplevel()
    window_group.title("")
    window_group.geometry("800x400")
    window_group.resizable(width = False , height = False)

        
    def get_word_data(word, urls):
        try:
            data = []
            for url in urls:
                response = requests.get(url.format(word))
                soup = BeautifulSoup(response.content, 'lxml')

                    
                # using regex to show only www.example.com form
                match = re.search(r"https://([^/]+)", url)
                match=match.group(1)

                # Extract data from the page
                # For example, let's extract all paragraphs that contain the word
                paragraphs = [p.text for p in soup.find_all('p')]
                data.extend([(p, match) for p in paragraphs])
            return data
        except (Exception , TypeError):
            print('Site URL may not be correct')

    try:
        try:
            # Get the data about the word
            data = get_word_data(Entry_word.get(), urls_2)
        except:
            messagebox.showerror("خطا", "کلمه مورد نظر خود را وارد کنید!!")



        # Store the data in a CSV file
        with open('word_data.csv', 'a',encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Text', 'URL'])
            for text, url in data:
                writer.writerow([text, url])

        print('Data stored in word_data.csv')

        # Create a Text widget
        text_widget = Text(window_group)
        text_widget.pack(side="left", fill="both", expand=True)

        scrollbar_group = Scrollbar(window_group,orient='vertical', command=text_widget.yview)
        #scrollbar_group.place(x=5,y=10, height=380)

        text_widget.configure(yscrollcommand=scrollbar_group.set)
        scrollbar_group.pack(side="right", fill="y")

        text_widget.pack()
            
        if not all([Entry_word.get()]):
            messagebox.showerror('Error', 'کلمه مورد نظر را وارد کنید!!!')
        else:
            Entry_word.delete(0, END)


        # Open the CSV file
        with open('word_data.csv', 'r',encoding="utf-8", newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                text = '\t'.join(row)
                text_widget.insert(tk.END, text + "\n\n")  
    except TypeError:
        print ('there is not any page about this word in this url')

#===============================================================
word_search=Button(Frame1 , text = "جستجو",image=search_icon ,compound=TOP,command=script_search).place(x=150,y=35)




#=====================================
#remove data button

def remove_data():
    # Open the CSV file in write mode, which will erase its contents
    with open('word_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])  # Write an empty list to the file

remove_data=Button(Frame1 , text = "remove data", image=remove_icon ,compound=TOP,command=remove_data).place(x=40,y=350)

#====================================



#====================================
def show_data():
    
    window_group = Toplevel()
    window_group.title("")
    window_group.geometry("800x400")
    window_group.resizable(width = False , height = False)

    # Create a Text widget
    text_widget = Text(window_group)
    text_widget.pack(side="left", fill="both", expand=True)

    scrollbar_group = Scrollbar(window_group,orient='vertical', command=text_widget.yview)
    #scrollbar_group.place(x=5,y=10, height=380)

    text_widget.configure(yscrollcommand=scrollbar_group.set)
    scrollbar_group.pack(side="right", fill="y")

    text_widget.pack()
        
    # Open the CSV file
    with open('word_data.csv', 'r',encoding="utf-8", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            text = '\t'.join(row)
            text_widget.insert(tk.END, text + "\n\n")  

remove_data=Button(Frame1 , text = "show data", image=show_info ,compound=TOP,command=show_data).place(x=130,y=350)

#====================================




win.mainloop()