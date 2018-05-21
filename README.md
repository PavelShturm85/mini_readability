# MiniReadability

## The module is recording news from sites to files.

# How to Install

Python 3 should be already installed. 

For linux:
```bash
$ sudo apt-get install virtualenv
$ cd path/to/current/dir
$ virtualenv .env
$ pip install -r requirements.txt 
```
For windows:
```CMD
$ cd path/to/current/dir
$ pip install -r requirements.txt
```
# Quickstart
**Ways to use:**
- Have to use  module `mini_readability.py` after `python3`.


Example of script launch on Linux, Python 3.5:

For linux:
```bash
$ cd path/to/current/dir
$ source .env/bin/activate
$ python3 mini_readability.py -u https://lenta.ru/news/2018/05/17/zubkov/

```
For windows:
```CMD
$ cd path/to/current/dir
$ python mini_readability.py -u https://lenta.ru/news/2018/05/17/zubkov/
```
If you have not entered the parameters -u, you will see an invitation to enter
or run the module as an executable:
```
Введите урл: https://www.gazeta.ru/business/news/2018/05/21/n_11561461.shtml?updated
Введите директорию назначения или оставьте пустой:
Введите путь к конфигурационному файлу или оставьте пустым:
``` 


Help to module:
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
