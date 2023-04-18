from tkinter import *
from tkinter import ttk
import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/show_available_room"

hotel = ["Kirimayaresort","Muthimaya","Atta"]

root = Tk()

root.title("Kiri")

def on_click():
    global photo


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
        #menu = om["menu"]
        #menu.delete(0, "end")
        #for key,value in data.items():
            #temp = key +  value
            #menu.add_command(label=temp,command=lambda value=temp: select_opt.set(value))
        print(data)
        #for key,value in data.items():
           # temp = str(key)
            #menu.add_command(label=temp,command=lambda value=temp: select_opt.set(value))
        for key,value in data.items():
            photo = PhotoImage(file=value)
            
            print(value)
            Button(root, text=str(key), bg="green", command=on_click).place(x=100,y=200+i)
            Button(root, image=photo, borderwidth=0 ).place(x=300,y=200+i)
            i+=150
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


btn = Button(root, text="Serch", bg="green", command=on_click)
btn.place(x = 485, y = 80)

choose_hotel = OptionMenu(root, select_hotel, *hotel)
choose_hotel.config(width=15)
choose_hotel.place(x= 650,y = 27)



root.geometry("1024x720+200+50")

root.mainloop()