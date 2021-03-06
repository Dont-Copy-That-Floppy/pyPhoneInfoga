<p align="center">
  <img src="docs/images/pyPhoneInfoGa.png" width=500 />
</p>

<!-- <div align="center">
  <a href="https://github.com/sundowndev/PhoneInfoga/actions">
    <img src="https://img.shields.io/endpoint.svg?url=https://actions-badge.atrox.dev/sundowndev/PhoneInfoga/badge?ref=master&style=flat-square" alt="build status" />
  <a href="https://hub.docker.com/r/sundowndev/phoneinfoga/builds">
    <img src="https://img.shields.io/docker/cloud/build/sundowndev/phoneinfoga.svg?style=flat-square" alt="Build Status" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/python-3.6-blue.svg?style=flat-square" alt="Python version" />
  </a>
  <a href="https://github.com/sundowndev/PhoneInfoga/releases">
    <img src="https://img.shields.io/github/release/SundownDEV/PhoneInfoga.svg?style=flat-square" alt="Latest version" />
  </a>
  <a href="https://github.com/sundowndev/PhoneInfoga/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/sundowndev/PhoneInfoga.svg?style=flat-square" alt="License" />
  </a>
</div>

<h4 align="center">Information gathering & OSINT reconnaissance tool for phone numbers</h4>

<p align="center">
  <a href="https://sundowndev.github.io/PhoneInfoga/">Documentation</a> •
  <a href="https://sundowndev.github.io/PhoneInfoga/usage/">Basic usage</a> •
  <a href="https://sundowndev.github.io/PhoneInfoga/resources/">OSINT resources</a> •
  <a href="https://medium.com/@SundownDEV/phone-number-scanning-osint-recon-tool-6ad8f0cac27b">Related blog post</a>
</p> -->

## About

pyPhoneInfoga is a rebase from version 1.11 of the [phoneinfoga](https://github.com/sundowndev/phoneinfoga), written by [sundowndev](https://github.com/sundowndev). The original developer chose to switch codebase from python to GoLang, but this repo will be an attempt to improve on the original python codebase, and add any additional features added to the GoLang version, but in keeping with python as the choice of language.

PhoneInfoga is one of the most advanced tools to scan phone numbers using only free resources. The goal is to first gather standard information such as country, area, carrier and line type on any international phone numbers with a very good accuracy. Then search for footprints on search engines to try to find the VoIP provider or identify the owner.

## Features

- Check if phone number exists and is possible
- Gather standard informations such as country, line type and carrier
- OSINT footprinting using external APIs, Google Hacking, phone books & search engines
- Check for reputation reports, social media, disposable numbers and more
- Scan several numbers at once
- Use custom formatting for more effective OSINT reconnaissance
- Automatic footprinting on several custom formats

![Footprinting process](https://i.imgur.com/qCkgzz8.png)

## License

Additions in this repo are under GPLv3.

The original tool by sundowndev is licensed under the GNU General Public License v3.0.

Some parts of this code comes from [Infoga](https://github.com/m4ll0k/infoga), another project licensed under GPLv3.0.

[Icon](https://www.flaticon.com/free-icon/fingerprint-search-symbol-of-secret-service-investigation_48838) made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a>.

<!-- [![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsundowndev%2FPhoneInfoga.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsundowndev%2FPhoneInfoga?ref=badge_large) -->