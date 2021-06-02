Omada SDN Example : School Campus
=================================

.. image:: /images/uc_school_campus.jpg
    :width: 100%
    :align: center

There are multiple buildings, stadiums, auditoriums in a school campus. Other than the network distribution on the same physical location, the way connecting different buildings together is important as well.

Fiber optic communication
-------------------------

Fiber optic communication is the straightforward solution that comes to mind in most of the network planning. It is the most efficient and the most flexible solution for long distance communication. TP-Link provides different optical connectivities to build different types of optical fiber network in a campus.

Single mode vs. multi-mode
^^^^^^^^^^^^^^^^^^^^^^^^^^

When choosing the fiber and fiber modules, you need to decide you are going with the single mode fiber or multi-mode fiber. The single mode fiber has a simplified light path and then can deliver the data for a longer distance. It has higher quality requirements and is more expensive. Multi-mode fiber has better physical tolerance and the distance of communication is shorter.

Duplex or simplex
^^^^^^^^^^^^^^^^^

Duplex optical communication using one fiber for data in a single direction. The two way data communication requires two fibers to build the link. The simplex optical module, using various WDM technologies, separates different directions of the light in different wavelengths. So, a two way communication on a single fiber can be build.

Media converter
^^^^^^^^^^^^^^^

The media converters are independent devices converting the copper communication to fiber optic communication. Here’s a list of the media converters:

.. figure:: /images/media_converter_gigabit.png
    :width: 100%
    :align: center

    Gigabit media converters

.. figure:: /images/media_converter_fe.png
    :width: 100%
    :align: center

    100Mbps media converters

SFP/ SFP+ Modules
^^^^^^^^^^^^^^^^^

Many of the Omada SDN switches has SFP for gigabit or SFP+ for 10G fiber optic modules. Here's a list of the compatible modules:

.. figure:: /images/sfp_modules.png
    :width: 100%
    :align: center

    Gigabit and 10G SFP/SFP+ fiber modules 

10G uplink managed SDN switches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here's the list of the SDN managed switches that supports SFP+ 10G fiber communication.

+--------------+-----------------+-------------+--------------+-------------+-------------+
| Model        | TL-SG3210XHP-M2 | TL-SG3428X  | TL-SG3428XMP | TL-SG3452X  | TL-SG3452XP |
+==============+=================+=============+==============+=============+=============+
| Access Ports | 8x 2.5G         | 24x Gigabit | 24x Gigabit  | 48x Gigabit | 48x Gigabit |
+--------------+-----------------+-------------+--------------+-------------+-------------+
| Uplink ports | 2x 10G SFP+     | 2x 10G SFP+ | 2x 10G SFP+  | 2x 10G SFP+ | 2x 10G SFP+ | 
+--------------+-----------------+-------------+--------------+-------------+-------------+
| PoE          | 240W            | --          | 384W         | --          | 384W        |
+--------------+-----------------+-------------+--------------+-------------+-------------+

Fiber aggregation switches
^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two 10G switches that can aggregate all the fiber connections and managed by the Omada SDN controller

+-------------+------------+------------+
| Model       | TL-SX3008F | TL-SX3016F |
+=============+============+============+
| Capacity    | 160G       | 320G       |
+-------------+------------+------------+
| Fiber Ports | 8          | 16         |
+-------------+------------+------------+