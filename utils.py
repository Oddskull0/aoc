def strip_line(s):
    return s.strip()

def read_file_as_string_list(file_path):
    fp = open(file_path)
    return list(map(strip_line, fp.readlines()))