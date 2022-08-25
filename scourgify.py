import sys              # for argv and exit
import csv              # for csv handling

def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")                     # checks whether argument passes enough arguments
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")                      # checks whether argument passes enough arguments
        elif sys.argv[1].endswith(".csv") == False:                         # checks whether first file name ends in .csv
            sys.exit("Not a CSV file")
        else:
            csv_clean(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def csv_clean(i, j):
    temp_list=[]
    with open(i) as first_file:
        reader = csv.DictReader(first_file)                                 # read first csv sheet into reader
        for row in reader:
            name = row["name"]
            house = row["house"]
            last_name, first_name = name.split(", ")
            temp_dict={"first": first_name, "last": last_name, "house": house}
            temp_list.append(temp_dict)

    with open(j, "w") as second_file:
        writer = csv.DictWriter(second_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for line in temp_list:
            writer.writerow(line)

main()
