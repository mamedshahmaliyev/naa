import time, os, random
from datetime import datetime
from threading import Thread

imagesUrlList = [f'imageUrl{i}' for i in range(random.randint(10, 15))]
maxConcurrentThreadCount = 3

def downloadImage(imageUrl):
    print(f'Downloading image from {imageUrl}')
    time.sleep(random.randint(1, 3))
    print(f'Download completd: {imageUrl}')
    
activeThreadList = []
for imageUrl in imagesUrlList:
    
    while len(activeThreadList) >= maxConcurrentThreadCount:
        print('Number of active threads = ', len(activeThreadList))
        activeThreadList = [t for t in activeThreadList if t.is_alive()]
        time.sleep(0.5)
    
    print(f'Creating new thread for image {imageUrl}. Active number of threads is: {len(activeThreadList)}')
    activeThreadList.append(Thread(target=downloadImage, args=(imageUrl,)))
    activeThreadList[-1].start()
    








