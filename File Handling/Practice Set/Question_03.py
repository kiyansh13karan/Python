# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder 



import os

# Create a folder for the files
folder_name = "Multiplication-Tables"
os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist

# Generate tables from 2 to 20
for i in range(2, 21) :
    filename = f"Table-of-{i}.txt"
    filepath = os.path.join(folder_name, filename)

    with open(filepath, "w") as f :
        f.write(f"Multiplication Table of {i}\n")
        f.write("-" * 25 + "\n")
        for j in range(1, 11) :
            f.write(f"{i} x {j} = {i*j}\n")

print(f"All multiplication tables saved in '{folder_name}' folder.")
