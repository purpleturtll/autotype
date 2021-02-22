# autotype
Simple automated typing cli, for working with files and clipboard.

Tested on:
- python 3.9.1
- pynput 1.7.3
- click 7.1.2
- Tcl/Tk 8.6

Usage:
```
Options:
  -c, --clipboard      Use first clipboard value as input instead of a file.
  -d, --delay INTEGER  How long to wait before I start typing.  [default: 5]
  -f, --file PATH      Input file.
  -s, --speed FLOAT    How fast should I type. -1 gives random speed between
                       50ms and 100ms. Using 0 can freeze websites.  [default:
                       -1.0]

  --help               Show this message and exit.
```
