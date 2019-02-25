import csv
import voter
import time
import random


def make_nfe(email):
    name, domain = email.split('@')

    if '.' in name:
        name = name.split('.')
    elif '_' in name:
        name = name.split('_')

    capitalized_name = [part.capitalize() for part in name]
    return ' '.join(capitalized_name)

def make_email(username):
    if '@anits.edu.in' in username:
        return username
    if '@' in username and username.index('@') != len(username) - 1:
        return username
    return username + '@gmail.com'

def make_name(name):
    name_parts = name.split()
    name_parts = [part.capitalize() for part in name_parts]
    new_name = ' '.join(name_parts)
    return new_name

def sleep_time():
    time_slot = random.uniform(0.3, 1.34)
    while True:
        yield time_slot * 60

def get_mr_ms_cursors():
    mr_cursors = ['Ganesh Patnaik', 'Aditya Adida', 'Aditya Adida', 'Ram Sudeep', 'Aditya Adida', 'Prema Durga Srvan Sai', 'Ram Nitin', 'Aditya Adida', 'Ram Nitin']
    ms_cursors = ['Meghana Janapareddy', 'Sravani Gembali', 'Meghana Janapareddy', 'Meghana Janapareddy', 'Prakhya Dasari', 'Meghana Janapareddy', 'Sravani Gembali']

    i = 0
    while True:
        yield (mr_cursors[i], 'Meghana Janapareddy')
        i = (i + 1) % len(mr_cursors)

voters_file = open('nz.csv', 'r')
voter_records = list(csv.reader(voters_file))
voters_file.close()

slot = sleep_time()
mr_ms_cursors = get_mr_ms_cursors()

points = {'Ram Sudeep': 0, 'Aditya Adida': 0, 'Prema Durga Srvan Sai': 0, 'Ganesh Patnaik': 0, 'Ram Nitin': 0,
          'Meghana Janapareddy': 0, 'Sravani Gembali': 0, 'Prakhya Dasari': 0}

with open('FailLog.txt', 'w') as fail_log:
    vote_caster = voter.Voter()
    for voter_record in voter_records:
        email = make_email(voter_record[1])
        name = make_name(voter_record[0])
        mr_cursors, ms_cursors = next(mr_ms_cursors)
        try:
            vote_caster.vote(email, name, mr_cursors, ms_cursors)
            vote_caster.submit()

            points[mr_cursors] += 1
            points[ms_cursors] += 1
            print(name, points)

            delay = next(slot)
            time.sleep(delay)
        except:
            print(name, 'vote not casted')
            fail_log.write(name + '\n')
