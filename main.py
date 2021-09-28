from bs4 import BeautifulSoup
from googlesearch import search
import requests


class WebsiteImageScraper():

    ''' Finds wikipedia page based on search_query
        and provides interface to work with images
        from that page.
        Can be used to get images as BS4 obj
        for further manipulation or can write
        html img elements to file for use
        elsewhere.\n

        :param str search_query: Search query \n
        :param str search_website: Website to scrape images from (only name not URL) \n  
        :param str file_path: Path to store image results as HTML \n 
        :method: write_filtered_images_to file() \n
        :method: get_html_imgs(), returns all images as bs4 obj \n
        :method: filter_correct_imgs(), filters imgs using filter class (not built) '''
    
    def __init__(self, search_query, search_website, file_path):
        
        self.search_website = search_website       
        self.search_query = search_website + ' ' + search_query
        self.file_path = file_path        
        self.html_images = self.get_html_imgs()         
        
    
    def get_html_imgs(self):    
        
        """ CALLED IN CONSTRUCTOR
            Takes search_query and returns all
            html images as bs4 obj from 1st wikipedia page
            resulting from google search using 
            search query.
             """           

        # searches google for first wikipedia result using provided search term
        for j in search(self.search_query, tld="co.in", num=1, stop=1, pause=2):
            result = j

        html_page = requests.get(result)
        # then parsed into beautiful soup
        soup = BeautifulSoup(html_page.content, 'html.parser')
        html_images = soup.findAll('img')
        return html_images

    
    def get_img_srcs_as_list(self):

        imgs = self.get_html_imgs()
        img_srcs = []
        for img in imgs:
            
            img_srcs += [img['src']]
        return img_srcs
    

    def write_filtered_images_to_file(self):
        
        """ writes all img elements as html to 
            previously specified file path """

        with open(self.file_path, 'w') as file:
        
            images_of_search_query = self.filter_correct_imgs()

            for img in images_of_search_query:
                file.write(str(img) + '\n\n')

    
    def filter_correct_imgs(self):
        # right now only adding to list for writing to file
        # but will call filter class later
        """ takes html images and filters them for correct 
            properties then adds to list """
        
        html_images = self.html_images
        
        images_of_search_query = []
        for image_element in html_images:           
            
            images_of_search_query += [image_element]
        return images_of_search_query



img_scraper = WebsiteImageScraper('elon musk', 'wikipedia', 'index.html')

img_scraper.write_filtered_images_to_file()