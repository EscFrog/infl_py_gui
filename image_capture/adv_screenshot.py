import time
import keyboard
from PIL import ImageGrab

def screenshot():
  curr_time = time.strftime("_%Y%m%d_%H%M%S")
  img = ImageGrab.grab()
  img.save(f"image{curr_time}.png")

keyboard.add_hotkey("F9", screenshot) # F9 키를 핫키로 등록

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행