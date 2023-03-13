import random as r
cards_kinds = {'거대 크라켄': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': '크라켄 잠수', '희생 여부': '가능'},
               '거울 촉수': {'비용': ['피', 1], '공격력': 'ㄱㅓㅇㅜㄹㅜㅇㅓㄱ', '체력': 3, '특성': '없음', '희생 여부': '가능'},
               '종 촉수': {'비용': ['피', 2], '공격력': '타종수', '체력': 3, '특성': '없음', '희생 여부': '가능'},
               '패 촉수': {'비용': ['피', 1], '공격력': '카드 세는 자', '체력': 1, '특성': '없음', '희생 여부': '가능'},
               '고양이': {'비용': ['피', 1], '공격력': 0, '체력': 1, '특성': '많은 목숨', '희생 여부': '다중'},
               '언데드 고양이': {'비용': ['피', 1], '공격력': 3, '체력': 6, '특성': '없음', '희생 여부': '가능'},
               '늑대': {'비용': ['피', 2], '공격력': 3, '체력': 2, '특성': '없음', '희생 여부': '가능'},
               '아기 늑대': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': '성장', '희생 여부': '가능'},
               '다람쥐': {'비용': '없음', '공격력': 0, '체력': 1, '특성': '없음', '희생 여부': '가능'},
               '다람쥐 공': {'비용': ['피', 1], '공격력': 0, '체력': 2, '특성': '다람쥐 분만', '희생 여부': '가능'},
               '담비': {'비용': ['피', 1], '공격력': 1, '체력': 2, '특성': '없음', '희생 여부': '가능'},
               '두더지': {'비용': ['피', 1], '공격력': 0, '체력': 4, '특성': '굴살이', '희생 여부': '가능'},
               '두더지인간': {'비용': ['피', 1], '공격력': 0, '체력': 6, '특성': ['굴살이', '비행 방어'], '희생 여부': '가능'},
               '무스': {'비용': ['피', 2], '공격력': 2, '체력': 4, '특성': '이동', '희생 여부': '가능'},
               '새끼 무스': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': ['이동', '성장'], '희생 여부': '가능'},
               '물총새': {'비용': ['피', 2], '공격력': 1, '체력': 1, '특성': ['잠수', '비행'], '희생 여부': '가능'},
               '민물 거북': {'비용': ['피', 2], '공격력': 1, '체력': 6, '특성': '없음', '희생 여부': '가능'},
               '민물 수달': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': '잠수', '희생 여부': '가능'},
               '매': {'비용': ['피', 2], '공격력': 3, '체력': 1, '특성': '비행', '희생 여부': '가능'},
               '블러드하운드': {'비용': ['피', 2], '공격력': 2, '체력': 3, '특성': '수호자', '희생 여부': '가능'},
               '비둘기': {'비용': ['피', 1], '공격력': 1, '체력': 2, '특성': '비행', '희생 여부': '가능'},
               '사마귀신': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': '삼분공격', '희생 여부': '가능'},
               '살무사': {'비용': ['피', 2], '공격력': 1, '체력': 1, '특성': '즉사', '희생 여부': '가능'},
               '스컹크': {'비용': ['피', 1], '공격력': 0, '체력': 3, '특성': '구린내', '희생 여부': '가능'},
               '포자스컹크': {'비용': ['피', 1], '공격력': 0, '체력': 3, '특성': ['구린내', '구린내'], '희생 여부': '가능'},
               '알파': {'비용': ['피', 1], '공격력': 1, '체력': 2, '특성': '리더', '희생 여부': '가능'},
               '우라율리': {'비용': ['피', 4], '공격력': 7, '체력': 7, '특성': '없음', '희생 여부': '가능'},
               '우로보로스': {'비용': ['피', 2], '공격력': 133, '체력': 133, '특성': '불사', '희생 여부': '가능'},
               '전기뱀장어': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': ['잠수', '배터리 운반자'], '희생 여부': '가능'},
               '코요테': {'비용': ['피', 1], '공격력': 2, '체력': 1, '특성': '없음', '희생 여부': '가능'},
               '큰까마귀': {'비용': ['피', 2], '공격력': 2, '체력': 3, '특성': '비행', '희생 여부': '가능'},
               '토끼': {'비용': '없음', '공격력': 0, '체력': 1, '특성': '없음'}, '희생 여부': '가능',
               '토끼굴': {'비용': ['피', 1], '공격력': 0, '체력': 3, '특성': '토끼굴', '희생 여부': '불가능'},
               '향유고래': {'비용': ['피', 2], '공격력': 2, '체력': 2, '특성': '잠수', '희생 여부': '가능'},
               '황소개구리': {'비용': ['피', 1], '공격력': 1, '체력': 2, '특성': '비행 방어', '희생 여부': '가능'},
               '회색곰': {'비용': ['피', 3], '공격력': 4, '체력': 6, '특성': '없음', '희생 여부': '가능'},
               '감시 드론': {'비용': ['에너지', 1], '공격력': 0, '체력': 1, '특성': '보초', '희생 여부': '가능'},
               '감시 포자': {'비용': ['에너지', 1], '공격력': 0, '체력': 1, '특성': ['보초', '보초'], '희생 여부': '가능'},
               '무효화 전도체': {'비용': ['에너지', 1], '공격력': 0, '체력': 1, '특성': '무효화 전도체', '희생 여부': '가능'},
               'L33pB0t': {'비용': ['에너지', 1], '공격력': 0, '체력': 2, '특성': '비행 방어', '희생 여부': '가능'},
               '고GI봇': {'비용': ['에너지', 2], '공격력': 0, '체력': 1, '특성': '고귀한 희생', '희생 여부': '가능'},
               '버프 전도체': {'비용': ['에너지', 2], '공격력': 0, '체력': 2, '특성': '공격 전도체', '희생 여부': '가능'},
               '봄버봇': {'비용': ['에너지', 2], '공격력': 1, '체력': 1, '특성': '폭탄', '희생 여부': '가능'},
               '에너지봇': {'비용': ['에너지', 2], '공격력': 0, '체력': 1, '특성': '배터리 운반자', '희생 여부': '가능'},
               '49er': {'비용': ['에너지', 2], '공격력': 1, '체력': 1, '특성': '이동', '희생 여부': '가능'},
               '곤충 드론': {'비용': ['에너지', 3], '공격력': 1, '체력': 1, '특성': '비행', '희생 여부': '가능'},
               '공장 전도체': {'비용': ['에너지', 3], '공격력': 0, '체력': 2, '특성': '생산 전도체', '희생 여부': '가능'},
               '목스 모듈': {'비용': ['에너지', 3], '공격력': 0, '체력': 2, '특성': '위대한 목스', '희생 여부': '가능'},
               '에너지 전도체': {'비용': ['에너지', 3], '공격력': 1, '체력': 2, '특성': '발전 전도체', '희생 여부': '가능'},
               '자동 장치': {'비용': ['에너지', 3], '공격력': 1, '체력': 1, '특성': '없음', '희생 여부': '가능'},
               '폭탄 부인': {'비용': ['에너지', 3], '공격력': 1, '체력': 2, '특성': '폭탄 바주카', '희생 여부': '가능'},
               '곡선넘이': {'비용': ['에너지', 4], '공격력': 2, '체력': 3, '특성': '없음', '희생 여부': '가능'},
               '두꺼운 드로이드': {'비용': ['에너지', 5], '공격력': 1, '체력': 3, '특성': '없음', '희생 여부': '가능'},
               '피버봇': {'비용': ['에너지', 5], '공격력': '주사위', '체력': 2, '특성': '없음', '희생 여부': '가능'},
               '사진충': {'비용': ['에너지', 5], '공격력': 1, '체력': 1, '특성': ['보초', '즉사'], '희생 여부': '가능'},
               '더블 거너': {'비용': ['에너지', 3], '공격력': 2, '체력': 1, '특성': '이분공격', '희생 여부': '가능'},
               '볼트하운드': {'비용': ['에너지', 6], '공격력': 2, '체력': 2, '특성': '수호자', '희생 여부': '가능'},
               '스팀봇': {'비용': ['에너지', 6], '공격력': 2, '체력': 2, '특성': '없음', '희생 여부': '가능'},
               '해골': {'비용': '없음', '공격력': 1, '체력': 1, '특성': '취약성', '희생 여부': '가능'},
               '뼈 무더기': {'비용': '없음', '공격력': 0, '체력': 1, '특성': '팽창', '희생 여부': '가능'},
               '드라우그르': {'비용': ['뼈', 1], '공격력': 0, '체력': 1, '특성': '해빙', '희생 여부': '불가능'},
               '뼈 굴착자': {'비용': ['뼈', 1], '공격력': 0, '체력': 3, '특성': '뼈 파내는 자', '희생 여부': '가능'},
               '포자굴착자': {'비용': ['뼈', 1], '공격력': 0, '체력': 3, '특성': ['뼈 파내는 자', '뼈 파내는 자'], '희생 여부': '가능'},
               '도굴꾼': {'비용': ['뼈', 2], '공격력': 0, '체력': 2, '특성': '도굴', '희생 여부': '가능'},
               '망령': {'비용': ['뼈', 2], '공격력': 3, '체력': 1, '특성': '취약성', '희생 여부': '가능'},
               '밴시': {'비용': ['뼈', 2], '공격력': 1, '체력': 1, '특성': '비행', '희생 여부': '가능'},
               '뼈 마법사': {'비용': ['뼈', 2], '공격력': 4, '체력': 1, '특성': ['보석 의존증', '취약성'], '희생 여부': '가능'},
               '좀비': {'비용': ['뼈', 2], '공격력': 1, '체력': 1, '특성': '없음', '희생 여부': '가능'},
               '네크로맨서': {'비용': ['뼈', 3], '공격력': 1, '체력': 2, '특성': '이중 사망', '희생 여부': '가능'},
               '부서진 은화(왼쪽)': {'비용': ['뼈', 3], '공격력': 0, '체력': 2, '특성': '가시', '희생 여부': '가능'},
               '부서진 은화(오른쪽)': {'비용': ['뼈', 3], '공격력': 0, '체력': 2, '특성': '골왕', '희생 여부': '가능'},
               '석관': {'비용': ['뼈', 4], '공격력': 0, '체력': 2, '특성': '성장', '희생 여부': '가능'},
               '유령선': {'비용': ['뼈', 4], '공격력': 0, '체력': 1, '특성': ['잠수', '해골 선원'], '희생 여부': '가능'},
               '익사한 영혼': {'비용': ['뼈', 4], '공격력': 1, '체력': 1, '특성': ['잠수', '즉사'], '희생 여부': '가능'},
               '워커즈': {'비용': ['뼈', 4], '공격력': 1, '체력': 2, '특성': '골왕', '희생 여부': '가능'},
               '죽은 손': {'비용': ['뼈', 5], '공격력': 1, '체력': 1, '특성': '손재주', '희생 여부': '가능'},
               '프랭크 & 스타인': {'비용': ['뼈', 5], '공격력': 2, '체력': 2, '특성': '없음', '희생 여부': '가능'},
               '파라오의 애완동물': {'비용': ['뼈', 6], '공격력': 0, '체력': 2, '특성': ['고귀한 희생', '많은 목숨'], '희생 여부': '다중'},
               '본하운드': {'비용': ['뼈', 7], '공격력': 2, '체력': 3, '특성': '수호자', '희생 여부': '가능'},
               '미라 제왕': {'비용': ['뼈', 8], '공격력': 3, '체력': 3, '특성': '없음', '희생 여부': '가능'},
               '목 없는 기사': {'비용': ['뼈', 13], '공격력': 5, '체력': 5, '특성': ['비행', '이동'], '희생 여부': '가능'},
               '루비 목스': {'비용': '없음', '공격력': 0, '체력': 1, '특성': '루비 목스', '희생 여부': '불가능'},
               '사파이어 목스': {'비용': '없음', '공격력': 0, '체력': 1, '특성': '사파이어 목스', '희생 여부': '불가능'},
               '에메랄드 목스': {'비용': '없음', '공격력': 0, '체력': 1, '특성': '에메랄드 목스', '희생 여부': '불가능'},
               '블린의 목스': {'비용': '없음', '공격력': 0, '체력': 2, '특성': ['사파이어 목스', '에메랄드 목스'], '희생 여부': '불가능'},
               '고란즈의 목스': {'비용': '없음', '공격력': 0, '체력': 2, '특성': ['루비 목스', '에메랄드 목스'], '희생 여부': '불가능'},
               '오를루의 목스': {'비용': '없음', '공격력': 0, '체력': 2, '특성': ['루비 목스', '사파이어 목스'], '희생 여부': '불가능'},
               '마그누스 목스': {'비용': '없음', '공격력': 0, '체력': 9, '특성': '위대한 목스', '희생 여부': '불가능'},
               '견습 마법사': {'비용': '없음', '공격력': 1, '체력': 1, '특성': '보석 의존증', '희생 여부': '가능'},
               '붉은 마법사': {'비용': ['보석', '루비'], '공격력': 0, '체력': 1, '특성': '목스 전원', '희생 여부': '가능'},
               '연습용 마법사': {'비용': ['보석', '루비'], '공격력': 0, '체력': 3, '특성': '없음', '희생 여부': '가능'},
               '루비 골렘': {'비용': ['보석', '루비'], '공격력': 1, '체력': 1, '특성': '루비 심장', '희생 여부': '가능'},
               '마법 기사': {'비용': ['보석', '루비'], '공격력': 1, '체력': 3, '특성': '보석 의존증', '희생 여부': '가능'},
               '파란 마법사': {'비용': ['보석', '사파이어'], '공격력': 0, '체력': 1, '특성': '심리적 뵤기', '희생 여부': '가능'},
               '파란 포자마법사': {'비용': ['보석', '사파이어'], '공격력': 0, '체력': 1, '특성': ['심리적 뵤기', '심리적 뵤기'], '희생 여부': '가능'},
               '보석 광인': {'비용': ['보석', '사파이어'], '공격력': 2, '체력': 1, '특성': '보석 의존증', '희생 여부': '가능'},
               '유영 마법사': {'비용': ['보석', '사파이어'], '공격력': 1, '체력': 1, '특성': '비행', '희생 여부': '가능'},
               '포스 마법사': {'비용': ['보석', '사파이어'], '공격력': 0, '체력': 1, '특성': ['역겨움', '보석 의존증'], '희생 여부': '가능'},
               '초록 마법사': {'비용': ['보석', '에메랄드'], '공격력': '에메랄드', '체력': 2, '특성': '없음', '희생 여부': '가능'},
               '견습 현자': {'비용': ['보석', '에메랄드'], '공격력': 1, '체력': 2, '특성': '없음', '희생 여부': '가능'},
               '근육 마법사': {'비용': ['보석', '에메랄드'], '공격력': 1, '체력': 1, '특성': '밀치기', '희생 여부': '가능'},
               '자극 마법사': {'비용': ['보석', '에메랄드'], '공격력': 0, '체력': 1, '특성': '자극', '희생 여부': '가능'},
               '미식마법사': {'비용': ['보석', '에메랄드'], '공격력': 0, '체력': 2, '특성': '팽창', '희생 여부': '가능'},
               '마스터 블린': {'비용': ['보석', ['사파이어', '에메랄드']], '공격력': 0, '체력': 4, '특성': '진정한 학자', '희생 여부': '가능'},
               '마스터 고란즈': {'비용': ['보석', ['루비', '에메랄드']], '공격력': 2, '체력': 6, '특성': '보석 의존증', '희생 여부': '가능'},
               '마스터 오를루': {'비용': ['보석', ['루비', '사파이어']], '공격력': 1, '체력': 1, '특성': ['비행', '약탈자'], '희생 여부': '가능'}}
match_ready_list = ['', '', '', '']
match_battle_list = ['', '', '', '']
player_battle_list = ['', '', '', '']
hand = []
my_health = 5
hoil = 0


def print_battle_plate():
    print(match_ready_list)
    print(match_battle_list)
    print(player_battle_list)


def battle_draw(deck):
    battle_deck = deck
    drawed_card = r.choice(battle_deck)
    hand.append(drawed_card)
    battle_deck.remove(drawed_card)


def start_draw(deck):
    for i in range(4):
        battle_draw(deck)
    print(*hand)


def draw(deck):
    if len(deck) < 20:
        print('덱이 20장 이하입니다.')
    hand = []
    for i in range(4):
        battle_draw(deck)
        print(*hand)
    while len(deck) > 0:
        input('엔터 키를 눌러 카드를 드로우하세요.')
        battle_draw(deck)
        print(*hand)


def card_set():
    global energy
    global bone
    while True:
        set_card = input('놓을 카드를 입력하세요.(카드 이름)')
        if set_card not in hand:
            print('정확한 이름을 입력하세요.')
            continue
    if cards_kinds[set_card]['비용'] != '없음':
        # 비용이 피일 때
        if cards_kinds[set_card]['비용'][0] == '피':
            need_blood = cards_kinds[set_card]['비용'][1]
            blood_card_list = player_battle_list
            can_be_blood = 0
            for i in range(4):
                if cards_kinds[player_battle_list[i]]['희생 여부'] == '가능' or cards_kinds[player_battle_list[i]]['희생 여부'] == '다중':
                    can_be_blood += 1
                if can_be_blood >= need_blood:
                    for i in range(need_blood):
                        print(*blood_card_list)
                        blood_card = input('희생할 카드를 입력하세요.(카드 이름)')
                        if cards_kinds[blood_card]['희생 여부'] == '다중':
                            need_blood -= 1
                        elif cards_kinds[blood_card]['희생 여부'] == '가능':
                            need_blood -= 1
                            player_battle_list.remove(blood_card)
                            bone += 1
                        elif cards_kinds[blood_card]['희생 여부'] == '불가능':
                            print('이 카드는 희생할 수 없습니다.')
                        blood_card_list.remove(blood_card)
        # 비용이 에너지일 때
        elif cards_kinds[set_card]['비용'][0] == '에너지':
            energy -= cards_kinds[set_card]['비용'][1]
        # 비용이 뼈일 때
        elif cards_kinds[set_card]['비용'][0] == '뼈':
            bone -= cards_kinds[set_card]['비용'][1]
        # 비용이 보석일 때
        elif cards_kinds[set_card]['비용'][0] == '루비' or cards_kinds[set_card]['비용'][0] == '사파이어' or \
                cards_kinds[set_card]['비용'][0] == '에메랄드':
            need_gem = [cards_kinds[set_card]['비용'][1] for i in range(len(cards_kinds[set_card]['비용']))]
            while True:
                if '루비 목스' in player_battle_list or '고란즈의 목스' in player_battle_list or '오를루의 목스' in player_battle_list:
                    need_gem.remove('루비')
                elif '사파이어 목스' in player_battle_list or '블린의 목스' in player_battle_list or '오를루의 목스' in player_battle_list:
                    need_gem.remove('사파이어')
                elif '에메랄드 목스' in player_battle_list or '블린의 목스' in player_battle_list or '고란즈의 목스' in player_battle_list:
                    need_gem.remove('에메랄드')
                if need_gem == []:
                    break
                else:
                    continue
                    

    while True:
        print_battle_plate()
        card_space = int(input('놓을 자리를 입력하세요.(1, 2, 3, 4)'))
        if card_space < 1 or card_space > 4:
            print('정확한 자리를 입력하세요.')
            continue
        elif player_battle_list[card_space] == '':
            player_battle_list[card_space] = [set_card, cards_kinds[set_card]]
            hand.remove(set_card)
            print_battle_plate()
        elif player_battle_list[card_space] != '':
            print('이미 카드가 그 자리에 있습니다.')
# 와! 수정! 아시는구나!

def match_set():
    print_battle_plate()
    set_card = input('대기할 카드를 입력하세요.(카드 이름)')
    card_space = int(input('놓을 자리를 입력하세요.(1, 2, 3, 4)'))
    match_ready_list[card_space] = [set_card, cards_kinds[set_card]]
    print_battle_plate()


def card_attack():
    global my_health
    global hoil
    # 플레이어가 공격하는 거
    # 상대 편 카드가 내려오는 거
    # 상대 카드가 공격하는 거
    # 공격받은 카드가 체력이 내려가는 거
    # 체력이 0이 되면 소멸하는 거
    # '강철 덫' 특성에 의해서 자신이 사망했을 때 특정 카드가 그 자리에 튀어나오게 하는 거
    # '비행' 특성에 의해서 앞에 카드가 있더라도 상대가 공격당하게 하는 거
    # '보초' 특성에 의해서 앞에 카드가 감지된 순간 피해를 받게 하는 거
    # '비행 방어' 특성에 의해서 '비행' 특성의 효과를 무효화 시키는 거
    # '이동' 특성에 의해서 카드가 양 옆의 랜덤한 빈 칸으로 이동하는 거
    # '잠수' 특성에 의해서 카드가 공격당하지 않고 상대가 공격당하는 거
    # '해빙' 특성에 의해서 카드가 사망했을 때 특정 카드가 그 자리에 튀어나오게 하는 거
    # '약탈자' 특성에 의해서 카드가 상대를 직접 공격했을 때 랜덤한 카드를 얻는 거
    for i in range(4):
        if player_battle_list[i] != '':
            # 상대편에 카드가 없을 때 내 카드의 공격력만큼 체력 회복
            if match_battle_list[i] == '':
                my_health += player_battle_list[i]['공격력']
            # 상대 편에 카드가 있을 때 해당 카드의 체력을 내 카드의 공격력만큼 감소, 0이 되면 사망
            elif match_battle_list[i] != '':
                cards_kinds[match_battle_list[i]]['체력'] += cards_kinds[player_battle_list[i]]['공격력']
            else:
                pass

                # if my_health <= 10:
                #     print('승리!')
                #     if my_health < 10:
                #         hoil += my_health - 10
