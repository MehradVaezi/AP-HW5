from pathlib import Path
import os


def create_dir(name, address):
    if not os.path.exists(f"{address}/{name}"):
        os.mkdir(f"{address}/{name}")
    else:
        print("Such Directory Exists!")

def create_file(name, address): ### RIGHT::: 'test.txt' / WRONG::: 'test' ###
    if not os.path.exists(f"{address}/{name}"):
        with open(f"{address}/{name}", "w+") as f:
            f.close()
    else:
        print("Such File Exists!")

def find(name, address):
    print(f"Paths Containing '{name}' are: ")
    print(sorted(Path(str(address)).glob(f"**/{name}*")))
    # Use the FULL file's name 
    # including its type and extensions:
    # RIGHT::: 'main.py' & 'test.txt' & 'result.pdf'
    # WRONG::: 'main'    & 'test'      & 'result'

def delete(name, address):  ### RIGHT::: 'test.txt' / WRONG::: 'test' ###
    if os.path.exists(f"{address}/{name}"):
        os.remove(f"{address}/{name}")
    else:
        print("Such File Does NOT Exist!")
    
def delete_dir(name, address):
    if os.path.exists(f"{address}/{name}"):
        os.rmdir(f"{address}/{name}")
    else:
        print("Such Directory Does NOT Exist!")