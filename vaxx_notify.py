import requests
import json
import time
from twython import Twython


def tweet_message(covid_center_url, cnt):
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    user = "put_user_here"
    tweet = f"@{user} {cnt} found slot at URL : {covid_center_url}"
    api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

    api.update_status(status=tweet)

def main():
    """main."""
    # sample URLs find them by yourself:
    covid_centers = [
        "https://www.doctolib.fr/centre-de-sante/paris/vaccinodrome-covid-19-porte-de-versailles?pid=practice-185273",
        "https://www.doctolib.fr/centre-de-sante/paris/centre-de-vaccination-paris-14e?pid=practice-164733",
    ]

    # sample URLs find them by yourself:
    urls = [
        "https://www.doctolib.fr/availabilities.json?start_date=2021-05-12&visit_motive_ids=2823401&agenda_ids=473228-473231-473227-467191-467179-467178-467162-467152-467164-467155-467153-467186-473230-473226-473223-467151-467154-467177-467189-467190-467150-467167-473225-467166-467174-467165-473232-467163-467175-467176-467188-467187&insurance_sector=public&practice_ids=185273&destroy_temporary=true&limit=4",
        "https://www.doctolib.fr/availabilities.json?start_date=2021-05-12&visit_motive_ids=2548939&agenda_ids=412039-466679-466676-466677-410948-466673-412036-466675&insurance_sector=public&practice_ids=164733&destroy_temporary=true&limit=4",
    ]
    i = 0
    while True:
        cnt = 0
        for url in urls:
            print(f"{cnt} : {url}")
            response = requests.get(url)
            json_out = response.json()
            if json_out['total'] != 0 and json_out['availabilities'] is not None:
                if json_out['availabilities'][0]['slots'] is not None:
                    print(f"found slots for {covid_centers[cnt]}")
                    print(json_out['availabilities'][0]['slots'])
                    tweet_message(covid_centers[cnt], i)

            cnt += 1
        i+=1
        time.sleep(12)


if __name__ == '__main__':
    main()
