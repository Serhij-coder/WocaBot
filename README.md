<h1 align="center">
  <br>
  <img src="./res/logo.png" alt="Markdownify" width="300"></a>
  <br>
  WocaBot
  <br>
</h1>

<h4 align="center">Bot which will solve Wocabee for you.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#installation">Installation</a> •
  <a href="#license">License</a>
</p>

![screenshot](./res/meme.jpg)

## Key Features

* Fully automated (except pexeso)
* Have modes:
  - Normal for packages
  - Training for points farming
  - And test for school (beta)
* Can solve
  - Word translation
  - Word completion
  - Word choosing
  - Finding pair
  - One out of many
  - Picture choosing
  - Picture description (only skip)
  - Words arranging (only skip)
  - And missing word
* Good readability and scalability of code
* CLI interface
* Cross platform
  - Windows, macOS and Linux ready.
* I think it is enaugh. Who want to do wocabee anyway? :D

## How To Use

### Start

To start bot you need to run `wocabot.py` file. You can do it by running command:
```bash
  python wocabot.py
```
Than select mode by writing number of mode you want to use:

![modeSelection](res/modeSelection)
> [!NOTE]
> You can setup default mode in `config.py` file.
>
> 0 - For choosing mode every time

Than browser window will open. You need to choose your class:

![classSelection](res/classSelection)

When you choose class, you need to click enter to start bot and continue with instructions.

### Modes overview
#### Mod 1

Normal mod which will do all uncompleted packages.\
It will automatically go through all packages and do all exercises(except pexeso).\

#### Mod 2
Training mod which will do wocabee training.\
It will start do training and will finis only when user stop it.
> [!WARNING]
> You need to click submit and exit than stop bot

> [!TIP]
> It`s the best way to farm wocapoints if you need to win some competition.

#### Mod 3

This mod is designed for school tests.\
And include 2 own submods:\
**Semi automatic**\
Will prepare ansvers for you and you need to click submit.

> [!TIP]
> Do some mistakes or wait for some time to not be suspicious.
> 
**Automatic**\
Will do everything for you.

> [!CAUTION]
> Dont implemented yet.

## Installation

For all OS you need to have installed google chrome and python.

### Linux
Use your package manager to install python-playwright.
```bash
  sudo pacman -S python-playwright
  sudo apt install python-playwright 
  ...
```

## Emailware

Markdownify is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <bullredeyes@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

## Credits

This software uses the following open source packages:

- [Electron](http://electron.atom.io/)
- [Node.js](https://nodejs.org/)
- [Marked - a markdown parser](https://github.com/chjj/marked)
- [showdown](http://showdownjs.github.io/showdown/)
- [CodeMirror](http://codemirror.net/)
- Emojis are taken from [here](https://github.com/arvida/emoji-cheat-sheet.com)
- [highlight.js](https://highlightjs.org/)

## Related

[Try Web version of Markdownify](https://notepad.js.org/markdown-editor/)

## Support

<a href="https://buymeacoffee.com/amitmerchant" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/amitmerchant">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## You may also like...

- [Pomolectron](https://github.com/amitmerchant1990/pomolectron) - A pomodoro app
- [Correo](https://github.com/amitmerchant1990/correo) - A menubar/taskbar Gmail App for Windows and macOS

## License

MIT

---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)

