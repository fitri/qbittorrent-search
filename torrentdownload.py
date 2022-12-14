#VERSION: 1.01
#AUTHORS: FitriRahim (fitri@fitri.me)

# LICENSING INFORMATION

from novaprinter import prettyPrinter

import pandas as pd
import requests
import numpy
import re

class torrentdownload(object):

    url = 'https://www.torrentdownload.info'
    name = 'Magnet TorrentDownload'

    def search(self, what, cat='all'):
        #get the table list from the website and load the table object for the result using index as df
        tablelist = pd.read_html(f"{self.url}/search?q={what}", extract_links='all')
        df = tablelist[1]

        # Renaming column parsed from website
        columns_name = ['result','date', 'size', 'seeder', 'leecher']

        for index, value in enumerate(columns_name):
            df.columns.values[index] = value
            
        #change to numpy for faster data translation
        dt = df.to_numpy().tolist()

        #initialize data dict
        data = {
                    'engine_url': f"{self.url}/search?q={what}"
                }

        #loop thru the each of the result and print
        for result in dt:
            #find the magnet link from each result
            page = requests.get(f'{self.url}/{result[0][1]}')
            find = re.findall(r'"magnet.*?"', page.text)
            link = find[0]

            #updating dictionary with current row value
            data.update({'link':eval(link)})
            data.update({'desc_link':f"{self.url}{result[0][1]}"})
            data.update({'name':result[0][0]})
            data.update({'size':result[2][0]})
            data.update({'seeds':result[3][0]})
            data.update({'leech':result[4][0]})

            #print to the gui
            prettyPrinter(data)
