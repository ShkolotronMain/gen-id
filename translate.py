def translate(inp: str) -> str:
    inp = inp.lower()
    word = list(inp)
    word2 = []
    word[0].lower()
    for i,j in enumerate(word):
        word2.append(analog(j))
    word2[0].capitalize()
    return ''.join(word2)

def analog(char: str) -> str:
    match char:
        case 'а':
            return 'a'
        case 'б':
            return 'b'
        case 'в':
            return 'v'
        case 'г':
            return 'g'
        case 'д':
            return 'd'
        case 'е':
            return 'e'
        case 'ё':
            return 'e'
        case 'ж':
            return 'zh'
        case 'з':
            return 'z'
        case 'и':
            return 'i'
        case 'й':
            return 'i'
        case 'к':
            return 'k'
        case 'л':
            return 'l'
        case 'м':
            return 'm'
        case 'н':
            return 'n'
        case 'о':
            return 'o'
        case 'п':
            return 'p'
        case 'р':
            return 'r'
        case 'с':
            return 's'
        case 'т':
            return 't'
        case 'у':
            return 'u'
        case 'ф':
            return 'f'
        case 'х':
            return 'kh'
        case 'ц':
            return 'ts'
        case 'ч':
            return 'ch'
        case 'ш':
            return 'sh'
        case 'щ':
            return 'shch'
        case 'ъ':
            return 'ie'
        case 'ы':
            return 'y'
        case 'ь':
            return ''
        case 'э':
            return 'e'
        case 'ю':
            return 'iu'
        case 'я':
            return 'ia'
        case ' ':
            return ' '
        case '-':
            return '-'
        case _:
            return ''
