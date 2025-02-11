import text_io

if __name__ == "__main__":
    ### text_io sample
    text = text_io.text_io("input\sample.txt")
    text.open_file()
    # ['Hello World!!\n', 'This is text file!!\n', 'End of file!!\n']
    text.print_file()
