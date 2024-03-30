import os
from tkinter import filedialog, END, messagebox
from PIL import Image
from options import MergeOptions

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

  if folder_selected == "":
    return

  txt_dest_path.delete(0, END)
  txt_dest_path.insert(0, folder_selected)


# 이미지 통합
def merge_image(options, file_list, dest_path, gui_elements):
  try:
    # 가로넓이
    img_width = options.width_val
    if img_width == "원본유지":
      img_width = -1 # -1 일때는 원본 기준으로
    else:
      img_width = int(img_width)

    # 간격
    img_space = options.space_val
    if img_space == "좁게":
      img_space = 30
    elif img_space == "보통":
      img_space = 60
    elif img_space == "넓게":
      img_space = 90
    else: # 없음
      img_space = 0
    
    # 포맷
    img_format = options.format_val.lower() # 소문자로 변경

    images = [Image.open(x) for x in file_list]
    
    # 이미지 사이즈를 리스트에 넣어서 하나씩 처리
    image_sizes = []
    if img_width > -1:
      image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
    else: # 원본 사이즈 사용
      image_sizes = [(x.size[0], x.size[1]) for x in images]

    # 각 이미지의 넓이와 높이를 각각 리스트에 담는다.
    widths, heights = zip(*(image_sizes)) # unzip 사용

    # 최대 넓이, 전체 높이 구해옴
    max_width, total_height = max(widths), sum(heights)

    # 스케치북 준비
    if img_space > 0: # 이미지 간격 옵션 적용
      total_height += (img_space * (len(images) - 1))

    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 배경 캔버스 생성

    y_offset = 0 # y 위치 조정을 위한 변수
    for idx, img in enumerate(images):
      # width 가 원본 유지가 아닐 경우에는 이미지 크기 조정
      if img_width > -1:
        img = img.resize(image_sizes[idx])

      result_img.paste(img, (0, y_offset))
      y_offset += (img.size[1] + img_space) # height 값 + 사용자가 지정한 간격

      progress = (idx + 1) / len(images) * 100  # 실제 percent 정보를 계산
      gui_elements.p_var.set(progress)  # p_var를 통해 프로그레스 바 업데이트
      gui_elements.progress_bar.update()  # UI 업데이트
    
    file_name = "result." + img_format
    final_path = os.path.join(dest_path, file_name)
    result_img.save(final_path)
    messagebox.showinfo("알림", "작업이 완료되었습니다.")
  except Exception as err: # 예외처리
    messagebox.showerror("에러", err)


# 병합 시작
def start(width_val, space_val, format_val, gui_elements):
  # 옵션 인스턴스 생성
  options = MergeOptions(width_val, space_val, format_val)

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
  merge_image(options, file_list, dest_path, gui_elements)
