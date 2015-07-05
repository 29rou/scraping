#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ブラウザの作成
from splinter import Browser
browser = Browser('phantomjs')

# Yahoo!JAPAN のサイトへ移動
browser.visit('https://opac.icu.ac.jp/opac/opac_search.cgi?smode=1')

# 検索ボックスに「猫」と入力
browser.find_by_name('kywd').first.fill(u'猫\n')

# 画像検索ボタンをクリック
#browser.find_by_id('isearch').first.click()
