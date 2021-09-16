from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
# Create your views here.

def scrap(request):
    url = "https://gktcs.in/blogs"
    responce = requests.get(url)
    htmlcontent = responce.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    # content = soup.find_all(id='login-btn')
    titles = []
    details = []
    images = []
    

    for content in soup.find_all('div', attrs={'class':'card-block'}):
        title = content.find('a')
        print(title)
        titles.append(title)
        
        context = {
            "content":titles
        }
    return render(request,'scrap_app/scrap.html',context)

def newfile(request):
    return render(request,'scrap_app/newfile.html')