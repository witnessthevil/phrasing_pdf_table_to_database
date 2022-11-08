import re


with open("/Users/danie/new_project_processing_diff_some_pdf_file/example.txt",'r') as r:
    file_content = r.read()
    page_four = "4 |   2020 World Population Data Sheet"
    page_end = "5 |   2020 World Population Data Sheet"
    
    try:
        page_four_start = file_content.find(page_four)
        page_four_end = file_content.find(page_end)
        target_data = file_content[page_four_start:page_four_end]
        print(target_data.replace(",",""))

    except:
        print("cannot find page four")

        

    #data_string = ""
    #for char in prettier_content[world_data_page_staet:world_data_page_end]:
    #    data_string += char
    #print(data_string)
        
    #print(file_content.replace("\n",''))