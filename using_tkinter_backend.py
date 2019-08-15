from using_tkinter_frontend import *
from tkinter import filedialog
import pandas
from geopy.geocoders import ArcGIS


filename = ""
df = None
variable = None

var = tkinter.StringVar()
var.set("Choose a CSV file")
r = 0


def load_csv():
    global df, filename, r
    if "Address" in df or "address" in df:
        colored = tkinter.Label(window, background="#00cc99")
        colored.grid(row=4, column=0, sticky="news", padx=300)
        r = 0
        c = 300
        geolocator = ArcGIS()
        df["Longitude"] = None
        df["Latitude"] = None
        i = 0
        for Address, City, State, Country in zip(df["Address"], df["City"], df["State"], df["Country"]):
            loc = geolocator.geocode(Address + City + State + Country)
            df["Longitude"][i] = "{0:.3f}".format(loc.longitude)
            df["Latitude"][i] = "{0:.3f}".format(loc.latitude)
            i += 1

        for col in df:
            # for row in col:
            label = tkinter.Label(window, width=10, height=2,
                                  text=col, relief=tkinter.RIDGE)
            label.grid(row=r+3, column=0, sticky="w", padx=c)
            for num in df[col]:
                r += 1
                label = tkinter.Label(window, width=10, height=2,
                                      text=num, relief=tkinter.RIDGE)
                label.grid(row=r+3, column=0, sticky="w", padx=c)
            r = 0
            c += 75
        download_button = tkinter.Button(window, text="Download", width=10, command=download)
        download_button.grid(row=len(df.index)+4, column=0, sticky="w", padx=550, pady=10)
    else:
        for color in range(20):
            coloring = tkinter.Label(window, background="#00cc99")
            coloring.grid(row=color+3, column=0, sticky='news')
        new = tkinter.Label(window, text="Please upload a file which contains \"Address\"column",
                            background="#00cc99", foreground="White")
        new.grid(row=4, column=0, sticky="w", padx=300)
        new.config(font=("serif", 20))


def choose():
    try:
        global filename, variable
        global df, var
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("text files", "*.csv"),
                                              ("all files", "*.*")))
        df = pandas.read_csv(filename)
        variable = filename.split("/")[-1]
        var.set(variable)

    except FileNotFoundError:
        pass


def download():
    filename1 = filedialog.asksaveasfile(initialdir="/", title="Select file", filetypes=(("text files", "*.csv"),
                                                                                        ("all files", "*.*")))
    df.to_csv(filename1.name + ".csv")
    success = tkinter.Label(window, text="File saved successfully. You can see it in\n{} folder".format(filename1.name),
                            background="#00cc99", foreground="white")
    success.grid(row=len(df.index)+5, column=0, sticky="w", padx=400)
    success.config(font=("serif", 20))


def submit():
    try:
        load_csv()
    except:
        label = tkinter.Label(window, text="Please check your internet connection.", background="#00cc99", foreground="white")
        label.grid(row=r+4, column=0, sticky="w", padx=400)
        label.config(font=("serif", 20))


submitting.configure(command=submit)
choose_file.configure(command=choose)
choosed_file_txt.configure(textvariable=var)
window.mainloop()
