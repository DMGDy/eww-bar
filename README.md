# my eww bar

## epic bar!
This uses [eww](https://github.com/elkowar/eww) to recreate and enhance my experience with [dwm](https://github.com/DMGDy/dwm).
Also because this runs well on [hyprland](https://github.com/hyprwm/Hyprland).

## dependencies
this bar relies on some other binaries as the tools to fetch the module information are compiled binaries in rust and in C.

* [eww-bar-widget-generator](https://github.com/DMGDy/eww-bar-widget-generator)
* [statuses](https://github.com/DMGDy/statuses)
* [statuses-rs](https://github.com/DMGDy/statuses-rs)

## purpose

Besides the wifi widget, all widgets apart of the bar are written in C and Rust because of compiled binary performance.
Too often people are lazy and write scripts for something that can just as easily be done by a single binary program.
As to why the wifi widget is not a compiled binary instead of a Python script, im too lazy. Additionally it is very slow and plan to change it at some point

## uses
run `eww open bar` 

## preview

<img src="preview.gif">


