Recipe: Change the LAN IP addresses
===================================

To change a LAN IP addresses, you need the Omada SDN router ER605 or ER7206 installed on your site.

Go **Settings > Wired Networks > LAN** and then click on the |edit| icon to change the LAN addresses.

.. |edit| image:: /images/omada_edit.png
    :height: 16

.. image:: /images/omada_controller_LAN_edit.png
    :align: center

Go head to change the **Gateway/Subnet**. Then, click on the **Update DHCP Range** to update the DHCP range. And then, double check if the DHCP range is what you want. Click **Save** to save the settings.

.. Note::
    After the LAN subnet change, the Omada gateway will reboot and change its LAN address to the new one. However, all the connecting devices are not going to aware the change before the DHCP expired. By default, it is 120 minutes. If you have physical access to the device, simply unplug and plugin again the network cable will refresh the DHCP lease. If you update the network remotely and don't want to wait for two hours until the DHCP expiration. Please change the lease time first. Reboot all the devices to make sure they all have the updated lease time. Then do the LAN address change. Remember to change the lease time back to longer period of time after setting for better network efficiency.