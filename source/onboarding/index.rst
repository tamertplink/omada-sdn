
Installation
============

The most easy way to set up an Omada SDN network is to have an Omada controller first. You can download and install a `software controller on Windows`_ for evaluation or set up.

.. _software controller on Windows: https://static.tp-link.com/2020/202012/20201211/Omada_Controller_V4.2.8_Windows.zip

Controllers
-----------

There are three different flavors of controllers in Omada SDN. Hardware, software, and cloud based. All the network control logics on different controllers are the same and it is flexible to move the network settings from one controller to another. The basic network domain is a site. A site is a logical network domain and usually is mapping to a physical network. You can set up a site and move it around on different controllers for flexibility. 

.. image:: /images/controller_compare.png


Standalone Mode
---------------

All the Omada SDN devices can work in standalone mode. No controller required to make it work.

.. toctree::
   :maxdepth: 1
   
   eap_onboarding
   controller_windows
   controller_ubuntu

