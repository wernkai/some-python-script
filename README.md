# some-python-script

Personal use python automation script, web scraping script.

## Table of Content
- [GenshinAutoRedeem](#GenshinAutoRedeem)
- [Pokemon Png Scrap](#Pokemon-Png-Scrap)
- [Pytest-Only](#Pytest-Only)

### GenshinAutoRedeem
<b><u>Description:</u></b> <br/>
Automating the process of redeeming Genshin codes.

<b><u>Note:</u></b> <br/>
- Still pending testing using a valid Genshin code. <br/>
- Use Selenium IDE to record the procedure and subsequently export it into a Python script. <br/>
- The script functions only under the condition that the reCAPTCHA is not triggered. <br/>

<b><u>How to:</u></b> <br/>
1. Replace line 47, 49 with correct email and password.
2. Replace line 97 with valid codes.

<b><u>To Do:</u></b> <br/>
Record the returned message to check whether the redemption is valid or not.

### Pokemon-Png-Scrap
<b><u>Description:</u></b> <br/>
Scrap pokemon script from pokemondb.net.

<b><u>Note:</u></b> <br/>
- The sprite downloaded is under lets-go-pikachu-eevee version.
- Use BeautifulSoup to crawl the HTML and request library to download the png.
- Some Pokemon name with special character might not be able to download, example: Nidoran male/female.

<b><u>How to:</u></b> <br/>
1. replace line 23 with targer download destination path.

<b><u>To Do:</u></b> <br/>
NA

### Pytest-Only
<b><u>Description:</u></b> <br/>
Some random PyTest script with different scenario.

<b><u>Note:</u></b> <br/>
- Class method functional test scenario.
- Rest API GET response test scenario.

<b><u>How to:</u></b> <br/>
NA

<b><u>To Do:</u></b> <br/>
- REST API POST response test scenario.
- REST API with Auth test scenario.
- REST API with Apache Spark dataframe scenario.

#### Package requirement
```
1. selenium
2. pytest
3. bs4
```