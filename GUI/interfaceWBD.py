import Climate.Temperature.GlobalWBD  as globalWBD

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from tkinter import ttk
from tkinter import messagebox as msg

import GUI.Smooth_Temperature as Smooth


def _msg():
    msg.showerror("Error", "Enter correct name!")


def WBD_TA_Country(placeHolder, countries):

    try :
        countries = countries.get().split(',')
        idx = 0
        for country in countries:
            countries[idx] = country.strip()
            idx += 1

        df = globalWBD.TemperatureByCountriesWBD(countries)
        figure = plt.Figure(figsize=(10, 6), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, placeHolder)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        #df.plot(x = 'Date', subplots=True,  ylabel='Temperature in degree celsius', ax=ax)
        Smooth.Get_Graph_Temperature(df , ax)
    except:
        _msg()
        return 0
    

def WBD_TA_State(placeHolder, country, states):
    
    states = states.get().split(',')
    idx = 0
    for state in states:
        states[idx] = state.strip()
        idx += 1

    df = globalWBD.TemperatureByStateWBD(country.get(), states)
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    #df.plot(x = 'Date', subplots=True,  ylabel='Temperature in degree celsius', ax=ax)
    Smooth.Get_Graph_Temperature(df , ax)
    
    

def stateBox(placeHolder, firstMessage, secondMessage, firstPos = 0):
    try :    
        stateName = tkinter.StringVar()
        countryName = tkinter.StringVar()

        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage)
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text="Enter Country Name ").grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=countryName).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text=secondMessage).grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=stateName).grid(
            column=1, row=1, padx=8, pady=4)

        b1 = tkinter.Button(f1, text="show", command=lambda : WBD_TA_State(placeHolder, countryName, stateName)).grid(
            row=2, columnspan=2, pady=2)
    except :
        _msg()


def countryBox(placeHolder, firstMessage, secondMessage, firstPos = 0):
    try :    
        countryName = tkinter.StringVar()

        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage)
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=countryName).grid(
            column=1, row=0, padx=8, pady=4)

        b1 = tkinter.Button(f1, text="show", command=lambda : WBD_TA_Country(placeHolder, countryName)).grid(
            row=1, columnspan=2, pady=2)
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

    countryBox(Tmp_analysis, "Country Analysis", "Enter Country Name", 0)
    countryBox(Tmp_analysis, "Countries Comparision", "Enter Countries Name (Comma Seperated)", 1)
    stateBox(Tmp_analysis, "State Analysis", "Enter State Name", 2)
    stateBox(Tmp_analysis, "States Comparision", "Enter States Name (Comma Seperated)", 3)

    win.mainloop()

if __name__ == "__main__":
    main()