from bs4 import BeautifulSoup

file = open("index.html", "r")
lines = file.read(-1)
soup = BeautifulSoup(lines, features="html.parser")
print(soup.find_all("p"))

file.close()
