class text_io:
    def __init__(self, path):
        self.path = path
        self.data = None
        """
        data[] (str): テキストファイルデータ
            [0] = "Hello World!!\n"
            [1] = "This is text file!!\n"
            [2] = "End of file!!\n"
        """
    
    def open_file(self):
        """
        テキストファイルを開く関数
        引数で指定されたパスのテキストファイル

        Args:
            path (str): ファイルパス
        """
        try:
            with open(self.path) as f:
                self.data = f.readlines()
        except FileNotFoundError as err:
            print(err)
    
    def print_file(self):
        print(self.data)
    
    def get_file(self):
        return self.data
