# # https://www.torrentdownload.info/search?q=white

# import pandas as pd
# import requests
# from pprint import pprint
# import numpy
# import re

# url = 'https://www.torrentdownload.info'

# obj = pd.read_html(f"{url}/search?q=testing", extract_links='all')
# # web = requests.get(url)

# df = obj[1]

# # Rename columns in Pandas
# columns_name = ['result','date', 'size', 'seeder', 'leecher']

# for index, value in enumerate(columns_name):
# 	df.columns.values[index] = value



# nl = df.head().to_numpy().tolist()

# # for i in nl:
# # 	print(f"Result: {i[0][0]}")
# # 	print(f"Link: {url}{i[0][1]}")
# # 	print(f"Date: {i[1][0]}")
# # 	print(f"Size: {i[2][0]}")
# # 	print(f"Seeder: {i[3][0]}")
# # 	print(f"Leecher: {i[4][0]}")
# # 	print("\n")


# # page = requests.get('https://www.torrentdownload.info/03366AF659D186EEBCE90C1575E901433009B92B/Antivirus-Testing-Software')
# # find = re.findall(r'"magnet.*?"', page.text)
# # print(find[0])



#TESTING DUMMY SCRIPT

from pprint import pprint
import pandas as pd
import requests
import numpy
import re

def prettyPrinter(dict):
	pprint(dict)

class fitri:

    url = 'https://www.torrentdownload.info'
    name = 'Custom Fitri'

    def search(self, what, cat='all'):
        #get the table list from the website and load the table object for the result using index as df
        tablelist = pd.read_html(f"{self.url}/search?q={what}", extract_links='all')
        df = tablelist[1]

        # Renaming column parsed from website
        columns_name = ['result','date', 'size', 'seeder', 'leecher']

        for index, value in enumerate(columns_name):
            df.columns.values[index] = value
            
        #change to numpy for faster data translation
        dt = df.head().to_numpy().tolist()

        print(dt)

        #default sample data description
        data = {
                    'link': "magnetic_link",
                    'name': "testing_name",
                    'size': "file_size",
                    'seeds': "seeder_number",
                    'leech': "leecher_number",
                    'engine_url': f"{self.url}/search?q={what}",
                    'desc_link': "per_page_link"
                }

        #loop thru the each of the result and print
        for result in dt:
            #find the magnet link from each result
            page = requests.get(f'{self.url}/{result[0][1]}')
            find = re.findall(r'"magnet.*?"', page.text)
            link = find[0]

            #updating dictionary with current row value
            data.update({'link':link})
            data.update({'desc_link':result[0][1]})
            data.update({'name':result[0][0]})
            data.update({'size':result[2][0]})
            data.update({'seeds':result[3][0]})
            data.update({'leech':result[4][0]})

            #print to the gui
            prettyPrinter(data)

td = fitri()
td.search('testing')