import os
import pathlib
from bs4 import BeautifulSoup


def list_files(path):
  """List all files in a path, including the folder name."""
  files = []
  files =  os.listdir(path)
  return files

def read_file(path):
  return open(path, "r").read()

def get_cleaned_file(strhtml):
  soup = BeautifulSoup(strhtml, 'html.parser')
  text_content = soup.get_text()
  result = text_content.split('\n')
  result = [x for x in result if x != ''] 
  return "\n".join(result)


if __name__ == "__main__":
  path = "PATH_WHERE_HTML_FILES_ARE_STORED"
  write_path = "PATH_WHERE_CLEANED_FILES_NEED_TO_BE_WRITTEN"
  files = list_files(path)
  for file in files:
    print(path+file)
    strhtml = read_file(path+file)
    clean_text = get_cleaned_file(strhtml)
    fd = open(write_path+file+".txt", "w")
    fd.write(clean_text)
    fd.close()


