
Introduction
============

TP-Link Omada SDN system is an easy-to-use business class corporate network system. An Omada controller consolidates all the system settings and helps to discover, set up, and manage the Omada SDN devices. With the holoscope of the system through the controller, the network administrator can manage multiple networks through a single control interface. With the free TP-Link Omada cloud directory service, and Omada mobile app, the network manager can monitor the system 24/7 anywhere. The system will notify the system manager when a triggered event happens. The solution includes the network controller, wireless access point, network switch, and load balance VPN router.

1. What is SDN?
---------------

The SDN stands for Software Defined Networking. Deploying a traditional network, you have to have a thorough understanding of the network equipment, the interaction behaviors in between, and the set-up commands to each one of the devices. The Omada SDN abstracts the system controls in one center controller, provides smooth integrations on the system level and saves the detailed device set up to the software commands.

2. Controllers
--------------

There are three different flavors of controllers in Omada SDN Solution, hardware controller, software controller, and cloud based controller. Each controller was designed to serve a targeted size of network. The OC200 can manage 100 Omada SDN devices. The OC300 can manage 500 devices. The software controller can manage up to 1,500 devices. The cloud based controller is a subscription based management service and has no limit in the number of managed devices.

.. note::

    The Omada Cloud-Based Controller, CBC was designed for easy to use. The on-line subscription is available in the http://omada.tplinkcloud.com portal. For off-line partner subscriptions, please register the business partner account and then request services. https://partner.tp-link.com/

The network control logics in different controllers are the same. Network devices, switch, router, and wireless access point, can be managed together as a site. A site is a logical network unit consisting of a group of network devices. In most of the cases, a logical site is mapping to a physical network site. In some cases, you can set up logical sites purely for managing purposes.

Once the site has been set up. It can freely migrate from one controller to another without extra effort. You can set up your first sites on an OC200 hardware controller to start your project. As your business is growing, you can migrate the site settings to the OC300, to the software controller or to the Cloud-Based Controller.

.. image:: /images/controller_compare.png

3. Wireless Access Points
-------------------------

TP-Link Omada EAP high density wireless access points were designed for crowded environments. With the latest WiFi 6 technology, the Omada EAP can service multi-gig communication wireless. The 802.11ac wave 2 (WiFi5) access points provide solid connections and well coverage for business. The 802.11n access points expands the wireless everywhere for your IoT devices. 

3.1 List of EAPs
~~~~~~~~~~~~~~~~

.. note::
    This is the list of Omada SDN selling in the US region. Wireless access points can be different by region due to the local regulation.

The Omada EAPs can be grouped by their model numbers. The Omada EAP6xx are WiFi 6 access points. The EAP2xx are 802.11ac wave 2 (WiFi 5) access points and the The EAP1xx are classic 802.11n access points. The EAP3xx series has been end-of-life since 2018.

3.1.1 High density series
^^^^^^^^^^^^^^^^^^^^^^^^^

+------------+-----------+-----------+-----------+
| Model      | EAP660 HD | EAP620 HD | EAP265 HD |
+============+===========+===========+===========+
| Class      | WiFi 6    | WiFi 6    | WiFi 5    |
+------------+-----------+-----------+-----------+
| Speed      | AX3600    | AX1800    | AC1750    |
+------------+-----------+-----------+-----------+
| Max clients| 1024      | 1024      | 620       |
+------------+-----------+-----------+-----------+
| Ethernet   | 2.5G      | Gigabit   | Gigabit   |
+------------+-----------+-----------+-----------+
| CBC        | Yes       | Yes       | No        |
+------------+-----------+-----------+-----------+

3.1.2 Ceiling mount EAPs
^^^^^^^^^^^^^^^^^^^^^^^^

+------------+-----------+----------+----------+-----------+-----------+-----------+
| Model      | EAP670    | EAP650   | EAP610   | EAP245    | EAP225    | EAP115    |
+============+===========+==========+==========+===========+===========+===========+
| Class      | 802.11ax  | 802.11ax | 802.11ax | 802.11ac  | 802.11ac  | 802.11n   |
+------------+-----------+----------+----------+-----------+-----------+-----------+
| Speed      | AX5400    | AX3000   | AX1800   | AC1750    | AC1350    | N300      |
+------------+-----------+----------+----------+-----------+-----------+-----------+
| Ethernet   | 2.5G      | Gigabit  | Gigabit  | Gigabit   | Gigabit   | 10/100    |
+------------+-----------+----------+----------+-----------+-----------+-----------+
| CBC        | Yes       | Yes      | Yes      | Yes       | Yes       | No        |
+------------+-----------+----------+----------+-----------+-----------+-----------+

* EAP653 is an industrial package remodeled from EAP650 and removing the power adapter accessory.

3.1.3 In-Wall EAPs
^^^^^^^^^^^^^^^^^^

+------------+-------------+-------------+--------------+
| Model      | EAP615-Wall | EAP235-Wall | EAP225-Wall  |
+============+=============+=============+==============+
| Class      | 802.11ax    | 802.11ac    | 802.11ac     |
+------------+-------------+-------------+--------------+
| Speed      | AX1800      | AC1200      | AC120        |
+------------+-------------+-------------+--------------+
| Ethernet   | Gigabit     | Gigabit     | 10/100       |
+------------+-------------+-------------+--------------+
| CBC        | Yes         | Yes         | No           |
+------------+-------------+-------------+--------------+

3.1.3 Outdoor EAPs
^^^^^^^^^^^^^^^^^^

+------------+----------------+----------------+----------------+
| Model      | EAP610-Outdoor | EAP225-Outdoor | EAP110-Outdoor | 
+============+================+================+================+
| Class      | 802.11ax       | 802.11ac       | 802.11n        | 
+------------+----------------+----------------+----------------+
| Speed      | AX1800         | AC1200         | N300           | 
+------------+----------------+----------------+----------------+
| Ethernet   | Gigabit        | Gigabit        | 10/100         |
+------------+----------------+----------------+----------------+
| CBC        | Yes            | Yes            | No             |
+------------+----------------+----------------+----------------+

4. Managed Switches
-------------------

All Omada SDN switches came from the field proof JetStream business manage switches. The connecting speed can be varied from 10G, 5G, 2.5G, gigabit, to 10/100. Deploy your network as flexible as you can and manage your network as easy as possible. With the Omada controller, setting virtual networks and personal authentications are just a few clicks away.

All 2021/2022 JetStream managed switches are compatible with Omada SDN and can be controlled by the Omada SDN controller. The new JetStream managed switches can still work in standalone mode as usual, and are enhanced by adding up the SDN capabilities. There are two subclasses of the managed switches, smart managed switch, model numbered TL-Sx2xx and the fully managed TL-Sx3xx models. The major differences between smart managed switches and fully managed switches are the features in standalone mode. In controller mode, the features on the switches are the same.

.. note:: The JetStream switch features may be different with the future Omada controller. With the version 5 controller, switch features are all the same when operating in the controller mode.
    
    There are selected models compatible to the Cloud-Based Controller. A superscript \ :sup:`[cbc]` will be marked in front of the model listed below for distinction.

The TL-SG3210XHP-M2 is an 8-port 2.5G managed switch with two SFP+ 10G uplink ports. This is the perfect partner with the EAP660 HD for 2.5G Ethernet back haul. No new wire is required, the traditional CAT5e cable supports 2.5G traffic over 100 meters and more.

4.1 10/100 Managed Switch
~~~~~~~~~~~~~~~~~~~~~~~~~

* TL-SL2428P(UN)V4.2 JetStream 24-Port 10/100Mbps + 4-Port Gigabit Smart Switch with 24-Port PoE+

4.2 Non-PoE Gigabit Switches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* TL-SG2008 JetStream 8-Port Gigabit Smart Switch
* \ :sup:`[cbc]` TL-SG3210(UN)V3.0 JetStream 8-Port Gigabit L2+ Managed Switch with 2 SFP Slots
* \ :sup:`[cbc]` TL-SG2218 JetStream 16-Port Gigabit and 2-Port SFP Smart Managed Switch
* \ :sup:`[cbc]` TL-SG3428 JetStream 24-Port Gigabit and 4-Port SFP L2+ Managed Switch
* \ :sup:`[cbc]` TL-SG3428X JetStream 24-Port Gigabit and 4-Port 10G SFP+ L2+ Managed Switch
* \ :sup:`[cbc]` TL-SG3452 JetStream 48-Port Gigabit and 4-Port SFP L2+ Managed Switch
* \ :sup:`[cbc]` TL-SG3452X JetStream 48-Port Gigabit and 4-Port 10G SFP+ L2+ Managed Switch

4.3 PoE Gigabit Switches
~~~~~~~~~~~~~~~~~~~~~~~~

* TL-SG2008P JetStream 8-Port Gigabit Smart Switch with 4-Port PoE+
* TL-SG2010P JetStream 8-Port Gigabit Smart Switch with 8-Port PoE+ and 2-port SFP
* \ :sup:`[cbc]` TL-SG2210MP(UN)V3.0 JetStream 8-Port Gigabit Smart Switch with 8-Port PoE+ and 2-port SFP (high power)
* \ :sup:`[cbc]` TL-SG2428P(UN)V1.0 JetStream 24-Port Gigabit Smart Switch with 24-Port PoE+ and 4-port SFP
* \ :sup:`[cbc]` TL-SG3428MP JetStream 24-Port Gigabit and 4-Port SFP L2+ Managed Switch with 24-Port PoE+
* \ :sup:`[cbc]` TL-SG3428XMP JetStream 24-Port Gigabit and 4-Port 10GE SFP+ L2+ Managed Switch with 24-Port PoE+
* \ :sup:`[cbc]` TL-SG3452P JetStream 48-Port Gigabit and 4-Port SFP L2+ Managed Switch with 48-Port PoE+

4.4 PoE Multi-Gig Switches
~~~~~~~~~~~~~~~~~~~~~~~~~~

* \ :sup:`[cbc]` TL-SX3008F(UN)V1.0 8-Port 10G SFP+ managed switch
* \ :sup:`[cbc]` TL-SX3016F(UN)V1.0 16-Port 10G SFP+ managed switch
* \ :sup:`[cbc]` TL-SG3210XHP-M2 JetStream 8-Port 2.5GBASE-T and 2-Port 10GE SFP+ L2+ Managed Switch with 8-Port PoE+
* \ :sup:`[cbc]` TL-SG3206HPP JetStream 4-Port 10GBASE-T and 2-Port 10GE SFP+ L2+ Managed Switch with 4-Port PoE++ (60W)

5. Load Balance VPN Router
--------------------------

The SafeStream Load Balance VPN routers were designed for small offices as well as the telecommuters. The router can connect up to 4 ISP for voice and data, corporate and private line. You can aggregate bandwidth with the multiple services, or set the rule to direct the certain traffic going to the dedicated line. Easy setup IPSEC VPN and OpenVPN for company connection and personal use. Attack detection and stateful firewall improves your network security. Portal access to personalize your network access. All the tools that everything you need to make the fast an secured connections are set inside the box.

There are two SMB routers in this category ER605 and ER7206. Both of the routers were designed for small offices and remote offices. The ER7206 is in a 9 inches wide metal box and ER605 is 6 inch in width. ER605 has a wall mount slot for easy placement.

.. note::
    TL-SG605 was the previous model number of ER605 and the TL-SG7206 was the previous model number of ER7206. 

5.1 Comparison of the ER7206 and ER605
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+-----------+-----------+
| Model      | ER7206    | ER605     |
+============+===========+===========+
| NAT        | 940Mbps   | 940Mbps   |
| Throughput |           |           |
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
| CBC        | Yes       | Yes       |
+------------+-----------+-----------+

5.2 Key Features
~~~~~~~~~~~~~~~~

There are many features the SafeStream routers can do in a small office environment. The key features are listed here:

* **IPSEC, L2TP, and OpenVPN** The IPSEC is the most popular VPN connection in use in the industry. The SafeStream IPSEC VPN connection can act as a server connecting to the clients remotely at home or at the coffee shop. L2TP (over IPSEC) provides an easier point to point connection through firewalls. OpenVPN is a proprietary, but very popular, VPN connection. You can almost set the end point anywhere and the OpenVPN can connect you through NAT and firewalls with no effort.

* **Load Balance** The SafeStream SMB router can connect up to 4 ISPs. Whether you want to make multiple connections to balance the traffic loads or simply make a connection as a fallback line, the SafeStream router can do the job for you.

* **Digital Phone System Friendly** The SafeStream works with different phone systems. You can enable/disable the SIP ALG. Set the priority route, using ACL to allow or block visitors 

* **Mobility** The ER605 version 2 adding a USB WAN port connecting LTE dongle or 4G hot spot for backup link or mobility.

.. note::
    The OpenVPN feature is only available when the SafeStream router is in the controller model

5.3 Site-to-Site vs. Client-to-Site VPN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The terms are self explained. The site-to-site VPN creates a secure tunnel between two sites. Computers on both sides don’t have to be aware of the existence of the secured tunnel and can communicate to end points on both sites without effort. In Omada SDN, you can create a site-to-site VPN tunnel which simply states which site you want to connect with and then the tunnel can be created.

If you have a single device you want to connect to the office securely. You can set up the client-to-site VPN server on the SafeStream router.

5.4 VPN Capacity
~~~~~~~~~~~~~~~~

VPN secure tunnel requires encryption and decryption to the traffic in both directions. Depending on the method of the encryption and decryption you choose, the passing through speed and tunnel capacity will be different.

+---------------+--------+-------+
| Model         | ER7206 | ER605 |
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

5.5 Load Balance
~~~~~~~~~~~~~~~~

The load balance SafeStream routers provided are not on the datagram based, but on session based. You can set your policy allowing which session going through which router and the session fall back can be performed based on the fall back rules. 

6. Your Deployment, Your Choice
-------------------------------

**Want more flexibility and scalability?**

**You got it!**

**All Omada devices can work with or without a controller, the controller can work with or without the cloud service. You have choices with your network design.**

All Omada SDN solution devices can still work in standalone mode without a controller. The Omada SDN controller can work standalone without TP-Link cloud service. Depending on your design and your preferences, you can choose the way you want your network to behave.

Quick Links
-----------

* :doc:`Omada SDN controller compatible devices</compatibility>`
* :doc:`Omada SDN managed switch naming Convention</introduction/omada_switch_naming>`