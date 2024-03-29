import os
from tkinter import filedialog, END, messagebox
from PIL import Image

# 파일 추가
def add_file(listbox_file):
  files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), initialdir="/Users/*/Pictures")

  # 사용자가 선택한 파일 목록
  for file in files:
    listbox_file.insert(END, file)


# 선택 삭제
def del_file(listbox_file):
  for index in reversed(listbox_file.curselection()):
    listbox_file.delete(index)


# 저장 경로 (폴더)
def browse_dest_path(txt_dest_path):
  folder_selected = filedialog.askdirectory(initialdir="/Users/*/Pictures")
  if folder_selected is None:
    return
  # print(folder_selected)
  txt_dest_path.delete(0, END)
  txt_dest_path.insert(0, folder_selected)


def merge_image(file_list, dest_path):
  images = [Image.open(x) for x in file_list]

  widths = [x.size[0] for x in images]
  heights = [x.size[1] for x in images]

  # 최대 넓이, 전체 높이 구해옴
  max_width, total_height = max(widths), sum(heights)

  # 스케치북 준비
  result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 배경 캔버스 생성
  y_offset = 0 # y 위치 조정을 위한 변수
  for img in images:
    result_img.paste(img, (0, y_offset))
    y_offset += img.size[1] # height 값 만큼 더해줌
  
  final_path = os.path.join(dest_path, "result.jpg")
  result_img.save(final_path)
  messagebox.showinfo("알림", "작업이 완료되었습니다.")


# 병합 시작
def start(cmb_width, cmb_space, cmb_format, listbox_file, txt_dest_path):
  # 각 옵션들 값을 확인
  print("가로넓이 : ", cmb_width.get())
  print("간격 : ", cmb_space.get())
  print("포맷 : ", cmb_format.get())

  # 파일 목록 확인
  if listbox_file.size() == 0:
    messagebox.showwarning("경고", "이미지 파일을 추가하세요")
    return
  file_list = listbox_file.get(0, END)
  
  # 저장 경로 확인
  dest_path = txt_dest_path.get()
  if len(dest_path) == 0:
    messagebox.showwarning("경고", "저장 경로를 선택하세요")
    return
  
  # 병합 함수 실행
  merge_image(file_list, dest_path)
