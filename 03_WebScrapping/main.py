from pprint import pprint
import json
# import re
import bs4
import requests
from fake_headers import Headers


def get_headers():
    return Headers(os="win", browser="chrome").generate()

def create_hh_link(page_number):
    return f"https://hh.ru/search/vacancy?text=python&area=1&area=2&page={page_number}"

def parse_page(job_tags, max_vacancy=None, dollar_sal=False):
    def append_data(parsed_data, relative_url, title, company, company_address, salary):
        parsed_data.append({
                    "title": title,
                    "company": company,
                    "company_address": company_address,
                    "salary": salary,
                    "link": relative_url
        })
    n=0
    parsed_data = []
    for job_tag in job_tags:
        h3_tag = job_tag.find("h3", class_="bloko-header-section-3")
        a_tag = h3_tag.find("a", class_="bloko-link")
        relative_url = a_tag["href"].split("?")[0]
        print(f'\rParsing: {relative_url}', end='')
        job_response = requests.get(relative_url, headers=get_headers())
        job_soup = bs4.BeautifulSoup(job_response.text, features="lxml")
        job_description_tag = job_soup.find("div", class_="vacancy-section")
        if not job_description_tag: continue

        if any(word in job_description_tag.text.lower() for word in ["django", "flask"]):
            title = a_tag.text
            company_tag = job_tag.find("div", class_="vacancy-serp-item__info")
            company = company_tag.find("a", attrs = {"data-qa" : "vacancy-serp__vacancy-employer"}).text
            company_address = company_tag.find("div", attrs = {"data-qa" : "vacancy-serp__vacancy-address"}).text
            salary_tag = job_tag.find("span", attrs = {"data-qa" : "vacancy-serp__vacancy-compensation"})
            # pattern = re.compile(r"<span[^>]*>(.*)</span>")
            # pattern2 = re.compile(r"<!-- -->")
            # pattern = re.compile(r"<span[^>]*>(.*)\s(<!-- -->)?(.*)</span>")
            
            if not salary_tag:
                salary = "зарплата не указана"
            else:
                salary = salary_tag.text
                # salary = str(salary_tag)
                # salary = re.sub(pattern, r"\1", salary)
                # salary = re.sub(pattern2, "", salary)

            if dollar_sal:
                # if re.findall(r"\$", salary):
                if '$' in salary:
                    append_data(parsed_data, relative_url, title, company, company_address, salary)
            else:
                append_data(parsed_data, relative_url, title, company, company_address, salary)
        if max_vacancy:
            if n == max_vacancy:
                print()
                return parsed_data
            else:
                n += 1
    print()
    return parsed_data



page = 0
def get_all_jobs(pages=1, max_vacancy=None, dollar_sal=False):
    print(f'Parsing {pages} pages')
    parsed_data = []
    for page in range(pages):
        response = requests.get(create_hh_link(page), headers=get_headers())
        main_html_data = response.text
        main_soup = bs4.BeautifulSoup(main_html_data.replace("\xa0", " "), features="lxml")
        tag_div_job_list = main_soup.find("main", class_="vacancy-serp-content")
        job_tags = tag_div_job_list.find_all("div", class_="serp-item serp-item_link")
        print(f"Page: {page+1} | Parsing {max_vacancy if max_vacancy else len(job_tags)} of {len(job_tags)} jobs")
        parsed_data.extend(parse_page(job_tags, max_vacancy=max_vacancy, dollar_sal=dollar_sal))
    return parsed_data        


#pprint(get_all_jobs(page=3, max_vacancy=10))
# pprint(parse_page(job_tags, max_vacancy=10))
jobs = get_all_jobs(pages=3, max_vacancy=5)
# jobs = get_all_jobs(pages=5, dollar_sal=True)
json.dump(jobs, open("data.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)