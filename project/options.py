class MergeOptions:
    def __init__(self, width, space, format):
        self.width = width
        self.space = space
        self.format = format


class GUIElements:
    def __init__(self, listbox_file, txt_dest_path, progress_bar, p_var):
        self.listbox_file = listbox_file
        self.txt_dest_path = txt_dest_path
        self.progress_bar = progress_bar
        self.p_var = p_var  # 프로그레스 바 값을 관리할 변수