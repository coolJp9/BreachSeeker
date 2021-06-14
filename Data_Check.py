from selenium import webdriver
import time
from pyfiglet import Figlet
from termcolor import colored

print("=" * 65)
print("=" * 65)
spt_nm = Figlet(font="banner3-D")
print(colored(spt_nm.renderText('Breach Seeker'), 'red'))
print("=" * 65)
print("=" * 65)

Data = input('Enter your email id : ')
Time1 = input('Enter time delay (in second) : ')

website = ["https://intelx.io/", "https://haveibeenpwned.com", "https://monitor.firefox.com/",
           "https://www.hotsheet.com/inoitsu/", "https://cybernews.com/personal-data-leak-check/",
           "https://www.avast.com/hackcheck", "https://whatismyipaddress.com/breach-check",
           "https://namescan.io/FreeEmailCompromisedCheck.aspx",
           "https://www.f-secure.com/en/home/free-tools/identity-theft-checker"]
searchbar = ['//*[@id="Term"]', '//*[@id="Account"]', '//*[@id="scan-email"]', '//*[@id="act"]',
             '/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/form/input[1]',
             '//*[@id="app"]/main/section[1]/div/section/div[1]/div/form/input', '//*[@id="txtemail"]',
             '//*[@id="cpM_txtEmail"]', '//*[@id="id-theft-form"]/div/div/input']
button = ['//*[@id="btnSearch"]', '//*[@id="searchPwnage"]', '//*[@id="scan-user-email"]/div[3]/input',
          '//*[@id="pawncheck"]/input[3]',
          '/html/body/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/form/input[2]',
          '//*[@id="app"]/main/section[1]/div/section/div[1]/a', '//*[@id="btnSubmit"]', '//*[@id="cpM_lnkSearch"]',
          '//*[@id="background-1648527111"]/div/div/div[1]/a']

# specify the location directly via executable_path
driver = webdriver.Firefox(executable_path='./geckodriver.exe')
############################################################
for i in range(0, len(website)):
    driver.get(website[i])  # navigate to site

    search_bar = driver.find_element_by_xpath(searchbar[i])
    search_bar.send_keys(Data)

    search_button = driver.find_element_by_xpath(button[i])
    search_button.click()
    print("Title : ", driver.title)
    print("URL : ", driver.current_url)
    time.sleep(Time1)
