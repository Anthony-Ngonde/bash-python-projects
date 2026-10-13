import ipaddress


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
