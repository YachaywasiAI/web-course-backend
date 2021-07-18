import datetime

def sort_people_by_age():
    today = datetime.datetime.now().date()
    persons = []
    for i in range(int(input('Insert number of persons: '))):
        print(f'Person {i + 1}')
        persons.append(
            {
                'name': input('Name: '),
                'dni': input('DNI: '),
                'birth': datetime.date(
                    *(int(x) for x in input('Date of birth yyyy-mm-dd: ').split('-'))
                )
            }
        )
        persons[-1]['_days'] = (today - persons[-1]['birth']).days
        print('======================')
    sorted_persons = sorted(persons, key=lambda person: person['_days'], reverse=False)

    print("Sorted list: ")
    for i, person in enumerate(sorted_persons):
        print(f"{person['name']}")

sort_people_by_age()
