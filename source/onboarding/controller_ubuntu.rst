
Install Omada Controller on Ubuntu or Debian
============================================

You can install the Omada Software Controller on Ubuntu or Debian 64-bit distribution. The Omada controller is operating on JVM with MongoDB database. 

.. note::
    This installation guide is based on Omada controller version 4.2.8. For installation guide on previous versions, please visit the software download site to download the user's guide on your version. https://www.tp-link.com/us/support/download/omada-software-controller/


Prerequisite
------------

You can run the Omada controller with minimum hardware requirements. Even on the Raspberry Pi3. In the production environment serving up to 1,500 devices with the controller, the following hardware is recommended:

* CPU: Intel Core i3-8100, i5-6500, or i7-4700 with 2 or more cores and 4 or more threads. 
* Memory: 6 GB RAM or more

Required software:

* Ubuntu version 14.04 or 16.04 **64-bit** 
* JRE version 8
* MongoDB version 3.0.15 ~ 3.6.18 (V3.6 is recommended)
* jsvc
* curl
* Omada Software Controller

Java Runtime Environment
------------------------

Run this command to install the JRE from your Ubuntu repository.

.. code-block:: bash

    sudo apt-get install openjdk-8-jre-headless


MongoDB 3.0.15 ~ 3.6.18
------------------------

Follow the instructions to install MongoDB 3.4 or visit this `link`_. to view more options.

.. _link: https://docs.mongodb.com/v3.4/tutorial/install-mongodb-on-ubuntu/


::

    sudo apt-get install openjdk-8-jre-headless
