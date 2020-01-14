def write_complain(office):
    with open(office, 'w') as office_name:
        complaint = input('What is your complaint? ')
        office_name.write(str(complaint))
        print('Your complaint is accepted.\n')
    with open( office) as office_name:
        n = office_name.read()
        print(n)

greeting = input('')
if greeting.lower() == 'hello':
    print('Please choose Google office: \ngoogle_kazakstan.txt')
    print('google_paris.txt')
    print('google_uar.txt')
    print('google_kyrgyzstan.txt')
    print('google_san_francisco.txt')
    print('google_germany.txt')
    print('google_moscow.txt')
    print('google_sweden.txt')
    google = input('')
    write_complain(google)
else: 
    print('Sorry, say "hello" first.')