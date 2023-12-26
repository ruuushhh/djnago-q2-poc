from time import sleep

def import_data():
    try:
        print('Importing data...')
        sleep(2)
        print('Import complete!')
    except Exception as e:
        print('Error importing data: {}'.format(e))