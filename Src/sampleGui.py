import tkinter as tk
import pandas as pd

vehicleRecords=pd.read_csv("vehicleData.csv")

window=tk.Tk()
labelTitle=tk.Label(text="License Plate Verification")
labelTitle.pack()
frame1=tk.Frame()
tk.Label(frame1,text="Enter image name:").grid(row=0, column=0)
entry1=tk.Entry(frame1)
entry1.grid(row=0, column=1)
frame1.pack()
textEntry=tk.Entry()
def disp():
    s1=vehicleRecords.loc[(vehicleRecords.RegNo==entry1.get())]
    name=s1.loc[0,'Name']
    textEntry.insert(0,name)
button1=tk.Button(text="Display", command=disp)
button1.pack()
textEntry.pack()


window.mainloop()
