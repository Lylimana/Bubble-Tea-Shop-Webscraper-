# Attempt 1
    # from bs4 import BeautifulSoup
    # import requests 

    # def scrapeTeaShops(): 
    #     pageToScrape = requests.get("https://www.google.com/search?sa=X&sca_esv=ba24c2d2484ecd3d&tbm=lcl&sxsrf=AE3TifOBVBcsDZOoPSp6xTxbxqxHLireEw:1756331709703&q=bubble+tea+shops+in+central+london&rflfq=1&num=10&ved=2ahUKEwj6rai9_auPAxVtVUEAHav-AJoQjGp6BAgvEAE&biw=1197&bih=1190&dpr=0.8#rlfi=hd:;si:;mv:[[51.5400213,0.0467541],[51.507119100000004,-0.15539809999999998]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2", timeout =5) # Add link to scrape here
    #     soup = BeautifulSoup(pageToScrape.text, "html.parser")
    #     TeaShopNames = soup.find_all('span' , attrs = {'class':'OSrXXb'})
        
    #     for TeaShopName in TeaShopNames: 
    #         print(TeaShopName.text)
            
    # def main() -> None: 
    #     scrapeTeaShops()
    
    # if __name__ == '__main__': 
    #     main()




# Attempt 2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrapeTeaShops(): 
    bobaData = []
    
    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (optional)
    
    # Service object
    service = Service(ChromeDriverManager().install())
    

    # initialise driver
    driver = webdriver.Chrome(service=service, options=options)
    url = "https://www.google.com/search?sca_esv=465159d7bf2b0b64&tbm=lcl&sxsrf=AE3TifNap3yiVLX0363JcDFmzLil_tN2wg:1756406355848&q=bubble+tea+shops+london&rflfq=1&num=10&sa=X&ved=2ahUKEwijua_Hk66PAxWOXEEAHVpCPFYQjGp6BAgpEAE&biw=1197&bih=1170&dpr=0.8#rlfi=hd:;si:;mv:[[51.566008,0.12081130000000001],[51.457359999999994,-0.19341699999999998]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
    driver.get(url)
    time.sleep(3)
    
    titles = driver.find_elements(By.CLASS_NAME, "OSrXXb") # Shop Name
    ratings = driver.find_elements(By.CLASS_NAME, "yi40Hd YrbPuc") # Rating

    
    for i in range(len(titles)):
        bobaData.append(
            titles[i].text,
            ratings[i].text
        )
        
    driver.quit()
        
def main() -> None: 
    scrapeTeaShops()

if __name__ == '__main__': 
    main()
