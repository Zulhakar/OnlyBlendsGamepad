  <img width="128" src="https://github.com/user-attachments/assets/4e1f87c0-af56-4854-ae49-ee93bb8492c3">
 <img width="256" src="https://github.com/user-attachments/assets/5b2671a5-5c2f-4a70-a4b3-199e26cc670e">

# OnlyBlends.Gamepad 0.5.0
Integrate Controller like Gamepads and other inputs via Nodes.
![ezgif-201d03e4d39d7b](https://github.com/user-attachments/assets/d9cdfb9d-281c-43e8-83d0-e930197c72ed)

## Features
- Connection to Geometry Nodes via New OnlyBlend.Gamepad Node Editor
- Supports multiple gamepads and multiple platforms (https://inputs.readthedocs.io/en/latest/user/hardwaresupport.html )
- Node Socket segmented into: *D-Pad* ; *Axis* (Sticks and Bumpers) ; *Buttons*
- The OnlyBlends.Gamepad Node Editor has Nodes to help with getting a Camera / object Controller

## Install
Download as zip or install in Blender via:

## Usage

In preference Tab toggle Gamepad listener and get state informations
![Bildschirmfoto vom 2025-06-21 18-53-56](https://github.com/user-attachments/assets/bbb71991-52eb-4f1f-aa7b-b1d715a4566b)

Generate Geometry Nodes for Axis, DPad and Buttons of your Gamepad and create your Example
![Bildschirmfoto vom 2025-06-28 21-20-39](https://github.com/user-attachments/assets/25b49438-d899-4c4e-b314-86d07170979c)

Or try out my special gamepad model example
![Bildschirmfoto vom 2025-06-28 21-18-42](https://github.com/user-attachments/assets/59cd12ef-2377-4b8e-a3f6-065cbd6edfe2)


## Upcoming features

- Mouse and Keyboard

## Change Log

0.5.0
- complete rewrite
- pip package inputs is used instead of pygame, only one wheel for all platforms
- OnlyBlends.Gamepad Node Editor and Custom Nodes
