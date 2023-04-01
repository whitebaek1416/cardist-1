import random as r
from collections import defaultdict
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
               '미식 마법사': {'비용': ['보석', '에메랄드'], '공격력': 0, '체력': 2, '특성': '팽창', '희생 여부': '가능'},
               '마스터 블린': {'비용': ['보석', ['사파이어', '에메랄드']], '공격력': 0, '체력': 4, '특성': '진정한 학자', '희생 여부': '가능'},
               '마스터 고란즈': {'비용': ['보석', ['루비', '에메랄드']], '공격력': 2, '체력': 6, '특성': '보석 의존증', '희생 여부': '가능'},
               '마스터 오를루': {'비용': ['보석', ['루비', '사파이어']], '공격력': 1, '체력': 1, '특성': ['비행', '약탈자'], '희생 여부': '가능'}}
match_ready_list = ['', '', '', '']
match_battle_list = ['', '', '', '']
player_battle_list = ['', '', '', '']
hand = []
my_health = 5

# 플레이어의 진행 목록
deck = []
collection = defaultdict(int)
hoil = 0
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
for i in animal_card_normal + animal_card_rare + machine_card_normal + machine_card_rare + ghost_card_normal + \
         ghost_card_rare + magic_card_normal + magic_card_rare:
    collection[i] = 0


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


def mox_search():
    if '루비 목스' in player_battle_list and '루비' not in gem or '고란즈의 목스' in player_battle_list and '루비' not in gem \
            or '오를루의 목스' in player_battle_list and '루비' not in gem or '위대한 목스' in player_battle_list and '루비' \
            not in gem:
        gem.append('루비')
    if '사파이어 목스' in player_battle_list and '사파이어' not in gem or '블린의 목스' in player_battle_list and '사파이어' not \
            in gem or '오를루의 목스' in player_battle_list and '사파이어' not in gem or '위대한 목스' in player_battle_list and\
            '사파이어' not in gem:
        gem.append('사파이어')
    if '에메랄드 목스' in player_battle_list and '에메랄드' not in gem or '블린의 목스' in player_battle_list and '에메랄드' not \
            in gem or '고란즈의 목스' in player_battle_list and '에메랄드' not in gem or '위대한 목스' in player_battle_list and\
            '에메랄드' not in gem:
        gem.append('에메랄드')


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
    mox_search()
    global energy
    global bone
    global gem
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
        elif cards_kinds[set_card]['비용'][0] == '보석':
            need_gem = [cards_kinds[set_card]['비용'][1] for i in range(len(cards_kinds[set_card]['비용']))]
            if '루비' in gem:
                need_gem.remove('루비')
            if '사파이어' in gem:
                need_gem.remove('사파이어')
            if '에메랄드' in gem:
                need_gem.remove('에메랄드')
            if need_gem != []:
                print('필요한 보석이 없습니다.')

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


def match_set():
    print_battle_plate()
    set_card = input('대기할 카드를 입력하세요.(카드 이름)')
    card_space = int(input('놓을 자리를 입력하세요.(1, 2, 3, 4)'))
    match_ready_list[card_space-1] = set_card
    print_battle_plate()


def card_attack():
    global my_health
    global bone
    global hoil
    for i in range(4):
        if player_battle_list[i] != '':
            # 상대편에 카드가 없을 때 내 카드의 공격력만큼 체력 회복
            if match_battle_list[i] == '':
                my_health += cards_kinds[player_battle_list[i]]['공격력']
            # 상대 편에 카드가 있을 때 해당 카드의 체력을 내 카드의 공격력만큼 감소, 0이 되면 사망
            elif match_battle_list[i] != '':
                cards_kinds[match_battle_list[i]]['체력'] += cards_kinds[player_battle_list[i]]['공격력']
                if cards_kinds[match_battle_list[i]]['체력'] <= 0:
                    match_battle_list.remove(match_battle_list[i])
                    if cards_kinds[match_battle_list[i]]['특성'] == '골왕':
                        bone += 4
                    else:
                        bone += 1
            else:
                pass

                # if my_health <= 10:
                #     print('승리!')
                #     if my_health < 10:
                #         hoil += my_health - 10
