"""

Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work
“9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM
and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries.
You’re welcome, but not required, to use re and/or sys.

"""
import re

def main():
    #str in 12-h format
    print(convert(input("Hours: ").strip()))


def convert(h):
    hour = []

    if matches := re.search(r"^([0-9]{1,2}):?([0-9]{1,2})? (AM|PM) to ([0-9]{1,2}):?([0-9]{1,2})? (AM|PM)$", h):

        if matches.group(2) == None and int(matches.group(1)) in range(1, 13):
            hour.append(f"{matches.group(1)},00,{matches.group(3)}")
        elif int(matches.group(1)) in range(1, 13) and int(matches.group(2)) in range(0, 60):
            #str in 24h format
            hour.append(f"{matches.group(1)},{matches.group(2)},{matches.group(3)}")
        else:
            raise ValueError("Hour not in range")

        if matches.group(5) == None and int(matches.group(4)) in range(1, 13):
            hour.append(f"{matches.group(4)},00,{matches.group(6)}")
        elif int(matches.group(4)) in range(1, 13) and int(matches.group(5)) in range(0, 60):
            #str in 24h format
            hour.append(f"{matches.group(4)},{matches.group(5)},{matches.group(6)}")
        else:
            raise ValueError()
    else:
        raise ValueError()

    return catch_hour(hour)

def catch_hour(s):
    converted_time = []
    for time in s:
        hours, minutes, meridiem = time.split(",")

        if meridiem == "PM" and hours != "12":
            hours = int(hours) + 12

        elif meridiem == "AM" and hours == "12":
            hours = int(hours) - 12

        converted_time.append(f"{int(hours):02}:{int(minutes):02}")
    time1, time2 = converted_time
    return f"{time1} to {time2}"



if __name__ == "__main__":
    main()
