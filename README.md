# my eww bar

## epic widget bar
This uses [eww](https://github.com/elkowar/eww) to recreate and enhance my experience with [dwm](https://github.com/DMGDy/dwm).
Also because this runs well on [hyprland](https://github.com/hyprwm/Hyprland).

## All modules are compiled binary
Notice how `Scripts/` is empty. all system information fetchers are compiled binaries. their associated repos are here:

* [eww-bar-widget-generator](https://github.com/DMGDy/eww-bar-widget-generator)
* [statuses](https://github.com/DMGDy/statuses)
* [statuses-rs](https://github.com/DMGDy/statuses-rs)
* [eww-windows](https://github.com/DMGDy/eww-windows)

compiled binaries are far faster and more efficient to run compared to scripts. would make sense for tools such as these that are always running.



## Features
* Dynamic workspace tracking bar
    * different css classes for `inactive`, `occupied`, and `empty`
    * dwm like look
* List of open windows similar to windows
    * click to switch to window (and attached workspace)
    * in order of recently accessed
* Window title and description
* System power buttons (hibernate,reboot,poweroff)
* status modules as compiled binaries
    * SSID, connection strength, indicator icon for connection
    * RAM usage (used/total)
    * Battery Life (with status on hover eg. time to discharge/charge) with dynamic icon
    * date and time

## dependencies
this bar relies on some other binaries as the tools to fetch the module information are compiled binaries in rust and in C.
also requires hyprland and whatever else package the status fetchers i wrote use. 

## uses
run `eww open bar` 

## preview

<img src="preview.gif">


