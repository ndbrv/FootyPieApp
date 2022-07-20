from flask import Flask
from flask.helpers import make_response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import by
from selenium.webdriver.chrome.options import Options
import time


app = Flask(__name__)

chrome_options = Options()
chrome_options.add_argument("--headless")

@app.route('/stats/<player_name>')
def get_stats(player_name):
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # browser = webdriver.Chrome(r'C:\Users\Nikola\Documents\chromedriver.exe',options=chrome_options)
    #browser = webdriver.PhantomJS(r'C:\Users\Nikola\Documents\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    path = "./chromedriver"
    browser = webdriver.Chrome(executable_path=path,options=chrome_options)
    browser.get("https://fbref.com/en/")

    #searchBar = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((by.By.XPATH, "/html/body/div[2]/div[2]/div[3]/form/div/div/input[2]")))
    #searchBar = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/form/div/div/input[2]")
    #searchBar = browser.find_element_by_class_name("completely")

    #searchBar.send_keys(player_name)
    #searchBar.send_keys(Keys.RETURN)
    browser.execute_script(f'document.getElementsByTagName("input")[1].value="{player_name}";')
    browser.execute_script('document.getElementsByTagName("form")[0].submit();')



    print(f"---------------------------------{browser.current_url}-------------------------------")
    name = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((by.By.CLASS_NAME, "players")))
    name = name.find_element_by_xpath("//div[1]//div[2]//h1//span")

    
                                                                                            
    table = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((by.By.TAG_NAME, "tbody")))
    #table = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((by.By.CSS_SELECTOR, "#scout_summary_FW > tbody:nth-child(4)")))
    npG = table.find_element_by_xpath("//tr[1]//td[1]")
    npGPercentile = table.find_element_by_xpath("//tr[1]//td[2]/div[1]")
    npxG = table.find_element_by_xpath("//tr[2]//td[1]")
    npxGPercentile = table.find_element_by_xpath("//tr[2]//td[2]/div[1]")
    shotsTotal = table.find_element_by_xpath("//tr[3]//td[1]")
    shotsTotalPercentile = table.find_element_by_xpath("//tr[3]//td[2]/div[1]")
    assists = table.find_element_by_xpath("//tr[4]//td[1]")
    assistsPercentile = table.find_element_by_xpath("//tr[4]//td[2]/div[1]")
    xA = table.find_element_by_xpath("//tr[5]//td[1]")
    xAPercentile = table.find_element_by_xpath("//tr[5]//td[2]/div[1]")
    npxGA = table.find_element_by_xpath("//tr[6]//td[1]")
    npxGAPercentile = table.find_element_by_xpath("//tr[6]//td[2]/div[1]")
    shotcreatingActions = table.find_element_by_xpath("//tr[7]//td[1]")
    shotcreatingActionsPercentile = table.find_element_by_xpath("//tr[7]//td[2]/div[1]")
    passesAttempted = table.find_element_by_xpath("//tr[9]//td[1]")
    passesAttemptedPercentile = table.find_element_by_xpath("//tr[9]//td[2]/div[1]")
    passCompletion = table.find_element_by_xpath("//tr[10]//td[1]")
    passCompletionPercentile = table.find_element_by_xpath("//tr[10]//td[2]/div[1]")
    progressivePasses = table.find_element_by_xpath("//tr[11]//td[1]")
    progressivePassesPercentile = table.find_element_by_xpath("//tr[11]//td[2]/div[1]")
    progressiveCarries = table.find_element_by_xpath("//tr[12]//td[1]")
    progressiveCarriesPercentile = table.find_element_by_xpath("//tr[12]//td[2]/div[1]")
    dribblesCompleted = table.find_element_by_xpath("//tr[13]//td[1]")
    dribblesCompletedPercentile = table.find_element_by_xpath("//tr[13]//td[2]/div[1]")
    touches = table.find_element_by_xpath("//tr[14]//td[1]")
    touchesPercentile = table.find_element_by_xpath("//tr[14]//td[2]/div[1]")
    progPassesRec = table.find_element_by_xpath("//tr[15]//td[1]")
    progPassesRecPercentile = table.find_element_by_xpath("//tr[15]//td[2]/div[1]")

    



    # playerName = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((by.By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/h1/span")))
    # npG = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((by.By.XPATH, "/html/body/div[2]/div[6]/div[2]/div[1]/div/div/div[4]/div[1]/table/tbody/tr[1]/td[1]")))
    # npxG = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((by.By.XPATH, "/html/body/div[2]/div[6]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[1]")))
    # shotsTotal = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((by.By.XPATH, "/html/body/div[2]/div[6]/div[2]/div[1]/div/div/div[4]/div[1]/table/tbody/tr[3]/td[1]")))
    # assists = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((by.By.XPATH, "/html/body/div[2]/div[6]/div[2]/div[1]/div/div/div[4]/div[1]/table/tbody/tr[4]/td[1]")))
    # xA = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((by.By.XPATH, "/html/body/div[2]/div[6]/div[2]/div[1]/div/div/div[4]/div[1]/table/tbody/tr[5]/td[1]")))


    response = {"name": "",
    "npG":"",
    "npxG":"",
    "shotsTotal":"",
    "assists":"",
    "npxG+xA":"",
    "shotCreatingActions":"",
    "passesAttempted":"",
    "passCompletion":"",
    "progPasses":"",
    "progCarries":"",
    "dribblesCompleted":"",
    "touches":"",
    "progPassesRec":""}
    response["name"] = name.text
    response["npG"] = [float(npG.text), float(npGPercentile.text)/100]
    response["npxG"] = [float(npxG.text), float(npxGPercentile.text)/100]
    response["shotsTotal"] = [float(shotsTotal.text), float(shotsTotalPercentile.text)/100]
    response["assists"] = [float(assists.text), float(assistsPercentile.text)/100]
    response["assistsX"] = [float(xA.text), float(xAPercentile.text)/100]
    response["npxG+xA"] = [float(npxGA.text), float(npxGAPercentile.text)/100]
    response["shotCreatingActions"] = [float(shotcreatingActions.text), float(shotcreatingActionsPercentile.text)/100]
    response["passesAttempted"] = [float(passesAttempted.text), float(passesAttemptedPercentile.text)/100]
    response["passCompletion"] = [round(float(passCompletion.text.strip('%'))/100,3), float(passCompletionPercentile.text)/100]
    response["progPasses"] = [float(progressivePasses.text), float(progressivePassesPercentile.text)/100]
    response["progCarries"] = [float(progressiveCarries.text), float(progressiveCarriesPercentile.text)/100]
    response["dribblesCompleted"] = [float(dribblesCompleted.text), float(dribblesCompletedPercentile.text)/100]
    response["touches"] = [float(touches.text), float(touchesPercentile.text)/100]
    response["progPassesRec"] = [float(progPassesRec.text), float(progPassesRecPercentile.text)/100]


    flask_resp = make_response(response)
    flask_resp.headers['Access-Control-Allow-Origin'] = "*"


    ##return browser.find_element_by_tag_name("span").text
    ##return browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/h1/span").text
    return flask_resp
