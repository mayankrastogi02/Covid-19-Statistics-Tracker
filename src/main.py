# student name: Mayank Rastogi
# student number: 74196783

# covid simple dashboard app

# imports
import string
from matplotlib import colors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from covid import Covid


from tkinter import *

import matplotlib
from numpy import column_stack
from pyparsing import col
matplotlib.use("TkAgg")


class CovidStatManager:

    def __init__(self, master):
        """ Constructor for the class"""
        self.master = master
        window.geometry("950x500")
        window.title("Covid Data Visualization")

    def getMasterCovidData() -> list:
        """ this function is called once to get the master data for 
            this application; 
            all data used in this application is derived from data 
            returned by this function
        """
        # covid = Covid()  # instantiate
        covid = Covid(source="worldometers")
        # Data is being received from worldometers
        data = covid.get_data()
        return data

    def getConfirmed(data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
            list of (country, confirmed) data
        """
        confirmed = []
        for i in data1:
            confirmed.append((i["country"], i["confirmed"]))
        #print("DEBUG: confirmed is ", confirmed)
        return confirmed

    def getActive(data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
            list of (country, active) data
        """
        active = []
        for i in data1:
            active.append((i["country"], i["active"]))
        # print("DEBUG: active is ", active)
        return active

    def getDeath(data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
            list of (country, death) data
        """
        death = []
        for i in data1:
            death.append((i["country"], i["deaths"]))
        # print("DEBUG: death is ", death)
        return death

    def getRecovered(data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
            list of (country, recovered) data
        """
        recovered = []
        for i in data1:
            recovered.append((i["country"], i["recovered"]))
        # print("DEBUG: recovered is ", recovered)
        return recovered

    def getCountries(data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
            list of (country, confirmed, deaths, recovered, active) data
        """
        country_data = []
        for i in data1:
            country_data.append((i["country"], i["confirmed"],
                                 i["deaths"], i["recovered"], i["active"]))
        # print("DEBUG: countries is ", country_data)
        # top10_countries ontains the top 10 countries. Countries start from index 8 in masterData
        top10_countries = [country_data[i] for i in range(8, 18)]
        return top10_countries

    def getWorld(data1: list) -> list:
        """ this function uses the masterdata data1 and returns a 
            list of (country, confirmed, deaths, recovered, active) data
        """
        countries = []
        for i in data1:
            countries.append((i["country"], i["confirmed"],
                             i["deaths"], i["recovered"], i["active"]))
        # print("DEBUG: countries is ", countries)
        # top10_with_world contains the top 10 entries from masterData. This data also contains the World statistics
        top10_with_world = [countries[i] for i in range(0, 10)]
        return top10_with_world

    def plotConfirmed(self):
        """ a callback function for the button;
            plots a histogram of the top 10 confirmed cases 
        """
        global plotted, canvas
        if plotted:
            self.clear()  # If a pre-existing graph is plotted, clear the canvas
        fig = Figure(figsize=(8, 5))
        plot1 = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=window)

        top10 = [self.confirmed[i] for i in range(8, 18)]
        # print("DEBUG: top10", top10)
        x = [top10[i][0] for i in range(10)]  # x contains the country names
        # y contains the number of confirmed cases
        y = [top10[i][1] for i in range(10)]
        plot1.bar(x, y, color='yellow')

        for tick in plot1.get_xticklabels():  # rotate the text slightly
            tick.set_rotation(15)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, rowspan=5000, columnspan=5000, padx=20)
        plotted = True

    def plotActive(self):
        """ a callback function for the button;
            plots a histogram of the top 10 active cases 
        """
        global plotted, canvas
        if plotted:
            self.clear()
        fig = Figure(figsize=(8, 5))
        plot2 = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=window)
        # canvas = FigureCanvasTkAgg(frame_right, fig)

        top10 = [self.active[i] for i in range(8, 18)]
        # print("DEBUG: top10", top10)
        x = [top10[i][0] for i in range(10)]  # x contains the country names
        # y contains the number of active cases
        y = [top10[i][1] for i in range(10)]
        plot2.bar(x, y, color='lightblue')

        for tick in plot2.get_xticklabels():  # rotate the text slightly
            tick.set_rotation(15)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, rowspan=5000, columnspan=5000, padx=20)
        plotted = True

    def plotDeath(self):
        """ a callback function for the button;
            plots a histogram of the top 10 death cases 
        """
        global plotted, canvas
        if plotted:
            self.clear()
        fig = Figure(figsize=(8, 5))
        plot3 = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=window)

        top10 = [self.death[i] for i in range(8, 18)]
        # print("DEBUG: top10", top10)
        x = [top10[i][0] for i in range(10)]    # x contains the country names
        # y contains the number of death cases
        y = [top10[i][1] for i in range(10)]
        plot3.bar(x, y, color='red')

        for tick in plot3.get_xticklabels():  # rotate the text slightly
            tick.set_rotation(15)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, rowspan=5000, columnspan=5000, padx=20)
        plotted = True

    def plotRecovered(self):
        """ a callback function for the button;
            plots a histogram of the top 10 recovered cases 
        """
        global plotted, canvas
        if plotted:
            self.clear()
        fig = Figure(figsize=(8, 5))
        plot4 = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=window)
        # canvas = FigureCanvasTkAgg(frame_right, fig)

        top10 = [self.recovered[i] for i in range(8, 18)]
        # print("DEBUG: top10", top10)
        x = [top10[i][0] for i in range(10)]  # x contains the country names
        # y contains the number of recovered cases
        y = [top10[i][1] for i in range(10)]
        plot4.bar(x, y, color='green')

        for tick in plot4.get_xticklabels():  # rotate the text slightly
            tick.set_rotation(15)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, rowspan=5000, columnspan=5000, padx=20)
        plotted = True

    def plotAllStats(self):
        """ a callback function for the button;
            plots a pie chart of the status of a country 
        """
        try:
            # gets the country from the OptionMenu
            index = top10_countries.index(list_menu.get())
            global plotted, canvas
            if plotted:
                self.clear()
            fig = Figure(figsize=(8, 5))
            plot4 = fig.add_subplot(111)
            canvas = FigureCanvasTkAgg(fig, master=window)

            top10 = [self.countries[i] for i in range(10)]
            # print("DEBUG: top10", top10)
            x = []  # list contains the values of the status
            for j in range(4):
                x.append(top10[index][j+1])
            # print("DEBUG: Country x is: ", x)
            y = ["Confirmed", "Deaths", "Recovered", "Active"]
            labels = []  # list containing strings of the form status: value
            for i in range(4):
                str_var = y[i] + ": " + str(x[i])
                labels.append(str_var)
            # print("DEBUG: labels is: ", labels)
            plot4.pie(x, labels=labels, startangle=90, colors=[
                'yellow', 'red', 'green', 'lightblue'], explode=(0, 0, 0, 0), autopct="%1.1f%%")

            for tick in plot4.get_xticklabels():  # rotate the text slightly
                tick.set_rotation(15)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=1, rowspan=5000, columnspan=5000, padx=20)
            plotted = True
        except ValueError:
            # If no option is selected from the OptionMenu, a pop up window is displayed
            top = Toplevel(window)
            top.geometry("300x80")
            top.title("Error Window")
            Label(top, text="Please select a country first!").grid(
                row=0, column=0, padx=60)
            exit_button = Button(
                top, text="Exit", command=top.destroy, bg="red")
            exit_button.grid(row=1, column=0, padx=60)

    def plotWorldStats(self):
        """ a callback function for the button;
            plots a pie chart of the world status 
        """
        # print("DEBUG country name is: ", country_name)
        world_data = [self.all_countries[i][0] for i in range(0, 10)]
        # print("All countries is: ", world_data)
        index = world_data.index('World')
        # print("Index is: ", index)
        global plotted, canvas
        if plotted:
            self.clear()
        fig = Figure(figsize=(8, 5))
        plot4 = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=window)
        x = []  # list contains the values of the status
        for j in range(4):
            x.append(self.all_countries[index][j+1])
        # print("DEBUG: Country x is: ", x)
        y = ["Confirmed", "Deaths", "Recovered", "Active"]
        labels = []  # list containing strings of the form status: value
        for i in range(4):
            str_var = y[i] + ": " + str(x[i])
            labels.append(str_var)
        # print("DEBUG: labels is: ", labels)
        plot4.pie(x, labels=labels, startangle=90, colors=[
            'yellow', 'red', 'green', 'lightblue'], explode=(0, 0, 0, 0), autopct="%1.1f%%")

        for tick in plot4.get_xticklabels():  # rotate the text slightly
            tick.set_rotation(15)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, rowspan=5000, columnspan=5000, padx=20)
        plotted = True

    def clear(self):
        """ a callback for the Clear button """
        global plotted, canvas
        if plotted:
            canvas.get_tk_widget().destroy()
            plotted = False

    # program starts here
    # get masterData
    masterData = getMasterCovidData()
    # print("Data: ", masterData)
    #print("DEBUG: type(masterData) is", type(masterData))
    confirmed = getConfirmed(masterData)
    #print("DEBUG: type(confirmed) is", type(confirmed))
    active = getActive(masterData)
    #print("DEBUG: type(confirmed) is", type(active))
    death = getDeath(masterData)
    #print("DEBUG: type(confirmed) is", type(death))
    recovered = getRecovered(masterData)
    #print("DEBUG: type(confirmed) is", type(recovered))
    countries = getCountries(masterData)
    #print("DEBUG: type(confirmed) is", type(recovered))
    all_countries = getWorld(masterData)
    #print("DEBUG: type(confirmed) is", type(recovered))


# instantiate the main window
window = Tk()
window.config(bg="#5d8bbb")
# Defining an object of the class
covid_object = CovidStatManager(window)
plotted = False

label = Label(
    window, text="Click on a button to see", bg="#5d8bbb", font=("Calibri", 12))
label.grid(row=0, column=0)

labe3 = Label(
    window, text="the status-wise statistics", bg="#5d8bbb", font=("Calibri", 12))
labe3.grid(row=1, column=0, pady=(0, 10))

# Button to show the confirmed cases plot
cofirmed_button = Button(
    master=window,
    command=lambda: covid_object.plotConfirmed(),
    height=2,
    width=22,
    bg="yellow",
    text="Plot: Top 10 CONFRIMED").grid(row=3, column=0, pady=(5, 0))

# Button to show the active cases plot
active_button = Button(
    master=window,
    command=lambda: covid_object.plotActive(),
    height=2,
    width=22,
    bg="lightblue",
    text="Plot: Top 10 ACTIVE").grid(row=4, column=0)

# Button to show the deaths cases plot
death_button = Button(
    master=window,
    command=lambda: covid_object.plotDeath(),
    height=2,
    width=22,
    bg="red",
    text="Plot: Top 10 DEATHS").grid(row=5, column=0)

# Button to show the recovered cases plot
recovered_button = Button(
    master=window,
    command=lambda: covid_object.plotRecovered(),
    height=2,
    width=22,
    bg="green",
    text="Plot: Top 10 RECOVERED").grid(row=6, column=0)

# Button to clear the plot from the canvas
clear_button = Button(
    master=window,
    command=lambda: covid_object.clear(),
    height=2,
    width=22,
    text="Clear Graph").grid(row=7, column=0)

labe2 = Label(
    window, text="Or choose a country to see", bg="#5d8bbb", font=("Calibri", 12))
labe2.grid(row=8, column=0, pady=(10, 0))
labe4 = Label(
    window, text="the country-wise statistics: ", bg="#5d8bbb", font=("Calibri", 12))
labe4.grid(row=9, column=0)

list_menu = StringVar(window)
list_menu.set("Choose country")  # default value

top10_countries = [covid_object.countries[i][0] for i in range(10)]
# print("DEBUG countries is: ", top10_countries)
option = OptionMenu(window, list_menu, *top10_countries).grid(row=10,
                                                              column=0, pady=(5, 10))

# Button to show the country cases pie chart
country_button = Button(
    master=window,
    command=lambda: covid_object.plotAllStats(),
    height=2,
    width=22,
    bg="orange",
    text="Show Country statistics").grid(row=11, column=0)

# Button to show the world cases pie chart
world_button = Button(
    master=window,
    command=lambda: covid_object.plotWorldStats(),
    height=2,
    width=22,
    bg="cyan",
    text="Show World statistics").grid(row=12, column=0)

# Button to clear the pie chart from the canvas
clear_button = Button(
    master=window,
    command=lambda: covid_object.clear(),
    height=2,
    width=22,
    text="Clear Chart").grid(row=13, column=0)

window.mainloop()
