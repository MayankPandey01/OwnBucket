
# OwnBucket 
 [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)   <a href="https://twitter.com/mayank_pandey01"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/mayank_pandey01?style=social"></a> 
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/MayankPandey01/OwnBucket) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

<p align="center">
  <img width="750" height="350" src="https://user-images.githubusercontent.com/29165227/210492763-1f3e82ba-9a77-470a-be57-e02e12017335.jpg"></p>

# 🤔 What's OwnBucket?

OwnBucket is a Python Based Recon tool for Storage Buckets. It scans for AWS S3 Bucket and GCP Buckets by bruteforcing using different permutations.


# 🚀 Usage
OwnBucket can be easily  used from the command line 
- `python3 ownbucket.py -t {COMPANY}`

![Screenshot 2023-01-04 150553](https://user-images.githubusercontent.com/29165227/210527562-dafcd534-2da8-487a-ad2d-9c19c50825b6.jpg)

 Additional Arguments can be passed to use tool in different way:
 
 - `-t` : To Provide a Company Name for Scanning
 - `--aws` : Only Check for AWS S3 Buckets (Default)
 - `--gcp` : Only Check for GCP Buckets 
 - `--all` : Check for both AWS S3 and GCP Buckets
 
 Sometimes the tool reaches the rate limit while scanning S3 buckets, to prevent this from happening `no_of_workers` are reduced to 10 , If you increase this it will result in true-negatives or will give no result at all.
Kepping less numbers of threads may drastically increase the total execution time of the scanner, but gives better results.


# 🔧Installation

## 🔨 Using Git
- ` git clone https://github.com/MayankPandey01/OwnBucket`
- `python3 ownbucket.py -h` 

## 🧪 Recommended Python Version:
- This Tool Only Supports Python 3.
- The recommended version for Python 3 is 3.8.x.

## ⛳ Dependencies:

The dependencies can be installed using the requirements file:

Installation on Windows:  ![](https://camo.githubusercontent.com/920e3f8eb007a3834e641d27fddb9c102da3fd0c619785b52efb4dabcef2da1c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f776f726b666c6f772f7374617475732f6369706865792f6369706865792f507974686f6e2532306170706c69636174696f6e3f6c6162656c3d57696e646f7773)
- python.exe -m pip3 install -r requirements.txt.

Installation on Linux: ![](https://camo.githubusercontent.com/973cbf24b31b5d10c7f8d4f65fda4c696de8d3bed0923536820f9ac262b8ad08/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f776f726b666c6f772f7374617475732f6369706865792f6369706865792f507974686f6e2532306170706c69636174696f6e3f6c6162656c3d4c696e7578)
- sudo python3 pip3 install -r requirements.txt.


## 🐞 Bug Bounties

This tool is focused mainly on `Bug Bounty Hunters` and `Security Professionals` . You Can Use OwnBucket to Scan For Different Storage Buckets of the Target Company. 


## 🎯 Contribution ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)
We Love to Get Contribution from the Open Source Community💙. You are Welcome to Provide your Important Suggestions to make this tool more Awesome. Open a PR  and we will See to it ASAP.

**Ways to contribute**
- Suggest a feature
- Report a bug
- Fix something and open a pull request
- Spread the word

## 📚 DISCLAIMER

This project is a [personal development](https://en.wikipedia.org/wiki/Personal_development). Please respect its philosophy and don't use it for evil purposes. By using OwnBucket, you agree to the MIT license included in the repository. For more details at [The MIT License &mdash; OpenSource](https://opensource.org/licenses/MIT).

Happy Hacking ✨✨

> This Tool is Highly Motivated by [LazyS3](https://github.com/nahamsec/lazys3)

## 📃 Licensing

This project is licensed under the MIT license.
