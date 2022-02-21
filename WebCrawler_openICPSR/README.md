# Web Crawler - OPEN ICPSR
This web crawler is an assignment from Dr. Xu NLP class at UTHealth SBMI.
The target website is [OPEN ICPSR](https://www.openicpsr.org/openicpsr/search/studies?start=0&ARCHIVE=openicpsr&sort=score%20desc%2CDATEUPDATED%20desc&rows=163&q=%22coronavirus%22%20OR%20tag%3A%22covid%2019%22%20OR%20%22coronavirus%22%20OR%20%22covid-19%22%20OR%20%22sars-cov-2%22) and extract all COVID-19 search results as well as data information from each project/researches. Each individual result is saved into JSON file by following [`NLP_json_format.json`](./NLP_json_format.json), which is derived from [Schema.org](https://schema.org/Dataset). 

## Requirements for this Web Crawler 
WebCrawler_openICPSR is developed under Python 3.7.9 and beautifulsoup4 4.10.0.

## Using the Web Crawler
Current searching keyword is `"coronavirus" OR tag:"covid 19" OR "coronavirus" OR "covid-19" OR "sars-cov-2"`.
To adjust the keyword is to replace the link inside the `hw2_code.py`.
And run it with console
```
python hw2_code.py
```
After the execution, the json files are saved to the folder,`json_file`.
