
#import file open
import_file = "allow_list.txt"
with open (import_file,  "r") as file:
    ip_addresses = file.read()
    ip_addresses_list = ip_addresses.split()

    for ip in ip_addresses_list:
        if ip in ip_addresses_list:
            ip_addresses_list.remove(ip)
update_ips = "\n".join(ip_addresses_list)
with open (import_file,  "w") as file:
    file.write(update_ips)

