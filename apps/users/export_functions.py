from time import sleep

def export_data():
    try:
        print('Exporting data...')
        sleep(2)
        print('Export complete!')
    except Exception as e:
        print('Error exporting data: {}'.format(e))