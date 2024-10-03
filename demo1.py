from tkinter import *
import psutil
import math
import speedtest
from PIL import Image,ImageTk

root = Tk()
root.config(bg='black')
image = Image.open('single.png')
tk_image = ImageTk.PhotoImage(image)
root.geometry("1700x1080")
root.title("CPU Status")

def usage():
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count,image=tk_image,compound='center',fg='#00ffff')

    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=cpu_usage,image=tk_image,compound='center',fg='#00ffff')
    cpu_usage_label.after(100,usage)

    ram_count = math.floor(psutil.virtual_memory()[0]/1000000000)
    ram_count_text = str(ram_count) + "GB"
    ram_count_label.config(text=ram_count_text,image=tk_image,compound='center',fg='#00ffff')

    ram_usage = psutil.virtual_memory()[2]
    ram_usage_text = str(ram_usage) + "%"
    ram_usage_label.config(text=ram_usage_text,image=tk_image,compound='center',fg='#00ffff')

    avail_ram = math.floor(psutil.virtual_memory()[1]/1000000000)
    avail_ram_text = str(avail_ram) + "GB"
    ram_avail_label.config(text=avail_ram_text,image=tk_image,compound='center',fg='#00ffff')


def internet_speed():
    print('Testing internet speed')
    st = speedtest.Speedtest(secure=True)
    download_speed = str(math.floor(st.download()/1000000)) + "Mb/s"
    upload_speed = str(math.floor(st.upload()/1000000)) + "Mb/s"
    ping = str(st.results.ping) + "MS"
    upload_label.config(text=upload_speed)
    download_label.config(text=download_speed)
    ping_label.config(text=ping)


#code for cpu count
cpu_count_label = Label(root,font=("Orbitron",35,'bold'),text="0",bd=-4)
cpu_count_label.grid(row=0,column=0)
l1 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="CPUs")
l1.grid(row=1,column=0)


#cpu usage
cpu_usage_label = Label(root,font=("Orbitron",35,'bold'),text="0",bd=-4)
cpu_usage_label.grid(row=0,column=1)
l2 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="CPU Usage in %")
l2.grid(row=1,column=1)

#Total ram
ram_count_label = Label(root,font=("Orbitron",35,'bold'),text="0",bd=-4)
ram_count_label.grid(row=0, column=2)
l3 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Total RAM")
l3.grid(row=1,column=2)

#Ram % usage
ram_usage_label = Label(root,font=("Orbitron",35,'bold'),text="0",bd=-4)
ram_usage_label.grid(row=0, column=3)
l4 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Total RAM")
l4.grid(row=1,column=3)

#Available Ram
ram_avail_label = Label(root,font=("Orbitron",35,'bold'),text="0",bd=-4)
ram_avail_label.grid(row=0, column=4)
l5 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Available RAM")
l5.grid(row=1,column=4)

speed_button = Button(root,text="Test internet speed", command=internet_speed, width=15,height=3,font=("Orbitron",15,'bold'))
speed_button.grid(row=3,column=0)


download_label = Label(root,font=("Orbitron",35,'bold'),text="0 Mb/S",image=tk_image,compound='center',fg='#00ffff',bd=-4)
download_label.grid(row=3,column=1)
l6= Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Downlaod Speed")
l6.grid(row=4,column=1)

upload_label = Label(root,font=("Orbitron",35,'bold'),text="0 Mb/S",image=tk_image,compound='center',fg='#00ffff',bd=-4)
upload_label.grid(row=3,column=2)
l7= Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Upload Speed")
l7.grid(row=4,column=2)

ping_label = Label(root,font=("Orbitron",35,'bold'),text="0 Mb/S",image=tk_image,compound='center',fg='#00ffff',bd=-4)
ping_label.grid(row=3,column=3)
l8= Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Ping Speed")
l8.grid(row=4,column=3)

usage()

root.mainloop()