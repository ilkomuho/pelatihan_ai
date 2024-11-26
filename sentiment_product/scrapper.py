from google_play_scraper import app, reviews_all, reviews, Sort

scrapped_data = reviews_all(
    'com.tokopedia.tkpd',
    sleep_milliseconds=0,
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=10
)

import csv
with open('scrapped_data.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["review", "rating"])
    for review in scrapped_data:
        writer.writerow([review['content'], review['score']])
print("Data berhasil disimpan dalam file CSV.")