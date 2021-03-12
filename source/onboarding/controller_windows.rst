
Omada Controller Installation on Windows System
===============================================

.. note::
    This installation guide is based on Omada controller version 4.2.8. For installation guide on previous versions, please visit the software download site to download the user's guide on your version. https://www.tp-link.com/us/support/download/omada-software-controller/

.. note::
    The Omada SDN software is a version 4 controller and does not compatible to legacy EAP devices. Please check this `list`_ for compatibility.

.. _list: https://www.tp-link.com/us/omada_compatibility_list/

Software
--------

You can download the Omada SDN Windows controller 4.2.8 `here`_.

.. _here: https://www.tp-link.com/us/support/download/omada-software-controller/#Controller_Software

Prerequisite
------------

You can run the Omada controller with minimum hardware requirements recommended by Windows system. In the production environment serving up to 1,500 devices with the controller, the following hardware is recommended:

* CPU: Intel Core i3-8100, i5-6500, or i7-4700 with 2 or more cores and 4 or more threads. 
* Memory: 6 GB RAM or more

Compatible Windows versions (64-bit versions of Windows on x86_64 architecture):

* Windows 10 / Windows Server 2016
* Windows 8.1 / Windows Server 2012 R2
* Windows 8 / Windows Server 2012
* Windows 7 / Windows Server 2008 R2

Installation
------------

Follow the instructions to install the Omada software controller. After the software installation, the controller will be launched and your default web browser will lead you to https://localhost:8043, the Omada controller default url.


.. note::
    A "Your connection is not private" warning may pop up due to the private security was used by default on the controller. Please choose the advanced option and accept the way of access. You can setup your own SSL key to remove this warning.

.. image:: /images/connection_is_not_private.png
    :width: 50%
    :align: center

