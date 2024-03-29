from tkinter import filedialog, END

# 파일 추가
def add_file(listbox_file):
  files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), initialdir="/Users/*/Pictures")

  # 사용자가 선택한 파일 목록
  for file in files:
    listbox_file.insert(END, file)

# 선택 삭제
def del_file(listbox_file):
  print(listbox_file.curselection())

  for index in reversed(listbox_file.curselection()):
    listbox_file.delete(index)