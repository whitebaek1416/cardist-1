import random as r
import cArd1sT1_Battle as cb
from collections import defaultdict
# 카드 종류
animal_card_normal = ['고양이', '늑대', '아기 늑대', '다람쥐', '다람쥐 공', '담비', '두더지', '무스', '새끼 무스', '물총새', '민물 거북',
                      '민물 수달', '매', '블러드하운드', '비둘기', '살무사', '스컹크', '코요테', '큰까마귀', '향유고래', '황소개구리',
                      '회색곰']
animal_card_rare = ['두더지인간', '사마귀신', '우라율리', '우로보로스', '전기뱀장어']
machine_card_normal = ['감시 드론', '무효화 전도체', 'L33pB0t', '고GI봇', '버프 전도체', '에너지봇', '봄버봇', '49er', '자동 장치',
                       '곤충 드론', '공장 전도체', '두꺼운 드로이드', '피버봇', '더블 거너', '볼트하운드', '스팀봇']
machine_card_rare = ['목스 모듈', '에너지 전도체', '폭탄 부인', '곡선넘이', '사진충']
ghost_card_normal = ['해골', '뼈 굴착자', '드라우그르', '망령', '밴시', '뼈 마법사', '좀비', '부서진 은화(왼쪽)', '부서진 은화(오른쪽)',
                     '석관', '유령선', '익사한 영혼', '워커즈', '프랭크 & 스타인', '본하운드', '미라 제왕']
ghost_card_rare = ['뼈 무더기', '도굴꾼', '네크로맨서', '죽은 손', '파라오의 애완동물', '목 없는 기사']
magic_card_normal = ['루비 목스', '사파이어 목스', '에메랄드 목스', '견습 마법사', '붉은 마법사', '연습용 마법사', '루비 골렘', '마법 기사',
                     '파란 마법사', '보석 광인', '유영 마법사', '포스 마법사', '초록 마법사', '견습 현자', '근육 마법사', '자극 마법사',
                     '미식마법사']
magic_card_rare = ['블린의 목스', '고란즈의 목스', '오를루의 목스', '마스터 블린', '마스터 고란즈', '마스터 오를루']

# 플레이어의 진행 목록
deck = []
collection = defaultdict(int)
for i in animal_card_normal + animal_card_rare + machine_card_normal + machine_card_rare + ghost_card_normal + \
         ghost_card_rare + magic_card_normal + magic_card_rare:
    collection[i] = 0

hoil = 0


def select_cardpack(select_rare, select_normal, one_random, two_random, three_random):
    cardpack.append(f'{r.choice(select_rare)}')
    for i in range(2):
        cardpack.append(f'{r.choice(select_normal)}')
    for i in range(2):
        random_cards = r.randint(1, 3)
        if random_cards == 1:
            cardpack.append(f'{r.choice(one_random)}')
        elif random_cards == 2:
            cardpack.append(f'{r.choice(two_random)}')
        elif random_cards == 3:
            cardpack.append(f'{r.choice(three_random)}')


# 시작 덱 결정
while True:
    starter_card = []
    choose_deck = input('당신의 시작 덱을 선택하시오.(짐승, 기계, 망자, 마력)')
    # 각각 시작 덱을 확인 후 콜렉션에 카드 추가
    if choose_deck == '짐승':
        choose_animal_deck = input('너의 야망은 레쉬를 대체해 짐승의 필경자가 되는 것인가?(덱을 가진다, 내버려둔다)')
        if choose_animal_deck == '덱을 가진다':
            starter_card = ['다람쥐'] * 6 + ['담비'] * 5 + ['코요테'] * 5 + ['늑대'] * 4
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_animal_deck == '내버려둔다':
            pass
    elif choose_deck == '기계':
        choose_machine_deck = input('너의 야망은 P03을 대체해 기술의 필경자가 되는 것인가?(덱을 가진다, 내버려둔다)')
        if choose_machine_deck == '덱을 가진다':
            starter_card = ['L33pB0t'] * 5 + ['49er'] * 4 + ['자동 장치'] * 4 + ['두꺼운 드로이드'] * 4 + ['스팀봇'] * 3
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_machine_deck == '내버려둔다':
            pass
    elif choose_deck == '망자':
        choose_ghost_deck = input('너의 야망은 그리모라를 대체해 망자의 필경자가 되는 것인가?(덱을 가진다, 내버려둔다)')
        if choose_ghost_deck == '덱을 가진다':
            starter_card = ['해골'] * 5 + ['뼈 채굴자'] * 4 + ['드라우그르'] * 4 + ['좀비'] * 4 + ['프랭크 & 스타인'] * 3
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_ghost_deck == '내버려둔다':
            pass
    elif choose_deck == '마력':
        choose_magic_deck = input('너의 야망은 매그니피쿠스를 대체해 마력의 필경자가 되는 것인가?(덱을 가진다, 내버려둔다)')
        if choose_magic_deck == '덱을 가진다':
            starter_card = ['루비 목스'] * 2 + ['사파이어 목스'] * 2 + ['에메랄드 목스'] * 2 + ['견습 마법사'] * 2 + \
                           ['루비 골렘'] * 2 + ['마법 기사'] * 2 + ['보석 광인'] * 2 + ['유영 마법사'] * 2 + ['초록 마법사'] * 2 + \
                           ['견습 현자'] * 2
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_magic_deck == '내버려둔다':
            pass

# 본 게임
while True:
    action = input('행동을 입력하시오.(덱 추가, 덱 제거, 배틀(미완성), 카드팩 획득)')
    # 가진 콜렉션에서 카드를 덱에 넣음
    if action == '덱 추가':
        print(*deck)
        while True:
            # 전체 콜렉션에서 0개가 아닌 카드가 있다면 그 이름과 수를 출력한다.
            print('콜렉션:')
            for i in collection:
                if collection[i] > 0:
                    print(f'{i}: {collection[i]}')
            deck_card = input("카드 이름을 입력하면 콜렉션에 있는 카드가 덱에 들어옵니다.('자동 완성'을 입력하면 무작위 카드가 덱에 들어옵니다."
                              " '완료'를 입력하면 덱 추가를 종료합니다.)")
            if deck_card == '완료':
                # 만약 덱이 20장 이상이라면 완료.
                if len(deck) >= 20:
                    break
                    # 20장 이하라면 완료되지 않음.
                elif len(deck) < 20:
                    print('덱은 최소 20장 이상의 카드로 이루어져 있어야 합니다.')
            # 20장이 될 때까지 자동으로 카드를 넣어줌
            elif deck_card == '자동 완성':
                # for문으로 필터
                # complection = {}
                # for key, value in collection.items():
                #     if value > 0:
                #         complection[key] = value
                # 뭔지 모르겠는 람다 함수 필터 사용법
                complection = dict(filter(lambda e: e[1] > 0, collection.items()))
                for deck_card, value in complection.items():
                    if len(deck) == 20:
                        break
                    for i in range(value):
                        deck.append(deck_card)
                        collection[deck_card] -= 1
                print(*deck)
            else:
                if collection[deck_card] != 0:
                    deck.append(deck_card)
                    collection[deck_card] -= 1
                print(*deck)
    # 가진 콜렉션에서 카드를 덱에서 뺌
    if action == '덱 제거':
        while True:
            for i in collection:
                if not collection[i] == 0:
                    print(f'{i}: {collection[i]}')
            deck_card = input("카드 이름을 입력하면 덱에 있는 카드가 콜렉션으로 돌아갑니다.('전체 제거'를 입력하면 모든 카드가 콜렉션으로"
                              " 돌아갑니다. '완료'를 입력하면 덱 제거를 종료합니다.)")
            if deck_card == '완료':
                print(*deck)
                break
            elif deck_card == '전체 제거':
                while len(deck) > 0:
                    for i in collection:
                        deck_card = i
                        if collection[deck_card] > 0:
                            deck.remove(deck_card)
                            collection[deck_card] += 1
                print(*deck)
            else:
                deck.remove(deck_card)
                collection[deck_card] += 1
                print(*deck)
    # 배틀 제작 중
    if action == '배틀':
        energy = 0
        bone = 0
        if len(deck) < 20:
            print('덱 미완성')
            continue
        battle_deck = deck
        hand = []
        cb.print_battle_plate()
        cb.start_draw(deck)
        while True:
            while True:
                cb.match_set()
                if input('턴') != '':
                    break
            if energy < 6:
                energy += 1
            while True:
                battle_action = input("카드를 놓으려면 '세트'를 입력하세요.")
                if battle_action == '세트':
                    cb.card_set()
                else:
                    break
            # 카드가 공격함
            # 내 체력이 올라감
            # 10 이상이면 승리
    # 카드팩 획득
    if action == '카드팩 획득':
        cardpack = []
        buy_pack = input('카드 팩 테마 입력')
        if buy_pack == '짐승':
            select_cardpack(animal_card_rare, animal_card_normal, machine_card_normal, ghost_card_normal,
                            magic_card_normal)
        elif buy_pack == '기계':
            select_cardpack(machine_card_rare, machine_card_normal, animal_card_normal, ghost_card_normal,
                            magic_card_normal)
        elif buy_pack == '망자':
            select_cardpack(ghost_card_rare, ghost_card_normal, animal_card_normal, machine_card_normal,
                            magic_card_normal)
        elif buy_pack == '마력':
            select_cardpack(magic_card_rare, magic_card_normal, animal_card_normal, machine_card_normal,
                            ghost_card_normal)
        input(f'{cardpack[0]}, {cardpack[1]}, {cardpack[2]}, {cardpack[3]}, {cardpack[4]}')
        print('너의 콜렉션에 카드가 추가되었다.')
        for i in cardpack:
            collection[i] += 1
