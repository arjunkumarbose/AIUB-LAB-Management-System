import json
# Loading or saved file existing PC records
try:
    with open("pc_records.json", "r") as f:
        pc_records = json.load(f)
except FileNotFoundError:
    pc_records = {}

# Function to add a new PC to the records
def add_pc():
    pc_num = input("Enter PC number: ")
    if pc_num in pc_records:
        print("This PC number already exists.")
        action = input("Do you want to modify the existing PC information (M), remove it (R), or take no action (N)? ")
        if action.lower() == "m":
            update_pc(pc_num)
        elif action.lower() == "r":
            remove_pc(pc_num)
        else:
            return
    os_installed = input("Enter operating system installed: ")
    status = input("Enter status: ")
    pc_records[pc_num] = {"os_installed": os_installed, "status": status}
    print("PC added successfully.")

# Function to update an existing PC's information
def update_pc(pc_num):
    os_installed = input("Enter new operating system installed: ")
    status = input("Enter new status: ")
    pc_records[pc_num] = {"os_installed": os_installed, "status": status}
    print("PC information updated successfully.")

# Function to remove an existing PC from the records
def remove_pc(pc_num):
    del pc_records[pc_num]
    print("PC removed successfully.")

# Function to display all PC records
def display_all_pcs():
    if not pc_records:
        print("No PC records found.")
    else:
        print("PC number\tOS installed\tStatus")
        for pc_num, pc_info in pc_records.items():
            print(f"{pc_num}\t\t{pc_info['os_installed']}\t\t\t{pc_info['status']}")

# Function to display information for a specific PC
def display_pc(pc_num):
    if pc_num in pc_records:
        pc_info = pc_records[pc_num]
        print(f"PC number: {pc_num}")
        print(f"Operating system installed: {pc_info['os_installed']}")
        print(f"Status: {pc_info['status']}")
    else:
        print("PC not found.")
        action = input("Do you want to add this PC to the lab (Y/N)? ")
        if action.lower() == "y":
            add_pc()

# Function to search for a specific PC
def search_pc():
    pc_num = input("Enter PC number to search: ")
    display_pc(pc_num)

# Function to store all PC records in a file
def store_pcs():
    with open("pc_records.json", "w") as f:
        json.dump(pc_records, f)
    print("PC records saved successfully.")
