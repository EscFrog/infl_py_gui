import time
from PIL import ImageGrab

time.sleep(5) # 5초 대기

for i in range(1, 6): # 2초 간격으로 5개 이미지 저장
  img = ImageGrab.grab()
  img.save(f"img{i}.png") # 파일로 저장
  time.sleep(2)