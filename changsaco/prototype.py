"""
한글타자연습을 파이썬으로 구현해보았다.
전공과 연계는 컴퓨터개론의 단어를 이용하였다.
"""

from random import *
import time
import os

def intro(name):
    print("\n안녕하세요, {0}님. 메인화면입니다.".format(name))
    choice = int(input("타자연습 시작       (1)\n단어 추가하기      (2)\n단어 목록보기      (3)\n단어장 지우기      (4)\n단어장 파일 지우기     (5)중 하나를 선택하세요 : "))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
        print("\n{0}를(을) 선택하셨습니다.".format(choice))
        print("잠시 후 실행됩니다...")
    else:
        print("\n잘못 선택하셨습니다. 처음으로 돌아갑니다...")
    return choice

def gamestart():
    sum = 0
    count = 0
    fs_count = time.time()
    with open("wordlist.txt", "rt") as f:    
        list1 = f.readlines()
        list2 = []
    while(True):
        for i in list1:
            list2.append(i[:-1])  
        shuffle(list2)
        s_count = time.time()
        x = input(list2[0]+"\n")
        if (x == list2[0]):
            e_count = time.time()
            div = e_count - s_count
            print("맞췄습니다!\n")
            count = count + 1
            result = (len(list2[0])/div) * 60
            sum += result
            continue
        else:
            print("틀렸습니다!\n")
        total_count = time.time()
        took = total_count - fs_count
        print("총 시간 : %.2f, 평균 타수 : %.2f" % (took, sum / count))
        break

def addword(add):
    if (add == 'quit'):
        print("추가를 종료합니다...\n")
    else:
        wordlist.append(add)
        print("'{0}' 추가 완료".format(add))

def print_list():
    total_leng = len(wordlist)
    print("\n")
    for i in range(total_leng):
        print("{0}".format(wordlist[i]))
        
def remove_file():
    if os.path.exists("wordlist.txt"):
        os.remove("wordlist.txt")
        print("파일 삭제 완료")
    else:
        print("이미 삭제 되어있습니다.")

name = input("이름을 입력하세요 : ")
wordlist = ['안녕', '하세요', '반갑', '습니다']

print("\n사용방법\n- 숫자를 선택해 하고자 하는 작업을 실행시킬 수 있다.\n- 4번을 선택해 파일의 내용을 지우고, 3번을 통해 추가하고 싶은 단어를 추가할 수 있다.")
print("- 타수는 다른 타자시스템과 기준이 맞지 않을 수도 있다는 점 유의해주세요.")
time.sleep(1)

while (True):
    with open("wordlist.txt", 'w') as f:
        leng = len(wordlist)
        for i in range(0, leng, 1):
            f.write("{0}\n".format(wordlist[i]))
    choice = intro(name)
    
    
    if choice == 1:
        # 게임 실행
        gamestart()

    elif choice == 2:
        # 단어 추가하기
        n = input("추가 할 단어 : ")
        addword(n)

    elif choice == 3:
        # 단어장 목록보기
        print_list()

    elif choice == 4:
        # 단어 전부 삭제하기
        wordlist.clear()
        print("단어 전부 삭제 완료!")

    elif choice == 5:
        remove_file()
    
    else:
        # 암것도 없음
        continue
