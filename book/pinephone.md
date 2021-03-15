# PinePhone Log

Mobian Community Edition PinePhone

 and turned it on. The phone prompted me to set a PIN and choose whether to enable encryption.


### Wifi requires battery
The first thing I wanted to do was connect to my wifi, so I went to Settings but didn't see but I didn't see anything about wifi listed. After some research, it turned out the problem was that I hadn't removed the plastic tab from the battery. The wifi hardware apparently can't run directly from the power cable without the battery connected.

### Choosing a mobile carrier
I popped in my AT&T SIM card just to see if it would work. It did not. If I recall correctly, I would need to register the PinePhone's IMEI with AT&T in order to connect. Since I want to keep using my other phone, I decided to look for a pay-as-you-go plan. I came across a number of no-contract plans, but they still charged a monthly rate. Even $10 or $15 a month is more than I want to spend on this endeavor. 

I eventually found [Tello](https://tello.com/buy/pay_as_you_go?destination=United+States), which offers pay-as-you-go credit for 1 min/1¢ or 1 GB/$20 in the United States. I purchases a $20 credit, which will not expire as long as I have an active plan. This includes a free SIM card. 

### Initial Mobian upgrade soft bricked my phone 
I opened up the *Software* application and saw there were some updates available. I clicked install and got the following error: "Unable to download updates: The following packages have unmet dependencies:" According to this [blog post](https://blog.mobian-project.org/posts/2021/02/09/pam_issue/) from Mobian, the initial upgrade is simply too massive for the *Software* application to handle. Instead, they say to run the following in the terminal, called *King's Cross*:

`sudo apt update`  
`sudo apt dist-upgrade`  
`sudo apt autoremove`

The blog post also mentions an issue with the pluggable authentication module (PAM). In short, after the initial upgrade, the phone needs to reboot before it will accept the PIN. Despite my intention to the contrary, I let my screen fall asleep during the upgrade and was not able to get past the PIN screen. It seems this is often resolved by rebooting the phone, but that was not my experience. I had disabled the locksreen in the settings while the update was in progress, but the change didn't take effect and I was still faced with the lockscreen.

My next step will be to download a new image and reinstall the OS. Mobian's blog post ends with a comforting reassurance that "Pinephones are really hard to permanently brick."