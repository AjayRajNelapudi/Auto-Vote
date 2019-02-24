import csv
import voter
import time

def make_email(username):
    if '@anits.edu.in' in username:
        return username
    return username + '@gmail.com'

def capitalize(name):
    name_parts = name.split()
    name_parts = [part.capitalize() for part in name_parts]
    return ' '.join(name_parts)

def sleep_time():
    time_slots = [3, 7, 12, 6, 2]
    i = 0
    while True:
        yield time_slots[i] * 60
        i = (i + 1) % len(time_slots)

def get_mr_ms_cursors():
    mr_cursors = ['Ganesh Patnaik', 'Aditya Adida', 'Aditya Adida', 'Ram Sudeep', 'Aditya Adida', 'Prema Durga Srvan Sai', 'Aditya Adida']
    ms_cursors = ['Meghana Janapareddy', 'Sravani Gembali', 'Meghana Janapareddy', 'Meghana Janapareddy', 'Prakhya Dasari', 'Meghana Janapareddy', 'Sravani Gembali']

    i = 0
    while True:
        yield (mr_cursors[i], ms_cursors[i])
        i = (i + 1) % len(mr_cursors)

voters_file = open('sheet1.csv', 'r')
voter_records = list(csv.reader(voters_file))
voters_file.close()

slot = sleep_time()
mr_ms_cursors = get_mr_ms_cursors()

points = {'Ram Sudeep': 0, 'Aditya Adida': 0, 'Prema Durga Srvan Sai': 0, 'Ganesh Patnaik': 0,
          'Meghana Janapareddy': 0, 'Sravani Gembali': 0, 'Prakhya Dasari': 0}

with open('FailLog.txt', 'w') as fail_log:
    vote_caster = voter.Voter()
    for voter_record in voter_records:
        email = make_email(voter_record[1])
        name = capitalize(voter_record[0])
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
