# PinePhone Log

Mobian Community Edition PinePhone

 and turned it on. The phone prompted me to set a PIN and choose whether to enable encryption.

### Intentions in buying a PinePhone

 I want to get away from Android, particularly with all the bloatware. I've purchased some low-end Samsung phones and found them satisfactory, except for the bloatware, which cluttered by UI and zapped the storage space.

 In buying a PinePhone, I want to work toward establishing a straightforward, open source daily driver solution that a non-technical person could use.


### Wifi requires battery
The first thing I wanted to do was connect to my wifi, so I went to Settings but didn't see but I didn't see anything about wifi listed. After some research, it turned out the problem was that I hadn't removed the plastic tab from the battery. The wifi hardware apparently can't run directly from the power cable without the battery connected.

### Choosing a mobile carrier

I popped in my AT&T SIM card just to see if it would work. It did not. If I recall correctly, I would need to register the PinePhone's IMEI with AT&T in order to connect. Since I want to keep using my other phone, I decided to look for a pay-as-you-go plan. I came across a number of no-contract plans, but they still charged a monthly rate. Even $10 or $15 a month is more than I want to spend on this endeavor. 

I eventually found [Tello](https://tello.com/buy/pay_as_you_go?destination=United+States), which offers pay-as-you-go credit for 1 min/1¢ or 1 GB/$20 in the United States. I purchased a $20 credit, which will not expire as long as I have an active plan. This includes a free SIM card. 

By the time the SIM card arrived, I was using PostmarketOS Phosh. I followed the directions from Tello, namely:

- Insert the SIM card with the phone off
- Enter the activation code on the Tello website from my desktop
- Wait five minutes before turning on the phone

I sent an SMS and made a call from the PinePhone to my Android phone and received both successfully. 

### Initial Mobian upgrade soft bricked my phone 
I opened up the *Software* application and saw there were some updates available. I clicked install and got the following error: "Unable to download updates: The following packages have unmet dependencies:" According to this [blog post](https://blog.mobian-project.org/posts/2021/02/09/pam_issue/) from Mobian, the initial upgrade is simply too massive for the *Software* application to handle. Instead, they say to run the following in the terminal, called *King's Cross*:

`sudo apt update`  
`sudo apt dist-upgrade`  
`sudo apt autoremove`

The blog post also mentions an issue with the pluggable authentication module (PAM). In short, after the initial upgrade, the phone needs to reboot before it will accept the PIN. Despite my intention to the contrary, I let my screen fall asleep during the upgrade and was not able to get past the PIN screen. It seems this is often resolved by rebooting the phone, but that was not my experience. I had disabled the locksreen in the settings while the update was in progress, but the change didn't take effect and I was still faced with the lockscreen.


Oh no! Something has gone wrong. A problem has occurred and the system can't recover. Please log out and try again.  Log out.

Pressing the log out button leads to a black screen.

My next step will be to download a new image and reinstall the OS. Mobian's blog post ends with a comforting reassurance that "Pinephones are really hard to permanently brick."

### Flashing the OS

I decided to use the [PinePhone multi-distro demo image](https://xnux.eu/p-boot-demo/) so that I could try out some of the other operating systems. The multi-distro image contains Arch, Lune, Maemo Leste, KDE Neon, Manjaro, Mobian, Post Market, Sailfish, and Ubuntu Touch. The instructions for writing the image to the SD card were fairly straightforward.

I want to find the OS that is the closest to being a reliable daily driver. Based on what I've read, Mobian 

Here are my impressions of each OS:

#### Arch ARM

Same desktop environment as Mobian

#### Maemo Leste

Very strange. Seems to be permanently, or at least by default, in landscape mode. Rather unpolished compared to others. I don't even see a phone application. Phone calls do not come through.

#### KDE Neon

Angelfish DE

#### Manjaro Phosh / ARM

Same DE as Mobian

#### Manjaro Plasma

Angelfish DE. Does not ring. Also requires entering the PIN before answering a call if the phone is locked.

#### PostmarketOS Plasma

More like a shrunken desktop experience. Actual cursor on the screen. Keyboard is tiny.

#### Postmarket GNOME

Not very polished. Rather bare bones. Applications don't fit on screen.

#### Postmark Phosh **

Same DE as Mobian. Faster than Mobian. Leading candidate for daily driver.

#### Postmarket SXMO

This one gets a lot of hype, and I can see why. It's a totally different experience from all the others. Menus are accessed by pressing the volume up and down buttons, and using the power button to select the option. It shies away from the typical smartphone experience. Some users talk claim it's the best once they configure everything to their liking. Others insist that it will wear out the physical buttons before long.

Personally, I like it but want to start with one that replicates the standard smartphone experience.

#### Sailfish OS

Not open source. Right away, they want me to create a Jolla account. That said, it has a polished look.

#### Ubuntu Touch

Sharp, snappy, looks really nice. 


After trying out all these options, I'm going to stick with PostmarketOS Phosh.

### Installing PostmarketOS Phosh and apps

It turns out it's not possible to install OSes directly from the multi-boot image, but the multi-boot image does contain Jumpdrive, which allows images to be flashed directly to the eMMC from a desktop via USB.

Initial update would not work through Software app. Instead, I used `apk upgrade -i` in the terminal, and it worked. `apk` is the package manager for Alpine, which postmarketOS is based on.

I'm still not seeing any apps that aren't already installed in the *Software* app. But using `apk add` I can install whatever I need from the terminal.

### Sending and receiving SMS

Sending SMS works reliably. However, there are some issues with receiving SMS:

- When the phone is on and *Chats* is open to the conversation with my Android, the message shows up and no sounds plays.
- When the phone is on and *Chats* is open to the conversation with my Android but the app is in the background, no sound plays and no notification shows up. When I go back to the app, the message has been successfully received.
- When the phone is on and *Chats* is open to the menu with the app in the foreground, the sound plays

### Phone calls

Ringer sounds even if screen is off. Screen does not light up.

### Battery

The battery level was a 77%. I charged it for several hours. The battery level was then at 61%, but the icon was completely full. A few minutes later, the level was at 53% and the icon was about 2/3 full. At this point, 