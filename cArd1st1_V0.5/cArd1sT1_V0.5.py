import random as r
import cArd1sT1_Battle as cb
from collections import defaultdict

deck = []
collection = defaultdict(int)
animal_card_normal = ['거대 크라켄', '거울 촉수', '종 촉수', '패 촉수', '고양이', '늑대', '아기 늑대', '다람쥐', '다람쥐 공', '담비', '두더지', '무스', '새끼 무스', '물총새', '민물 거북',
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
match_ready_list = ['', '', '', '']
match_battle_list = ['', '', '', '']
player_battle_list = ['', '', '', '']
normal_cards = animal_card_normal + machine_card_normal + ghost_card_normal + magic_card_normal
rare_cards = animal_card_rare + machine_card_rare + ghost_card_rare + magic_card_rare
for i in animal_card_normal + animal_card_rare + machine_card_normal + machine_card_rare + ghost_card_normal + \
         ghost_card_rare + magic_card_normal + magic_card_rare:
    collection[i] = 0
hoil = 0
my_health = 5


def select_cardpack(select_rare, select_normal, one_random, two_random, three_random):
    cardpack = []
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
    return cardpack


def earn_cardpack(buy_pack):
    cardpack = []
    if buy_pack == '짐승':
        cardpack = select_cardpack(animal_card_rare, animal_card_normal, machine_card_normal, ghost_card_normal,
                        magic_card_normal)
    elif buy_pack == '기계':
        cardpack = select_cardpack(machine_card_rare, machine_card_normal, animal_card_normal, ghost_card_normal,
                        magic_card_normal)
    elif buy_pack == '망자':
        cardpack = select_cardpack(ghost_card_rare, ghost_card_normal, animal_card_normal, machine_card_normal,
                        magic_card_normal)
    elif buy_pack == '마력':
        cardpack = select_cardpack(magic_card_rare, magic_card_normal, animal_card_normal, machine_card_normal,
                        ghost_card_normal)
    input(f'{cardpack[0]}, {cardpack[1]}, {cardpack[2]}, {cardpack[3]}, {cardpack[4]}')
    print('너의 콜렉션에 카드가 추가되었다.')
    for i in cardpack:
        collection[i] += 1


# 시작 덱 결정
while True:
    starter_card = []
    choose_deck = input('당신의 시작 덱을 선택하시오.(짐승, 기계, 망자, 마력)')
    # 각각 시작 덱을 확인 후 콜렉션에 카드 추가
    if choose_deck == '1':
        choose_animal_deck = input('너의 야망은 레쉬를 대체해 짐승의 필경자가 되는 것인가?(덱을 가진다, 내버려둔다)')
        if choose_animal_deck == '1':
            starter_card = ['다람쥐'] * 6 + ['담비'] * 5 + ['코요테'] * 5 + ['늑대'] * 4
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_animal_deck == '2':
            pass
    elif choose_deck == '2':
        choose_machine_deck = input('너의 야망은 P03을 대체해 기술의 필경자가 되는 것인가?(덱을 가진다, 내버려둔다)')
        if choose_machine_deck == '1':
            starter_card = ['L33pB0t'] * 5 + ['49er'] * 4 + ['자동 장치'] * 4 + ['두꺼운 드로이드'] * 4 + ['스팀봇'] * 3
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_machine_deck == '2':
            pass
    elif choose_deck == '3':
        choose_ghost_deck = input('너의 야망은 그리모라를 대체해 망자의 필경자가 되는 것인가?(덱을 가진다, 내버려둔다)')
        if choose_ghost_deck == '1':
            starter_card = ['해골'] * 5 + ['뼈 채굴자'] * 4 + ['드라우그르'] * 4 + ['좀비'] * 4 + ['프랭크 & 스타인'] * 3
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_ghost_deck == '2':
            pass
    elif choose_deck == '4':
        choose_magic_deck = input('너의 야망은 매그니피쿠스를 대체해 마력의 필경자가 되는 것인가?(덱을 가진다, 내버려둔다)')
        if choose_magic_deck == '1':
            starter_card = ['루비 목스'] * 2 + ['사파이어 목스'] * 2 + ['에메랄드 목스'] * 2 + ['견습 마법사'] * 2 + \
                           ['루비 골렘'] * 2 + ['마법 기사'] * 2 + ['보석 광인'] * 2 + ['유영 마법사'] * 2 + ['초록 마법사'] * 2 + \
                           ['견습 현자'] * 2
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_magic_deck == '2':
            pass
    else:
        print('그것은 너의 야망이 될 수 없다.')

# 본 게임
while True:
    print(f'호일: {hoil}개')
    action = input('행동을 입력하시오.(덱 추가, 덱 제거, 덱 보기, 콜렉션 보기, 배틀(제작 중), 상인)')
    # 가진 콜렉션에서 카드를 덱에 넣음
    if action == '1':
        print('덱:')
        print(*deck)
        while True:
            print('콜렉션:')
            for i in collection:
                if collection[i] > 0:
                    print(f'{i}: {collection[i]}')
            deck_card = input("카드 이름을 입력하면 콜렉션에 있는 카드가 덱에 들어옵니다.('자동 완성'을 입력하면 무작위 카드가 덱에 들어옵니다."
                              " '완료'를 입력하면 덱 추가를 종료합니다.)")
            if deck_card == '2':
                # 만약 덱이 20장 이상이라면 완료.
                if len(deck) >= 20:
                    print('이제 충분히 찼구나.')
                    break
                    # 20장 이하라면 완료되지 않음.
                elif len(deck) < 20:
                    print('너의 덱은 아직 충분치 않다. 최소한 20장은 넣어야 한다.')
            # 20장이 될 때까지 자동으로 카드를 넣어줌
            elif deck_card == '1':
                if len(deck) >= 20:
                    print('이제 충분히 찼구나.')
                    break
                # for문으로 필터
                # complection = {}
                # for key, value in collection.items():
                #     if value > 0:
                #         complection[key] = value
                # 뭔지 모르겠는 람다 함수 필터 사용법
                complection = dict(filter(lambda e: e[1] > 0, collection.items()))
                for deck_card, value in complection.items():
                    for i in range(value):
                        deck.append(deck_card)
                        collection[deck_card] -= 1
            elif deck_card not in collection:
                print('그것은 네가 가진 카드가 아니다.')
            elif deck_card in collection and collection[deck_card] == 0:
                print('그 카드는 이미 충분히 넣었다.')
            elif deck_card in collection:
                if collection[deck_card] != 0:
                    deck.append(deck_card)
                    collection[deck_card] -= 1
            else:
                continue
            print('덱:')
            print(*deck)
    # 가진 콜렉션에서 카드를 덱에서 뺌
    if action == '2':
        print('덱:')
        print(*deck)
        while True:
            for i in collection:
                if not collection[i] == 0:
                    print(f'{i}: {collection[i]}')
            deck_card = input("카드 이름을 입력하면 덱에 있는 카드가 콜렉션으로 돌아갑니다.('전체 제거'를 입력하면 모든 카드가 콜렉션으로"
                              " 돌아갑니다. '완료'를 입력하면 덱 제거를 종료합니다.)")
            if deck_card == '2':
                print('덱:')
                print(*deck)
                break
            elif deck_card == '1':
                if len(deck) == 0:
                    print("뺄 것이 무엇이 있다고 빼려 하는가.")
                temp_deck = deck.copy()
                for i in temp_deck:
                    deck.remove(i)
                    collection[i] += 1
                print('덱:')
                print(*deck)
            elif deck_card in deck:
                deck.remove(deck_card)
                collection[deck_card] += 1
                print(*deck)
            else:
                print('그것은 네가 가진 카드가 아니다.')
    # 내 덱 보기
    if action == '3':
        print('덱:')
        print(*deck)
    # 내 카드 모음 보기
    if action == '4':
        print('콜렉션:')
        for i in collection:
            if collection[i] > 0:
                print(f'{i}: {collection[i]}')
    # 배틀 제작 중
    if action == '5':
        if len(deck) < 20:
            print('아직 너의 덱은 충분치 않다.')
            continue
        win_lose = False
        max_energy = 1
        energy = 0
        bone = 0
        gem = []
        battle_deck = deck
        cb.start_draw(battle_deck)
        while not win_lose:
            cb.print_battle_plate(match_ready_list, match_battle_list, player_battle_list)
            while True:
                turn = input("턴 넘기기 시 '1'을 입력.")
                if turn == '1':
                    break
                else:
                    cb.match_set(match_ready_list, match_battle_list, player_battle_list)
            if max_energy <= 6:
                max_energy += 1
            energy = max_energy
            cb.draw(battle_deck)
            while True:
                turn = input("턴 넘기기 시 '1'을 입력.")
                if turn == '1':
                    break
                else:
                    cb.mox_search(player_battle_list)
                    energy, bone, player_battle_list = cb.card_set(energy, bone, gem, match_ready_list, match_battle_list, player_battle_list)
            my_health, match_battle_list = cb.card_attack(my_health, match_battle_list, player_battle_list)
            print(f'{my_health} : {10 - my_health}')
            hoil, win_lose = cb.win_lose(my_health, hoil)
            match_ready_list, match_battle_list = cb.match_ready_go(match_ready_list, match_battle_list)
            my_health, bone, player_battle_list = cb.match_attack(my_health, bone, match_battle_list, player_battle_list)
            print(f'{my_health} : {10 - my_health}')
            hoil, win_lose = cb.win_lose(my_health, hoil)
    # 상인
    if action == '6':
        if hoil != 0:
            while True:
                print('원하시는 물건이 있으시다면...')
                print('랜덤한 카드팩: 포일 5 / 랜덤한 일반 카드: 포일 1 / 랜덤한 레어 카드: 포일 3')
                print(f'호일: {hoil}개')
                buying = input('구매 항목: 일반 카드, 레어 카드, 카드팩, 나가기')
                if buying == '1' and hoil >= 1:
                    random_card_normal = r.choice(normal_cards)
                    print(random_card_normal)
                    collection[random_card_normal] += 1
                    hoil -= 1
                    break
                elif buying == '2' and hoil >= 3:
                    random_card_rare = r.choice(rare_cards)
                    print(random_card_rare)
                    collection[random_card_rare] += 1
                    hoil -= 3
                    break
                elif buying == '3' and hoil >= 5:
                    random_cardpack = r.choice(['짐승', '기계', '망자', '마력'])
                    earn_cardpack(random_cardpack)
                    hoil -= 5
                    break
                elif buying == '4':
                    break
                else:
                    print('그런 물건은 취급하지 않습니다만...')
                    continue
            print('이용해주셔서 감사합니다.')
