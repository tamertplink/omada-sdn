Omada SDN Example : Airbnb
==========================

.. image:: /images/uc_airbnb.png
    :width: 100%
    :align: center

Sharing an additional house or an extra bedroom through Airbnb can turn your property to a cash cow and meet some new friends at the same time. To make your guest feel like at home , you will want to provide a good guest WiFi connection with a good control.

Most of the Airbnb hosts start providing WiFi service with a soho router with the guest network features. That will work to share the Internet, but totally no control of it. For traffic control or preventing legal issues, you may want a better system to manage the network.

Guest Networking
----------------

The first thing you want to control is separate the guest network to your home wireless. Provide a dedicated guest wireless network name (SSID) and prevent access to the home network is important. And, it is easy to set up on the Omada SDN. Just create a new wireless name and choose the **Guest Networking** and then everything is set.

.. image:: /images/uc_airbnb_guest.png
    :width: 50%
    :align: center


Bandwidth management
--------------------

.. image:: /images/uc_airbnb_rate_limit.png
    :width: 70%
    :align: center

You want to share a handsome amount of bandwidth to your guest, but don’t want all the bandwidth taken by the guest. Most of the guest clients require the most 3 ~ 5Mbps for HD video streaming. You can limit the bandwidth by the wireless ID, or by the client. Just attach the rule to the wireless or the client and the SDN system will do the rest for you.

Password management
-------------------

.. image:: /images/uc_wifi_password.jpg
    :width: 30%
    :align: center

Sharing a fixed password can leave your Internet access with no control. The voucher login feature in Omada SDN can expire a password after a fixed amount of time automatically. You can have a piece of mind not worrying unauthorized access with the fixed password.

.. image:: /images/uc_airbnb_voucher.png
    :width: 90%
    :align: center

Furthermore, you can monitor the client activities to log the time when guests are coming and leaving.
    
VPN and content filtering
-------------------------

Omada SDN router comes with website address filtering and VPN connection capabilities. You can create separate login passwords for family members. Filtering contents as a way of parental control.

.. image:: /images/uc_airbnb_vpn.png
    :width: 60%
    :align: center

In another situation, you may want to protect your ISP account, not to be listed by your ISP as abused for illegal download, you want to set the VPN for your guest connection as a legal protection. The Omada SDN router can do all that for you.


Promotion
---------

Omada SDN comes with the Facebook WiFi and portal advertising feature. User may log in to the WiFi using Facebook log in. no new username or password to setup by you. At the sametime, optional Facebook check-in can increase your exposure on popular social media.

.. image:: /images/uc_airbnb_portal.png
    :width: 100%
    :align: center

A portal advertising page can be shown when the user is logged in. You can provide local information, emergency contact information, housing rules, or link for local resources. Easy notifications for every guest.

.. image:: /images/uc_airbnb_ad.png
    :width: 60%
    :align: center

Indoor, Outdoor, and multi-levels
---------------------------------

If you do have multiple levels for your residency and the guest rooms. Or, if you have a beautiful backyard that needs a good WiFi connection, you can add more EAP wireless access points. Once the additional access point is powered up and adopted, all your settings will apply to the new access point. When you want to make a change, simply change the settings on the controller and the controller will distribute the commands to all connecting devices.

.. image:: /images/uc_airbnb_topo.png
    :width: 85%
    :align: center