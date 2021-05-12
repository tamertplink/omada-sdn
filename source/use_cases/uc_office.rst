Omada SDN Example : Office Networking
=====================================

.. image:: /images/uc_office.png
    :width: 100%
    :align: center

Company network and Internet access is one of the most important things when you set up an office. The basic planning of an office network including wired networking for data, phone, and video surveillance. As the modern wireless technology changes our way of work, it also changes the way of deploying the office network as well. 

Wired or Wireless?
------------------

If you have a brand new office, wired networking is usually the most efficient and the most cost effective way of setting up the office network. However, as the number of the cubicle increases, the complexity of wiring increases.

If you have your office for over a decade, or you have a building built of bricks and stones, it is not easy to deploy new wires. A total wireless coverage may be a better solution. And, there are more and more wireless desk phones and cameras that you can choose to support the no-new-wire solution.

Integrated services
-------------------

The Omada SDN system is smart and capable enough to support pure data networking, phone networking and video (surveillance) networking. You can build a single network for all three requirements. The built-in SDN feature simplifies the steps of set up to build the VLAN and subnets. Quality of Service features can be automatically deployed from the phone all the way to the PBX and the Internet with the set up on the controller center.

Micro cell or macro cell?
-------------------------

There are mainly two styles of wireless access points designed for office wireless networking, in-wall unit and ceiling mount. The in-wall unit was designed for a small area such as a meeting room or in the manager’s office. It does come with additional network ports for desk phones or other wired devices. The ceiling mount access point can serve more clients with better coverage. Depending on the office layout, you can choose the best access point for that location.

.. image:: /images/uc_office_b_heatmap.png
    :width: 100%
    :align: center

Guest Networking
----------------

You may want to provide a secure guest network for the visitors. Providing a dedicated guest wireless network name (SSID) and preventing access to the company network is important. You can simply create a new wireless name and choose the Guest Networking and then the guest network is set.

.. image:: /images/uc_office_guest.png
    :width: 70%
    :align: center

If you want to control the wired network, you can setup the guest VLAN and management VLAN as well.

Network topology
----------------

A typical office network includes a router, switches and wireless access points. Using a hardware controller to manage the office network is the best choice in most of the cases. The Omada SDN router comes with network load balance and VPN features. You can connect up to 4 ISPs to balance the data usage or prioritize the traffic.


.. image:: /images/uc_office_topo.png
    :width: 100%
    :align: center