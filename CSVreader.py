import csv

# Open the CSV file
with open('your_file.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Optional: Read the header row
    header = next(csv_reader)
    print("Header:", header)

    # Read and print each row of the CSV file
    for row in csv_reader:
        print(row)