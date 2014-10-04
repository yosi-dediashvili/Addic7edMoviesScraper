# Addic7ed movie subtitles scraper

Extracts information about all the movie subtitles that www.Addic7ed.com stores.

## Usage

```
python addic7ed_movies_scraper.py <output_path>
```

The output is a `CSV` list where each line describes a version of a movie.

Each line contains the following data:

* Movie name
* Movie code in Addic7ed's databases
* Version string
* Language code
* Version code in Addic7ed databases

## Example output

```
3 Days To Kill  (2014),movie/86374,1,Unspecific,/original/86374/3
300: Rise of an Empire (2014),movie/86024,1,Webdl,/original/86024/0
300: Rise of an Empire (2014),movie/86024,1,Unspecific-HDR,/original/86024/2
300: Rise of an Empire (2014),movie/86024,8,Unspecific-HDR,/original/86024/3
300: Rise of an Empire (2014),movie/86024,10,WEBRIP,/original/86024/1
36 Hours (1965),movie/88834,1,Unspecific-DVD,/original/88834/0
36 Hours (1965),movie/88834,8,Unspecific-DVD,/original/88834/1
47 Ronin (2013),movie/84593,38,AQUOS,/original/84593/3
47 Ronin (2013),movie/84593,1,720p.BluRay.YIFY,/original/84593/2
```