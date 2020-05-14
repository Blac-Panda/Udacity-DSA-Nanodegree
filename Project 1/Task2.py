from datetime import datetime
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


"""
Get calls within a specificed date range
"""
def callRange(call, month, year):

    timestamp = call[2]
    date = datetime.strptime(timestamp, '%d-%m-%Y %H:%M:%S')
    if(date.year == year and date.month == month):
        return True
    else:
        return False
    

"""
Get all the phone calls made during September 2016
"""
records = filter(lambda x: callRange(x, 9, 2016), calls)


"""
Add up the duration of all calls made and save the data in a dictionary
"""


def callDuration(dict, phoneNumber, duration):
    if(dict.get(phoneNumber) == None):
        dict[phoneNumber] = duration
    else:
        dict[phoneNumber] = int(
            dict.get(phoneNumber)) + int(duration)
    return dict


"""
Track the duraction of the september calls that were made
"""
dict = {}
for record in records:
    outgoing = record[0]
    recieving = record[1]
    timestamp = record[2]
    duration = record[3]

    dictionary = callDuration(dict, outgoing, duration)
    dictionary = callDuration(dict, recieving, duration)


"""
Get the details for the phone number that spent the longest time spent on the phone during september 2016
"""
maxCall = max(dict.items(), key=lambda x: int(x[1]))


# print(len(list(records)))
# print(phoneMax);

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxCall[0], maxCall[1]))
