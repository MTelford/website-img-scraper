# Website Image Scraper

_Website Image Scraper_

A tool for scraping images off a webpage

## Description

This tool can be used to scrape images from a specified website. 
Provide a search term (such as a name or object) and a website name (not the URL).
The images found on the page, which is the top Google result, are written to the users file of choice in HTML format. (There is also a method for aquiring all HTML image element sources as a list).

## Getting Started

### Dependencies

Python 3.8+


### Installing

Clone the repo via your preferred method <br></br>
Create a virtual envirnoment, for eg
``` python3.8 -m virutalenv env ```

Activate virtual envirnoment
``` source/env/bin/activate ```

Install dependencies
``` pip install -r requirements.txt ```

The class is now ready to use!

### Using the code

Simply instatiate the class and call desired methods.

For eg.

``` 
img_scraper = WebsiteImageScraper('elon musk', 'wikipedia', 'index.html')
img_scraper.write_filtered_images_to_file()
```
    
This code will search Google for the Wikipedia page that best corresponds to the search term 'elon musk'.
It will then write the scraped images to the specified file ```index.html```. 

**Note:**
There is a method in the class for filtering scraped images that is essentially non functional
at this point. The idea here is to add some filtering method in the future (such as ML models) to further specify the images. This could be achieved by subclassing and overriding the filter method with the preferred method for filtering the images.

## Authors

_Michael Telford_ <br></br>
https://github.com/MTelford/


## License

This project is licensed under the MIT License - see the LICENSE.md file for details

