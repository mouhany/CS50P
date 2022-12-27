months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            mm, dd, yyyy = date.split("/")
        elif "," in date:
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")
            # No need to check if mm in months. KeyError is handled separately.
            mm = (months.index(mm)) + 1
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break