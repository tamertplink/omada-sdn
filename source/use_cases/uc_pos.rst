Omada SDN Example : Point of Sales System
================================================

.. image:: /images/uc_pos.jpg
    :width: 100%
    :align: center

A good point-of-sale (POS) system can help smooth sales transactions. Whether you are choosing a simple handheld POS machine, or a complex ordering system, you need the secured connection for your payment.

PCI Data Security Standard (PCI DSS) Compliance
-----------------------------------------------

The PCI Data Security Standard (PCI DSS)  is the global security standard for payment information processing created by the Payment Card Industry Security Standards Council (PCI SSC), formed by the major credit card companies. All the digital payment process should follow the PCI DSS guidelines to make sure the secured payment transactions. PCI SSC website: https://www.pcisecuritystandards.org/

6 focuses
^^^^^^^^^

According to the PCI Data Security Standard, the requirements can be summarized in 6 focuses:
1. Build and maintain a secure network
2. Protect cardholder data
3. Maintain a vulnerability management program
4. Implement strong access control measures
5. Regularly monitor and test networks
6. Maintain an information security policy

12 requirements
^^^^^^^^^^^^^^^

From these 6 focuses, 12 requirements were listed:
1. Install and maintain a firewall configuration to protect cardholder data
2. Do not use vendor-supplied defaults for system passwords and other security parameters
3. Protect stored cardholder data
4. Encrypt transmission of cardholder data across open, public networks 
5. Use and regularly update anti-virus software or programs
6. Develop and maintain secure systems and applications
7. Restrict access to cardholder data by business need to know
8. Assign a unique ID to each person with computer access
9. Restrict physical access to cardholder data
10. Track and monitor all access to network resources and cardholder data
11. Regularly test security systems and processes
12. Maintain a policy that addresses information security for all personnel
 
Setup your network with data security in mind
---------------------------------------------

Protect data from unauthorized access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The most important thing to protect the payment data is to prevent unauthorized access, physically or logically. Keep your credit card machine and transaction receipts in the physically secured place. Protect the connecting data port from unauthorized connection to other devices. Separate the payment network physically or logically. Prevent any unauthorized access from outside with a network firewall.

The Omada SDN devices equipped security features to keep your network PCI DSS compliant:

* SPI firewall
* Attack protection
* Management VLAN, Port VLAN, MAC VLAN, 802.1Q VLAN
* MAC Authentication, MAB binding, ARP anti-spoof
* Switch and router, and access point level access control, ACL
* Radius/AAA authentication
 
Omada SDN also provide the wireless security features to help PCI DSS compliance
 
* SSID-VLAN mapping
* Management VLAN
* Rogue AP analysis
* Physical security design
* Schedule control
* Guest network

PoE for POS devices
-------------------

Many POS devices, such as the credit pard machine, supports the PoE technology. You can supply the power and the data through a single cable. You can use the TP-Link PoE switch or PoE injector for the connection.