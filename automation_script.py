import pandas as pd
import os

# فعال کردن پشتیبانی از رنگ در ترمینال ویندوز
os.system('')

def red(text): 
    return text.replace(text, f"\033[91m{text}\033[0m") 
def green(text):
    return text.replace(text, f"\033[92m{text}\033[0m")
def yellow(text):
    return text.replace(text, f"\033[93m{text}\033[0m")

def convert_txt_to_csv(txt_file):
    """تبدیل فایل txt به csv"""
    csv_file = txt_file.replace('.txt', '.csv')
    try:
        with open(txt_file, 'r') as txt, open(csv_file, 'w') as csv:
            csv.write("Task,Priority\n")  # نوشتن هدر
            for line in txt:
                line = line.strip()
                if line:  # اگر خط خالی نبود
                    # فرض می‌کنیم فرمت: task,priority
                    csv.write(f"{line}\n")
        return csv_file
    except Exception as e:
        print(red(f"Error converting file: {e}"))
        return None




file_name=input("\nEnter the name of your file to sort : ")

if file_name.endswith('.txt'):
    file_name = convert_txt_to_csv(file_name)
    if not file_name:
        exit()


try:
    data = pd.read_csv(file_name)
    print("File loaded successfully!")
except FileNotFoundError:
    print("Error: 'data.csv' not found!")
    exit()

def sort_to_do_list():
    print(f"{'Task':<25} | {'Priority':<10}")
    print("-" * 60)
    for _, row in data.iterrows():
        if row['Priority']=="High":
             hight = red(f"{row['Task']:<25} | {row['Priority']:<10}")
             print(hight)
    for _, row in data.iterrows():
        if row['Priority']=="Medium":
             Medium = green(f"{row['Task']:<25} | {row['Priority']:<10}")
             print(Medium)
    for _, row in data.iterrows():
        if row['Priority']=="Low":
             Low = yellow(f"{row['Task']:<25} | {row['Priority']:<10}")
             print(Low)



sort_to_do_list()
