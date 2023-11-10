import requests
from bs4 import BeautifulSoup

#------------------------------------------------------------------------------------------------

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
webpage = response.text

#------------------------------------------------------------------------------------------------
soup = BeautifulSoup(webpage, "html.parser")
movies_list_number = [movie_title.getText().split(")")[0] for movie_title in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")]
movies_list_number.reverse()
movies_list = [movie_title.getText().split(")")[1] for movie_title in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")]
movies_list.reverse()
# print(movies_list_number)
# print(movies_list)

with open("Day_45\movies_list.txt", "w", encoding="utf-8") as file:
    for i in range(len(movies_list_number)):
        file.write(f"{movies_list_number[i]}) {movies_list[i]}\n")