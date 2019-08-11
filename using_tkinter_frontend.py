import tkinter

window = tkinter.Tk()
window.geometry("1300x960")
window.title("GeoCoder Desktop App")
window.config(background="#00cc99")

app_title = tkinter.Label(window, text="GeoCoder App", background="#00cc99", foreground="white")
app_title.grid(row=0, column=0, sticky="w", padx=380)
app_title.config(font=("serif", 44))

description = tkinter.Label(window, text="Please upload a csv file which contains column address or Address", background="#00cc99", foreground="white")
description.grid(row=1, column=0, sticky="w", padx=200)
description.config(font=("serif", 22))

choose_file = tkinter.Button(window, text="Choose a file", width=10)
choose_file.grid(row=2, column=0, sticky="w", pady=20, padx=400)

choosed_file_txt = tkinter.Label(window, font=('serif', 15), background="#00cc99", foreground="white")
choosed_file_txt.grid(row=2, column=0, sticky="w", pady=20, padx=480)
choosed_file_txt.configure(relief="flat")

submitting = tkinter.Button(window, text="Submit", width=10)
submitting.grid(row=2, column=0, sticky="w", pady=20, padx=705)
