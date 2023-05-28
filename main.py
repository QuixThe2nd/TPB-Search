from requests import get
from bs4 import BeautifulSoup

while True:
    if input('Search (s) or Trending (t) ').lower() == 't':
        trending_movies = get('https://www.imdb.com/chart/moviemeter/').text

        soup = BeautifulSoup(trending_movies, 'html5lib')
        movies = soup.select('tbody.lister-list > tr')
        for movie in movies:
            movie_soup = BeautifulSoup(str(movie), 'html5lib')
            info = movie_soup.select('a')[0]
            id = info['href'].split('/')[2]
            title = info.select('img')[0]['alt']
            response = get(f'https://apibay.org/q.php?q={id}').json()[0]
            if response['name'] != 'No results returned':
                print(title, f'https://itorrents.org/torrent/{response["info_hash"]}.torrent')
    else:
        name = input('Search: ')
        response = get(f'https://apibay.org/q.php?q={name}').json()
        if len(response) == 0:
            print('No results returned')
        else:
            for torrent in response:
                if torrent['name'] != 'No results returned':
                    print(torrent['name'], f'https://itorrents.org/torrent/{torrent["info_hash"]}.torrent')
