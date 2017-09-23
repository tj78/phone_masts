import csv

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


# Print the total to the console


# Create a dictionary with a count of each tenant's masts, i.e.
#   {'Tenant': mast_count, etc.}


# Print this dictionary in a readable format


# List the data where 'Lease Start Date' is between 1st June 1999 and 31st August 2007


# Print this data, with the date in the format 'DD/MM/YYYY'
