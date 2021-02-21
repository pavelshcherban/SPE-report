import os
from pyWinSpec.winspec import SpeFile, Header
from tkinter import filedialog
import tkinter as tk
import csv

class SpeReport:

    def read_files(self, filename):
        spefile = SpeFile(filename)
        head = {'filename':filename}
        for field_name, field_type in spefile.header._fields_:
            print(field_name, getattr(spefile.header, field_name))
            head[field_name] = getattr(spefile.header, field_name)
        self.headers.append(head)

    def select_files(self):
        dirname = filedialog.askdirectory(
            initialdir=".",
            title="Select a Directory",
            mustexist = tk.TRUE,
        )
        for subdir, dirs, files in os.walk(dirname):
            for filename in files:
                filepath = subdir + os.sep + filename
                if filepath.endswith(".SPE") or filepath.endswith(".spe"):
                    print(filepath)
                    self.read_files(filepath)

    def headers_to_csv(self):
        csv_file = "spereport.csv"
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.csv_columns, lineterminator='\n')
            writer.writeheader()
            for data in self.headers:
                writer.writerow(data)
    
    def set_csv_columns(self):
        self.csv_columns = ['filename']
        for field_name, field_type in Header._fields_:
            self.csv_columns.append(field_name)

    def __init__(self) -> None:
        self.headers = []
        self.select_files()
        self.set_csv_columns()
        self.headers_to_csv()
        pass

SpeReport()