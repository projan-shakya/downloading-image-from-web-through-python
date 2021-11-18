import requests
import os

url='https://www.facebook.com/images/fb_icon_325x325.png'
r = requests.get(url) #get method

print(r.headers['Content-Type'])

path=os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(r.content)
