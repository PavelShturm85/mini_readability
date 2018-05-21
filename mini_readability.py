# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import requests
import textwrap
import argparse
import re
import os
from tld import get_tld
from bs4 import BeautifulSoup
try:
    import configparser
except ImportError:
    import ConfigParser as configparser


def create_parser():
    parser = argparse.ArgumentParser(
        description='Module get news from site.')
    parser.add_argument(
        '-p', '--path', default='rule_pars.ini',
        help='Where get the config file.')
    parser.add_argument(
        '-out', '--output', default='news/',
        help='Where to put the files.')
    parser.add_argument(
        '-u', '--url',
        help='Enter site URL')
    return parser


class MiniReadability():

    def __init__(self, url, path='rule_pars.ini', output='news/'):
        self.output = output
        self.url = url
        self.path = path
        self.title_rule, self.text_rule, \
            self.rule_path, self.encode = self.get_rule

    @property
    def get_page(self):
        page = requests.get(self.url)
        page.encoding = self.encode
        return BeautifulSoup(page.text, 'html.parser')

    @property
    def site_name(self):
        return get_tld(self.url, fix_protocol=True)

    @property
    def get_path_to_file(self):
        path = re.findall(self.rule_path, self.url)[0]
        if path[-1] == '/':
            return path[:-1] + '.txt'
        else:
            return path + '.txt'

    @property
    def get_rule(self):

        config = configparser.ConfigParser()
        config.read(path)

        try:
            title_rule = config.get(self.site_name, "title")
            text_rule = config.get(self.site_name, "text")
            rule_path = config.get(self.site_name, "rule_path")
            encode = config.get(self.site_name, "encode")
            return title_rule, text_rule, rule_path, encode

        except configparser.NoSectionError:
            config.add_section(self.site_name)
            config.set(self.site_name, "title", '')
            config.set(self.site_name, "text", '')
            config.set(self.site_name, "rule_path", '')
            config.set(self.site_name, "encode", '')

            with open(path, "w") as config_file:
                config.write(config_file)

            print(
                'Введите для данного сайта правило \
                в конфигурационный файл и повторите операцию!')

    def get_title(self):
        title = self.get_page.select_one(self.title_rule).text
        return textwrap.fill(title, width=79)

    def get_text(self):
        for p in self.get_page.select_one(self.text_rule).find_all("p"):
            yield textwrap.fill(p.text, width=79)
            for href in p.select('a'):
                url = '[' + href.get('href') + ']'
                yield textwrap.fill(url, width=79)

    def write_file(self):
        full_file_path = os.path.normpath(self.output + self.get_path_to_file)
        path = os.path.dirname(full_file_path)
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        with open(full_file_path, "w") as file_text:
            file_text.write('*' + self.get_title() + '*' + '\n\n')
            for text in self.get_text():
                file_text.write(text + '\n\n')


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    output = namespace.output
    path = namespace.path
    url = namespace.url
    if url:
        get_news = MiniReadability(url, path, output)
        get_news.write_file()

    else:
        print('Повторите попытку с параметром -u и аргументом(URL сайта)!')
