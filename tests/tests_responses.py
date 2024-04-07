file_name = "tests/test_id.txt"

def save_UID(UID):
    try:
        with open(file_name, 'w') as file:
            file.write(UID)
        print(f"Data written to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def get_UID():
    try:
        with open(file_name, 'r') as file:
            print("inside get")
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None
    

if __name__ == "__main__" : 
    save_UID("NA")
    print(get_UID())
