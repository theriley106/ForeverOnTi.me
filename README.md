## Inspiration

I was inspired to create this project after frustratingly waking up for 17 years of my life.  After properly calculating the time of my sleep cycles, I have been able to wake up earlier and I feel far more refreshed after doing so.  I wanted to create a device that would make it easier for users to wake up in the morning, and  I was able to seamlessly connect both the hardware and software parts of this project to create a functioning "Smart Alarm Clock" prototype.

## What it does

Forever on Time is an internet connected Alarm Clock that can be connected to the Fitbit Sleep Tracking API to find ideal times to wake up the owner of the device.  It's essentially a full-linux system built into the form factor of a common alarm clock.  Forever on Time can be controlled using a custom Flask-based REST API that can be implemented into any network-accessible programming language.  This infrastructure allows developers to easily create third party applications for the device.


## How I built it

I purchased an inexpensive alarm clock from a Walmart Store nearby and gutted the internals.  I picked up a Dragonboard 410C from the hardware desk, and had to find a way to  fit the mix of electronic components into the alarm clock case.  After installing everything, I created a python framework to interact with the clock and a Flask-based REST API to make it easier for users to develop third party applications for the device.

## Challenges I ran into

The WiFi was difficult to connect to from the command line, and I actually went through 2 Dragonboards until I decided to just use my phone hotspot.  I have also never really used Arduino in this way before, so it was a relatively steep learning curve to get everything functioning.

## Accomplishments that I'm proud of

I think the clock looks really cool, and it's very similar to how I imagined it would look at the end of the project.  Like I mentioned earlier, this is one of my first large hardware projects and it looks much better than some of the other failed projects I've worked on in the past.  Also **76** Github commits...

## What I learned

I learned a ton about Arduino and C++

## What's next for ForeverOnTime

I have to give these parts back to the hardware desk, so most likely disassembly is the next step for ForeverOnTime. 
 Perhaps a Facebook buyout may come soon after ;)
