iOS Hotspot Proxy
=================

Cellular traffic proxy for ad hoc network on iOS. No jailbreak. Need Python for iOS.


In A Nutshell
=============

When iOS device connects to ad hoc network (Mac computer-to-computer network), it can still access the internet via device's 2G/3G/4G channel. Your laptop is connected to the iOS device, and your iOS device is connected to the internet. Ta-da! Your laptop is connected to internet!

How It Works
============

Python 2.7 for iOS can run python scripts! With common libraries! A simple multithreading with socket programming does the trick. The Python script listens to the ad hoc network and acts as a proxy. When receiving the request from laptop, it connects to a remote proxy and bidirectionally forwords the traffic.

Prerequisite
------------

* Download the Python 2.7 for iOS
* Run your proxy and make it public
* Modify PROXYHOST, PROXYPORT in proxy.py with you public proxy info
* Copy the script to Python 2.7 for iOS

Do the Magic
------------

* Create ad hoc network from your laptop
* Connect your iOS device to your laptop
* Assign two different IP for these two devices
* Set appropriate subnet mask, of course
* Leave the router address empty on iOS device
* Ping your iOS device from you laptop, it should work
* Change your laptop global http/https proxy configuration, use the iOS device IP and proxy port, default 50007
* Open your browser and enjoy

TODO
====

Pipe the socket or implement the actual proxy

License
=======

BSD

What I Want to Say
==================

* Better than the single thread websocket solution.
* Python multiprocessing lib doesn't work well in that app
* I use appshopper.com to watch that app's price. Half year's waiting and missed $0.99 deal on Apr 16 '13
* Adium needs to use global http/https proxy setting
* Use your finger to keep the screen active
* It can **warm** your heart when proxying
* Sprint 3G network sucks! Especially for my 4s
* Please press CTRL + W if you don't understand the project