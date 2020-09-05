with open('./users', 'r') as f:
    emails = []
    for line in f:
        emails.append(line.split('|')[3])
        

write_file = open('./emails', 'w')
write_file.writelines(emails)