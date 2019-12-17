from indeed import extract_indeed_pages, extract_indeed_jobs #Call function

last_indeed_pages = extract_indeed_pages() #Get last page

indeed_jobs = extract_indeed_jobs(last_indeed_pages) #Find the job

print(indeed_jobs) #Check the all of job informations