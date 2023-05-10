def q2(url: str) -> str:
    domen = '.'.join(url.split('/')[2].split('.')[:-1])
    return domen


print(q2('https://leetcode.com/problems/plus-one/'))
print(q2('http://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2'))
