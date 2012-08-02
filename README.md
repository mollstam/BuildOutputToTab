BuildOutputToTab
================
This plugin will stream build output in Sublime Text 2 to a single read-only tab titled "Build" instead of the usual bottom panel.

I made it because I thought the panel was too small and didn't want to waste screen real estate on making it larger, this hack works fine for me. :)

Note: Only tested on OS X Mountain Lion but should work on all the computers.

Installation
------------
Place BuildOutputToTab.py in your `Packages/User` folder (where Sublime store stuff)

Usage
-----
Add this to your preferences file

    "show_panel_on_build": false,
    "build_output_to_tab": true

We hide the build panel because it'll just be empty.

Todo
----
Feel free to fork and dig in to any of these, it's open source, right?
+ Move this and below list to issue tracker
+ Scroll tab to bottom when output is written

Known Issues
------------
+ Performance in the tab is a bit meh if writing like 1000 lines per second, I'm sure the panels work better for this, or I was just imagining the performance loss.
