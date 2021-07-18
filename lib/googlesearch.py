#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# @name   : PhoneInfoga - Phone numbers OSINT tool
# @url    : https://github.com/sundowndev
# @author : Raphael Cerveaux (sundowndev)

import os
import re
import json
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from lib.output import *
from lib.request import send
from config import *
import sys

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


browser = None


def getBrowser():
    if os.environ.get("webdriverRemote"):
        return webdriver.Remote(
            os.environ.get("webdriverRemote"),
            webdriver.DesiredCapabilities.FIREFOX.copy(),
        )

    if browser_path == "":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")

        # Disable Chrome's PDF Viewer
        profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
                   "download.default_directory": './', "download.extensions_to_open": "applications/pdf"}
        options.add_experimental_option("prefs", profile)
        if(sys.platform == 'win32'):
            return webdriver.Chrome(chrome_options=options, executable_path="chromedriver.exe")
        else:
            return webdriver.Chrome(chrome_options=options, executable_path="./chromedriver")
    else:
        binary = FirefoxBinary(browser_path)
        return webdriver.Firefox(firefox_binary=binary)


def closeBrowser():
    if browser is not None:
        browser.quit()


def search(req, stop):
    global browser

    if google_api_key and google_cx_id:
        return searchApi(req, stop)

    try:
        browser = getBrowser()
    except Exception as e:
        error(e)

    try:
        REQ = urlencode({"q": req, "num": stop, "hl": "en"})
        URL = "https://www.google.com/search?tbs=li:1&{}&amp;gws_rd=ssl&amp;gl=us".format(
            REQ
        )
        browser.get(URL)
        htmlBody = browser.find_element_by_css_selector("body").get_attribute(
            "innerHTML"
        )

        soup = BeautifulSoup(htmlBody, "html5lib")

        while soup.find("div", id="recaptcha") is not None:
            warn(
                "You are temporary blacklisted from Google search. Complete the captcha then press ENTER."
            )
            token = ask(">")
            htmlBody = browser.find_element_by_css_selector("body").get_attribute(
                "innerHTML"
            )
            soup = BeautifulSoup(htmlBody, "html5lib")

        results = soup.find("div", id="search").find_all("div", class_="g")

        links = []

        for result in results:
            url = result.find("a").get("href")
            url = re.sub(r"(?:\/url\?q\=)", "", url)
            url = re.sub(r"(?:\/url\?url\=)", "", url)
            url = re.sub(r"(?:\&sa\=)(?:.*)", "", url)
            url = re.sub(r"(?:\&rct\=)(?:.*)", "", url)

            if re.match(r"^(?:\/search\?q\=)", url) is not None:
                url = "https://google.com" + url

            if url is not None:
                links.append(url)

        return links
    except Exception as e:
        error(
            "Request failed. Please retry or open an issue on https://github.com/sundowndev/PhoneInfoga."
        )
        print(e)
        return []


def searchApi(req, stop):
    options = urlencode(
        {"q": req, "key": google_api_key, "cx": google_cx_id, "num": stop}
    )
    r = send("GET", "https://www.googleapis.com/customsearch/v1?%s" % (options))
    response = r.json()

    if "error" in response:
        error(
            "Error while fetching Google search API. Maybe usage limit ? Please verify your keys."
        )
        print(response["error"])
        askForExit()
        return []

    if "items" not in response:
        return []

    results = response["items"]

    links = []

    for result in results:
        if result["link"] is not None:
            links.append(result["link"])

    return links
