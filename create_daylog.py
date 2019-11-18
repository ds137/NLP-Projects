import os
import sys
import time

def get_day(value):
    value -= 1
    if(value > 4 or value < 0):
        return None
    days_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return days_array[value]

def create_file():
    today_date = str(time.strftime("%d %B %Y"))
    file_date_name = str(time.strftime("%d-%m-%Y"))

    gen_obj = os.walk(".") # access current directory
    files_arr = []
    inner_files = None

    for val in gen_obj:
        files_arr.append(val)

    recent_folder = "Week {}".format(len(files_arr) - 1)
    for root, dirs, files in os.walk("{}/{}".format(os.getcwd() , recent_folder)):
        inner_files = files

    week_num = len(files_arr[0][1])
    number_entries = len(inner_files)

    if(week_num == 0):
        # if no files or folders exist
        # then create the first folder
        os.mkdir("Week 1")
        week_num = 1
        number_entries = 0

    if(number_entries == 5):
        # If 5 files already exist in the most recent folder
        # Create a new folder add files to.
        os.mkdir("Week {}".format(week_num + 1))
        week_num += 1
        number_entries = 0

    file_name = "Week {}\\{}.txt".format(week_num, file_date_name)
    try:
        txt_file = open(file_name,'a')
        txt_file.write("=========================\n{} {}\n=========================\n".format(get_day(number_entries + 1), today_date))
        txt_file.close()
        os.startfile(file_name)
        return
    except:
        print("Error")
        sys.exit(0)

# main function
def main():
    create_file()
    return

if __name__ == '__main__':
    main()
