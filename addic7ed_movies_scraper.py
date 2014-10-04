import re
import sys
from urllib2 import urlopen
import argparse

class ADDIC7ED_PAGES:
    DOMAIN      = 'http://www.addic7ed.com'
    SEARCH      = '/search.php?search=%s&Submit=Search'

class ADDIC7ED_REGEX:
    SEARCH_RESULTS_PARSER = ('(?<=\<a href\=\")(?P<MovieCode>.*?)(?:\"\>)' + 
                             '(?P<MovieName>.*?)(?=\<\/a\>)')
    RESULT_PAGE_PARSER    = ('(?<=Version )(?P<VerSum>.*?)(?:, .*?javascript\:' +
                             'saveFavorite\(\d+,)(?P<Language>\d+)(?:,\d+\).*?' +
                             '<a class=\"buttonDownload\" href=\")(?P<VerCode>' +
                             '.*?)(?=\">)')

def yield_versions():
    root_page = urlopen(ADDIC7ED_PAGES.DOMAIN + "/movie-subtitles")\
        .read().replace("\r", "").replace("\n", "")
    movies = re.findall(ADDIC7ED_REGEX.SEARCH_RESULTS_PARSER, root_page)
    movies = filter(lambda m: m[0].startswith("movie"), movies)
    for movie_code, movie_name in movies:
        movie_page = urlopen(ADDIC7ED_PAGES.DOMAIN + "/" + movie_code)\
            .read().replace("\r", "").replace("\n", "")
        versions = re.findall(ADDIC7ED_REGEX.RESULT_PAGE_PARSER, movie_page)
        for version_string, language, version_code in versions:
            yield movie_name, movie_code, language, version_string, version_code

def perform_main_logic():
    for version in yield_versions():
        write_output_line(','.join(version))

_output_handle = None
def write_output_line(line):
    _output_handle.write("%s\n" % str(line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract movie information from www.Addic7ed.com.')
    parser.add_argument(
        type=str, default=None, dest='output_path', nargs='?',
        help='The output path (Leave empty for console)')
    args = parser.parse_args()

    global _output_handle
    if args.output_path:
        _output_handle = open(args.output_path, "w")
    else:
        _output_handle = sys.stdout

    print "Starting: %s" % _output_handle
    try:
        perform_main_logic()
    finally:
        if _output_handle != sys.stdout:
            _output_handle.close()
    print "Finished."