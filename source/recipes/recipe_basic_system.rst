Recipe: Setup a basic network
=============================

This example demonstrates the most easy way to set up a basic network. You can of course mix and match the different combinations of the devices to fit your need. Here we just choose one typical network and a smooth way of installation. You can read other sections of this document for more detail.

1. Bill of material
-------------------

* ER605 (TL-R605) router
* TL-SG2008P switch, 8-port gigabit switch with 4 port POE
* EAP225
* OC200
* Android Phone or iPhone

2. Topology
-----------

.. image:: /images/topology_basic.png
    :width: 70%
    :align: center

Connecting your devices with above topology

* Connect the LAN port of your ISP gateway to the ER605 WAN port
* Connect the ER605 LAN port to one of the TL-SG2008P non-PoE port (port 5 to port 8)
* Connect the OC200 LAN port to one of the TL-SG2008P PoE port (port 1 to port 4)
* Connect the EAP225 LAN port to one of the TL-SG2008P PoE port (port 1 to port 4)
* Make sure all the devices have the latest firmware and with the factory default setting

Power them up and wait for the system checking and booting. The boot up time is longer than the SOHO products for more features to kick up. Wait for 5 minutes and check the status lights. If the OC200 **Cloud** LED is blinking. It means the OC200 has the Internet access everything is ready. If not, double check the wiring and reset the devices again to make sure they are all in the factory default state.

.. note::
    The ER605/ER7206 has default network set to 192.168.0.1. If your ISP gateway was set to the same local subnet, you can remove the ER605/ER7206 from the topology for now. We can add it back later.

3. System Installation
----------------------

Reference this page to install the OC200 :doc:`/onboarding/controller_hardware`

Log into the Omada cloud portal at http://omada.tplinkcloud.com, click on the the |omada_launch| icon to launch the controller. The setup wizard will show up for the first time setup. Click **Let's Get Started**

.. |omada_launch| image:: /images/omada_launch.png
    :height: 16

.. image:: /images/omada_controller_setup_1.png
    :width: 50%
    :align: center

Name your controller, select the country or region, and your timezone. Choose one of the scenario that make sense to your application. Then click on the **Next**

.. image:: /images/omada_controller_setup_2.png
    :align: center

The OC200 controller will discover all the devices connected. Select all devices and then click on the **Next**

.. image:: /images/omada_controller_setup_3.png
    :align: center

Enter the wireless ID (SSID) and password and then click on **Next**

.. image:: /images/omada_controller_setup_4.png
    :align: center

Enter the administrator name. This administrator name is different and not related to the cloud account ID. You can use this credential to access the controller directly when you have the local access. The email address is for notifications. You have to setup the SMTP server later to enable the email notification. Enter all the information and then click on the **Next** button.

.. image:: /images/omada_controller_setup_5.png
    :align: center

Review all the settings and then click on the **Finish**. If you want to change the settings, click on the **Back** button.

.. image:: /images/omada_controller_setup_6.png
    :align: center

The system setup is done by now. You can then click through the overview to familiar with the user interface.

.. image:: /images/omada_controller_setup_7.png
    :align: center

3. Customizations
-----------------

Double check if all the devices are adopted. Check on the :doc:`/faq/faq` for trouble shootings.

The Omada gateway default LAN IP is 192.168.0.1, you can change this IP if it conflicts to your other subnet. Or, you simply have a preset number of the subnet that is not 192.168.0.0/24. Please reference this tutorial to change your LAN IP address: :doc:`/recipes/recipe_LAN_edit`