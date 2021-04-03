Frequent Asked Questions
========================

My device cannot be adopted
---------------------------

There are many possible reasons that the device adoption will go wrong. Many of the time, it was because the device administration credential was changed from the factory default setting. When the system prompt the device cannot be adopted, please just try to adopt it again. If the system prompt to ask you the username and password, you need to find out what the device administrator credential was changed to.

If the advice was adopted by other controller before, you can find the device credential on the previous controller. Go to the site configuration and look for the **device account**

.. figure:: /images/omada_controller_device_account_v4.png
    :width: 50%
    :align: center

    Device Account in V4 controller

.. figure:: /images/omada_controller_device_account_v3.png
    :width: 80%
    :align: center

    Device Account in V3 controller

What is a subnet?
-----------------

A subnetwork or subnet is a logical subdivision of an IP network. The `Wikipedia`_ has the in depth explanations.

.. _Wikipedia: https://en.wikipedia.org/wiki/Subnetwork

A subnet mask defines the group size and can be expressed in dot-decimal notation or in Classless Inter-Domain Routing (CIDR) notation. In data networking, the first IP is the subnet network address and last IP is the broadcast address, both are reserved for networking and cannot be assigned to a client. Therefore, the minimum subnet you can set in the Omada SDN DHCP is /30.

+-----------------+------+------------+
| Dot-decimal     | CIDR | Group size |
+=================+======+============+
| 255.255.255.255 | /32  | 1          |
+-----------------+------+------------+
| 255.255.255.254 | /31  | 2          |
+-----------------+------+------------+
| 255.255.255.252 | /30  | 4          |
+-----------------+------+------------+
| 255.255.255.248 | /29  | 8          |
+-----------------+------+------------+
| 255.255.255.240 | /28  | 16         |
+-----------------+------+------------+
| 255.255.255.224 | /27  | 32         |
+-----------------+------+------------+
| 255.255.255.192 | /26  | 64         |
+-----------------+------+------------+
| 255.255.255.128 | /25  | 128        |
+-----------------+------+------------+
| 255.255.255.0   | /24  | 256        |
+-----------------+------+------------+

What is the available IP addresses that I can use on the LAN?
-------------------------------------------------------------

The Internet Engineering Task Force (IETF) has directed the Internet Assigned Numbers Authority (IANA) to reserve the IP addresses for private use.

IPv4
~~~~

There are three private IP blocks available in IPv4.

+-------------------------------+----------------+------------+
| IP Range                      | CIDR           | Size       |
+===============================+================+============+
| 10.0.0.0 ~ 10.255.255.255     | 10.0.0.0/8     | 16,777,216 |
+-------------------------------+----------------+------------+
| 172.16.0.0 ~ 172.31.255.255   | 172.16.0.0/12  | 1,048,576  |
+-------------------------------+----------------+------------+
| 192.168.0.0 ~ 192.168.255.255 | 192.168.0.0/16 | 65,536     |
+-------------------------------+----------------+------------+

IPv6
~~~~

All address starting with **fd** are private IP addresses.

+----------------+----------------------------+
| CIDR           | Size                       |
+================+============================+
| fd00::/8       | 18,446,744,073,709,551,616 |
+----------------+----------------------------+

Multicast
~~~~~~~~~

IPv4 (RFC2365): Administratively Scoped Addresses 239.0.0.0 ~ 239.255.255.255 

IPv6 (RFC3513): Organization-local scope ffx8\:\: