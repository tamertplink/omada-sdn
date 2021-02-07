
Installation
============

The most easy way to set up an Omada SDN network is to have an Omada controller first. You can download and install a `software controller on Windows`_ for evaluation or set up.

.. _software controller on Windows: https://www.tp-link.com/us/support/download/omada-software-controller/#Controller_Software

Controllers
-----------

There are three different flavors of controllers in Omada SDN. Hardware, software, and cloud based. All the network control logics on different controllers are the same and it is flexible to move the network settings from one controller to another. The basic network in Omada SDN netowrking is a **site**. A site is a logical network domain and usually is mapping to a physical network. For example a network in a retail store. You can set up a site and move it around on different controllers for flexibility. 

.. image:: /images/controller_compare.png


Standalone Mode
---------------

All the Omada SDN devices can work in standalone mode. No controller required. Just power it on and set up your device through the graphical web interface and it will work. Most of the devices come with the telnet, ssh and SNMP features for CLI control. Please reference the user's manual of the respective product for details.

Installation Guides
-------------------
.. toctree::
   :maxdepth: 1
   
   basic_system_onboarding
   app_ios
   controller_hardware
   controller_windows
   controller_ubuntu
   eap_onboarding