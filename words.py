
import numpy as np
import requests

url = "https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt"

response = requests.get(url)



if response.status_code == 200:
    text = response.text
    arr = text.split()
    words = np.array([w for w in arr if len(w) >= 3])

else:
    print("Couldn't read")  

# with open('words.txt', 'r') as file:
#     words_list = file.read().splitlines()
    
# words = np.array(words_list)