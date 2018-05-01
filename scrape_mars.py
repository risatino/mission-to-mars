## scraping

# dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import tweepy
import time
import pandas as pd

# scrape function
def Scrape():

    print("COMMENCING SCRAPE")
    print("----------------------------------")

    # empty dict
    mars_dict = {}

    ### nasa mars news

    # mars news URL
    url = "https://mars.nasa.gov/news/"

    # retrieve page with the requests module
    html = requests.get(url)

    # create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # get title + description
    news_title = soup.find('div', 'content_title', 'a').text
    news_p = soup.find('div', 'rollover_description_inner').text

    # adding to dict
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p

    print("NEWS TITLE & DESCRIPTION ACQUIRED")


    ### JPL Mars Space Images

    # JPL mars URL
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # set up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # move through pages
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    # create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # get featured image
    results = soup.find('article')
    extension = results.find('figure', 'lede').a['href']
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension

    mars_dict["featured_image_url"] = featured_image_url

    print("FEATURED IMAGE ACQUIRED")


    # ## Mars Weather

    # twitter API credentials
    consumer_key = open("Keys/consumer_key.txt").read()
    consumer_secret = open("Keys/consumer_secret.txt").read()
    access_token = open("Keys/access_token.txt").read()
    access_token_secret = open("Keys/access_token_secret.txt").read()

    # use Tweepy to authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # target user
    target_user = "@MarsWxReport"

    # get tweet
    tweet = api.user_timeline(target_user, count=1)[0]

    # store weather
    mars_weather = tweet['text']

    mars_dict["mars_weather"] = mars_weather

    print("WEATHER ACQUIRED")


    ### mars facts

    # mars facts URL
    url = "https://space-facts.com/mars/"

    # retrieve page with the requests module
    html = requests.get(url)

    # create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # empty dict for info
    mars_profile = {}

    # get info
    results = soup.find('tbody').find_all('tr')

    # storing profile information
    for result in results:
        key = result.find('td', 'column-1').text.split(":")[0]
        value = result.find('td', 'column-2').text
        
        mars_profile[key] = value
        
    # create a DataFrame
    profile_df = pd.DataFrame([mars_profile]).T.rename(columns = {0: "Value"})
    profile_df.index.rename("Description", inplace=True)

    # convert to html
    profile_html = "".join(profile_df.to_html().split("\n"))

    # add to dictionary
    mars_dict["profile_html"] = profile_html

    print("FACTS ACQUIRED")


    ### mars hemispheres

    # mars hemispheres URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # empty list of image urls
    hemisphere_image_urls = []


    #### valles marineris

    # set up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # move through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)

    # create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # store link
    valles_link = soup.find('div', 'downloads').a['href']

    # create dict
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_link
    }

    # append dict
    hemisphere_image_urls.append(valles_marineris)


    #### cerberus

    # set up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # move through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    # create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # store link
    cerberus_link = soup.find('div', 'downloads').a['href']

    # create dict
    cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": cerberus_link
    }

    # append dict
    hemisphere_image_urls.append(cerberus)


    #### schiaparelli

    # set up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # move through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)

    # create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # store link
    schiaparelli_link = soup.find('div', 'downloads').a['href']

    # create dict
    schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": schiaparelli_link
    }

    # append dict
    hemisphere_image_urls.append(schiaparelli)


    #### syrtis major

    # set up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # move through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)

    # create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # store link
    syrtis_link = soup.find('div', 'downloads').a['href']

    # create dict
    syrtis_major = {
        "title": "Syrtis Major Hemisphere",
        "img_url": syrtis_link
    }

    # append dict
    hemisphere_image_urls.append(syrtis_major)

    # add to dict
    mars_dict["hemisphere_image_urls"] = hemisphere_image_urls

    print("HEMISPHERE IMAGES ACQUIRED")
    print("----------------------------------")
    print("SCRAPING COMPLETED")

    return mars_dict