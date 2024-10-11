import csv


#CUSTOMER LIST TO CSV FILE

#FUNCTION DEFINITION TO ADD CUSTOMER DETAILS
def add_customer(name, email, order_number, filename='customers.csv'):
    with open(filename, mode='a', newline='') as file:    #a to not overwrite existing data
        writer = csv.writer(file)
        writer.writerow([name, email, order_number])
    print(f"Customer '{name}' added successfully.")  #CONFIRMATION


#FUNCTION TO READ THE CUSTOMER FILES
def read_customers(filename='customers.csv'):
    try:
        with open(filename, mode='r') as file:   #READ THE CONTENTS OF THE FILE
            reader = csv.reader(file)
            print("Customer Details:")
            print("Name, Email, Order Number")
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("No customer data found. Add some customers first.") #EMPTY MESSAGE


#LOOPS TO ACCEPT CUSTOMER DETAILS
while True:
    print("\nOptions:")
    print("CUSTOMER DETAILS")
    print("1. Add a new customer")
    print("2. View all customers")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        name = input("Enter customer's name: ")  #ENTER CUSTOMER DETAILS
        email = input("Enter customer's email: ")
        order_number = input("Enter customer's order number: ")

        add_customer(name, email, order_number) #CALLING FUNCTION TO ADD FILES TO THE CSV FILE

    elif choice == '2':
        read_customers()   #CALLING FUNCTION TO READ CUSTOMER DETAILS

    elif choice == '3':
        #END PROGRAM
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")