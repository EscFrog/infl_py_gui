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


# 저장 경로 선택(폴더)
def browse_dest_path(txt_dest_path):
  folder_selected = filedialog.askdirectory(initialdir="/Users/*/Pictures")

  if folder_selected is None:
    return

  txt_dest_path.delete(0, END)
  txt_dest_path.insert(0, folder_selected)


def merge_image(file_list, dest_path, gui_elements):
  images = [Image.open(x) for x in file_list]

  widths = [x.size[0] for x in images]
  heights = [x.size[1] for x in images]

  # 최대 넓이, 전체 높이 구해옴
  max_width, total_height = max(widths), sum(heights)

  # 스케치북 준비
  result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 배경 캔버스 생성

  y_offset = 0 # y 위치 조정을 위한 변수
  for idx, img in enumerate(images):
    result_img.paste(img, (0, y_offset))
    y_offset += img.size[1] # height 값 만큼 더해줌

    progress = (idx + 1) / len(images) * 100  # 실제 percent 정보를 계산
    gui_elements.p_var.set(progress)  # p_var를 통해 프로그레스 바 업데이트
    gui_elements.progress_bar.update()  # UI 업데이트
  
  final_path = os.path.join(dest_path, "result.jpg")
  result_img.save(final_path)
  messagebox.showinfo("알림", "작업이 완료되었습니다.")


# 병합 시작
def start(options, gui_elements):
  # 인자로 받은 클래스 인스턴스에서 데이터에 접근
  print("가로넓이: ", options.width)
  print("간격: ", options.space)
  print("포맷: ", options.format)

  # 파일 목록과 저장 경로 접근
  if gui_elements.listbox_file.size() == 0:
    messagebox.showwarning("경고", "이미지 파일을 추가하세요")
    return
  file_list = gui_elements.listbox_file.get(0, END)

  # 저장 경로 확인
  dest_path = gui_elements.txt_dest_path.get()
  if len(dest_path) == 0:
    messagebox.showwarning("경고", "저장 경로를 선택하세요")
    return
  
  # 병합 함수 실행
  merge_image(file_list, dest_path, gui_elements)
