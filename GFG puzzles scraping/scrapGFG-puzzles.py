from random import randint
import time
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = False
driver = webdriver.Firefox(options=options,executable_path='C:/Program Files/Mozilla Firefox/geckodriver-v0.29.0-win64/geckodriver.exe') # Add your own path here
driver.set_window_size(randint(800, 1080), randint(1024, 1920))

def getPuzzleLinks():
    try:
        driver.get('https://www.geeksforgeeks.org/puzzles/')
        puzLink =  driver.find_elements_by_tag_name('ol')[0].find_elements_by_tag_name('a')[:-1]
        print(puzLink[0].get_attribute('href'))
        try:
            return [link.get_attribute("href") for link in puzLink]
        except Exception as e:
            print('Error in obtaining links from the obtained HTML elements-',str(e))
            return None
    except Exception as e:
        print('Error encountered on GFG page-',str(e))
        return None

def scrapPuzzle(link):
    try:
        driver.get(link)
        time.sleep(2)
        try:
            name = driver.find_elements_by_class_name('title')[0].text
        except Exception as e:
            print(f'Puzzle name not found-{str(e)}')
            return None
        print(name)
        try:
            blog = driver.find_elements_by_class_name('text')[-1]
            blog_parts = blog.find_elements_by_tag_name('p')
            pText = [p.text for p in blog_parts]
            # All the 3 can be chained together but which part is raising error wont be known. 
        except Exception as e:
            print(f'Error in finding main text of puzzles-{str(e)}')
            return None
        res = dict()
        try:
            puzzle_no = name.split(' ')[1][:2] if name.split(' ')[1] != '|' else '35'
            res['id'] = int(puzzle_no)
        except Exception as e:
            print(name.split(' ')[1], len(name.split(' ')[1]))
            print(f'Puzzle index not obtained with error-{str(e)}')
        try:
            res['name'] = name[(name.index('(')+1):-1]
        except Exception as e:
            print(f'Puzzle index not obtained with error-{str(e)}')
            if puzzle_no in [43,44]:
                res['name'] = name(name.index('|')+2)
        res['question'] = pText[0]
        ans = list()
        for p in pText[1:]:
            if len(p.strip()) >5 and p.strip()[:6] not in ['Please','Source']:
                ans.append(p.strip().replace('\u201c','\"').replace('\u201d','\"').replace('\u2019','\''))
        res['answer'] = (' ').join(ans) + ' \nSource: '+ link
        return res
    except Exception as e:
        print(f'Puzzle page not obtained for puzzle link {link} with error-{str(e)}')
        return None


links = getPuzzleLinks()
output = list(map(scrapPuzzle, links))
driver.quit()
with open('result-1.json', mode= 'w') as f:
    f.write(json.dumps(output))
