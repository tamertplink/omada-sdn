Adding your own HTTPS certificate to the controller
===================================================

.. image:: /images/rp_qr_code.jpg
    :width: 100%
    :align: center
 
We’ve gone through the most difficult time. The COVID19 forced us to close the stores to prevent the spread of the virus. Now, we are opening our business again. And, we are opening carefully and not letting the variant virus shut us down again.
eMenu is one of the popular strategies for restaurants reducing the contact over the  COVID19 close down period. And, it remains popular for its possible interaction and low service cost.
 
The Online version (with cell phone data)
-----------------------------------------
 
The easiest way to build an eMenu is building a website and making a QR code for customer scanning on the table.
 
The website
^^^^^^^^^^^
 
There are many free services for simple website hosting, such as Google Business (http://www.google.com/business) You can simply take a picture of your paper menu, or you can upload your menu book and organize it with the web design tools. 
 
You are will have a unique web address for your online menu such as http:// {your_business_name}.mybusiness.site for Google myBusiness. We can then use this web address making the QR code in the next step.
 
The QR code
^^^^^^^^^^^
 
Search the free tool online to create QR code representing your menu site.

Here is an example with Free Generator QR Online (https://free-qr.com/)

.. image:: /images/rp_qr_generator.png
    :width: 70%
    :align: center

1. Choose the **Link** as the data type.
2. Enter the Link (URL) with your menu website address.
3. Click **Generate QR Code**
4. Download the QR code

Then, you can print the QR code on the paper that sits on the table for scanning. 

And that’s it. You have the most simple eManu setup.
 
The Online Version (with local WiFi)
------------------------------------
 
Creating the Online eMenu is quick and easy, but the previous set up relies on the data usage of your customers’ data plan. If the cell phone connection is not be good at your location or you simply want to provide a more responsive eMenu, you can provide a local WiFi access.
 
You need a wireless access point with portal authentication feature to connect the phone to the store WiFi, and then redirect the connection to your eMenu. You need wireless access points which is capable signing in new client and redirect the traffic to designated location. The feature is portal authentication. All Omada EAP access supports the portal authentication. You can set up a single EAP in standalone mode or multiple EAP in controller mode with this feature.
 
Set up WiFi Portal in standalone mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
1. Login to your EAP by entering the IP address or http://tplinkeap.net
 
2. Create an SSID with or without password. This wireless is going to be public accessed, the security is not the focus in this use case.

.. image:: /images/rp_table_qr_code.jpg
    :width: 70%
    :align: center
 
3. Create a portal profile and connect to the SSID you have created
 
4. Check the redirection option 
