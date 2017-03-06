#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client Web per http://www.packtpub.com/packt/offers/free-learning
@author: Nil Agut - nilagut@gmail.com
'''
import urllib2
from bs4 import BeautifulSoup


class Client(object):
    def get_web(self, page):
        '''baixar-se la Web'''
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
        '''Buscar el text'''
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div", "dotd-title")
        title = elements.find("h2")
        if title:
            title = title.text
        else:
            title = "Sense Titol"
        return title

    def beauty_result(self, title):
        title = title.replace("\t","")
        title = title.strip()
        return title

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning/')
        resultat = self.search_text(web)
        resultat = self.beauty_result(resultat)
        # imprimir resultats
        print "The daily free ebook is: ",resultat


if __name__ == '__main__':
    client = Client()
client.main()