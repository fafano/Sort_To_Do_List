from tabulate import tabulate
import pandas as pd
from datetime import datetime
import os

os.system('')

def colorize(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def red(text): return colorize(text, 91)
def green(text): return colorize(text, 92)
def yellow(text): return colorize(text, 93)
def blue(text): return colorize(text, 94)

def sort_to_do_list(data):
    tasks = []
    for _, row in data.iterrows():
        task = row['Task']
        priority = row['Priority']
        if priority == "High":
            task = red(task)
            priority = red(priority)
            tasks.append([task, priority])
    for _, row in data.iterrows():
        task = row['Task']
        priority = row['Priority']
        if priority == "Medium":
            task = green(task)
            priority = green(priority)
            tasks.append([task, priority])
    for _, row in data.iterrows():
        task = row['Task']
        priority = row['Priority']
        if priority == "Low":
            task = yellow(task)
            priority = yellow(priority)
            tasks.append([task, priority])
    
    headers = [blue("Task"), blue("Priority")]
    print(tabulate(tasks, headers=headers, tablefmt="grid"))

file_name = input("\nEnter the name of your file to sort: ")

try:
    data = pd.read_csv(file_name)
    print(green("File loaded successfully!"))
except FileNotFoundError:
    print(red("Error: File not found!"))
    exit()
def show_stats(data):
    counts = data['Priority'].value_counts()
    print(f"\n{blue('Task Statistics:')}")
    print(f"High: {red(str(counts.get('High', 0)))}")
    print(f"Medium: {green(str(counts.get('Medium', 0)))}")
    print(f"Low: {yellow(str(counts.get('Low', 0)))}")

sort_to_do_list(data)
show_stats(data)
print(f"\nLast updated: {blue(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")