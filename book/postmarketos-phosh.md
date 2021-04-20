<meta name="title" content="Using postmarketOS Phosh on Pinephone for a Daily Driver">

# Using postmarketOS Phosh on the Pinephone

After trying out a number of mobile Linux OSes with the [multi-distro demo image](pinephone-multidistro.html), I decided to go with postmarketOS Phosh, since it's the only one that met the base requirements for a daily driver.

### Installing PostmarketOS Phosh and apps

It turns out it's not possible to install OSes directly from the multi-boot image, but the multi-boot image does contain Jumpdrive, which allows images to be flashed directly to the eMMC from a desktop via USB. Use `dd` to flash the image to the eMMC.

Initial update would not work through Software app. Instead, I used `apk upgrade -i` in the terminal, and it worked. `apk` is the package manager for Alpine, which postmarketOS is based on.

I'm still not seeing any apps that aren't already installed in the *Software* app. But using `apk add` I can install whatever I need from the terminal.