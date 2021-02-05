
Omada Enterprise Access Point, EAP
==================================

There are different ways to group the Omada EAP. The Omada EAP6xx series has WiFi 6 access points. The EAP2xx series has 802.11ac wave 2 (WiFi 5) access points and the The EAP1xx series has classic 802.11n access points. The EAP3xx series has been end of life since 2018.

Here's a quick comparison of the Omada EAPs

High density series:

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

Ceiling mount EAPs:

+------------+-----------+-----------+-----------+
| Model      | EAP245    | EAP225    | EAP115    |
+============+===========+===========+===========+
| Class      | 802.11ac  | 802.11ac  | 802.11n   |
+------------+-----------+-----------+-----------+
| Speed      | AC1750    | AC1350    | N300      |
+------------+-----------+-----------+-----------+

Other EAPs:

+------------+----------------+----------------+-------------+--------------+
| Model      | EAP225-Outdoor | EAP110-Outdoor | EAP235-Wall | EAP225-Wall  |
+============+================+================+=============+==============+
| Class      | 802.11ac       | 802.11n        | 802.11ac    | 802.11ac     |
+------------+----------------+----------------+-------------+--------------+
| Speed      | AC1200         | N300           | AC1200      | AC120        |
+------------+----------------+----------------+-------------+--------------+
| Ethernet   | Gigabit        | 10/100         | Gigabit     | 10/100       |
+------------+----------------+----------------+-------------+--------------+

Standalone mode
---------------

With the mobile app
~~~~~~~~~~~~~~~~~~~

You can set up the EAPs using the Omada app for `Apple`_ or `Android`_ with this `video`_.

.. _Apple: https://apps.apple.com/app/id1327615864
.. _Android: https://play.google.com/store/apps/details?id=com.tplink.omada
.. _video: https://youtu.be/m_i8qROEwuk

The Omada app is a very useful tool to set up and manage your Omada devices. You can use it to discover and install the EAP now. Later on, you can use the same app to install the controller, switch, and router. You can also monitor your network on the go.

With the desktop tool
~~~~~~~~~~~~~~~~~~~~~

If you like the classic way to set up your EAP, you can connect your computer wireless to the EAP and set it up using web browser.

.. note::
    Before set up your EAP, make sure your EAP is with factory default setting. To make the EAP back to the factory default, first, power on your EAP and wait 30 seconds for boot up. The LED will become solid green when the boot sequence has done. The reset button is near by the Ethernet network port. Find a pin and press the reset button all the way until the LED starts blinking. Waiting for another 30 seconds for EAP boot up and ready to use.

1. Connecting to the EAP. Find the TP-LINKxxxx SSID and connect with it. No password is required for the setup SSID.
2. Type the tplinkeap to get the web login page.

.. note::
    For advanced user, the EAP with get the dynamic IP if the DHCP server is available and it has an fallback IP 192.168.0.254 if the DHCP is not available. 

