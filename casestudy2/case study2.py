patient_name = input("Enter Patient Name: ")

req_dept = []
n = int(input("How many departments do you want to send request for? "))
for i in range(n):
    dept = input("Enter requested dept " + str(i + 1) + ": ")
    req_dept.append(dept)

avail_dept = []
n = int(input("How many available departments in hospital? "))
for i in range(n):
    dept = input("Enter available dept " + str(i + 1) + ": ")
    avail_dept.append(dept)

prev_dept = []
n = int(input("How many previously visited departments? "))
for i in range(n):
    dept = input("Enter previous dept " + str(i + 1) + ": ")
    prev_dept.append(dept)

emg_dept = []
n = int(input("How many emergency departments? "))
for i in range(n):
    dept = input("Enter emergency dept " + str(i + 1) + ": ")
    emg_dept.append(dept)

req_set = set(req_dept)
avail_set = set(avail_dept)
prev_set = set(prev_dept)
emg_set = set(emg_dept)

avail_req = req_set & avail_set
unavail_dept = req_set - avail_set
common_dept = req_set & prev_set
urgent_dept = req_set & emg_set

rec_dept = None

if len(urgent_dept) > 0:
    rec_dept = list(urgent_dept)[0]
elif len(avail_req) > 0:
    rec_dept = list(avail_req)[0]

if rec_dept:
    status = "Confirmed in " + rec_dept
else:
    status = "Rejected (No requested departments are available)"

print("FINAL APPOINTMENT REPORT: ", patient_name.upper())
print("Patient Name             : ", patient_name)
print("Requested Departments    : ", req_dept)
print("Available Departments    : ", list(avail_req))
print("Unavailable Departments  : ", list(unavail_dept))
print("Common Departments       : ", list(common_dept))
print("Previous Departments     : ", prev_dept)
print("Emergency Departments    : ", list(urgent_dept))
print("Recommended Department   : ", rec_dept or "None")
print("Final Appointment Status : ", status)