import csv

class csv_io:
    def __init__(self, path):
        self.path = path
        self.data = None
        """
        data[][] (str): csvファイルデータ
            [0][0] = "00"
            [0][1] = "01"
            [0][2] = "02"
            [1][0] = "10"
            [1][1] = "11"
            [1][2] = "12"
            [2][0] = "csv file"
            [2][1] = "end"
            [2][2] = "!!"
        """
    
    def open_file(self):
        """
        csvファイルを開く関数
        引数で指定されたパスのcsvファイル

        Args:
            path (str): ファイルパス
        """
        try:
            with open(self.path) as f:
                tmp = csv.reader(f)
                self.data = [row for row in tmp]
        except FileNotFoundError as err:
            print(err)
    
    def print_file(self):
        print(self.data)
    
    def get_file(self):
        return self.data
