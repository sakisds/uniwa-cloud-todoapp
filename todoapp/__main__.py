'''
Entrypoint for todo app
'''

from argparse import ArgumentParser

from todoapp import serve, db


# Check CMD arguments
argparser = ArgumentParser()
argparser.add_argument("command", choices=['init-db', 'serve'])
args = argparser.parse_args()

command = args.command

if command == 'serve':
    print('Starting web server!')
    serve()
elif command == 'init-db':
    print('Initializing database')
    db.create_all()
