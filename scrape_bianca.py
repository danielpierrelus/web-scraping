import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def web_scraping_bianca_home(event, context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  
    chrome_options.add_argument('--no-sandbox')  
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get('https://bianca.com')
        
        # Extrair o conteúdo HTML da página
        html_content = driver.page_source
        
        # Analisar o conteúdo HTML com BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extrair o título da página
        title = soup.find('title').get_text()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'title': title,

            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
    finally:
        driver.quit()
import json
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#app = Flask(_name_)
app = Flask(__name__)


@app.route('/scrape-bianca-home', methods=['GET'])
def scrape_bianca_home():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')  
        chrome_options.add_argument('--no-sandbox')  

        
        driver = webdriver.Chrome(options=chrome_options)
        
        driver.get('https://bianca.com')
        
        html_content = driver.page_source
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extrair o título da página
        title = soup.find('title').get_text()
        
        driver.quit()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'title': title,
                
            })
        }
    except Exception as e:
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }


    
if __name__ == '__main__':
    app.run(debug=True)

 