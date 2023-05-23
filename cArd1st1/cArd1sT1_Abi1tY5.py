import random as r
cards_kinds = {'거대 크라켄': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': '크라켄 잠수', '희생 여부': '가능'},
               '거울 촉수': {'비용': ['피', 1], '공격력': ['ㄱㅓㅇㅜㄹㅜㅇㅓㄱ', 0], '체력': 3, '특성': '없음', '희생 여부': '가능'},
               '종 촉수': {'비용': ['피', 2], '공격력': ['타종수', 0], '체력': 3, '특성': '없음', '희생 여부': '가능'},
               '패 촉수': {'비용': ['피', 1], '공격력': ['카드 세는 자', 0], '체력': 1, '특성': '없음', '희생 여부': '가능'},
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


def abilty_growth(set_card):
    if set_card == '아기 늑대':
        set_card = ['늑대', cards_kinds['늑대']['공격력'], set_card[2] + cards_kinds['늑대']['체력']]
    elif set_card == '새끼 무스':
        set_card = ['무스', cards_kinds['무스']['공격력'], set_card[2] + cards_kinds['무스']['체력']]
    elif set_card == '석관':
        set_card = ['미라 제왕', cards_kinds['미라 제왕']['공격력'], set_card[2] + cards_kinds['미라 제왕']['체력']]
    return set_card


def my_turn_change(bone, player_battle_list):
    for i in range(4):
        if player_battle_list[i] != '':
            if cards_kinds[player_battle_list[i]]['특성'] == '뼈 채굴자':
                bone += 1
            if cards_kinds[player_battle_list[i]]['특성'] == '성장':
                player_battle_list[i] = abilty_growth(player_battle_list[i])
    return bone, player_battle_list


def match_turn_change(match_battle_list):
    for i in range(4):
        if match_battle_list[i] != '':
            if cards_kinds[match_battle_list[i]]['특성'] == '성장':
                match_battle_list[i] = abilty_growth(match_battle_list[i])
    return match_battle_list