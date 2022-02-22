Adding your own HTTPS certificate to the controller
===================================================

.. note::

  This recipe is only good for hardware controllers (OC200 or OC300) or software controllers, not for cloud-based controller (CBC). When installing the HTTPS certification, you have to use the direct access to the controller. Remote access through the cloud connection is not going to work (url starts with https//:omada.tplinkcloud.com).

This recipe demonstrates how to add a X.509 certificate on a controller version 5.0 and above. You can set up the HTTPS certificate to the previous version of controllers. A better resource on howto install the certificate on controller 2.7 and above is available on the community post https://community.tp-link.com/en/business/forum/topic/150083

 
Prerequisite
------------
 
* You need a public URL registered with a domain service, the signed X.509 certificate and chain certifications. Most of the CA service providers are giving out the .pem X.509 certificate and .crt chain certificates. 

* The controller accepts the Java key store file to store the HTTPS certificate. Therefore, you need the OPENSSL app to transformat the X.509 format to PKCS format and then use Java  TOOLKIT utility to make the key store.

* To upload the HTTPS Java key store, you need to visit your controller directly, accessing the controller through cloud connection is not going to work.

The certificate
---------------
 
In this recipe, we use let’s encrypt as the CA signing our certificate with certbot client tool. The example domain is mydomain.com. In Linux command line, you can get the certificate like this:

.. code-block:: bash

    ./certbot-auto certonly --standalone --preferred-challenges http -d mydomain.com

Your certificate may store in the following directory, together with other necessary files:

.. code-block:: bash

    Successfully received certificate.
    Certificate is saved at: /etc/letsencrypt/live/mydomain.com/fullchain.pem
    Key is saved at:         /etc/letsencrypt/live/mydomain.com/privkey.pem
 
Transform the certificate format
--------------------------------
 
To transform the X.509 format to PCKS12 format, you need the openssl.

An example command can be:

.. code-block:: bash

    openssl pkcs12 -export \
    -in /etc/letsencrypt/live/mydomain.com/cert.pem \
    -inkey  /etc/letsencrypt/live/mydomain.com/privkey.pem \
    -out mydomain.com.p12 \
    -certfile /etc/letsencrypt/live/mydomain.com/chain.pem \
    -name eap

* **openssl:** The name of the app
* **pkcs12:** The PKCS format of certificate file
* **-export:** export the certificate to a file
* **-in:** loading the X.509 file, following with the file path name of the X.509 certificate.
* **-inkey:** loading certificate private key, following with the file path name of the private key.
* **-out:** specify the output file name, we use mydomain.com.p12 here and you can choose an appropriate name yourself.
* **-certfile:** loading the chain of the certifications, following with the file path name of the certification file.
* **-name:** the name of this certificate. Please keep it as eap so you don't have to change the controller property settings.
* **(When prompted to enter the password):** The app will prompt to ask adding a password for this certificate. Enter any legal password. We use the **epac** as the password in this recepie.
  
Installing the certificate in a Java keystore
---------------------------------------------
 
The keytool app is coming with your previous installed JVM 8. Enter the command like this to create a java key store.

.. code-block:: bash

    keytool -importkeystore \
    -destkeystore myDomain.jks \
    -deststorepass keyStorePassword \
    -destkeypass keyPassword \
    -srckeystore mydomain.com.p12 \
    -srcstoretype PKCS12 \
    -srcstorepass eapc

* **keytool:** The name of the app
* **-importkeystore:** Asking the app to import a key to the key store.
* **-destkeystore:** export the key store to a file. You can change the name to a preferred one. We use **myDomain.jks** as the file name here.
* **-deststorepass:** The destination key store password. Setup your own key store password here.
* **-destkeypass:** The destination private key password. Setup your own private key password here.
* **-srckeystore:** specify the name of the PCKS key file name. **mydomain.com.p12** in this example.
* **-srcstoretype:** The type of the certificate. Enter **PCKS12** as the type
* **-srcstorepass:** The key password you have set in previous step. Enter **epac** if you enter the same password in this recepie.

Upload the Java keystore file to the controller
-----------------------------------------------

.. image:: /images/https_import.png
    :align: center

Click on the **Import** button to choose the java key store we've just created. And then, enter the keystore password and private key password. Then, scroll down to click on the **Save** button to save the change.

Reboot the controller
---------------------

You need to restart the controller to make it in effect. Go to **Maintenance > Reboot** to reboot your controller.

.. image:: /images/reboot.png
    :width: 70%
    :align: center

Now you can visit your domain url with the port in your settings

.. image:: /images/controller_port.png
    :width: 70%
    :align: center

.. note::

  1. The google browser may remember your last visit to the url and complain with the cert_err. Try to visit the url with incognito mode.
  2. In incognito mode, the google chrome may complain **Bad Request, This combination of host and port requires TLS.** Please just change the port number (80 or 8088) with HTTP. The controller will then redirect to HTTPS with signed TLS.