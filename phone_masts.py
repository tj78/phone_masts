import csv
from datetime import datetime

# Read in the CSV file
with open('Mobile Phone Masts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Sort the data - by 'Current Rent' ascending
    sorted_by_rent = sorted(reader, key=lambda row: float(row['Current Rent']))
# Output the data to console
print("\n\nThe first 5 entries in Mobile Phone Masts.csv, ", end="")
print("sorted by 'Current Rent' (ascending), are: \n")

for data in sorted_by_rent[:5]:
    print(data)

# Tests to check that the correct data is being returned
assert(sorted_by_rent[0]['Unit Name'] == 'Potternewton Est Playing Field')
assert(sorted_by_rent[1]['Unit Name'] == 'Queenswood Hgt-Telecom App.')
assert(sorted_by_rent[2]['Unit Name'] == 'Burnsall Grange CSR 37865')
assert(sorted_by_rent[3]['Unit Name'] == 'Seacroft Gate (Chase) block 2-Telecom App.')
assert(sorted_by_rent[4]['Unit Name'] == 'Seacroft Gate (Chase) - Block 2, WYK 0414')

# Create list where 'Lease Years' == 25
lease_years_25 = []
print("\n\nThe data entries where 'Lease Years' == 25 are:\n")
for row in sorted_by_rent:
    if int(row['Lease Years']) == 25:
        lease_years_25.append(row)
        # Print the list to the console
        print(row)

# Tests to check that the correct data is being returned
assert(lease_years_25[0]['Unit Name'] == 'Queenswood Hgt-Telecom App.')
assert(lease_years_25[1]['Unit Name'] == 'Burnsall Grange CSR 37865')
assert(lease_years_25[2]['Unit Name'] == 'Seacroft Gate (Chase) block 2-Telecom App.')
assert(lease_years_25[3]['Unit Name'] == 'Seacroft Gate (Chase) - Block 2, WYK 0414')
assert(len(lease_years_25) == 4)

# Calculate the total rent for the list (where 'Lease Years' == 25)
total_rent = 0
for row in lease_years_25:
    total_rent += float(row['Current Rent'])
# Print the total to the console
print("\nThe total annual rent for phone masts where 'Lease Years' == 25", end="")
print(", is £{0:.2f}".format(total_rent),  "per year.")
print("\nThe total rent for these phone masts over the length of the 25 years", end="")
print(", is £{0:.2f}".format(total_rent*25))

# Check that the correct totals are calculated
assert(total_rent == 46500)
assert(total_rent*25 == 1162500)

# Create a dictionary with a count of each tenant's masts, i.e.
#   {'Tenant': mast_count, etc.}
tenant_masts = {}
import re
for tenant in sorted_by_rent:
    #if x['Tenant Name'] in tenant_masts:
    if tenant['Tenant Name'].replace('.', '') in tenant_masts:
        tenant_masts[tenant['Tenant Name'].replace('.', '')] += 1
    else:
        tenant_masts[tenant['Tenant Name'].replace('.', '')] = 1

# Print this dictionary in a readable format
print("\n\n'Tenant Name' (count of their phone masts):")
for tenant in tenant_masts.keys():
    print(tenant, "\t", end="")
    print("(" + str(tenant_masts[tenant]) + ")")

# List the data where 'Lease Start Date' is between 1st June 1999 and 31st August 2007
FIRST_LEASE_START = '1999/06/01'
END_LEASE_START = '2007/08/31'
list_by_lease_start = []
for row in sorted_by_rent:
    find_date = datetime.strptime(row['Lease Start Date'],'%d %b %Y')
    preformatted_date = datetime.strftime(find_date, '%Y/%m/%d')
    if(preformatted_date > FIRST_LEASE_START) and (preformatted_date < END_LEASE_START):
        formatted_date = datetime.strftime(find_date, '%d/%m/%Y')
        list_by_lease_start.append({"Property":row['Property Name'], "Date":formatted_date})

# Print this data, with the date in the format 'DD/MM/YYYY'
print("\n\nData entries with 01/06/1999 < 'Lease Start Year' < 31/08/2007:")
print("'Property Name' ('Lease Start Year')\n")
for data in list_by_lease_start:
    print(data["Property"] + "\t(" + data["Date"] + ")")
