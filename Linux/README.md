## Linux Resources

#### Recommended Linux Distributions

The [Raspberry Pi Desktop](https://www.raspberrypi.org/downloads/raspberry-pi-desktop/) distribution provided by the Raspberry Pi Foundation is the easiest way to get a self-contained linux environment on a flash drive.
* It's portable
* It doesn't require installing a second OS on your personal computer (which can get tricky)
* It comes with an easy way to reset it. Selecting "Run and reset persistence" during startup will do a "factory reset"

![startup_options](Pictures/startup_options.png)

Some flash drives do not handle running an entire OS well (even if they're big enough to fit it). I have found that [these](https://www.amazon.com/SanDisk-Ultra-Flair-Flash-Drive/dp/B015CH1JIW/ref=sxin_4_sxwds-bovbs?crid=QV1LBMTH6TQK&keywords=sandisk%2Busb%2B3.0%2Bflash%2Bdrives&pd_rd_i=B015CH1NAQ&pd_rd_r=79bd4b04-892b-4203-bff4-d45c097a402b&pd_rd_w=jwEjY&pd_rd_wg=la3ML&pf_rd_p=55b738be-ff12-48ad-8ad2-6a14afb06d32&pf_rd_r=082CXTJ7NZ8P5B31AQEJ&qid=1560481825&s=gateway&sprefix=sandisk%2Busb%2Caps%2C465&th=1) SanDisk drives work great.
* The flash drive should be at least 16GB in size. I suggest 32 GB so you have plenty of space for projects, programs, documents, and anything else you may want to save.
* Get a USB 3.0 flash drive. Since it's faster than USB 2.0, the final linux system is more responsive.
* I have not had success with PNY flash drives, and I don't recommend them.


1. Click the link above to go to the download page. Download the .iso file. If you're given an option to save or open the file, save it.
![RPD](Pictures/rpd_iso_download.png)
2. After downloading the .iso file, burn it to a flash drive with Etcher, which can be downloaded [here](https://etcher.io/).

      2.1. Select the image

      ![Etcher1](Pictures/etcher.png)

      2.2. Select the flash drive (insert the flash drive into your computer if you haven't already.)

      ![Etcher2](Pictures/etcher2.png)

      2.3. Flash it

      ![Etcher3](Pictures/etcher3.png)

3. After flash is complete, reboot your computer without removing the flash drive
##### Warning: Steps 4 and 5 can be hard to follow because they are heavily dependent on the computer being used. They are also done before your computer is fully booted, and therefore vulnerable to destructive accidents. If you are unsure, DON'T GUESS. [Open an issue](https://github.com/mzurzolo/STBS/issues) with your computer brand (Dell, HP, etc.) and model number, and specific instructions for your system will be provided. If you don't know your computer's model number, open an issue with as much information as you can, and I'll try my best to figure it out, and then provide specific instructions.

4. While the computer is starting up, you need to access the boot menu, which is only available for a short window of time during a reboot.

    * The boot menu can usually be accessed by hitting one of the F keys during the first stages of startup. Try F12 first. (F2, F10, F11, and F12 are all commonly used keys for accessing boot menus)

    * You should hit the F key as soon as you see the first logo appear on your screen, and you may need to hit it more than once.

    * Pay attention to any text that may flash on the screen. Sometimes it will tell you what F key to hit.

    * Searching "<computer type/model> access boot menu" will usually give clear instructions.

    * Mac users should follow [this guide](https://support.apple.com/en-us/HT202796)

5. Once you have the boot menu up, you need to tell the computer to boot your newly-created flash drive. These menu options vary from one computer to another, but here are some general notes/things to look for:

  * If you see "One time boot menu", "UEFI", "BIOS", or "Legacy", you're likely in the right place. Look for an option that has "USB", "USB Hard disk", "<your flash drive's brand name>", "Stretch", "RPD", "Debian", or some other indication that it's your newly-created flash drive. Select this option.

  * If you DON'T see any of the words above, you should be looking for sections that say things like: "Hardware", "Boot", "Boot order", or "Advanced". The goal is to tell your computer to boot from your flash drive.

#### Continue to the [python getting started guide](../Python/README.md)
