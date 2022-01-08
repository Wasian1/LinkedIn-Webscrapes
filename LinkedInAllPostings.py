
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = Options()

#use pd.set_option to expand view of dataframe and avoid "..." when using print()

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#create variable for the directory path that your chromedriver.exe is stored in
PATH = "C://Program Files (x86)//chromedriver.exe"

#set up driver variable to store your Chrome Webdriver activation code
driver = webdriver.Chrome(PATH)

#set up url variable to access LinkedIn. Replace the job title (Chemical Engineer) and location (Arizona) in the url to configure the search according to your desired parameters. 

url = 'https://www.linkedin.com/jobs/search?keywords=Chemical%20Engineer&location=Arizona&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

#maximize Chrome to avoid opening job descriptions in a new window when clicking on postings

driver.maximize_window()

#use driver.get method on your url variable to open the link

driver.get(url)

#set up a variable to contain the number of jobs your search returns. Use get_attribute method to get the inner text of the webelement

no_of_jobs = int(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/h1/span[1]').get_attribute('innerText'))

#set up brackets for Python list

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

#use loop below to scroll down to the bottom of the job postings page. Use a try and except to click the load more jobs button when it appears. 

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

#use find_element_by_class_name to create a webelement of the job search results

job_lists = driver.find_element_by_class_name('jobs-search__results-list')

#set up a list of all elements under <li> tags inside the job search result web element (Each job posting is embedded inside a <li> tag in the LinkedIn HTML)

jobs = job_lists.find_elements_by_tag_name('li')

#print the number of elements in your list (Should be the same as the number of job postings returned by your search parameters)

print(len(jobs))

#set up a for loop to iterate through your jobs webelement list and collect the 'JobTitle', 'Company Name', 'Location', 'Date Posted' and 'Job Link URL' from each post

for job in jobs:
    #use css selector method to get job_title element from underneath the h3 tags. Get text with get_attribute innerText
    job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
    #append job_title0 text to your Job Title Python list
    job_title.append(job_title0)

    #use css selector method to get company_name element from underneath the h4 tags. Get text with get_attribute innerText
    company_name0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
    #append company_name0 to your Company Name Python list
    company_name.append(company_name0)

    #use css selector method to get location element based on its class. Get text with get_attribute innerText
    location0 = job.find_element_by_css_selector('[class="job-search-card__location"]').get_attribute('innerText')
    #append location0 to your Location Python list
    location.append(location0)

    #use css selector method to get the date posted from under the div tags and time. Use get_attribute datetime to get the date posted
    date0 = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
    #append date0 to your Date Python list
    date.append(date0)

    #use css selector method to get link from underneath the a tag. Use get_attribute href to get the href link
    job_link0 = job.find_element_by_css_selector('a').get_attribute('href')
    #append job_link0 to your Job Link Python list
    job_link.append(job_link0)

    #use another for loop to first click on the job posting, then click the show more button to open the full job posting description. 
    #use len(jobs) to iterate through all job postings. The xpath for clicking the job postings and show more buttons will change and necessitates a few try and excepts
    #for item in range  is used to cycle through each posting by changing the li tag number to move from one posting to another
for item in range(len(jobs)):
    try:
        job_click_path = f'/html/body/div[1]/div/main/section[2]/ul/li[{item + 1}]/div/a'
        job_click = driver.find_element_by_xpath(job_click_path).click()
        time.sleep(5)
    except:
        job_click_path2 = f'/html/body/div[1]/div/main/section[2]/ul/li[{item + 1}]/a'
        job_click2 = driver.find_element_by_xpath(job_click_path2).click()
        time.sleep(5)

        #use WebDriverWait to wait until job posting is clicked and show more button loads
        #show_more xpath also changes and neccessitates try and except
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
