class MergeOptions:
    def __init__(self, width_val, space_val, format_val):
        self.width_val = width_val
        self.space_val = space_val
        self.format_val = format_val


class GUIElements:
    def __init__(self, listbox_file, txt_dest_path, progress_bar, p_var):
        self.listbox_file = listbox_file
        self.txt_dest_path = txt_dest_path
        self.progress_bar = progress_bar
        self.p_var = p_var  # 프로그레스 바 값을 관리할 변수