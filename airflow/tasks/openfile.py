import re
from Logger import Logger
import time
import psutil

logger = Logger().get_logger(__name__)
# use perf counter to check for the most accurate solution
def select_data_page(file):
    with open(file,'r') as r:
        file_content = r.read()
        page_four = "4 |   2020 World Population Data Sheet"
        page_end = "21 |   2020 World Population Data Sheet"

        page_four_start = file_content.find(page_four)
        page_four_end = file_content.find(page_end)
        target_data = file_content[page_four_start:page_four_end].replace(",","").replace("\n\n","\n")
        data_lines = target_data.split("\n")
        return data_lines

def writing_2_file_to_csv(file):
    data_lines = select_data_page(file)
    targeted_table = []
    targeted_index = []
    for idx,line in enumerate(data_lines):
        counter = 0 
        for char in line:
            if char.isspace():
                counter += 1
        if counter >= 10:
            targeted_table.append(line)

    for i in targeted_table:
        for idx,char2 in enumerate(i):
            if char2.isdigit() or char2 == "—":
                targeted_index.append((i[:idx].strip(),i[idx:].replace(" ",",")))
                break
    final_list = list(map(lambda x: x[0] + "," + x[1],targeted_index))
     

    final_list_1 = [line for line in final_list if line.count(",") == 14]
    final_list_2 = [line for line in final_list if line.count(",") == 10]
    def writing_to_csv(file_name,list):
        with open(file_name,"a") as csvfile:
            for i in list:
                csvfile.write(i + '\n')
    logger.info("now writing the first csv file")
    writing_to_csv(*("/tmp/example1.csv",final_list_1))
    logger.info("now writing the second csv file")
    writing_to_csv(*("/tmp/example2.csv",final_list_2))
    logger.info("successfully load two file")

if __name__ == "__main__":
    logger.info("now performing the transforming part!")
    start_time = time.perf_counter()
    writing_2_file_to_csv("/Users/danie/new_project_processing_diff_some_pdf_file/example.txt")
    end_time = time.perf_counter()
    logger.info(f'Extract CPU usage {psutil.cpu_percent()}%')
    logger.info(f"writing pdf txt to csv have used {end_time - start_time}s")

            
        

   

                

        

    #data_string = ""
    #for char in prettier_content[world_data_page_staet:world_data_page_end]:
    #    data_string += char
    #print(data_string)
        
    #print(file_content.replace("\n",''))