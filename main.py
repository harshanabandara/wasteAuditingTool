import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import os
import csv
from csv import writer
import pathlib
import pandas as pd


def loadHistory():
    pass


def loadWasteMaterialTypes():
    with open('wasteMaterial') as f:
        lines = f.read().splitlines()
    return lines


def addWasteMaterialType(wasteMaterial):
    with open('wasteMaterial', 'a') as f:
        f.write(wasteMaterial)


def loadDumpLocations():
    with open('dumpLocation') as f:
        lines = f.read().splitlines()
    return lines


def addDumpLocation(dumpLocation):
    pass


def loadDisposalMethods():
    with open('disposalMethods') as f:
        lines = f.read().splitlines()
    return lines


def addDisposalMethod(disposalMethod):
    pass


def writeToCSV(dict):
    print(dict)
    headers = ["Type", "Waste Material", "Quantity", "Unit", "Date", "Dump Location", "Disposal Method"]
    if not os.path.exists('data.csv'):
        with open('data.csv', 'w') as f:
            dw = csv.DictWriter(f, delimiter=',', fieldnames=headers)
            dw.writeheader()
    print(';(')
    with open('data.csv', 'a') as f:
        dw = csv.DictWriter(f, fieldnames=headers)
        dw.writerow(dict)


def loadCSV():
    pass


def save():
    if validate():
        print('saved')
        data = {
            "Type": clickedAT.get(),
            "Waste Material": clickedWM.get(),
            "Quantity": qty.get(),
            "Unit": unit.get(),
            "Date": dateEntry.get(),
            "Dump Location": clickedDL.get(),
            "Disposal Method": clickedDM.get()}
        writeToCSV(data)
    else:
        print("Invalid data")


def validate():
    # dateEntry.validate()
    if dateEntry.validate() and True:
        return True
    return False


def validateQty():
    qty_ = qtyEntry.get()
    if qty_:
        try:
            if float(qty_):
                return True
        except ValueError:
            qty = ""
            return False


if __name__ == '__main__':
    window = tk.Tk()
    s = ttk.Style(window)
    s.theme_use('clam')
    print("hello")

    window.geometry("1080x720")
    window.maxsize(1080, 720)
    window.minsize(1080, 720)

    window.title("Waste Auditing Tool")

    auditTypes = ["Construction", "Demolition"]
    clickedAT = tk.StringVar()
    clickedAT.set(auditTypes[0])
    auditTypeDropDown = tk.OptionMenu(window, clickedAT, *auditTypes)
    auditTypeDropDown.configure(width=30, justify="left", anchor="w")
    # wasteMaterialDropDown.pack(pady=10, padx=10)
    auditTypeLabel = tk.Label(window, text="Select this", width=20, justify="left", anchor="w")
    auditTypeLabel.grid(row=0, column=0, padx=2, pady=10, sticky="w")
    auditTypeDropDown.grid(row=0, column=1, pady=10, sticky="w")

    wasteMaterialTypes = loadWasteMaterialTypes()
    clickedWM = tk.StringVar()
    clickedWM.set(wasteMaterialTypes[0])
    wasteMaterialDropDown = tk.OptionMenu(window, clickedWM, *wasteMaterialTypes)
    wasteMaterialDropDown.configure(width=30, justify="left", anchor="w")
    # wasteMaterialDropDown.pack(pady=10, padx=10)
    wasteMaterialLabel = tk.Label(window, text="Waste Material", width=20, justify="left", anchor="w")
    wasteMaterialLabel.grid(row=1, column=0, padx=2, pady=10, sticky="w")
    wasteMaterialDropDown.grid(row=1, column=1, pady=10, sticky="w")

    qty = tk.StringVar()
    qtyLabel = tk.Label(window, text="Quantity", width=20, justify="left", anchor="w")
    qtyEntry = tk.Entry(textvariable=qty, width=30, validate="focusout", validatecommand=validateQty)
    qtyLabel.grid(row=2, column=0, padx=2, pady=10, sticky="w")
    qtyEntry.grid(row=2, column=1, pady=10, sticky="w")

    unit = tk.StringVar()
    unitLabel = tk.Label(window, text="Unit", width=20, justify="left", anchor="w")
    unitEntry = tk.Entry(textvariable=unit, width=30)
    unitLabel.grid(row=3, column=0, padx=2, pady=10, sticky="w")
    unitEntry.grid(row=3, column=1, pady=10, sticky="w")

    date = tk.StringVar()
    dateLabel = tk.Label(window, text="Date", justify="left", anchor="w")
    # dateEntry = tk.Entry(textvariable=date)
    dateEntry = DateEntry(window, width=30, date_pattern='dd/mm/yyyy')

    dateLabel.grid(row=4, column=0, padx=2, pady=10, sticky="w")
    dateEntry.grid(row=4, column=1, pady=10, sticky="w")

    dumpLocations = loadDumpLocations()
    clickedDL = tk.StringVar()
    clickedDL.set(dumpLocations[0])
    dumpLocationDropDown = tk.OptionMenu(window, clickedDL, *dumpLocations)
    dumpLocationDropDown.configure(width=30, justify="left", anchor="w")
    dumpLocationLabel = tk.Label(window, text="Dump Location", width=20, justify="left", anchor="w")
    dumpLocationLabel.grid(row=5, column=0, padx=2, pady=10, sticky="w")
    dumpLocationDropDown.grid(row=5, column=1, pady=10, sticky="w")

    disposalMethods = loadDisposalMethods()
    clickedDM = tk.StringVar()
    clickedDM.set(disposalMethods[0])
    disposalMethodDropDown = tk.OptionMenu(window, clickedDM, *disposalMethods)
    disposalMethodDropDown.configure(width=30, justify="left", anchor="w")
    disposalMethodLabel = tk.Label(window, text="Disposal Method", width=30, justify="left", anchor="w")
    disposalMethodLabel.grid(row=6, column=0, padx=2, pady=10, sticky="w")
    disposalMethodDropDown.grid(row=6, column=1, pady=10, sticky="w")

    saveBtn = tk.Button(window, command=save, text="save")
    saveBtn.grid(row=8, column=3, columnspan=3)

    window.mainloop()
