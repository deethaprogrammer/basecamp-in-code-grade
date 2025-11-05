import sys

valid_lines = []
corrupt_lines = []

def read_csv_as_string_list(filepath: str) -> list:
    """
    Reads a CSV file and returns a list of strings,
    each representing a row (excluding the first row which is the header).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines[1:]:
        cleaned_line = line.strip()
        cleaned_lines.append(cleaned_line)
    return cleaned_lines

def is_valid_postcode(postcode: str) -> bool:
    """
    Validates Dutch postcode format using basic loops and string checks.
    Format: 4 digits followed by 2 uppercase letters (optional space allowed).
    """
    for i in range(4):
        if postcode[i].isdigit():
            continue
        else:
            return False
    for j in range(4,6):
        if postcode[j].isalpha():
            return True
        else:
            return False
    # todo: finish the implementation
    pass

def is_positive(value: str) -> bool:
    """
    Checks if the value is a positive non-zero float.
    """    
    try:
        return float(value) > 0
        
    except ValueError:
        return False
    # todo: finish the implementation
    
    pass

def valid_name(name: str) -> bool:
    return name.replace(" ", "").isalpha()

def filter_data(rows: list) -> None:
    """
    Processes the rows extracted from the input file, checks all the requested validity conditions 
    and fills valid_lines and corrupt_lines.
    """
    for row in rows:
        values = row.split(",")
        problem = []

        if not valid_name(values[0]) or not valid_name(values[1]):
            problem.append("Invalid sender name")

        if not valid_name(values[2]) or not valid_name(values[3]):
            problem.append("Invalid receiver name")
        
        for k, label in zip([4, 5, 6, 7], ["weight", "length", "width", "height"]):
            if not is_positive(values[k]):
                problem.append(f"invalid {label}")
                
        if not is_valid_postcode(values[10]):
            problem.append("invalid postcode")
        
        if problem:
            corrupt_lines.append(f"{row} \n --> {'; '.join(problem)}")
            
        else: valid_lines.append(row)
        # todo: finish the implementation
    pass

def is_valid_print():
    print("### VALID LINES ###")
    for i in range(len(valid_lines)):
        print(valid_lines[i])
        
def organise_packages_by_postcode(valid_rows)->None:
    """
    For each valid package row:
    - Calculates volume: Length * Width * Height
    - Creates a tuple: (postcode, street + house number, volume)
    - Prints all triples for reporting
    """
    is_valid_print()
    
    package_groups = []
    for row in valid_rows:
        split = row.split(",")
        volume = float(split[5]) * float(split[6]) * float(split[7])
        postcode = split[10].strip().upper()
        street_housenumber = f'{split[8]} {split[9]}'
        formvolume = f'{volume:.2f}'
        package_groups.append((postcode, street_housenumber, formvolume))
    print("--- Grouped Packages by Postcode ---")
    for postcode, street_housenumber, volume in package_groups:
        print(f'Postcode: {postcode}, Address: {street_housenumber}, Volume: {volume}')
    # todo: finish the implementation
    pass

def report_corrupt_data()->None:
    """
    Prints all corrupt rows with their issues.
    """
    print('### CORRUPT LINES ###')
    for i in range(len(corrupt_lines)):
        print(corrupt_lines[i])
    # todo: finish the implementation
    pass

def main():
    # Define the file path relative to the script
    filename = __file__.replace("\\", "/").rsplit("/", 1)[0] + "/packages.csv" # Replace with your actual CSV filename
    # Step 1: Read and clean the data
    rows = read_csv_as_string_list(filename)
    # Step 2: Polish and validate the data
    filter_data(rows)
    # Step 3: Report valid lines and group packages
    organise_packages_by_postcode(valid_lines)
    # Step 4: Report corrupt lines
    report_corrupt_data()

if __name__ == "__main__":
    main()