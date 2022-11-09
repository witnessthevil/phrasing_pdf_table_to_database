import re
import csv
import numpy as np
from collections import OrderedDict 
from Logger import Logger

logger = Logger(__name__)

with open("/Users/danie/new_project_processing_diff_some_pdf_file/example.txt",'r') as r:
    file_content = r.read().replace(",","").lower()

    # collect the table inside page 4
    page_four = "4 |   2020 World Population Data Sheet".lower()
    page_end = "5 |   2020 World Population Data Sheet".lower()
    
    page_four_start = file_content.find(page_four)
    page_four_end = file_content.find(page_end)
    target_data = file_content[page_four_start:page_four_end]
    # Since table all start with world in page 4
    line_list = target_data.split("\n")
    identifier = ["world","more developed","less developed","less developed (excluding china)","least developed","high income","middle income","upper middle income","lower middle income","low income"]
    table_line = []

    # extract line that only start with the identifier
    for line in line_list:
        for index in identifier:
            if line.startswith(index) and not line.isalpha():
                table_line.append(line)

    # remove the alpha character
    def extracting_number(line:str):
        number = ""
        for char in line:
            if char.isdigit() or char == "—" or char == "-" or char.isspace():
                number += char  
        return number
    
    # split the first half and second half for merging 
    final_list = np.array_split(list(map(lambda x: extracting_number(x).strip().replace(" ",","),table_line)),2)
    # remove duplicate
    final_list = list(map(lambda x: list(dict.fromkeys(x)),final_list))

    # write to csv
    with open("example.csv","w") as csvfile:
        for i in range(len(final_list[0])):
            if i <= len(final_list[1]) - 1:
                line = identifier[i] + "," + final_list[0][i] + "," + final_list[1][i] 
                csvfile.write(line + "\n")