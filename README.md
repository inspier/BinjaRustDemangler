# Rust Demangle (v0.1.0)
Author: **inspier**

## Description:
This plugin demangles Rust symbols making them easier to read.

![Image demoing plugin](https://github.com/inspier/BinjaRustDemangler/blob/master/img/RustDemangleExample.png)

## Installation Instructions

Install all needed packages from pip in requirements.txt (Windows and MacOS Binja ship with an embedded python, [read here on how the docs say to install pip packages](https://docs.binary.ninja/guide/plugins.html#installing-prerequisites), or what I reccomend doing is just changing the python interpreter to a system install of python3 in settings)
### Windows

Clone this repository into `%APPDATA%/Binary Ninja/plugins/`

### Darwin

Clone this repository into `~/Library/Application Support/Binary Ninja/plugins/`

### Linux

Clone this repository into `~/.binaryninja/plugins/`

## Minimum Version

Binary Ninja v1200

## License

This plugin is released under a MIT license.
## Metadata Version

2

## Credits:
* [Alex Crichton for rustc-demangle](https://github.com/alexcrichton/rustc-demangle)
