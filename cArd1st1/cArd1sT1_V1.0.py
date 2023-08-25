import random as r
import cArd1sT1_8aTt1e as cb
from collections import defaultdict
# 초기 변수들
deck = []
collection = defaultdict(int)
animal_card_normal = ['거대 크라켄', '거울 촉수', '종 촉수', '패 촉수', '고양이', '늑대', '아기 늑대', '다람쥐', '다람쥐 공', '담비',
                      '두더지', '들쥐', '무스', '새끼 무스', '물총새', '매', '블러드하운드', '큰까마귀', '큰까마귀 알', '토끼굴', '토끼',
                      '황소개구리', '회색곰']
animal_card_rare = ['두더지인간', '사마귀신', '우라율리', '우로보로스', '전기뱀장어']
machine_card_normal = ['감시 드론', '무효화 전도체', 'L33pB0t', '고GI봇', '버프 전도체', '에너지봇', '봄버봇', '49er',
                       '자동 장치', '곤충 드론', '공장 전도체', '두꺼운 드로이드', '피버봇', '더블 거너', '볼트하운드', '스팀봇']
machine_card_rare = ['목스 모듈', '에너지 전도체', '폭탄 부인', '곡선넘이', '사진충']
ghost_card_normal = ['해골', '뼈 굴착자', '드라우그르', '망령', '밴시', '뼈 마법사', '좀비', '부서진 은화(왼쪽)',
                     '부서진 은화(오른쪽)', '석관', '유령선', '익사한 영혼', '워커즈', '프랭크 & 스타인', '본하운드', '미라 제왕']
ghost_card_rare = ['도굴꾼', '네크로맨서', '뼈의 왕의 뿔피리', '죽은 손', '파라오의 애완동물', '목 없는 기사']
magic_card_normal = ['루비 목스', '사파이어 목스', '에메랄드 목스', '견습 마법사', '붉은 마법사', '연습용 마법사', '루비 골렘', '마법 기사',
                     '파란 마법사', '보석 광인', '유영 마법사', '포스 마법사', '초록 마법사', '견습 현자', '근육 마법사']
magic_card_rare = ['블린의 목스', '고란즈의 목스', '오를루의 목스', '마스터 고란즈', '마스터 오를루']
match_ready_list = ['', '', '', '']
match_battle_list = ['', '', '', '']
player_battle_list = ['', '', '', '']
normal_cards = animal_card_normal + machine_card_normal + ghost_card_normal + magic_card_normal
rare_cards = animal_card_rare + machine_card_rare + ghost_card_rare + magic_card_rare
all_cards = normal_cards + rare_cards
for i in animal_card_normal + animal_card_rare + machine_card_normal + machine_card_rare + ghost_card_normal + \
         ghost_card_rare + magic_card_normal + magic_card_rare + ['포자쥐', '감시 포자', '포자굴착자', '파란 포자마법사']:
    collection[i] = 0
hoil = 0


def select_cardpack(select_rare, select_normal, one_random, two_random, three_random):
    cardpack = [f'{r.choice(select_rare)}']
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
    choose_deck = input('당신의 시작 덱을 선택하시오.(짐승(1), 기계(2), 망자(3), 마력(4))')
    # 각각 시작 덱을 확인 후 콜렉션에 카드 추가
    if choose_deck == '1':
        choose_animal_deck = input('너의 야망은 레쉬를 대체해 짐승의 필경자가 되는 것인가?(덱을 가진다(1), 내버려둔다(2))')
        if choose_animal_deck == '1':
            starter_card = ['다람쥐'] * 7 + ['담비'] * 5 + ['황소개구리'] * 4 + ['늑대'] * 4
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_animal_deck == '2':
            pass
    elif choose_deck == '2':
        choose_machine_deck = input('너의 야망은 P03을 대체해 기술의 필경자가 되는 것인가?(덱을 가진다(1), 내버려둔다(2))')
        if choose_machine_deck == '1':
            starter_card = ['L33pB0t'] * 5 + ['49er'] * 4 + ['자동 장치'] * 4 + ['두꺼운 드로이드'] * 4 + ['스팀봇'] * 3
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_machine_deck == '2':
            pass
    elif choose_deck == '3':
        choose_ghost_deck = input('너의 야망은 그리모라를 대체해 망자의 필경자가 되는 것인가?(덱을 가진다(1), 내버려둔다(2))')
        if choose_ghost_deck == '1':
            starter_card = ['해골'] * 5 + ['뼈 채굴자'] * 4 + ['드라우그르'] * 4 + ['좀비'] * 4 + ['프랭크 & 스타인'] * 3
            for i in starter_card:
                collection[i] += 1
            print('너의 콜렉션에 카드가 추가되었다.')
            break
        elif choose_ghost_deck == '2':
            pass
    elif choose_deck == '4':
        choose_magic_deck = input('너의 야망은 매그니피쿠스를 대체해 마력의 필경자가 되는 것인가?(덱을 가진다(1), 내버려둔다(2))')
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
    action = input('행동을 입력하시오. [덱 추가(1), 덱 제거(2), 덱 보기(3), 콜렉션 보기(4), 배틀(5), 상인(6)]')
    # 가진 콜렉션에서 카드를 덱에 넣음
    if action == '1':
        print('덱:')
        print(*deck)
        while True:
            # 콜렉션 출력
            print('콜렉션:')
            for i in collection:
                if collection[i] > 0:
                    print(f'{i}: {collection[i]}')
            deck_card = input("카드 이름을 입력하면 콜렉션에 있는 카드가 덱에 들어옵니다.('자동 완성'(1)을 입력하면 무작위 카드가 덱에 들어옵니다. '완료'(2)를 입력하면 덱 추가를 종료합니다.)")
            # 완료
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
            # 입력한 카드 없을 때
            elif deck_card not in collection:
                print('그것은 네가 가진 카드가 아니다.')
            # 카드가 있는데 콜렉션엔 없을 때
            elif deck_card in collection and collection[deck_card] == 0:
                print('그 카드는 이미 충분히 넣었다.')
            # 수동으로 카드 넣을 때
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
        if not deck:
            continue
        print('덱:')
        print(*deck)
        while True:
            # 콜렉션 출력
            for i in collection:
                if not collection[i] == 0:
                    print(f'{i}: {collection[i]}')
            deck_card = input("카드 이름을 입력하면 덱에 있는 카드가 콜렉션으로 돌아갑니다.('전체 제거'(1)를 입력하면 모든 카드가 콜렉션으로 돌아갑니다. '완료'(2)를 입력하면 덱 제거를 종료합니다.)")
            # 완료
            if deck_card == '2':
                print('덱:')
                print(*deck)
                break
            # 전체 제거
            elif deck_card == '1':
                if len(deck) == 0:
                    print("뺄 것이 무엇이 있다고 빼려 하는가.")
                temp_deck = deck.copy()
                for i in temp_deck:
                    deck.remove(i)
                    collection[i] += 1
                print('덱:')
                print(*deck)
            # 수동 제거
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
    # 배틀
    if action == '5':
        my_health = 5
        # 덱 개수 제한
        if len(deck) < 20:
            print('아직 너의 덱은 충분치 않다.')
            continue
        # 함수 초기 설정
        win = False  # 승리 여부 체크
        max_energy = 0  # 최대 에너지
        energy = 0  # 소지한 에너지
        bone = 0  # 소지한 뼈
        gem = []  # 소지한 보석
        hand = []  # 패
        is_first_turn = True # 첫 턴 여부
        # 덱 및 패의 기본 카드 설정
        r.shuffle(deck)
        battle_deck = deck
        battle_deck, hand = cb.start_draw(battle_deck, hand)  # 기본 3장 드로우
        # 배틀 메인 루프
        while not win:
            cb.print_battle_plate(match_ready_list, match_battle_list, player_battle_list)  # 배틀 판 출력
            # 상대 턴(대기)
            while True:
                turn = input("(상대) 턴 넘기기 시 '1'을 입력. 카드 소환 시 '2'를 입력.")
                if turn == '1':
                    break
                # 보석 현황 파악 및 카드 소환 및 전도체 확인
                elif turn == '2':
                    gem = cb.match_mox_search(gem, match_battle_list)
                    bone, match_ready_list = cb.match_set(bone, gem, match_ready_list, match_battle_list, player_battle_list)
                    match_battle_list, energy, max_energy = cb.match_conducting(match_battle_list, energy, max_energy)
            # 턴 경과 시 발동 특성
            bone, player_battle_list = cb.my_turn_change(bone, player_battle_list)  # 성장, 뼈 채굴자 특성 발동
            # 에너지/최대 에너지 증가
            if max_energy < 6:
                max_energy += 1
            energy = max_energy
            battle_deck, hand = cb.draw(battle_deck, hand)
            # 내 턴
            while True:
                turn = input("(플레이어) 턴 넘길 시 '1'을 입력. 카드 소환 시 '2'를 입력. 수동 효과 발동 시 '3'를 입력.")
                if turn == '1':
                    break
                # 보석 현황 파악 및 카드 설치 및 전도체 확인
                elif turn == '2':
                    gem = cb.my_mox_search(gem, player_battle_list)
                    hand, energy, max_energy, bone, player_battle_list, match_battle_list, battle_deck = cb.card_set(hand, energy, max_energy, bone, gem, match_ready_list, match_battle_list, player_battle_list, battle_deck)
                    player_battle_list, energy, max_energy = cb.player_conducting(player_battle_list, energy, max_energy)
                # 수동 효과 발동
                elif turn == '3':
                    player_battle_list, battle_deck, hand, energy, bone, gem = cb.player_unauto_abilty(player_battle_list, battle_deck, hand, energy, bone, gem)
            # 내 공격
            player_battle_list, match_battle_list = cb.player_change_attack(player_battle_list, match_battle_list)
            hand, bone, my_health, match_battle_list, player_battle_list = cb.card_attack(hand, bone, my_health, match_battle_list, player_battle_list, gem, all_cards)
            print(f'{my_health} : {10 - my_health}')
            hoil, win = cb.win_lose(my_health, hoil)
            # 상대 턴 경과 시 발동 특성
            match_battle_list = cb.match_turn_change(match_battle_list)
            match_ready_list, match_battle_list = cb.match_ready_go(match_ready_list, match_battle_list)
            # 상대의 공격
            player_battle_list, match_battle_list = cb.player_change_attack(player_battle_list, match_battle_list)
            my_health, hand, bone, match_battle_list, player_battle_list = cb.match_attack(my_health, hand, bone, match_battle_list, player_battle_list)
            print(f'{my_health} : {10 - my_health}')
            hoil, win = cb.win_lose(my_health, hoil)
    # 상점 방문
    if action == '6':
        have_uro = False
        if collection['우로보로스'] >= 1:
            have_uro = True
        if hoil != 0:
            while True:
                print('원하시는 물건이 있으시다면...')
                print(f'호일: {hoil}개')
                if not have_uro:
                    buying = input('[구매 항목: 랜덤 일반 카드(포일 1개), 랜덤 레어 카드(포일 3개), 랜덤 카드팩(포일 5개), 우로보로스(포일 8개)], 나가기')
                if have_uro:
                    buying = input('[구매 항목: 랜덤 일반 카드(포일 1개), 랜덤 레어 카드(포일 3개), 랜덤 카드팩(포일 5개)], 나가기')
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
                elif buying == '4' and hoil >= 8:
                    collection['우로보로스'] += 1
                    hoil -= 8
                    break
                elif buying == '5':
                    print('이용해주셔서 감사합니다.')
                    break
                else:
                    print('그런 물건은 취급하지 않습니다만...')
                    continue
    # 진균학자 방문
    if action == 'tlfgja':
        print('dkssudgktlsrk?')
        print('djtjdhk! djtjdhk!')
        print('tlfgjacpsms wnsqlehoTsk?')
        print('tlfgja! tlfgja!')
        tlfgjacp = input('tlfgjacpfmf soshkfk!')
        if tlfgjacp == '들쥐' and collection['들쥐'] <= 2:
            print('dlrp qkfh sork gkrh tlvdjTejs rjdi!')
            print('tlfgjadlek! tlfgja!')
            collection['들쥐'] -= 2
            collection['포자쥐'] += 1
        elif tlfgjacp == '감시 드론' and collection['감시 드론'] <= 2:
            print('wlsWkfh tlfgjacp rngodhs rjdi?')
            print('dlwp tlfgjadldi! akstp!')
            collection['감시 드론'] -= 2
            collection['감시 포자'] += 1
        elif tlfgjacp == '뼈 굴착자' and collection['뼈 굴착자'] <= 2:
            print('dhk! wlsWk tlfgjacpwksgdk!')
            print('emdldj! tlfgjadl! ehlsek!')
            collection['뼈 굴착자'] -= 2
            collection['포자굴착자'] += 1
        elif tlfgjacp == '파란 마법사' and collection['파란 마법사'] <= 2:
            print('tlfgjacp? rhakdnj!')
            print('rhakdnj! rhakdnj!')
            collection['파란 마법사'] -= 2
            collection['파란 포자마법사'] += 1
