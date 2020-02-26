# AddressMacNetworkWatcher
Local network notification app

You'll also need superuser privileges to run `arp-scan`, you have have a few
options but be sure to understand what you're doing before you do it:

* Edit `/etc/sudoers` to allow user to run `arp-scan` as root without a
  password.

	`user host = (root) NOPASSWD: /usr/bin/arp-scan`
* Check `arp-scan` bin location:

   `which arp-scan`

* Set the SUID bit on the `arp-scan` bin:

	 `sudo chmod u+s <which output>`
