from scapy.all import Ether, Raw, sendp, get_if_hwaddr

CUSTOM_TYPE = 0x88B5

interface = input("Enter your network interface name: ")
username = input("Enter your username: ")

src_mac = get_if_hwaddr(interface)
dst_mac = "ff:ff:ff:ff:ff:ff"

print("Ethernet Chat Sender Started")
print("Type 'exit' to quit.")

while True:
    message = input(f"{username}: ")

    if message.lower() == "exit":
        break

    payload = f"{username}|{message}"

    frame = Ether(
        src=src_mac,
        dst=dst_mac,
        type=CUSTOM_TYPE
    ) / Raw(load=payload)

    sendp(frame, iface=interface, verbose=False)

print("Sender closed.")