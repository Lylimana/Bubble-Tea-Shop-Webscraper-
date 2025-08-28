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
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    
    # Service object
    service = Service(ChromeDriverManager().install())
    

    # initialise driver
    driver = webdriver.Chrome(service=service, options=options)
    url = f"https://www.google.com/search?sca_esv=465159d7bf2b0b64&tbm=lcl&sxsrf=AE3TifNap3yiVLX0363JcDFmzLil_tN2wg:1756406355848&q=bubble+tea+shops+london&rflfq=1&num=10&sa=X&ved=2ahUKEwijua_Hk66PAxWOXEEAHVpCPFYQjGp6BAgpEAE&biw=1197&bih=1170&dpr=0.8"
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
