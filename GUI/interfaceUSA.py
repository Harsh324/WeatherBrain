from Climate.Temperature.USA  import TemperatureAnalysisUS as USA

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from tkinter import ttk
from tkinter import messagebox as msg
import GUI.Smooth_Temperature as Smooth

def _msg():
    msg.showerror("Error", "Enter correct name!")


def USA_TA_City(placeHolder, cities, month, day):

    cities = cities.get().split(',')
    idx = 0
    subplotsCondition = True
    for city in cities:
        cities[idx] = city.strip()
        idx += 1
    if len(cities) == 1:
        cities = cities[0]
        # subplotsCondition = True

    month = month.get()
    if not month:
        month = 0
    day = day.get()
    if not day:
        day = 0
        
    df = USA().citiesAnalysis(cities, month, day)
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    #df.plot(x = 'Date', subplots=subplotsCondition,  ylabel='Temperature in degree celsius', ax=ax)
    Smooth.Get_Graph_Temperature_SubTrue_Global(df , ax)
    

def cityBox(placeHolder, firstMessage, secondMessage, firstPos = 0):
    try :    
        cities = tkinter.StringVar()
        month = tkinter.StringVar()
        day = tkinter.IntVar()
        
        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage)
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=cities).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text="Enter month (Leave blank to take all data)").grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=1, padx=8, pady=4)

        l3 = tkinter.Label(f1, text="Enter day (Leave blank to take all data)").grid(
            column=0, row=2, padx=8, pady=4)

        e3 = tkinter.Entry(f1, textvariable=day).grid(
            column=1, row=2, padx=8, pady=4)

        b1 = tkinter.Button(f1, text="show", command=lambda : USA_TA_City(placeHolder, cities, month, day)).grid(
            row=3, columnspan=2, pady=2)
    except :
        _msg()


def main():

    win = tkinter.Tk()
    win.title("Python Mini Project")


    tabcontrol = ttk.Notebook(win)
    about = ttk.Frame(tabcontrol)
    tabcontrol.add(about, text="About")

    Tmp_analysis = ttk.Frame(tabcontrol)
    tabcontrol.add(Tmp_analysis, text="Temperature Analysis")

    tabcontrol.pack(expand=1, fill="both")
    cityBox(Tmp_analysis, "City Analysis", "Enter city Name", 0)
    cityBox(Tmp_analysis, "Cities Comparision", "Enter cities Name (Comma Seperated)", 1)

    win.mainloop()


if __name__ == "__main__":
    main()