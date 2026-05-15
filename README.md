# CSCI-4345-Final-Project-Ethernet-Chat
# Ethernet Chat Project

# Overview

This project implements a simple chat application using raw Ethernet frames instead of TCP/IP communication. Messages are sent directly at Layer 2 of the OSI model using MAC addresses and a custom EtherType.

The project was built in Python using Scapy and analyzed using Wireshark.


# Features

- Raw Ethernet frame communication
- Custom EtherType (0x88B5)
- Broadcast MAC transmission
- Custom message payload format
- Packet analysis using Wireshark


# Technologies Used

- Python
- Scapy
- Wireshark
- Npcap


# Installation

1. Install Python

2. Install Scapy:

    In the terminal, run: pip install scapy

3. Install Npcap

4. Install Wireshark

# Run the project

1. Find the network interfaces

    In the terminal, run: python interface.py
   
    and select the active network interface
   
2. Start the receiver

    In the terminal, run: python receiver.py

   and enter the interface you previously selected

3. Start the sender

     Open another terminal and run: python sender.py

     When prompted, enter the same network interface and a username of your choice


# You can now enter messages to send Ethernet chat frames.

# Wireshark

To view the custom Ethernet frames in wireshark use eth.type == 0x88b5 in the display filter, begin capturing and see the packets being transmitted as you enter messages into the sender.py application.
