from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://www.easports.com/fifa/ultimate-team/web-app/')

print('Only Key In the following after transfer page screen is loaded, DO NOT press the final search button!')
time.sleep(0.5)
refreshCount = input('How many times do you want to refresh?(more refreshes = longer) : ')
time.sleep(0.5)
Lagtime = input('How fast do you want the refreshes to be, note: if too fast the screen will not load, we recommend 0.5s: ') 




#automated clicker to force search refresh
def ButtonClickSwitcher(i):
    if (i % 2) == 0:
        ibButton = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]')
        ibButton.click()
    else:
        dbButton = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[1]')
        dbButton.click()

def SearchClick():
    FinalSB = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]')
    FinalSB.click()

SearchClick()
time.sleep(1)

for i in range(int(refreshCount)):
    try:
        time.sleep(float(Lagtime))
        Max_BNP2 = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[3]/span[2]').text

    except:
        backButton = driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]')
        backButton.click()
        ButtonClickSwitcher(i)
        SearchClick()
        continue
    else:

        Max_BNP2Button = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]')
        Max_BNP2Button.click()
        FinalBuyButton = driver.find_element_by_xpath('/html/body/div[4]/section/div/div/button[1]')
        FinalBuyButton.click()
        print('Player Bought')
        break


print('Process Finished')




