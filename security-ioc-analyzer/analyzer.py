import ipaddress
import re


def validate_ipv4():

#    value = input("\nEnter IP Address: ").strip()

    ip = ipaddress.ip_address(value)

    try:
       if ip.version == 4:
#          print("Valid IP Address")
          return True

    except ValueError:
#           print("Invalid IP Address")
           pass

    return False

#validate_ipv4()


def validate_email():

#    value = input("\nEnter Email Address: ").strip()

    pattern = "^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\\.[A-Za-z0-9-]+)$"

    return re.fullmatch(pattern, value) is not None


#if validate_email():
   print("Valid Email")

#else:
#    print("Invalid Email")



