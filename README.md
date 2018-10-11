# ulauncher-cheats

> Provides quick access to your Cheat sheets in multiple formats. It is deep integrated with [hawkeye](https://github.com/brpaz/hawkeye) file previewer to quiclky preview your files in an overlay window minimizing the need of context switching.

## Demo

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7
* python-glob2 (pip install glob2)

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```https://github.com/brpaz/ulauncher-cheats```

## Configuration
* Any file that is placed inside cheats dir (path configurable) will appear in the extension.
* Optionally, a URLs file can be created to show a list of URLs as well (check out examples folder).

## Development

```
make link
```

To see your changes, stop ulauncher and run it from the command line with: ```ulauncher -v```.

## Credits
Icons (partly) by [webalys](https://www.iconfinder.com/webalys)

## License

MIT
