digits = 8  
prefix = "" # you can change this to whatever starting number you want
filename = "8.txt"

limit = 10 ** digits

print(f"start generation '{prefix}' {digits} digits in file {filename}...")

with open(filename, "w") as f:
    for i in range(limit):

        f.write(f"{prefix}{i:0{digits}d}\n")

print("done!")