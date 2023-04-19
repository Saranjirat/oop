from tkinter import *
from tkinter import ttk
import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/show_available_room"

hotel = ["Kirimayaresort","Muthimaya","Atta"]

root = Tk()

root.title("Kiri")

room_name1 = None
room_name2 = None

def on_click():
    global photo1
    global btn_list
    global photo2
    global text1
    global text2
    global room_name1
    global room_name2


    text1 = None
    text2= None

    photo1 = None
    photo2 = None
    print('on click')
    st_date= str(dayin.get())+'-'+str(monthin.get()) +'-'+ str(yearin.get())
    end_date = str(dayout.get())+'-'+str(monthout.get()) +'-'+ str(yearout.get())
    print(st_date)
    payload = {
        "Hotel" : select_hotel.get(),
        "start_date": st_date,
        "start_time": "9:00",
        "end_date": end_date,
        "end_time": "16:00",   
    }
    response = requests.post(API_ENDPOINT1, json=payload)
    if response.ok:
        data = response.json()
        data = data['Data']
        print(data)
        i=0
        j=0
        btn_list = []

        key_list = []
        value_list = []
        for key,value in data.items():
            
            key_list.append(key)
            value_list.append(value)

            
            print(value)

           # btn1 = Button(root, text=str(key), bg="green").place(x=100,y=200+i)
           # btn2= Button(root, image=photo, borderwidth=0 ).place(x=300,y=200+i)

        print(key_list)
        if room_name1 == None:
            room_name1.destroy()
        if room_name2 == None:
            room_name2.destroy()

        
        if len(key_list) == 1:
            text1= str(key_list[0])
            room_name1 =Button(root,text=text1).place(x=100,y=200)
            #btn_list.append(room_name1)

        if len(key_list) == 2:
            text1= str(key_list[0])
            text2= str(key_list[1])
            room_name1 =Button(root,text=text1).place(x=100,y=200)
            
            j+=150
            room_name2 =Button(root,text=text2).place(x=100,y=200+j)
           #btn_list.append(room_name1)
            #btn_list.append(room_name2)

###########################################################
        print(value_list)
        j=0
        if len(value_list) == 1:
            photo1 = PhotoImage(file=value_list[0])
            label1 = Label(root,image=photo1).place(x=300,y=200)
            #btn_list.append(label1)

        if len(value_list) == 2:
            photo1 = PhotoImage(file=value_list[0])
            label1 = Label(root,image=photo1).place(x=300,y=200)
            photo2 = PhotoImage(file=value_list[1])
            j+=150
            label2 = Label(root,image=photo2).place(x=300,y=200+j)
            #btn_list.append(label1)
            #btn_list.append(label2)

        print(btn_list)
    return


dayin = StringVar()
monthin  = StringVar()
yearin = StringVar()
dayout = StringVar()
monthout  = StringVar()
yearout = StringVar()
select_hotel = StringVar()

cbo_day_pickup = ttk.Combobox(root, values = list(range(1,32)), width = 3, state="readonly",textvariable=dayin)
cbo_day_pickup.current(0)
cbo_day_pickup.place(x = 200 , y = 30)

cbo_month_pickup = ttk.Combobox(root, values = list(range(1,13)), width = 4,state = "readonly",textvariable=monthin)
cbo_month_pickup.current(1)
cbo_month_pickup.place(x = 245, y = 30)

cbo_year_pickup = ttk.Combobox(root, values = list(range(2023,2025)), width = 5,textvariable=yearin)
cbo_year_pickup.current(0)
cbo_year_pickup.place(x = 295 , y = 30)





cbo_day_return = ttk.Combobox(root, values = list(range(1,32)), width = 3, state="readonly",textvariable=dayout)
cbo_day_return.current(0)
cbo_day_return.place(x = 430 , y = 30)

cbo_month_return = ttk.Combobox(root, values = list(range(1,13)), width = 4,state = "readonly",textvariable=monthout)
cbo_month_return.current(1)
cbo_month_return.place(x = 475, y = 30)

cbo_year_return = ttk.Combobox(root, values = list(range(2023,2025)), width =5,textvariable=yearout)
cbo_year_return.current(0)
cbo_year_return.place(x = 525 , y = 30)


btn = Button(root, text="Search", bg="green", command=on_click)
btn.place(x = 485, y = 80)

choose_hotel = OptionMenu(root, select_hotel, *hotel)
choose_hotel.config(width=15)
choose_hotel.place(x= 650,y = 27)



root.geometry("1024x720+200+50")

root.mainloop()