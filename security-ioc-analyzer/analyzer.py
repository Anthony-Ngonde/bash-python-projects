import ipaddress
import re
from pathlib import Path
import sys
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "iocs.txt"
REPORT_DIR = BASE_DIR / "reports"


#value = input("\nEnter IOC: ").strip()


def validate_ipv4(value):

#    value = input("\nEnter IP Address: ").strip()

    try:
       ip = ipaddress.ip_address(value)


       if ip.version == 4:
#          print("Valid IP Address")
          return True

    except ValueError:
#           print("Invalid IP Address")
           pass

    return False

#validate_ipv4()


def validate_email(value):

#    value = input("\nEnter Email Address: ").strip()

    pattern = "^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\\.[A-Za-z0-9-]+)$"

    return re.fullmatch(pattern, value) is not None


#if validate_email():
#   print("Valid Email")

#else:
#    print("Invalid Email")

def validate_domain(value):

#    value = input("\nEnter domain: ").strip()

    if len(value) > 253:
#       print("Invalid Domain")
       return False

    if value.endswith("."):
       value = value[:-1]

    labels = value.split(".")

    if len(labels) < 2:
#       print("Invalid Domain")
       return False

    for label in labels:

        if not label:
#           print("Invalid Domain")
           return False

        if len(label) > 63:
#           print("Invalid Domain")
           return False

        if label.startswith("-") or label.endswith("-"):
#           print("Invalid Domain")
           return False

        if not re.fullmatch(r"[A-Za-z0-9-]+", label):
#           print("Invalid Domain")
           return False

#    print("Valid Domain")
    return True

#validate_domain()


def validate_md5(value):

#    value = input("\nEnter MD5: ").strip()

    return re.fullmatch(r"[A-Fa-f0-9]{32}", value) is not None


#if validate_md5():
#   print("Valid MD5")

#else:
#    print("Invalid MD5")



def validate_sha256(value):

#    value = input("\nEnter SHA256: ").strip()

    return re.fullmatch(r"[A-Fa-f0-9]{64}", value) is not None


#if validate_sha256():
#   print("Valid SHA256")

#else:
#    print("Invalid SHA256")



def classify_ioc(value):

    value = value.strip()

    if not value:
       return "Unknown"

    if validate_ipv4(value):
       return "IPv4"

    if validate_email(value):
       return "Email"

    if validate_domain(value):
       return "Domain"

    if validate_md5(value):
       return "MD5"

    if validate_sha256(value):
       return "SHA256"

    return "Unknown"


#ioc_type = classify_ioc(value)
#print(ioc_type)


def load_iocs():

    iocs = []

    with DATA_FILE.open("r", encoding="utf-8") as file:
         for line in file:
             line = line.strip()

             if not line:
                continue

             parts = line.split("|", 2)

             if len(parts) != 3:
                continue

             timestamp, ioc_type, value = parts

             ioc = {
               "timestamp": timestamp,
                "type": ioc_type,
                "value": value
             }

             iocs.append(ioc)

    return iocs


def save_ioc(ioc_type, value):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:S")

    with DATA_FILE.open("a", encoding="utf-8") as file:
         file.write(f"{timestamp}|{ioc_type}|{value}\n")


def add_ioc(value):

    value = value.strip()

    ioc_type = classify_ioc(value)

    if ioc_type == "Unknown":
       print("INVALID. Enter a valid IOC")
       return 1

    iocs = load_iocs()

    for ioc in iocs:
        if ioc["value"].lower() == value.lower():
           print("IOC already exists")
           return 1

    save_ioc(ioc_type, value)

    print("IOC added successfully")
    print(f"Type: {ioc_type}")
    print(f"Value: {value}")
    return 0


def classify_command(value):

    ioc_type = classify_ioc(value)

    print(ioc_type)

    if ioc_type == "Unknown":
       return 1

    return 0



def search_ioc(value):

    value = value.strip()

    iocs = load_iocs()

    matches = []

    for ioc in iocs:
        if ioc["value"].lower() == value.lower():
           matches.append(ioc)

    if not matches:
       print("No matching IOCs found")
       return 1

    print("\n=============")
    print("Search Results")
    print("===============")

    for ioc in matches:

        print(f"Timestamp: {ioc['timestamp']}")
        print(f"Type: {ioc['type']}")
        print(f"Value: {ioc['value']}")
        print("--------------------------------")
        return 0


def list_iocs():

    iocs = load_iocs()

    if not iocs:
       print("No stored IOCs available")
       return 0

    print("\n===========")
    print("STORED IOCs")
    print("=============")

    print(f"{'TYPE':<10} {'VALUE':<45} {'TIMESTAMP'}")

    for ioc in iocs:
        print(
          f"{ioc['type']:<10}"
          f"{ioc['value']:<45}"
          f"{ioc['timestamp']}"
        )

    return 0


def count_ioc_types():

    iocs = load_iocs()

    counts = {
      "IPv4": 0,
      "Email": 0,
      "Domain": 0,
      "MD5": 0,
      "SHA256": 0

    }

    for ioc in iocs:
        ioc_type = ioc["type"]

        if ioc_type in counts:
           counts[ioc_type] += 1

    total = len(iocs)

    print("\n==============")
    print("IOC Statistics")
    print("================")

    print(f"IPv4: {counts['IPv4']}")
    print(f"Email: {counts['Email']}")
    print(f"Domain: {counts['Domain']}")
    print(f"MD5: {counts['MD5']}")
    print(f"SHA256: {counts['SHA256']}")
    print("-----------------------------")
    print(f"Total: {total}")

    return 0






def main():

    if len(sys.argv) < 2:
       return 1

    command = sys.argv[1]

    if command == "add":

       if len(sys.argv) != 3:
          print("Error: add requires an IOC")
          return 1

       return add_ioc(sys.argv[2])


    elif command == "classify":

         if len(sys.argv) != 3:
            print("Error: classify requires an IOC")
            return 1

         return classify_command(sys.argv[2])

    elif command == "search":

         if len(sys.argv) != 3:
            print("Error: search requires an IOC")
            return 1

         return search_ioc(sys.argv[2])


    elif command == "list":

         if len(sys.argv) != 2:
            print("Error: list does not require an IOC")
            return 1

         return list_iocs()


    elif command == "count":

         if len(sys.argv) != 2:
            print("Error: count does not require an IOC")
            return 1

         return count_ioc_types()







if __name__ == "__main__":
     sys.exit(main())

