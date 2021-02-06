
SafeStream Load Balance VPN Router
==================================

There are two SMB routers in this category ER605 and ER7206. Both of the routers were designed for small office and remote office. The ER7206 is in a 9 inches wide metal box and ER605 has 6 inch in width. ER605 has wall mount slot for easy placement.

.. note::
    TL-SG605 was the previous model number of ER605 and the TL-SG7206 was the previous model number of ER7206.

Comparison of the ER7602 and ER605
----------------------------------

+------------+-----------+-----------+
| Model      | ER7602    | ER605     |
+============+===========+===========+
| Speed      | Gigabit   | Gigabit   |
+------------+-----------+-----------+
| Concurrent | 150K      | 25K       |
| Session    |           |           |
+------------+-----------+-----------+
| New Session| 5.5K/s    | 2.4K/s    |
| Rate       |           |           |
+------------+-----------+-----------+
| IPSEC VPN  | 291.6Mbps | 41.5Mbps  |
| Throughput |           |           |
+------------+-----------+-----------+

Key Features
~~~~~~~~~~~~

There are many features the SafeStream routers can do in a small office environment. The key features are listed here:

* **IPSEC, L2TP, and OpenVPN** The IPSEC is the most popular VPN connections in use in the industry. The SafeStream IPSEC VPN connection can act as a server connecting to the clients remotely at home or at the coffee shop. L2TP (over IPSEC) provides an easier point to point connection through firewalls. OpenVPN is a proprietary, but very popular, VPN connection. You can almost set the end point anywhere and the OpenVPN can connect you through NAT and firewalls with no effort.

.. note::
    The OpenVPN feature is only available when the SafeStream router is in the controller model

* **Load Balance** The SafeStream SMB router can connect up to 4 ISPs. Whether you want to make the multiple connection to balance the traffic loads or simply make a connection as a fallback line, the SafeStream router can do the job for you.

* **Digital Phone System Friendly** The SafeStream works with different phone systems. You can enable/disable the SIP ALG. Set the priority route, using ACL to allow or block visitors 


Site-to-site vs. Client-to-site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The terms are self explained. The site-to-site VPN creates a secured tunnel between two sites. Computers on both sides don't have to aware the existence of the secured tunnel and can communicate to end points on both sites without effort. In Omada SDN, you can create a site-to-site VPN tunnel simply states which site you want to connect with and then the tunnel can be created.

If you have a single device you want to connect to the office securely. You can setup the client-to-site VPN server on the SafeStream router. 

VPN Capacity
------------

VPN secured tunnel requires encryption and decryption to the traffic on both directions. Depends on the method of the encryption and decryption you choose, the passing through speed and tunnel capacity will be different. 

+---------------+--------+-------+
| Model         | ER7602 | ER605 |
+===============+========+=======+
| IPSEC Tunnels | 100    | 20    |
| with 3DES     |        |       |
+---------------+--------+-------+
| OpenVPN       | 50     | 16    |
| Tunnel        |        |       |
+---------------+--------+-------+
| OpenVPN       | 10     | 10    |
| Client        |        |       |
+---------------+--------+-------+

Load Balance
------------

The load balance SafeStream routers provided are not on the datagram based, but on session based. You can set your policy allowed which session going through which router and the session fall back can be performed based on the fall back rules. 