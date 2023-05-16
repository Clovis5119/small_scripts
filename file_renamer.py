import os

# Directory of files to be renamed
path = "D:/Music Production/Samples/Choirs/Choir - Fadeouts (FX)"

# Program will keep string before or after this one
cutoff = "Key"
before_cutoff = 0

# Program replaces the rest with this string
new_text = "Choir - Fadeouts (FX)"

# Cycles through files in the directory
for item in os.listdir(path):
    key = item.split(cutoff)[1]
    new_name = new_text + key

    # Needed to make os.rename work
    old_file = os.path.join(path, item)
    new_file = os.path.join(path, new_name)

    print(f"Renaming {item}", end="... ")
    os.rename(old_file, new_file)
    print("Done")
