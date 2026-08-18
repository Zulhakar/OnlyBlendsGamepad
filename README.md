 <img width="128" src="https://github.com/user-attachments/assets/4e1f87c0-af56-4854-ae49-ee93bb8492c3">
 <img width="256" src="https://github.com/user-attachments/assets/5b2671a5-5c2f-4a70-a4b3-199e26cc670e">

# OnlyBlends.Gamepad 0.5.2

Integrate Controller like Gamepads and other inputs via Nodes.
![preview-gif-obg](https://github.com/user-attachments/assets/33b6383c-2c7a-4bdd-93ea-5fa8b39d3f3c)

## Features

- Connection to Geometry Nodes via New OnlyBlend.Gamepad Node Editor
- Supports multiple gamepads and multiple platforms (https://inputs.readthedocs.io/en/latest/user/hardwaresupport.html )
- Node Socket segmented into: *D-Pad* ; *Axis* (Sticks and Bumpers) ; *Buttons*
- The OnlyBlends.Gamepad Node Editor has Nodes to help building a Camera / Object Controller
- "Start Game" Operator in the Render Properties
  -> Spawn a Fullscreen Standalone Blender Instance

## Install

Download as zip or install in Blender via:

## Usage

### Geometry Node Connection

- Select the OnlyBlends.Gamepad Node Editor

![image_1](https://github.com/user-attachments/assets/a77a0f85-f9a1-4881-a84e-df1bd2be2cb4)
- Add a Gamepad Node
- Create a Geometry Node Modifier and add Input Sockets
- The 'Modifier Control' Node can manipulate the Inputs of an Geometry Nodes Modifier and has an Object as Output Socket (the Geometry of the Modifier)
- This means you can send Data from Gamepad Nodes to Geometry Nodes in Realtime
- 
![image_2](https://github.com/user-attachments/assets/13f36047-4eda-4fe1-97fe-e37f54a39d29)

### Fullscreen

- You can start a Full Screen Instance of Blender
- Not tested on Mac

![image_3](https://github.com/user-attachments/assets/8f8e308c-554a-4d0d-9dc1-1836eeb03a76)

![image_4](https://github.com/user-attachments/assets/26814ef8-461f-4c62-92ce-a33497d7b9ad)

### Optional

- Use the Transform Object Node to build a Controller for Cameras and Objects

![image_4](https://github.com/user-attachments/assets/8366d3c6-863b-4e6b-a73f-73342eacca7b)

## Special Thanks to

- Zeth
- https://github.com/zeth
- https://github.com/zeth/inputs

## Upcoming features

- Mouse and Keyboard

## Change Log

0.5.0

- Complete rewrite
- pip package inputs is used instead of pygame, only one wheel for all platforms
- OnlyBlends.Gamepad Node Editor and Custom Nodes

0.5.0-1

- Fix Plug and Play for Windows
- "Start Game" Operator in the Render Properties
  -> Spawn a Fullscreen Standalone Blender Instance, like you know...
- Tested on:
    - [x] Linux
    - [x] Windows
    - [ ] Mac

0.5.1

- Fix "Start Game" Operator of Fullscreen Mode (Windows)
- Fix spamming of temporary save path
- Fix Scene Info Node
- It is possible to use also OnlyBlends.Mixer Nodes if it's installed (after the 0.5.1 release of Mixer) with Copy / Paste from on Tree to another

0.5.2

- internal fixes to get listed on extensions platform again
  - [x] critical packages queue and threading no longer used
  - [x] changes from (https://github.com/Zulhakar/OnlyBlendsCore)
  - [x] "Geometry Modifier Object" renamed to "Modifier Control"
