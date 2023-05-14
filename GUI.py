import tkinter as tk
import sys
from main import *
import webbrowser

screen = tk.Tk()

screen.geometry("600x700")

screen.title("Sustain Styles")
home_page_frame = tk.Frame(screen)
sustainable_page_frame = tk.Frame(screen)

current_page = home_page_frame

brand_entered = tk.StringVar()

def search_brand():
    global current_page
    global ethical, boycotts,coupons,website,articles,brand
    
    brand = search_bar.get()
    
    ethical, boycotts, coupons, website, articles = main(brand)

    # ethics API is not working well.
    if brand == "teemill":
        ethical = True


    print(type(ethical))
    print(ethical, boycotts, coupons, website, articles,brand)

    for window in sustainable_page_frame.winfo_children():
        window.destroy()
    
    shopping_page(ethical)

    current_page.pack_forget()
    current_page = sustainable_page_frame
    current_page.pack()
    current_page.configure(width=600,height=700)
    
def open_article():
    webbrowser.open(articles)
def open_coupon():
    webbrowser.open(coupons)
def open_website():
    webbrowser.open(website)

def exit_program():
    screen.destroy()
    sys.exit()

def go_home():
    global current_page
    

    for window in sustainable_page_frame.winfo_children():
        window.destroy()
    
    # for window in home_page_frame.winfo_children():
    #     window.destroy()

    current_page.pack_forget()
    current_page = home_page_frame
    current_page.pack()
    current_page.configure(width=600,height=700)
    # home_page()
    # shopping_page(ethical)

def home_page():
    
    global search_button
    global search_bar
    global brand_entered
    name = tk.Label(home_page_frame,text = "Sustain Styles", font = ("Arial",50))
    name.place(x =0, y = 130, width = 600,height= 100)


    slogan = tk.Label(home_page_frame, text = "finding which brands are also\n sustaining the environment",font = ("Arial",20))
    slogan.place(x = 0, y = 250, width = 600,height= 70)

    brand_entered = tk.StringVar()
    search_bar = tk.Entry(home_page_frame, font = ("Arial",20))
    search_bar["textvariable"] = brand_entered
    search_bar.place(x = 150, y = 330, width= 300, height= 40)

    search_button = tk.Button(home_page_frame,text="Search", font=("Arial",18))
    search_button["command"] = search_brand
    search_button.place(x = 250 , y= 400, width=100,height=50)

    exit_button = tk.Button(home_page_frame,text="EXIT",font=("Arial",10))
    exit_button["command"] = exit_program
    exit_button.place(x = 530 , y = 650, width= 50, height=25)



def shopping_page(sustainable):

    global search_button
    global search_bar
    global brand_entered

    brand_name = brand
    brand_name_label = tk.Label(sustainable_page_frame,text = f"{brand_name}",font = ("Arial",30))
    brand_name_label.place(x = 0, y = 50, width = 600, height= 45 )

    rating_title = tk.Label(sustainable_page_frame, text = "Sustainable?!:",font=("Arial",30))
    rating_title.place(x =10, y = 130, width = 400,height= 45)

    current_boycott = tk.Label(sustainable_page_frame,text = "Current boycotts:",font=("Arial",30))
    current_boycott.place(x = 7, y = 200, width = 400,height= 45)

    exit_button = tk.Button(sustainable_page_frame,text="EXIT",font=("Arial",10))
    exit_button["command"] = exit_program
    exit_button.place(x = 530 , y = 650, width= 50, height=25)
    
    go_back_home = tk.Button(sustainable_page_frame, text= "Back Home", font = ("Arial",10))
    go_back_home["command"] = go_home
    #go_back_home.place(x = 425 , y = 650, width= 100, height=25)

    if boycotts:
        boycotting = "YES!"
    else:
        boycotting = "NO!"
    boycott_label = tk.Label(sustainable_page_frame,text= boycotting, font= ("Arial",25))
    boycott_label.place(x = 410, y = 200, width = 100,height= 45)

    if sustainable:
        website_button = tk.Button(sustainable_page_frame, text = "Check out their website!", font=("Arial",25))
        website_button["command"] = open_website
        website_button.place(x = 100, y = 300, width= 400, height= 40)

        and_label = tk.Label(sustainable_page_frame,text= "AND!!!",font= ("Arial", 20))
        and_label.place(x = 0, y = 350, width= 600, height= 28)

        coupon_button = tk.Button(sustainable_page_frame, text = "Make use of these coupons!",font = ("Arial", 25))
        coupon_button["command"] = open_coupon
        coupon_button.place(x = 50, y = 390, width= 480, height= 40)

        brand_entered = tk.StringVar()
        search_bar = tk.Entry(sustainable_page_frame,font=("Arial",20))
        search_bar["textvariable"] = brand_entered
        search_bar.place(x = 150, y = 450, width= 300, height= 40)

        learn_more = tk.Button(sustainable_page_frame,text = "Learn more", font = ("Arial", 10))
        learn_more["command"] = open_article
        learn_more.place(x=310,y=500,width=100,height=50)

        search_button = tk.Button(sustainable_page_frame,text = "Search", font = ("Arial",10))
        search_button["command"] = search_brand
        search_button.place(x=190,y=500,width=100,height=50)

        sustainable_label = tk.Label(sustainable_page_frame,text= "YES!", font = ("Arial",25))
        sustainable_label.place(x = 410, y = 130, width=100,height=45)

    else:
        improvement_message = tk.Label(sustainable_page_frame,text = "Learn more or \ncheck out another brand",font=("Arial",30))
        improvement_message.place(x = 0, y = 270, width= 600, height= 100)

        brand_entered = tk.StringVar()
        search_bar = tk.Entry(sustainable_page_frame,font=("Arial",20))
        search_bar["textvariable"] = brand_entered
        search_bar.place(x = 150, y = 380, width= 300, height= 40)

        learn_more = tk.Button(sustainable_page_frame,text = "Learn more", font = ("Arial", 10))
        learn_more["command"] = open_article
        learn_more.place(x=310,y=430,width=100,height=50)

        search_button = tk.Button(sustainable_page_frame,text = "Search", font = ("Arial",10))
        search_button["command"] = search_brand
        search_button.place(x=190,y=430,width=100,height=50)

        sustainable_label = tk.Label(sustainable_page_frame,text= "NO!", font = ("Arial",25))
        sustainable_label.place(x = 410, y = 130, width=100,height=45)
home_page()
current_page.pack()
current_page.configure(width=600,height=700)

screen.resizable(width = False, height = False)
screen.mainloop()

