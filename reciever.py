from scapy.all import sniff, Ether, Raw

CUSTOM_TYPE = 0x88B5

interface = input("Enter your network interface name: ")

def handle_packet(packet):
    if Ether in packet and packet[Ether].type == CUSTOM_TYPE:
        src_mac = packet[Ether].src

        if Raw in packet:
            data = packet[Raw].load.decode(errors="ignore")

            if "|" in data:
                username, message = data.split("|", 1)
                print(f"\n[{src_mac}] {username}: {message}")

print("Receiver started...")
print("Listening on:", interface)
print("Waiting for Ethernet chat messages...")

sniff(iface=interface, prn=handle_packet, store=False)