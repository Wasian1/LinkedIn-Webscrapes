from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from itertools import islice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument("window-size=1400,1400")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

PATH = "C://Program Files (x86)//chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = 'https://www.linkedin.com/jobs/search?keywords=Chemical%20Engineer&location=Arizona&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

driver.maximize_window()

driver.get(url)

no_of_jobs = int(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/h1/span[1]').get_attribute('innerText'))

job_title = []
company_name = []
location = []
date = []
job_link = []
jd = []
seniority = []
emp_type = []
job_func = []
industries = []

i = 2
while i <= int(no_of_jobs/25)+1:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    i = i + 1
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/main/section[2]/button').click()
        time.sleep(5)
    except:
        pass
        time.sleep(5)

job_lists = driver.find_element_by_class_name('jobs-search__results-list')
jobs = job_lists.find_elements_by_tag_name('li')
print(len(jobs))

limit = 3
for job in islice(jobs, limit):
    job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
    job_title.append(job_title0)

    company_name0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
    company_name.append(company_name0)

    location0 = job.find_element_by_css_selector('[class="job-search-card__location"]').get_attribute('innerText')
    location.append(location0)

    date0 = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
    date.append(date0)

    job_link0 = job.find_element_by_css_selector('a').get_attribute('href')
    job_link.append(job_link0)

for item in range(3):
    try:
        job_click_path = f'/html/body/div[1]/div/main/section[2]/ul/li[{item + 1}]/div/a'
        job_click = driver.find_element_by_xpath(job_click_path).click()
        time.sleep(5)
    except:
        job_click_path2 = f'/html/body/div[1]/div/main/section[2]/ul/li[{item + 1}]/a'
        job_click2 = driver.find_element_by_xpath(job_click_path2).click()
        time.sleep(5)

    try:
        show_more = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/section/div[2]/div[1]/section[1]/div/div[2]/section/button[1]')))
        show_more.click()
        time.sleep(5)
    except:
        pass

    try:
        show_more2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/section/div[2]/div[1]/section[1]/div/div/section/button[1]')))
        show_more2.click()
        time.sleep(5)
    except:
        pass

    try:
        show_more3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/section/div[2]/div[1]/section[1]/div/div/section/button[1]')))
        show_more3.click()
        time.sleep(5)
    except:
        pass

    jd_path = '/html/body/div[1]/div/section/div[2]/div/section[1]/div'
    jd0 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, (jd_path))))
    jd00 = jd0.get_attribute('innerText')
    jd.append(jd00)

    try:
        seniority_path = '/html/body/div[1]/div/section/div[2]/div[1]/section[1]/div/ul/li[1]/span'
        seniority0 = driver.find_element_by_xpath(seniority_path).get_attribute('innerText')
        print(seniority0)
    except NoSuchElementException:
        try:
            seniority_path_2 = '/html/body/div[1]/div/section/div[2]/div[1]/section[2]/div/ul/li[1]/span'
            seniority0 = driver.find_element_by_xpath(seniority_path_2).get_attribute('innerText')
            print(seniority0)
        except NoSuchElementException:
            seniority0 = 'N/A'
            print(seniority0)

    seniority.append(seniority0)

    try:
        emp_type_path = '/html/body/div[1]/div/section/div[2]/div/section[1]/div/ul/li[2]/span'
        emp_type0 = driver.find_element_by_xpath(emp_type_path).get_attribute('innerText')
    except NoSuchElementException:
        try:
            emp_type_path_2 = '/html/body/div[1]/div/section/div[2]/div[1]/section[2]/div/ul/li[2]/span'
            emp_type0 = driver.find_element_by_xpath(emp_type_path_2).get_attribute('innerText')
        except NoSuchElementException:
            emp_type0 = 'N/A'

    emp_type.append(emp_type0)

    try:
        job_func_path = '/html/body/div[1]/div/section/div[2]/div/section[1]/div/ul/li[3]/span'
        job_func0 = driver.find_element_by_xpath(job_func_path).get_attribute('innerText')
    except NoSuchElementException:
        try:
            job_func_path_2= '/html/body/div[1]/div/section/div[2]/div[1]/section[2]/div/ul/li[3]/span'
            job_func0 = driver.find_element_by_xpath(job_func_path_2).get_attribute('innerText')
        except NoSuchElementException:
            job_func0 = 'N/A'

    job_func.append(job_func0)

    try:
        industries_path = 'html/body/div[1]/div/section/div[2]/div[1]/section[1]/div/ul/li[4]/span'
        industries0 = driver.find_element_by_xpath(industries_path).get_attribute('innerText')
    except NoSuchElementException:
        try:
            industries_path_2 = '/html/body/div[1]/div/section/div[2]/div[1]/section[2]/div/ul/li[4]/span'
            industries0 = driver.find_element_by_xpath(industries_path_2).get_attribute('innerText')
        except NoSuchElementException:
            industries0 = 'N/A'

    industries.append(industries0)

job_data = pd.DataFrame({'Job Title': job_title,
                         'Company Name': company_name,
                         'Location': location,
                         'Date': date,
                         'Job Link': job_link,
                         'Job Description': jd,
                         'Seniority': seniority,
                         'Employment Type': emp_type,
                         'Job Function': job_func,
                         'Industry': industries
                         })

job_data['Job Description'] = job_data['Job Description'].str.replace('\n', ' ')
print(job_data)
job_data.to_csv('test_scrape.csv', index=False, encoding='utf-8')
