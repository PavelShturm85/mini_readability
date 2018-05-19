# MiniReadability

## The module is recording news from sites to files.

# How to Install

Python 3 should be already installed. 

```bash
$ sudo apt-get install virtualenv
$ cd path/to/current/dir
$ virtualenv .env
$ source .env/bin/activate
$ pip install -r requirements.txt 
```

# Quickstart
**Ways to use:**
- Have to use  module `mini_readability.py` after `python3`.


Example of script launch on Linux, Python 3.5:


```bash
$ cd path/to/current/dir
$ source .env/bin/activate
$ python3 mini_readability.py -u https://lenta.ru/news/2018/05/17/zubkov/

```

Help for module:
```
$ python3 mini_readability.py -h
usage: mini_readability.py [-h] [-p PATH] [-out OUTPUT] [-u URL]

Module get news from site.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Where get the config file.
  -out OUTPUT, --output OUTPUT
                        Where to put the files.
  -u URL, --url URL     Enter site URL
```
