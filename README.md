# Roambot

just a bot that roams around, shows you places [@roambot](https://twitter.com/roambot)

## Background

Back in 2016, I wanted to experiement with building Twitter bots. Something that particularly interested me was how places change over time. I hoped to build a bot that picked a random spot and used Google Maps to find its street views at different points in time. I found that the Google Maps API didn't offer time selection of street views, so I settled for something simpler: a bot that picks a random city, then picks a random spot in that city, and then shows us a street view of that spot. A snapshot of a place we might never think to find ourselves.

I originally built Roambot in 2016 in JavaScript, ran it locally and enjoyed the results, but never deployed it to a server to run continuously. Now that I primarily use Python, I decided to rewrite to bot in Python, utilize a few new APIs, and deploy it. This repository is the result.

## APIs and libraries

In order for the bot to do its thing, it relies on a handful of APIs and libraries.

1. [GeoDB Cities API](https://wirefreethought.github.io/geodb-cities-api-docs/) enables Roambot to randomly choose a city over a certain population threshold.
2. [Nominatim API](https://nominatim.org/release-docs/develop/api/Overview/) allows Roambot to find the bounding box of the randomly chosen city.
3. [Google Maps Street View Static API](https://developers.google.com/maps/documentation/streetview/intro) allows Roamboat to get a street view of a randomly chosen spot. This API used to be free, but now requires a credit card to use. The use for this bot will likely cost a few dollars a month, but it's worth keeping an eye on the quota, especially when playing with it locally. I wanted to preserve the original vision for this bot, but in the future, I'll prioritize free and open-source tools for bots.

## Running locally

the bot will not always produce something.