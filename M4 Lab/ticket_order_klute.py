# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M4 Lab - Python Input/Output
# Ticket Ordering System
# ----------------------------------

# Constants for Admin
SALES_TAX = 0.08
SERVICE_FEE = 2.99
TICKET_PRICE = 19.99

# Needed Variables from user
num_tickets = input("Please input the number of tickets you would like to buy: ")
ticket_count = int(num_tickets)

# Math needed
total_ticket_cost = ticket_count * TICKET_PRICE
subtotal = total_ticket_cost + SERVICE_FEE
total_sales_tax = subtotal * SALES_TAX
total_bill = total_ticket_cost + total_sales_tax + SERVICE_FEE

# User Receipts
print(
    "\nYour Ticket(s) Receipt\n\n" 
    f"Total Ticket Cost: {total_ticket_cost:>10.2f}\n"
    f"Service Fee: {SERVICE_FEE:>16.2f}\n"
    f"Subtoal: {subtotal:>20.2f}\n"
    "-----------------------------\n"
    f"Sales Tax Due: {total_sales_tax:>14.2f}\n"
    f"Total Bill: {total_bill:>17.2f}"
)