import requests
from bs4 import BeautifulSoup as BS
from common import datePars

def playbill(cinema):

    id_cinema = ""
    chiselko = ''

    pointer = cinema.count("1")

    if cinema == "goldmile":
        id_cinema = "3008946"
        chiselko = datePars.timer()
    if cinema == "bur":
        id_cinema = "8320137"
        chiselko = datePars.timer()
    if cinema == "rio":
        id_cinema = "8151399"
        chiselko = datePars.timer()
    if cinema == "sky":
        id_cinema = "8325625"
        chiselko = datePars.timer()
    if cinema == "indigo":
        id_cinema = "8157094"
        chiselko = datePars.timer()

    if cinema == "goldmile-1":
        id_cinema = "3008946"
        chiselko = str(datePars.add_day())
    if cinema == "bur-1":
        id_cinema = "8320137"
        chiselko = str(datePars.add_day())
    if cinema == "rio-1":
        id_cinema = "8151399"
        chiselko = str(datePars.add_day())
    if cinema == "sky-1":
        id_cinema = "8325625"
        chiselko = str(datePars.add_day())
    if cinema == "indigo-1":
        id_cinema = "8157094"
        chiselko = str(datePars.add_day())

    kino = ''
    arr = []

    r = requests.get(f"https://nn.kinoafisha.info/cinema/{id_cinema}/schedule/?date={chiselko}&order=movie")
    html = BS(r.content, 'html.parser')
    soup = BS(r.text, 'html.parser')
    print(chiselko)
    if r.status_code == 200:

        chislo = str(datePars.timer())[6:]
        Day_name = soup.findAll('span', class_='week_name')[0].text

        #print(soup.findAll('span', class_='week_num')[0].text, ' - ', int(str(datePars.add_day())[6:]), " - ", Day_name)

        # if Day_name == "Сегодня" and chislo == chiselko:
        #     Day_name = "Сегодня"
        #     chislo = chiselko
        # elif Day_name == "Завтра" or chislo != chiselko:
        #     chislo = str(datePars.add_day())[6:]
        #     Day_name = "Завтра"
        # if pointer == 0 and (soup.findAll('span', class_='week_num')[0].text == str(datePars.add_day())[6:]):
        #     return 'Кажется нет расписания...'

        if pointer == 0 and Day_name == "Завтра" and (datePars.timer()[6:] != soup.findAll('span', class_='week_num')[0].text):
            return 'Кажется нет расписания...'
        elif pointer == 0 and Day_name == "Сегодня" and (datePars.timer()[6:] == soup.findAll('span', class_='week_num')[0].text):
            Day_name = 'Сегодня'
            chislo = datePars.timer()[6:]
        else:
            Day_name = "Завтра"
            chislo = datePars.add_day()[6:]

        #print(soup.findAll('span', class_='week_num')[0].text, ' - ', int(str(datePars.add_day())[6:])," - " ,Day_name)


        items = html.select(".schedule_showtimes > .showtimes_item > .showtimes_cell > .showtimesMovie_wrapper")

        movie_showtimes = soup.find_all('div', class_='showtimes_item')

        time = []
        names = []
        for el in movie_showtimes:
            if el.find('span', class_='showtimesMovie_name') != None:
                movie_name = el.find('span', class_='showtimesMovie_name').text
                names.append(movie_name)
                showtimes = el.find_all('span', class_='session_time')
                time.append(showtimes[0].text)

        for el in items:
            title = el.select(".showtimesMovie_info > span")
            arr.append(title[0].text)
        for i in range(len(arr)):
            kino += str(i + 1) + ") " + "'" + arr[i] + "'" + ". " + f"{Day_name}, {chislo}-го числа. Ближайшее время {time[i]}." + "\n\n"
        if kino == '': kino = 'Кажется нет расписания...'

    else: kino = 'Error: Bad Request!'

    return kino