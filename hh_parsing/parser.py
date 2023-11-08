import requests
import re
import multiprocessing

def add_ids(url):
    job_title = 'Data Analyst'
    number_of_pages = 20
    ids = []

    for i in range(number_of_pages):
        par = {'text': job_title, 'area': 113, 'per_page': 100, 'page':i}
        r = requests.get(url, params=par)        
        e = r.json()

        for i in range(len(e['items'])):
            ids.append(e['items'][i].get('id'))
    return ids

def fill(row):      
    def celar_description(data):
        return re.sub(r"<[^>]+>", "", data, flags=re.S)
        
    def key_skills_fill(data):
        res = []
        if data != None and len(data) != 0:
            return [el["name"] for el in data]
        else:
            return None
            
    def name(data):
        return data['name']
        
    res = [row.get('name'), name(row.get('area')), row.get('salary'), row.get('published_at'), name(row.get('employer')), 
           key_skills_fill(row.get('professional_roles')), name(row.get('experience')), name(row.get('schedule')),
           name(row.get('employment')), key_skills_fill(row.get('key_skills')), celar_description(row.get('description'))]

    return res

def create_df(ids, url):
    interesting_columns = ['name', 'area', 'salary', 'published_at', 'employer', 'professional_roles', 'experience', 'schedule',
                           'employment', 'key_skills', 'description']
    df = pd.DataFrame(columns = interesting_columns)
    
    for i in range(len(ids)):
        data = requests.get(url+ids[i]).json()
        df.loc[i] = fill(data)
    return df

url = 'https://api.hh.ru/vacancies/'

ids = add_ids(url)
df = create_df(ids, url)

for _ in range(multiprocessing.cpu_count()):
        multiprocessing.Process(target=add_ids, args=(url,)).start()

for _ in range(multiprocessing.cpu_count()):
        multiprocessing.Process(target=create_df, args=(ids, url)).start()
    
df.to_csv('hh.csv', index = False)