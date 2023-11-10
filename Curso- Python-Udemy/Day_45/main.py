from bs4 import BeautifulSoup

# import lxml # in case of html parsing doesnt work properly
# with open ("Day_45\website.html", encoding="utf8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title) #Will print the title of the document
# print(soup.title.string) #Will print the string inside the title
# print(soup.prettify()) #Will print the html structure prettified
# print(soup.a) #Will print the fisrt "a" tag of the document

# all_anccor_tags = soup.find_all(name="a")
# print(all_anccor_tags)

# for tag in all_anccor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    # pass

# heading = soup.find(name="h1", id="name")
# print(heading.getText())

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

#css selectors
# company_url = soup.select_one(selector="p a") 
# print(company_url.get("href"))
