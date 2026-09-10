# CS1350 Mini-Project 1: Contact Manager
# Dictionaries & Dictionary Patterns


# ============================================================
# DATA PROVIDED BY THE ASSIGNMENT
# ============================================================

# Contact records: name -> dictionary of details
contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}


# Call log: name -> {month -> minutes talked that month}
call_log = {
    "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
    "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
    "Sister": {"Jan": 80, "Mar": 70},
    "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
    "Roommate": {"Feb": 15, "Mar": 25},
    "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
    "Professor": {"Feb": 20, "Mar": 35},
    "Dentist": {"Jan": 10},
}


# ============================================================
# PHASE 1 - QUICK CONTACTS
# ============================================================

print("=== Phase 1: Quick Contacts ===")

# Create an empty dictionary
quick_contacts = {}

# Add five contacts
quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-5678"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"

# Print the whole dictionary
print(quick_contacts)

print("--- Access and Modify ---")

# Print Mom's number using bracket notation
print("Mom's number:", quick_contacts["Mom"])

# Update Dad's number
quick_contacts["Dad"] = "555-4321"

# Add Dentist
quick_contacts["Dentist"] = "555-2222"

# Look up Grandma using get()
grandma = quick_contacts.get("Grandma")

if grandma is None:
    print("Looking up Grandma: Contact not found")
else:
    print("Looking up Grandma:", grandma)

# Print updated dictionary
print("Updated contacts:", quick_contacts)

print("--- Delete and Analyze ---")

# Remove Pizza Place using del
del quick_contacts["Pizza Place"]

# Remove Work using pop()
old_work = quick_contacts.pop("Work")

print("Removed work number:", old_work)

# Print number of contacts, names, and phone numbers
print("Contacts remaining:", len(quick_contacts))
print("Contact names:", list(quick_contacts.keys()))
print("Phone numbers:", list(quick_contacts.values()))


# ============================================================
# PHASE 2 - CONTACT ACTIVITY
# ============================================================

print()
print("=== Phase 2: Contact Activity ===")

# This dictionary will store each person's total minutes
total_minutes = {}

# Loop through each contact
for name, months in call_log.items():

    # Number of months called
    month_count = len(months)

    # Total minutes
    total = sum(months.values())

    # Average minutes per month
    average = total / month_count

    # Variables for finding busiest month
    busiest_month = ""
    busiest_minutes = 0

    # Inner loop through the months
    for month, minutes in months.items():

        if minutes > busiest_minutes:
            busiest_minutes = minutes
            busiest_month = month

    # Store total minutes for this contact
    total_minutes[name] = total

    # Print contact information
    print(
        f"{name}: {month_count} month(s), "
        f"{total} min total, "
        f"avg: {average:.2f}, "
        f"busiest: {busiest_month} ({busiest_minutes})"
    )


# ============================================================
# PHASE 3 - AGGREGATIONS
# ============================================================

print()
print("=== Phase 3: Aggregations ===")


# ------------------------------------------------------------
# PHASE 3A - MONTH STATISTICS
# ------------------------------------------------------------

month_stats = {}

# Loop through every contact
for name, months in call_log.items():

    # Loop through every month for that contact
    for month, minutes in months.items():

        # Create the month if it does not exist
        if month not in month_stats:
            month_stats[month] = {
                "minutes": [],
                "total": 0,
                "avg": 0,
                "contacts": 0
            }

        # Add the minutes to the month's list
        month_stats[month]["minutes"].append(minutes)

        # Add minutes to the month's total
        month_stats[month]["total"] += minutes

        # Count the contact
        month_stats[month]["contacts"] += 1


# Calculate average for each month
for month, stats in month_stats.items():
    stats["avg"] = stats["total"] / stats["contacts"]


print("Monthly summary (sorted by average, highest first):")

# Sort months by average, highest first
sorted_months = sorted(
    month_stats.items(),
    key=lambda item: item[1]["avg"],
    reverse=True
)

# Print monthly information
for month, stats in sorted_months:
    print(
        f"  {month}: {stats['total']} min total, "
        f"{stats['avg']:.2f} avg "
        f"({stats['contacts']} contacts)"
    )


# ------------------------------------------------------------
# PHASE 3B - CATEGORY, CITY, AND HEADCOUNT
# ------------------------------------------------------------

minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

# Loop through contact_book
for name, details in contact_book.items():

    category = details["category"]
    city = details["city"]
    total = total_minutes[name]

    # Add minutes by category
    minutes_by_category[category] = (
        minutes_by_category.get(category, 0) + total
    )

    # Add minutes by city
    minutes_by_city[city] = (
        minutes_by_city.get(city, 0) + total
    )

    # Count contacts by city
    contacts_per_city[city] = (
        contacts_per_city.get(city, 0) + 1
    )

print("Minutes by category:", minutes_by_category)
print("Minutes by city:", minutes_by_city)
print("Contacts per city:", contacts_per_city)


# ============================================================
# PHASE 4 - DICTIONARY COMPREHENSIONS
# ============================================================

print()
print("=== Phase 4: Comprehensions ===")

# Every contact -> phone number
phone_book = {
    name: details["phone"]
    for name, details in contact_book.items()
}

# Only Fort Wayne contacts
local_contacts = {
    name: details["phone"]
    for name, details in contact_book.items()
    if details["city"] == "Fort Wayne"
}

# Frequent if 200+ minutes, otherwise Occasional
activity_level = {
    name: "Frequent" if total >= 200 else "Occasional"
    for name, total in total_minutes.items()
}

print("Phone book:", phone_book)
print("Local contacts (Fort Wayne):", local_contacts)
print("Activity level:", activity_level)


# ============================================================
# PHASE 5 - TIERS, DISTRIBUTION, AND RANKINGS
# ============================================================


# ------------------------------------------------------------
# PHASE 5A - TIER FUNCTION
# ------------------------------------------------------------

def get_tier(minutes):
    """Return the contact tier based on total minutes."""

    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"


print()
print("=== Phase 5: Tier Report ===")

# Print each contact and their tier
for name, total in total_minutes.items():

    tier = get_tier(total)

    print(f"{name}: {total} min ({tier})")


# ------------------------------------------------------------
# PHASE 5B - TIER DISTRIBUTION
# ------------------------------------------------------------

platinum = 0
gold = 0
silver = 0
bronze = 0
inactive = 0

# Count each tier
for name, total in total_minutes.items():

    tier = get_tier(total)

    if tier == "Platinum":
        platinum += 1
    elif tier == "Gold":
        gold += 1
    elif tier == "Silver":
        silver += 1
    elif tier == "Bronze":
        bronze += 1
    else:
        inactive += 1


print("--- Tier Distribution ---")
print("Platinum:", platinum)
print("Gold:", gold)
print("Silver:", silver)
print("Bronze:", bronze)
print("Inactive:", inactive)


# ------------------------------------------------------------
# PHASE 5C - MOST AND LEAST CONTACTED
# ------------------------------------------------------------

top_name = ""
top_minutes = 0

bottom_name = ""
bottom_minutes = float("inf")

# Find highest and lowest
for name, total in total_minutes.items():

    if total > top_minutes:
        top_minutes = total
        top_name = name

    if total < bottom_minutes:
        bottom_minutes = total
        bottom_name = name


print("--- Top and Bottom ---")
print(f"Most contacted: {top_name} ({top_minutes} min)")
print(f"Least contacted: {bottom_name} ({bottom_minutes} min)")


# Grand total
grand_total = sum(total_minutes.values())

# Average per contact
average_per_contact = grand_total / len(total_minutes)

print("Total minutes:", grand_total)
print(f"Average per contact: {average_per_contact:.2f}")


# Contacts above average
print("--- Above Average Contacts ---")

for name, total in total_minutes.items():

    if total > average_per_contact:
        print(f"{name}: {total}")


# ============================================================
# PHASE 6 - CONTACT HUB REPORT
# ============================================================

print()
print("=== Phase 6: Contact Hub Report ===")

print("Name         Category     City             Minutes Tier")
print("-------------------------------------------------------")

# Sort contacts by total minutes, highest first
sorted_contacts = sorted(
    total_minutes.items(),
    key=lambda item: item[1],
    reverse=True
)

# Print each contact
for name, total in sorted_contacts:

    details = contact_book[name]

    category = details["category"]
    city = details["city"]
    tier = get_tier(total)

    print(
        f"{name:<12}"
        f"{category:<13}"
        f"{city:<17}"
        f"{total:>7} "
        f"{tier}"
    )

print("-------------------------------------------------------")

# Final summary
print(
    f"{len(total_minutes)} contacts | "
    f"{grand_total} total minutes | "
    f"{average_per_contact:.2f} average"
)