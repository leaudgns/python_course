import requests
from bs4 import BeautifulSoup

LIMIT = 20
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?l=%EA%B4%91%EC%A3%BC&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        # pages.append(link.find("span").string)
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    #company = html.find("span",{"class" : "company"}).string
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company:
        if company_anchor != None:
            company = str(company_anchor.string.strip())
        else:
            company = str(company.string.strip())
    else:
        company = None
    # location = str(html.find("span",{"class" : "location"}).string)
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    location = location.strip()
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, 'link': f"https://www.indeed.com/rc/clk?jk={job_id}&from=vj&pos=bottom"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed page : {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
