from tkinter import ttk
from tkinter import *
import datetime

import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/show_available_room"

hotel = ["Kirimayaresort","Muthimaya","Atta"]

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
        i=1
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
           
            
            print(value)
            Button(root, text=str(key), bg="green", command=on_click).grid(row=6+i, column=0, columnspan=1)
            Button(root, image=PhotoImage(file=value), borderwidth=0 ).grid(row=6+i, column=1, columnspan=1)
            i+=1
    return

def set_input1():
    st_date.set("26-03-2023")
    st_time.set("09:00")
    end_date.set("26-03-2023")
    end_time.set("16:00")


root = Tk()
root.option_add("*Font","impact 18")
root.title("KIri")

#st_date = StringVar()
#st_time = StringVar()
#end_date = StringVar()
#end_time = StringVar()
#capacity = StringVar()
select_opt = StringVar()
select_hotel = StringVar()
dayin = StringVar()
monthin  = StringVar()
yearin = StringVar()
dayout = StringVar()
monthout  = StringVar()
yearout = StringVar()

select_hotel.set('Select hotel')

data_list = ['0']

month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']


Label(root, text="Date Arrival :").grid(row=0, column=0,padx=10 , ipady=5, sticky='E')
cbo_day = ttk.Combobox(root, values=list(range(1,32)),width=3,textvariable=dayin)
cbo_day.current(0)
cbo_day.grid(row=0,column=1)

cbo_month = ttk.Combobox(root, values=month_list, width=3,textvariable=monthin )
cbo_month.current(0)
cbo_month.grid(row=0,column=2)

cbo_year = ttk.Combobox(root, values=list(range(2023,2025)),width=5,textvariable=yearin)
cbo_year.current(0)
cbo_year.grid(row=0,column=3)

Label(root, text="Date Depature :").grid(row=1, column=0,padx=10, ipady=5, sticky='E')

cbo_day2 = ttk.Combobox(root, values=list(range(1,32)),width=3,textvariable=dayout)
cbo_day2.current(1)
cbo_day2.grid(row=1,column=1)

cbo_month2 = ttk.Combobox(root, values=month_list, width=3 ,textvariable=monthout)
cbo_month2.current(0)
cbo_month2.grid(row=1,column=2)

cbo_year3 = ttk.Combobox(root, values=list(range(2023,2025)),width=5,textvariable=yearout)
cbo_year3.current(0)
cbo_year3.grid(row=1,column=3)


#Entry(root, textvariable=st_time, width=12, justify="left").grid(row=1, column=1, padx=10)
#Label(root, text="End Date :").grid(row=2, column=0,padx=10, ipady=5, sticky='E')
#Entry(root, textvariable=end_date, width=12, justify="left").grid(row=2, column=1, padx=10)
#Label(root, text="End Time :").grid(row=3, column=0,padx=10, ipady=5, sticky='E')
#Entry(root, textvariable=end_time, width=12, justify="left").grid(row=3, column=1, padx=10)


choose_hotel = OptionMenu(root, select_hotel, *hotel)
choose_hotel.config(width=15)
choose_hotel.grid(row=4,column=0, columnspan=1)

#set_input1()
Button(root, text="Serch", bg="green", command=on_click).grid(row=4, column=1, columnspan=1)



#om = OptionMenu(root, select_opt, *data_list)
#om.grid(row=6, column=1)
#om.config(width=15)


root.mainloop()
