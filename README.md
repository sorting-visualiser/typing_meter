<h1 align="center"> ⌨ Typing Meter ⌨ </h1>
<p align="center">
    Typing Speed Test in Terminal
    <br />
  <br />
<img src="https://api.codeclimate.com/v1/badges/4d0397d4c7dd3b81a205/maintainability"></a>
<img src="https://img.shields.io/pypi/v/mitype.svg"></a>
<a href="LICENSE.txt"><img src="https://img.shields.io/pypi/l/mitype.svg"></a>
<a href="https://github.com/ambv/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<br />
<img src="media/Windows-Terminal.gif" alt=>
</p>

**Typing Meter** is a program to test (and hence improve) your typing speed right from the ease of your terminal.

Written completely in python with no external dependencies!

## ✨ Main Features

- 🖥️ Cross-platform
- 🎦 See your replay
- 📝 Choose custom text input
- 🅰️ 6000 text samples
- 🌈 Colored texts

## 📈 Usage

You can run typing meter simply as:

```bash
cd /path/to/typing_meter/
python -m typing_meter
```

You can also customize each run by specifying the following options as:

- ```-f FILENAME, --file FILENAME```
  Uses contents of file as sample text.
- ```-d N, --difficulty N```
  N can be in range [1, 5] with 1 being the easiest. This decides the length of the text.
- ```-i ID, --id ID```
  ID can be in range [1, 6000].

You can quit typing_meter anytime by pressing the `ESC` key or `CTRL-C`.

## 📜 License

Licensed under the [GPL](LICENSE.txt) license.

Text samples in database are collected from [Typeracer Data](http://typeracerdata.com/texts).
