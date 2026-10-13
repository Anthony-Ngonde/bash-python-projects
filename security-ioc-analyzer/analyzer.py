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
#   print("Valid Email")

#else:
#    print("Invalid Email")

def validate_domain():

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


def validate_md5():

#    value = input("\nEnter MD5: ").strip()

    return re.fullmatch(r"[A-Fa-f0-9]{32}", value) is not None


#if validate_md5():
#   print("Valid MD5")

#else:
#    print("Invalid MD5")



def validate_sha256():

#    value = input("\nEnter SHA256: ").strip()

    return re.fullmatch(r"[A-Fa-f0-9]{64}", value) is not None


#if validate_sha256():
#   print("Valid SHA256")

#else:
#    print("Invalid SHA256")
