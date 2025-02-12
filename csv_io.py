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
    
    def print_data(self):
        print(self.data)
    
    def get_data(self):
        return self.data

    def write_data(self, path, data):
        """
        csvファイルを出力する関数

        Args:
            path (str): ファイルパス
            data (str):
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
        with open(path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            writer.writerows(data)
