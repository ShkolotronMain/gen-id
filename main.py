#!/usr/bin/env python

from secrets import choice, randbelow
import time
import sys

from translate import translate

small_literas = 'abcdefghijklmnopqrstuvwxyz'
big_literas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '_^*#!@%;:'


def main():
    if len(sys.argv) == 1:
        print('<скрипт> <номер контейнера> [номер]')
    else:
        container = sys.argv[1]
        print(f'{container} - #undone\n')

        if len(sys.argv) == 3:
            print(sys.argv[2])
        else:
            print('==Phone==')

        print(gen_password(16))

        man = gen_person()
        print(man[0])
        print(man[1])

        birth = gen_date()
        print(birth)

        print(gen_email(man, birth, container))
        print(gen_address())


def gen_password(length=15) -> str:
    raw_pass = []
    running = True
    while running == True:
        for i in range(length):
            k = randbelow(80)
            if k < 21:
                raw_pass.append(choice(small_literas))
            elif k < 41 and k > 20:
                raw_pass.append(choice(numbers))
            elif k < 61 and k > 40:
                raw_pass.append(choice(symbols))
            else:
                raw_pass.append(choice(big_literas))

        checklist = []
        for i in raw_pass:
            if i in small_literas:
                checklist.append('sl')
            elif i in big_literas:
                checklist.append('bl')
            elif i in numbers:
                checklist.append('nu')
            else:
                checklist.append('sm')

        if len(set(checklist)) == 4:
            running = False

    return ''.join(raw_pass)


def gen_person() -> list[str]:
    name = ''
    surname = ''
    with open('male_names_rus.txt','r') as namelist:
        name = choice(namelist.readlines()).replace('\n', '')
    with open('male_surnames_rus.txt','r') as surnamelist:
        surname = choice(surnamelist.readlines()).replace('\n', '')
    person = [name, surname]
    return person

def gen_date() -> str:
    now = int(time.time())
    deltaday = randbelow(31)
    now += deltaday*86400
    deltayear = randbelow(12)+19
    now -= deltayear*31536000
    now_str=time.strptime(time.ctime(float(now)))
    return time.strftime('%d.%m.%Y',now_str)

def gen_address() -> str:
    base = 'Университетский проспект, 100А\n'
    home = randbelow(16*16)+15
    return base+str(home)

def gen_email(person: list[str], birthday: str, container: str) -> str:
    name = translate(person[0])
    surname = translate(person[1])
    birth = birthday[-2::]
    domen = "yandex.ru"

    with open('hobbies.txt', 'r') as file:
        hobby = choice(file.readlines())[:-1]

    k = randbelow(100)
    match (k % 10):
        case 0:
            return f'{surname}-{name}-{hobby}@{domen}'
        case 1:
            return f'{surname}-{name}-{birth}@{domen}'
        case 2:
            return f'{name}-{surname}-{hobby}@{domen}'
        case 3:
            return f'{birth}-{name}-{hobby}@{domen}'
        case 4:
            return f'{hobby}-{surname}-{birth}@{domen}'
        case 5:
            return f'{surname}-{hobby}-{birth}@{domen}'
        case 6:
            return f'{container}-{name}-{hobby}@{domen}'
        case 7:
            return f'{surname}-{container}-{birth}@{domen}'
        case 8:
            return f'{container}-{hobby}-{birth}@{domen}'
        case 9:
            return f'{name}-{surname}-{container}@{domen}'

if __name__ == '__main__':
    main()
