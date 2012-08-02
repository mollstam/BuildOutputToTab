```
                                                  `T",.`-, 
                                                     '8, :. 
                                              `""`oooob."T,. 
                                            ,-`".)O;8:doob.'-. 
                                     ,..`'.'' -dP()d8O8Yo8:,..`, 
                                   -o8b-     ,..)doOO8:':o; `Y8.`, 
                                  ,..bo.,.....)OOO888o' :oO.  ".  `-. 
                                , "`"d....88OOOOO8O88o  :O8o;.    ;;,b 
                               ,dOOOOO""""""""O88888o:  :O88Oo.;:o888d 
                               ""888Ob...,-- :o88O88o:. :o'"""""""Y8OP 
                               d8888.....,.. :o8OO888:: :: 
                              "" .dOO8bo`'',,;O88O:O8o: ::, 
                                 ,dd8".  ,-)do8O8o:"""; ::: 
                                 ,db(.  T)8P:8o:::::    ::: 
                                 -"",`(;O"KdOo::        ::: 
                                   ,K,'".doo:::'        :o: 
                                    .doo:::"""::  :.    'o: 
        ,..            .;ooooooo..o:"""""     ::;. ::;.  'o. 
   ,, "'    ` ..   .d;o:"""'                  ::o:;::o::  :; 
   d,         , ..ooo::;                      ::oo:;::o"'.:o 
  ,d'.       :OOOOO8Oo::" '.. .               ::o8Ooo:;  ;o: 
  'P"   ;  ;.OPd8888O8::;. 'oOoo:.;..         ;:O88Ooo:' O"' 
  ,8:   o::oO` 88888OOo:::  o8O8Oo:::;;     ,;:oO88OOo;  ' 
 ,YP  ,::;:O:  888888o::::  :8888Ooo::::::::::oo888888o;. , 
 ',d: :;;O;:   :888888::o;  :8888888Ooooooooooo88888888Oo; , 
 dPY:  :o8O     YO8888O:O:;  O8888888888OOOO888"" Y8o:O88o; , 
,' O:  'ob`      "8888888Oo;;o8888888888888'"'     `8OO:.`OOb . 
'  Y:  ,:o:       `8O88888OOoo"""""""""""'           `OOob`Y8b` 
   ::  ';o:        `8O88o:oOoP                        `8Oo `YO. 
   `:   Oo:         `888O::oP                          88O  :OY 
    :o; 8oP         :888o::P                           do:  8O: 
   ,ooO:8O'       ,d8888o:O'                          dOo   ;:. 
   ;O8odo'        88888O:o'                          do::  oo.: 
  d"`)8O'         "YO88Oo'                          "8O:   o8b' 
 ''-'`"            d:O8oK  -hrr-                   dOOo'  :o": 
                   O:8o:b.                        :88o:   `8:, 
                   `8O:;7b,.                       `"8'     Y: 
                    `YO;`8b' 
                     `Oo; 8:. 
                      `OP"8.` 
                       :  Y8P 
                       `o  `, 
                        Y8bod. 
                        `""""'
```

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
