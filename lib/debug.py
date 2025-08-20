

#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Reset the table each time for debugging
Department.drop_table()
Department.create_table()

# Create Departments
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

# Update HR
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

# Delete Payroll from DB
print("Delete Payroll")
payroll.delete()  # deletes row but object still exists in memory
print(payroll)    # <Department 1: Payroll, Building A, 5th Floor>

# Drop into interactive debugger
ipdb.set_trace()
