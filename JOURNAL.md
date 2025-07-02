---
title: "stno"
author: "@itsme (Heinrich Xiao)"
description: "A one-handed steno keyboard with joysticks for thumb keys"
created_at: "2025-06-19"
---

# stno

## June 19 
My goal for this project is to make use a microcontroller directly. then, after i tried making the schematic, i realized that i didn't want the process of programming to involve an external programming board (i wanted usbc programming), and i also didn't want to solder a bunch of smd chips. these two things are incompatible, so i decided if i was gonna use a microcontroller directly, i'd have to git gud at soldering smd which im currently horrible at.

Time spent: 35 minutes (didnt waste as much time as i expected to waste)

## June 20
I realized my goals were a bit too ambitious and decided on an arduino nano esp32. and i started designing the schematic around that. this is also when i decided to use joysticks, specifically the hall effect ones cuz they're smooth and feel nice.

![image](https://github.com/user-attachments/assets/02490b6e-efa1-4ba8-8cf3-ab5f3791891c)


Time spent: 3hr

## June 21 
I made the PCB for the left half. (twice) the first time, i just put the key switches in the order they happened to be in, which was not at all good for the wiring, so i stopped and realized that was a horrible idea after finishing half of the wiring.

after that, i learned my lesson and spent some time positioning my components. the wiring was a lot better than last time.
<img width="980" alt="image" src="https://github.com/user-attachments/assets/e4a0cf48-e35f-4b38-9c78-85a58dc7171e" />


Time spent: 6hr


## June 22 
Today, I'm backjournaling cuz i forgot to journal before. also, this is when i decided to reinforce the trend of my previous keyboards (they're all one handed), so i dont need a right half.

Time spent: 30 minutes

## June 23
Today, I spent too much time making the case. I also learned that I could just use thicken on a surface in onshape, so I didn't have to painstakingly go through every point and move them slightly further away from the original point so that I can extrude the area in between.

then I added heatset inserts. I couldn't find a model that was the size im actually gonna use, so I just went with the one I found first. I also wanted to use l7 m3s but apparently there aren't any models for that so I just went with an l6.

Time spent: 9hr 28mins (I need to touch grass)

## June 24
I made the assembly in onshape. this was annoying because I also just realized that I used the wrong footprint on my PCB. but I didn't have access to kicad since I was on a school Chromebook,so I had to remote into my computer and fix the footprint, export a step file, email it to myself, and then finally import it into onshape. then I realized that the 3d model I had for my joystick was the wrong one for the footprint, and I didn't want to remote again (I was on a different Chromebook) so I had to find a joystick model (specifically, the pins were slightly different. slightly meaning millimetres) that was actually the on I was using (PS4) this took forever.

Time spent: 4hr (at school and approximately and also on five different Chromebooks)

## June 25
I realized that all the hotswap sockets were the wrong way around. so i had to rewire all of them. pain. 

Time spent: 2hr 30mins 

## June 26
I spent 3hr just watching videos and listening to how switches sound and reading wiki articles on which switches to use for steno (apparently i need light switches which makes sense and i liked light switches anyways). So, i landed on the Gateron Clear / White and ill switch the springs out for 20 gram springs (https://stenokeyboards.com/products/20-gram-springs)

Time spent: 3hr 

## June 28
I spent a lot of time adding the 3d models switch by switch, so i asked around, and was told i could do them all at once by just making a new library and using that footprint (includes 3d models) instead.

so with that, i also added the diodes. then i added the arduino nano esp32.

Time spent: 5hr

i spent the rest of the day figuring out which hinge to use, to use 3d printed screws or not to use 3d printed screws, making the mechanism, tuning parameters (parameters being the lengths of stuff. how many holes to put, stuff like that). then i just spent a few hours using mc master carr figuring out what m meant and whether to use imperial or metric (used metric, proud canadian). i decided on 96016A556 for the thumb screw (round ones look better and from my experience feel better too)  93635A017 and 90591A250 for bolts and nuts respectively only because its dimensions worked. 
![image](https://github.com/user-attachments/assets/488a4c84-64c8-472e-bf4e-89268a71b3d4)
![image](https://github.com/user-attachments/assets/7f784a09-3d85-462b-90c8-0cedfa90f059)
i hope i wont have to get more parts that come in packs of 100... not foreshadowing.

Time spent: 7hr

Total time spent: 12hr......

## June 30
found all the parts. yay! now i know how much debt im in. and its a lot. ~200usd. bom is in the readme.

Time spent: 3hr

## July 1 
Celebrated Canada Day! Also drank a shot of maple syrup.

Time spent: 0. Time spent being patriotic: 25hr.

## July 2
I made the firmware. this was very annoying. the javelin firmware that i was gonna use wasn't compatible with joysticks for some reason (i wonder why). i spent a bunch of time tryna use qmk, but i realized joysticks would be annoying to make. so i just had to go with kmk and plover. kmk for some reason did support joysticks. so, i went with kmk and using non-embedded steno. there was also a lot of optimizing my layout.

Time spent: 9hr
