import text_io
import csv_io

if __name__ == "__main__":
    ### text_io sample
    text = text_io.text_io("input\sample.txt")
    text.open_file()
    # ['Hello World!!\n', 'This is text file!!\n', 'End of file!!\n']
    text.print_data()
    tmp = text.get_data()
    tmp.append("Add data!!\n")
    text.write_data("output\sample.txt", tmp)

    ### csv_io sample
    csv = csv_io.csv_io("input\sample.csv")
    csv.open_file()
    # [['00', ' 01', ' 02'], ['10', ' 11', ' 12'], ['csvfile', ' end', ' !!!']]
    csv.print_data()
    tmp = csv.get_data()
    tmp.append(['add element1', 'add element2'])
    csv.write_data("output\sample.csv", tmp)
