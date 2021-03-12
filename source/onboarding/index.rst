
Installation
============

The Omada SDN was designed as a complete system with center control. In the real world installation, you may find the use case requires third party product integration. Omada SDN products are flexible to that request. You can set and use the device standalone or managed by a controller. When Omada SDN product works in standalone mode, it can be integrated into other software define networking system through traditional telnet, SNMP, or CLI over console port. You can also control the devices through CLI over SSH and controlled by the Ansible playbook. 

Cloud or No Cloud
-----------------

It is your decision to use TP-Link cloud services or not. The **TP-Link cloud directory service** provides an easy way to discover and connect to your device and get notification from the system. TP-Link cloud directory service shares the account credential over different systems. If you already in use one of the TP-Link product, the Kasa, Deco, Tapo, or Vigi, you probably have the service account already. If you want to total control your Omada SDN network, you can still do it with some manual set ups. the cloud directory service is not required to build the network. However, it is required if you want to receive notification on your mobile phone. This service is free.

**TP-Link Omada Cloud Based Controller** is a Omada network controller maintained by TP-Link. It is a subscription based service with annual fee. Check the `product page`_ for price details. The cloud based controller has all the features comes with the software controller and the hardware controller. The extra benefit is that it is backed by TP-Link AI server for extra zero touch provisioning and automatic wireless power and channel adjustment features.

.. _product page: https://www.tp-link.com/us/business-networking/omada-sdn-controller/omada-cloud-based-controller/


Choose your controller
----------------------

There are three different flavors of controllers in Omada SDN. Hardware, software, and cloud based controller. All the controllers designed with the same network logic and it is flexible to move the network settings from one controller to another. If Omada SDN is new to you and you want just to experience it, you can simply download a free Omada software controller to have an initial try. 

The basic network in Omada SDN network is a **site**. A site is a logical network domain and usually is mapping to a physical network. For example a network in a retail store. You can set up a site and move it around on different controllers for flexibility. 

When you are done with the proof of the concept, you can prepare a dedicate server for the software controller. Or, you can simply buy a preinstalled controller hardware. Depends on the number of devices you are going to manage, you can choose different controllers. As always, you can move the **site** from one controller to another to scale up or scale down your management.

+---------------+-------+-------+---------------------+------------------------+
| Model         | OC200 | OC300 | Software Controller | Cloud based controller |
+===============+=======+=======+=====================+========================+
| Max. Devices  | 100   | 500   | 1,500               | Subscription based     |
+---------------+-------+-------+---------------------+------------------------+

An Example Basic Network Setup 
------------------------------

You can follow through this set up example to experience the complete system setup from the beginning to the end. `An example setting up a basic network`_

.. _An example setting up a basic network: ../recipes/recipe_basic_system.html

Installation Guides
-------------------

Other step by step set up guides are listed here:

.. toctree::
   :maxdepth: 1
   

   app_ios
   app_android
   controller_hardware
   controller_windows
   controller_ubuntu
   eap_onboarding
   ssh