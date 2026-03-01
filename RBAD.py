from datetime import datetime

# ----------------------------
# 1) Medicine Categories
# ----------------------------
categories = ["Medicine", "Supplements", "Personal Care", "Medical Devices"]

# ----------------------------
# 2) Medicines Management
# ----------------------------
medicines = []

class Medicine:
    def __init__(self, id, name, price, category, description=""):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.description = description

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}€, Category: {self.category}, Description: {self.description}"


def add_medicine():
    id = int(input("Enter medicine ID: "))
    name = input("Enter medicine name: ")
    price = float(input("Enter medicine price: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    medicine = Medicine(id, name, price, category, description)
    medicines.append(medicine)
    print("Medicine added successfully!")


def remove_medicine():
    id = int(input("Enter medicine ID to remove: "))
    global medicines
    medicines = [m for m in medicines if m.id != id]
    print("Medicine removed successfully!")


def show_medicine():
    id = int(input("Enter medicine ID to show: "))
    for medicine in medicines:
        if medicine.id == id:
            print(medicine)
            return
    print("Medicine not found!")


def show_all_medicines():
    if not medicines:
        print("No medicines available.")
    for medicine in medicines:
        print(medicine)


def search_medicine_by_name():
    name = input("Enter medicine name to search: ").lower()
    for medicine in medicines:
        if medicine.name.lower() == name:
            print(medicine)
            return
    print("Medicine not found!")


def search_by_keyword():
    keyword = input("Enter keyword to search in description: ").lower()
    found = False
    for medicine in medicines:
        if keyword in medicine.description.lower():
            print(medicine)
            found = True
    if not found:
        print("No medicine found with this keyword.")


# ----------------------------
# 3) Prescriptions Management
# ----------------------------
prescriptions = []

class Prescription:
    def __init__(self, id):
        self.id = id
        self.date = datetime.now()
        self.products = {}  # {medicine: quantity}
        self.cancelled = False

    def add_medicine(self, medicine, qty):
        if medicine in self.products:
            self.products[medicine] += qty
        else:
            self.products[medicine] = qty

    def remove_medicine(self, medicine):
        if medicine in self.products:
            del self.products[medicine]

    def total_price(self):
        return sum(m.price * qty for m, qty in self.products.items())

    def cancel(self):
        self.cancelled = True

    def __str__(self):
        status = "Cancelled" if self.cancelled else "Active"
        result = f"\nPrescription ID: {self.id}\nDate: {self.date}\nStatus: {status}\nProducts:\n"
        for m, qty in self.products.items():
            result += f"  - {m.name} x{qty} = {m.price * qty}€\n"
        result += f"Total: {self.total_price()}€\n"
        return result


def add_prescription():
    id = int(input("Enter prescription ID: "))
    prescription = Prescription(id)
    prescriptions.append(prescription)
    print("Prescription added successfully!")


def remove_prescription():
    id = int(input("Enter prescription ID to remove: "))
    global prescriptions
    prescriptions = [p for p in prescriptions if p.id != id]
    print("Prescription removed successfully!")


def show_prescription():
    id = int(input("Enter prescription ID: "))
    for prescription in prescriptions:
        if prescription.id == id:
            print(prescription)
            return
    print("Prescription not found!")


def add_medicine_to_prescription():
    pres_id = int(input("Enter prescription ID: "))
    med_id = int(input("Enter medicine ID: "))
    qty = int(input("Enter quantity: "))

    prescription = next((p for p in prescriptions if p.id == pres_id), None)
    medicine = next((m for m in medicines if m.id == med_id), None)

    if prescription and medicine:
        prescription.add_medicine(medicine, qty)
        print("Medicine added to prescription!")
    else:
        print("Prescription or medicine not found!")


def cancel_prescription():
    id = int(input("Enter prescription ID to cancel: "))
    for prescription in prescriptions:
        if prescription.id == id:
            prescription.cancel()
            print("Prescription cancelled!")
            return
    print("Prescription not found!")


def show_all_prescriptions():
    if not prescriptions:
        print("No prescriptions available.")
    for prescription in prescriptions:
        print(prescription)


def total_sales():
    total = sum(p.total_price() for p in prescriptions if not p.cancelled)
    print(f"Total Sales Amount: {total}€")


# ----------------------------
# 4) Menu
# ----------------------------
def menu():
    while True:
        print("\n===== Pharmacy Management System =====")
        print("1. Add Medicine")
        print("2. Remove Medicine")
        print("3. Show Medicine")
        print("4. Show All Medicines")
        print("5. Search Medicine by Name")
        print("6. Search by Keyword")
        print("7. Add Prescription")
        print("8. Add Medicine to Prescription")
        print("9. Show Prescription")
        print("10. Cancel Prescription")
        print("11. Show All Prescriptions")
        print("12. Total Sales")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_medicine()
        elif choice == "2":
            remove_medicine()
        elif choice == "3":
            show_medicine()
        elif choice == "4":
            show_all_medicines()
        elif choice == "5":
            search_medicine_by_name()
        elif choice == "6":
            search_by_keyword()
        elif choice == "7":
            add_prescription()
        elif choice == "8":
            add_medicine_to_prescription()
        elif choice == "9":
            show_prescription()
        elif choice == "10":
            cancel_prescription()
        elif choice == "11":
            show_all_prescriptions()
        elif choice == "12":
            total_sales()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


# Run the program
menu()
