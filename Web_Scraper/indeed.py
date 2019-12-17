import requests #Navigating with Python
from bs4 import BeautifulSoup #extract Indeed pages

LIMIT = 50
URL = f"https://www.indeed.ca/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser") #extract html

  #find the pagination that is div's class name
  pagination = soup.find("div", {"class": "pagination"})

  #Find all anchor
  pages = pagination.find_all('a')
  spans = [] # append the span
  for page in pages[:-1]: # except the last one that is 'next'
    spans.append(int(page.string))
  max_page = spans[-1] #find the last_page
  return max_page 

def extract_job(html):
  title = html.find("div",{"class": "title"}).find("a")["title"]
  company = html.find("span", {"class": "company"}) #find the span with class "company"
  company_anchor = company.find("a") #make another soup with anchor
  if company_anchor is not None:
    company = str(company_anchor.string)
  else:
     company = str(company.string)
  company = company.strip()
  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"] # There is hidden value so I need to access different method
  job_id = html["data-jk"]
  return {
    'title': title, 
    'company': company, 
    'location': location, 
    "link": f"https://www.indeed.ca/viewjob?jk={job_id}"
    }

def extract_indeed_jobs(last_pages):
  jobs=[]
  for page in range(last_pages):
    print(f"Scrappin page {page}") # Count the scrapping pages
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser") #extract html
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs