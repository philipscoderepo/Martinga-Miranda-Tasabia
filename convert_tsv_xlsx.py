import os
import csv
from xlsxwriter.workbook import Workbook

def convert_tsv_xlsx(directory):
    os.chdir(directory)

    for beds in os.listdir(directory):
        tsv_reader = csv.reader(open(beds, 'rt'), delimiter='\t')
        if beds.endswith(".tsv"):
            new_filename = beds.replace(".tsv",".xlsx")
            workbook = Workbook(new_filename)
            worksheet = workbook.add_worksheet()
            for row, data in enumerate(tsv_reader):
                worksheet.write_row(row, 0, data)
            workbook.close()