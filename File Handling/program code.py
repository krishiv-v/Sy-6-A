try:
    with open("input.txt","r") as file:
        lines = file.readlines()

    total_lines = len(lines)

    first_two_lines = lines[:2]

    with open("output.txt","w") as file: 
        file.write(f"Total lines :{total_lines}\n")
        file.writelines(first_two_lines)
        
        print("Done output written to output.txt")

except FileNotFoundError:
    print("Error : input .txt not found")
    
