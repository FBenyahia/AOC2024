import os
import requests
from cookie import COOKIE
YEAR = 2024 
DIR4 = [(-1, 0), (0, 1), (1, 0), (0, -1)] #* URDL
DIR8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # Up then clockwise 


def get_input(day, year=YEAR):
    cache_file = f"inputs/day{day}.txt"
    if os.path.isfile(cache_file):
        print("Reading from cache file")
        return open(cache_file).read()
    print("Fetching from the web")
    req = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers={'cookie':'session='+COOKIE})
    if "Please don't repeatedly request" in req.text:
        print("Error: Problem, not open yet.")
        return None
    with open(cache_file, 'w') as f:
        f.write(req.text)
    return req.text

def get_example(year, day, offset=0):
    req = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers={'cookie':'session='+COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0].replace('<em>', '').replace('</em>', '')

def submit(day, answer, level=1, skip_confirm=False):
    if not skip_confirm:
        input(f'You are about to submit the follwing answer:\n>>>>>>>>>>>>>>>>> {answer}\nPress enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer', headers={'cookie':'session='+AOC_COOKIE}, data=data)
    if 'You gave an answer too recently' in response.text:
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        print('VERDICT : INVALID LEVEL')
        if level == 1:
            print('Retrying on level 2')
            submit(day, answer, 2, skip_confirm=True)
        else:
            print('Retrying on next day')
            submit(day + 1, answer, 1, skip_confirm=True)
    else:
        print('VERDICT : OK !')
