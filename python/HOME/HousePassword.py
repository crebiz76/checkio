'''
스테판과 소피아는 보안에 대한 개념이 없어서 항상 간단한 비밀번호를 사용합니다. 
니콜라가 비밀번호의 보안수준을 체크하는 모듈을 만들 수 있게 도와주세요. 
비밀번호가 충분히 강력하다고 할 수 있으려면, 비밀번호의 길이는 10보다 크거나 같아햐 하고, 
1개 이상의 숫자, 1개 이상의 대문자, 1개 이상의 소문자를 포함하고 있어야 합니다. 
비밀번호는 ASCII 로마자만을 포합합니다.

입력: 비밀번호 문자열.

출력: 비밀번호가 안전한지 아닌지를 나타내는 진리값(boolean), 혹은 진리값으로 간주할 수 있는 아무 자료형.

예시:

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

쓰임새: 당신의 서비스나 앱의 보안이 걱정된다면, 사용자의 비밀번호가 충분히 복잡한지 체크해볼 수 있습니다. 
여기서 배운 스킬을 활용하면 더 많은 조건(구두점 혹은 유니코드)을 요구하는 모듈을 쉽게 만들 수 있을 것입니다.

전제조건:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
'''

def checkio(data: str) -> bool:

    #replace this for solution
    a = False
    b = False
    c = False
    d = False
    pw = ''
    
    if(len(data) >= 10):
        a = True
    for pw in data:
        if(pw.isdigit() == True):
            b = True
        if(pw.isupper() == True):
            c = True
        if(pw.islower() == True):
            d = True
    return (a & b & c & d)

#Some hints
#Just check all conditions

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")