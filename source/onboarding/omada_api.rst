Control your Omada system through the API
=========================================
 
The API document
----------------
There is no official Omada API document available, but you can find the Omada version 2 API in the community posts. Here’s the quick links for the API documents: 
 
`Omada_SDN_Controller_V4.1.5 API Document.zip <https://static-community.tp-link.com/attach/22/2/2021/9f2bea8b9cf74b51867d15219858d7ef.zip>`_
 
`Omada_SDN_Controller_V5.0.15 API Document.zip <https://static-community.tp-link.com/attach/7/2/2022/5bf7cfe185134370b9b5ea453f017f83.zip>`_
 
 
 
 
A simple Python wrapper for the Omada controller API
----------------------------------------------------
 
And, here is a good example demonstrating how to access the Omada controller by turning the LED on or off.
 
https://github.com/ghaberek/omada-api
 
These codes work with version 4 controller. Visiting version 5 controller, you need to tweak the codes a little bit. Compared to Omada SDN Controller v4, the main changes are as follows:
 
1. Add Controller ID to the URL.
2. Add the HTTP header, which carries the CSRF Token.

More details of the changes and sample codes are available here: https://www.tp-link.com/us/support/faq/3231/
