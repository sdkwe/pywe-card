# -*- coding: utf-8 -*-

from pywe_card import Card

from local_wecfg_example import WECHAT


class TestCardCommands(object):

    def test_card_create(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        card = Card(appid=appid, secret=appsecret)
