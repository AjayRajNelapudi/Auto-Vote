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

voters_file = open('/Users/ajayraj/Documents/SpyryCertificates/sheet1.csv', 'r')
voter_records = list(csv.reader(voters_file))
voters_file.close()

with open('FailLog.txt', 'w') as fail_log:
    vote_caster = voter.Voter()
    for voter_record in voter_records:
        email = make_email(voter_record[1])
        name = capitalize(voter_record[0])
        try:
            vote_caster.vote(email, name)
            vote_caster.submit()

            time.sleep(3)
        except:
            print(email, name, 'vote not casted')
            fail_log.write(name + '\n')
