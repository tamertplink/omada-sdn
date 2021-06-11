Omada SDN Example : Student Housing
===================================

.. image:: /images/uc_student_housing.jpg
    :width: 100%
    :align: center

In student housing, the Internet is provided by the housing authority instead of individual subscriptions directly to the ISP. Unlike the office deployment, the student housing deployment has its own unique challenges.

IDF setup
---------

Choosing an Intermediate Distribution Frame, IDF, location has its limitations compared to the multi dwelling unit, MDU, deployment to the office building deployment. You may need to install the IDF in the wall. And, the requirement of the noise level, heat dissipation, and power consumption will be different than in the server room.

.. image:: /images/uc_student_housing_box.png
    :width: 30%
    :align: center

Network port protection 
-----------------------

There might be network ports exposed in the residency. And, they can be used only with assigned devices. The Omada SDN can help to protect the network from illegal access with MAC binding, ACL ruling, or management VLAN implementation.

High density
------------

The Omada EAP can handle different numbers of client associations at the same time. The EAP660 HD and EAP620 HD can associate up to 1,024 clients and EAP265 HD can handle up to 620 associations.
For the traffic capacity, the lab test shows the EAP is capable of delivering 30 HD Netflix streaming with no waiting and no buffering.
