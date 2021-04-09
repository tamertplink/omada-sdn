
Omada Controller Installation on Windows System
===============================================

.. note::
    This installation guide is based on Omada controller version 4.2.11. For installation guide on previous versions, please visit the software download site to download the user's guide on your version. https://www.tp-link.com/us/support/download/omada-software-controller/

.. note::
    The Omada SDN software is a version 4 controller and does not compatible to legacy EAP devices. Please check this `list`_ for compatibility.

.. _list: https://www.tp-link.com/us/omada_compatibility_list/

1. Software
-----------

You can download the Omada SDN Windows controller 4.2.11 `here`_.

.. _here: https://static.tp-link.com/2021/202102/20210209/Omada_Controller_V4.2.11_Windows.zip

2. Prerequisite
---------------

You can run the Omada controller with minimum hardware requirements recommended by Microsoft. In the production environment serving up to 1,500 devices with the controller, the following hardware is recommended:

* CPU: Intel Core i3-8100, i5-6500, or i7-4700 with 2 or more cores and 4 or more threads. 
* Memory: 6 GB RAM or more

Compatible Windows versions (64-bit versions of Windows on x86_64 architecture):

* Windows 10 / Windows Server 2016
* Windows 8.1 / Windows Server 2012 R2
* Windows 8 / Windows Server 2012
* Windows 7 / Windows Server 2008 R2

3. Software Installation
------------------------

Step 1. Download and unzip the Omada controller. Click the **Extract All**

.. image:: /images/controller_windows_01.png
    :width: 40%
    :align: center

Step 2. Click on the |Omada_Software| to start installation. 

.. |Omada_Software| image:: /images/controller_windows_03.png
    :height: 18

Step 3. Click **Run** to confirm the installation.

.. image:: /images/controller_windows_04.png
    :width: 50%
    :align: center

Step 4. Click **Next**

.. image:: /images/controller_windows_05.png
    :width: 50%
    :align: center

Step 5. Change the installation folder or allow the installer choose the default install location. Then click **Next**

.. image:: /images/controller_windows_06.png
    :width: 50%
    :align: center

Step 6. Click **Install** to start copying the files.

    .. image:: /images/controller_windows_07.png
        :width: 50%
        :align: center

Step 7. Click **Finish** to finish the installation and starting the Omada controller.

    .. image:: /images/controller_windows_08.png
        :width: 50%
        :align: center

Step 8. Depends on the computer you are installing the controller, you may wait for less than a minute or a couple of minutes to bring the server on. Once you've got the confirmation. You can click on the **Launch a Browser to Manage the Network**

    .. image:: /images/controller_windows_10.png
        :width: 50%
        :align: center

Your default web browser will lead you to https://localhost:8043, the Omada controller default url. If you want to access the controller from other computer, please setup the Windows firewall opened at port 8088 for http and 8043 for https. The http port is just for the connectivity. The communication is going through https.

.. note::
    A "Your connection is not private" warning may pop up due to the self-signed private security used by the controller. Please choose the advanced option and accept the way of access. You can setup your own SSL key to remove this warning after setting.

.. image:: /images/connection_is_not_private.png
    :width: 50%
    :align: center

4. Controller Initialization
----------------------------

Step 1. Click **Let's Get Started** to initialize the software controller

.. image:: /images/omada_controller_setup_1.png
    :width: 50%
    :align: center

Step 2. Name your controller, select the country or region, and your timezone. Choose one of the scenario that make sense to your application. Then click on the **Next**

.. image:: /images/omada_controller_setup_2.png
    :align: center

Step 3. The controller will discover all the devices connected. Select all devices and then click on the **Next**

.. image:: /images/omada_controller_setup_3.png
    :align: center

Step 4. Enter the wireless ID (SSID) and password and then click on **Next**

.. image:: /images/omada_controller_setup_4.png
    :align: center

Step 5. Enter the administrator name. This administrator name is different and not related to the cloud account ID. You can use this credential to access the controller directly when you have the local access. The email address is for notifications. You have to setup the SMTP server later to enable the email notification. Enter all the information and then click on the **Next** button.

.. image:: /images/omada_controller_setup_5.png
    :align: center

Step 6. Review all the settings and then click on the **Finish**. If you want to change the settings, click on the **Back** button.

.. image:: /images/omada_controller_setup_6.png
    :align: center

Step 7. The system setup is done by now. You can then click through the overview to familiar with the user interface.

.. image:: /images/omada_controller_setup_7.png
    :align: center

More Readings
-------------

:doc:`/recipes/recipe_basic_system`