import random as r

class Cards:
    def __init__(self, name, price, attack, health, attribute, bloody):
        self.name = name
        self.price = price
        self.attack = attack
        self.health = health
        self.attribute = attribute
        self.bloody = bloody



cards = {'강철 덫': Cards('강철 덫', '없음', 0, 5, ['강철 덫', '굴살이'], False),
         '거대 크라켄': Cards('거대 크라켄', ['피', 1], 1, 1, '크라켄 잠수', True),
         '거울 촉수': Cards('거울 촉수', ['피', 1], 'ㄱㅓㅇㅜㄹㅜㅇㅓㄱ', 3, '크라켄 잠수', True),
         '패 촉수': Cards('패 촉수', ['피', 1], '카드 세는 자', 1, '크라켄 잠수', True),
         '종 촉수': Cards('종 촉수', ['피', 2], '타종수', 3, '크라켄 잠수', True),
         '고양이': Cards('고양이', ['피', 1], 0, 1, '많은 목숨', True),
         '언데드 고양이': Cards('언데드 고양이', ['피', 1], 3, 6, '없음', True),
         '늑대': Cards('늑대', ['피', 2], 3, 2, '없음', True),
         '아기 늑대': Cards('아기 늑대', ['피', 1], 1, 1, '성장', True),
         '다람쥐': Cards('다람쥐', '없음', 0, 1, '없음', True),
         '다람쥐 공': Cards('다람쥐 공', ['피', 1], 0, 1, '다람쥐 분만', True),
         '담비': Cards('담비', ['피', 1], 1, 2, '없음', True),
         '두더지': Cards('두더지', ['피', 1], 0, 4, '굴살이', True),
         '두더지인간': Cards('두더지인간', ['피', 1], 0, 6, ['굴살이', '비행 방어'], True),
         '들쥐': Cards('들쥐', ['피', 2], 2, 2, '생식력', True),
         '무스': Cards('무스', ['피', 2], 2, 4, '이동', True),
         '새끼 무스': Cards('새끼 무스', ['피', 1], 1, 1, ['이동', '성장'], True),
         '물총새': Cards('물총새', ['피', 2], 1, 1, ['잠수', '비행'], True),
         '매': Cards('매', ['피', 2], 3, 1, '비행', True),
         '블러드하운드': Cards('블러드하운드', ['피', 2], 2, 3, '수호자', True),
         '사마귀신': Cards('사마귀신', ['피', 1], 1, 1, '삼분공격', True),
         '연어': Cards('연어', ['피', 2], 2, 2, ['잠수', '이동'], True),
         '우라율리': Cards('우라율리', ['피', 4], 7, 7, '없음', True),
         '우로보로스': Cards('우로보로스', ['피', 2], uroboros_power, uroboros_power, '불사', True),
         '전기뱀장어': Cards('전기뱀장어', ['피', 1], 1, 1, ['잠수', '배터리 운반자', True),
         '큰까마귀': Cards('큰까마귀', ['피', 2], 2, 3, '비행', True),
         '큰까마귀 알': Cards('큰까마귀', ['피', 1], 0, 2, '성장', True),
         '토끼': Cards('토끼', '없음', 0, 1, '삼분공격', True),
         '토끼굴': Cards('토끼굴', ['피', 1], 0, 3, '토끼굴', False),
         '포자쥐': Cards('포자쥐', ['피', 2], 2, 2, ['생식력', '생식력'], True),
         '황소개구리': Cards('황소개구리', ['피', 1], 1, 2, '비행 방어', True),
         '회색곰': Cards('회색곰', ['피', 3], 4, 6, '없음', True),
         '감시 드론': Cards('감시 드론', ['에너지', 1], 0, 1, '보초', True),
         '감시 포자': Cards('감시 포자', ['에너지', 1], 0, 1, ['보초', '보초'], True),
         '무효화 전도체': Cards('무효화 전도체', ['에너지', 1], 0, 1, '무효화 전도체', True),
         'L33pB0t': Cards('L33pB0t', ['에너지', 1], 0, 2, '비행 방어', True),
         '고GI봇': Cards('고GI봇', ['에너지', 2], 0, 1, '고귀한 희생', True),
         '버프 전도체': Cards('버프 전도체', ['에너지', 2], 0, 2, '공격 전도', True),
         '봄버봇': Cards('봄버봇', ['에너지', 2], 1, 1, '폭탄', True),
         '에너지봇': Cards('에너지봇', ['에너지', 2], 0, 1, '배터리 운반자', True),
         '49er': Cards('49er', ['에너지', 2], 1, 1, '이동', True),
         '곤충 드론': Cards('곤충 드론', ['에너지', 3], 1, 1, '비행', True),
         '공장 전도체': Cards('공장 전도체', ['에너지', 3], 0, 2, '생산 전도체', True),
         '목스 모듈': Cards('목스 모듈', ['에너지', 3], 0, 2, '위대한 목스', True),
         '에너지 전도체': Cards('에너지 전도체', ['에너지', 3], 1, 2, '발전 전도체', True),
         '자동 장치': Cards('자동 장치', ['에너지', 3], 1, 1, '없음', True),
         '폭탄 부인': Cards('폭탄 부인', ['에너지', 3], 1, 2, '폭탄 바주카', True),
         '곡선넘이': Cards('곡선넘이', ['에너지', 4], 2, 3, '없음', True),
         '두꺼운 드로이드': Cards('두꺼운 드로이드', ['에너지', 5], 1, 3, '없음', True),
         '피버봇': Cards('L33pB0t', ['에너지', 5], 0, 2, '전기 주사위', True),
         '사진충': Cards('L33pB0t', ['에너지', 5], 1, 1, ['보초', '즉사'], True),
         '더블 거너': Cards('L33pB0t', ['에너지', 6], 2, 1, '이분공격', True),
         '볼트하운드': Cards('L33pB0t', ['에너지', 6], 2, 2, '수호자', True),
         '스팀봇': Cards('L33pB0t', ['에너지', 6], 2, 2, '없음', True),
         '해골': Cards('해골', '없음', 0, 1, '', True),
         '뼈 무더기': Cards('뼈 무더기', '없음', 0, 1, '', True),
         '드라우그르': Cards('드라우그르', ['뼈', 1], 0, 1, '', True),
         '뼈 굴착자': Cards('뼈 굴착자', ['뼈', 1], 0, 3, '', True),
         '포자굴착자': Cards('포자굴착자', ['뼈', 1], 0, 3, '', True),
         '도굴꾼': Cards('도굴꾼', ['뼈', 2], 0, 2, '', True),
         '망령': Cards('망령', ['뼈', 2], 3, 1, '', True),
         '밴시': Cards('밴시', ['뼈', 2], 1, 1, '', True),
         '뼈 마법사': Cards('뼈 마법사', ['뼈', 2], 4, 1, '', True),
         '좀비': Cards('좀비', ['뼈', 2], 1, 1, '', True),
         '네크로맨서': Cards('네크로맨서', ['뼈', 3], 1, 2, '', True),
         '부서진 은화(왼쪽)': Cards('부서진 은화(왼쪽)', ['뼈', 3], 0, 2, '', True),
         '부서진 은화(오른쪽)': Cards('부서진 은화(오른쪽)', ['뼈', 3], 0, 2, '', True),
         '뼈의 왕의 뿔피리': Cards('뼈의 왕의 뿔피리', ['뼈', 3], 1, 1, '', True),
         '석관': Cards('석관', ['뼈', 4], 0, 2, '', True),
         '유령선': Cards('유령선', ['뼈', 4], 0, 1, '', True),
         '익사한 영혼': Cards('익사한 영혼', ['뼈', 4], 1, 1, '', True),
         '워커즈': Cards('워커즈', ['뼈', 4], 1, 2, '', True),
         '죽은 손': Cards('죽은 손', ['뼈', 5], 1, 1, '', True),
         '프랭크 & 스타인': Cards('프랭크 & 스타인', ['뼈', 5], 2, 2, '', True),
         '파라오의 애완동물': Cards('파라오의 애완동물', ['뼈', 6], 0, 2, '', True),
         '본하운드': Cards('본하운드', ['뼈', 7], 2, 3, '', True),
         '미라 제왕': Cards('미라 제왕', ['뼈', 8], 3, 3, '', True),
         '목 없는 기사': Cards('목 없는 기사', ['뼈', 13], 5, 5, '', True)
         }


cards_kinds = {'강철 덫': {'비용': '없음', '공격력': 0, '체력': 5, '특성': ['강철 덫', '굴살이'], '희생 여부': '가능'},
               '거대 크라켄': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': '크라켄 잠수', '희생 여부': '가능'},
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
               '들쥐': {'비용': ['피', 2], '공격력': 2, '체력': 2, '특성': '생식력', '희생 여부': '가능'},
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
               '알파': {'비용': ['피', 1], '공격력': 1, '체력': 2, '특성': '리더', '희생 여부': '가능'},
               '연어': {'비용': ['피', 2], '공격력': 2, '체력': 2, '특성': ['잠수' , '이동'], '희생 여부': '가능'},
               '우라율리': {'비용': ['피', 4], '공격력': 7, '체력': 7, '특성': '없음', '희생 여부': '가능'},
               '우로보로스': {'비용': ['피', 2], '공격력': 1, '체력': 1, '특성': '불사', '희생 여부': '가능'},
               '전기뱀장어': {'비용': ['피', 1], '공격력': 1, '체력': 1, '특성': ['잠수', '배터리 운반자'], '희생 여부': '가능'},
               '코요테': {'비용': ['피', 1], '공격력': 2, '체력': 1, '특성': '없음', '희생 여부': '가능'},
               '큰까마귀': {'비용': ['피', 2], '공격력': 2, '체력': 3, '특성': '비행', '희생 여부': '가능'},
               '큰까마귀 알': {'비용': ['피', 1], '공격력': 0, '체력': 2, '특성': '없음', '희생 여부': '가능'},
               '포자쥐': {'비용': ['피', 2], '공격력': 2, '체력': 2, '특성': ['생식력', '생식력'], '희생 여부': '가능'},
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
               '피버봇': {'비용': ['에너지', 5], '공격력': 0, '체력': 2, '특성': '전기 주사위', '희생 여부': '가능'},
               '사진충': {'비용': ['에너지', 5], '공격력': 1, '체력': 1, '특성': ['보초', '즉사'], '희생 여부': '가능'},
               '더블 거너': {'비용': ['에너지', 6], '공격력': 2, '체력': 1, '특성': '이분공격', '희생 여부': '가능'},
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
               '뼈의 왕의 뿔피리': {'비용': ['뼈', 3], '공격력': 1, '체력': 1, '특성': '뼈 프린터', '희생 여부': '가능'},
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
               '자극 마법사': {'비용': ['보석', '에메랄드'], '공격력': 0, '체력': 1, '특성': '자극', '희생 여부': '가능'},
               '미식 마법사': {'비용': ['보석', '에메랄드'], '공격력': 0, '체력': 2, '특성': '팽창', '희생 여부': '가능'},
               '마스터 블린': {'비용': ['보석', ['사파이어', '에메랄드']], '공격력': 0, '체력': 4, '특성': '진정한 학자', '희생 여부': '가능'},
               '마스터 고란즈': {'비용': ['보석', ['루비', '에메랄드']], '공격력': 2, '체력': 6, '특성': '보석 의존증', '희생 여부': '가능'},
               '마스터 오를루': {'비용': ['보석', ['루비', '사파이어']], '공격력': 1, '체력': 1, '특성': ['비행', '약탈자'], '희생 여부': '가능'}}


uroboros_power = 1


def abilty_growth(set_card):
    if set_card == '아기 늑대':
        set_card = ['늑대', cards_kinds['늑대']['공격력'], set_card[2] + cards_kinds['늑대']['체력']]
    elif set_card == '새끼 무스':
        set_card = ['무스', cards_kinds['무스']['공격력'], set_card[2] + cards_kinds['무스']['체력']]
    elif set_card == '석관':
        set_card = ['미라 제왕', cards_kinds['미라 제왕']['공격력'], set_card[2] + cards_kinds['미라 제왕']['체력']]
    return set_card


def player_change_attack(player_battle_list, match_battle_list):
    for i in player_battle_list:
        if type(i) == list:
            if cards_kinds[i[0]]['특성'] == '구린내' and match_battle_list[i][1] <= 1:
                match_battle_list[i][1] -= 1
            elif cards_kinds[i[0]]['특성'] == '리더':
                try:
                    player_battle_list[i-1][1] += 1
                except:
                    pass
                try:
                    player_battle_list[i+1][1] += 1
                except:
                    pass
            elif cards_kinds[i[0]]['특성'] == '목스 전원':
                for j in player_battle_list:
                    if cards_kinds[i]['특성'] == '루비 목스' or cards_kinds[i]['특성'] == '사파이어 목스' or cards_kinds[i]['특성'] == '에메랄드 목스' or cards_kinds[i]['특성'] == '위대한 목스':
                        j[1] += 1
        elif type(i) == str:
            continue
    return player_battle_list, match_battle_list


def match_change_attack(player_battle_list, match_battle_list):
    for i in match_battle_list:
        if cards_kinds[i]['특성'] == '구린내' and player_battle_list[i][1] <= 1:
            player_battle_list[i][1] -= 1
        elif cards_kinds[i]['특성'] == '리더':
            try:
                match_battle_list[i-1][1] += 1
            except:
                pass
            try:
                match_battle_list[i+1][1] += 1
            except:
                pass
        elif cards_kinds[i]['특성'] == '목스 전원':
            for j in match_battle_list:
                if cards_kinds[i]['특성'] == '루비 목스' or cards_kinds[i]['특성'] == '사파이어 목스' or cards_kinds[i]['특성'] == '에메랄드 목스' or cards_kinds[i]['특성'] == '위대한 목스':
                    j[1] += 1
    return player_battle_list, match_battle_list


def my_turn_change(bone, player_battle_list):
    for i in range(4):
        if player_battle_list[i] != '':
            player_ability = cards_kinds[player_battle_list[i][0]]['특성']
            if player_ability == '뼈 채굴자':
                bone += 1
            elif player_ability == '성장':
                player_battle_list[i] = abilty_growth(player_battle_list[i])
            elif player_ability == '크라켄 잠수':
                tentacles = r.choice(['거울 촉수', '종 촉수', '패 촉수'])
                player_battle_list[i] = [tentacles, cards_kinds[tentacles][1], cards_kinds[tentacles][2]]
    return bone, player_battle_list


def match_turn_change(match_battle_list):
    for i in range(4):
        if match_battle_list[i] != '':
            if cards_kinds[match_battle_list[i]]['특성'] == '성장':
                match_battle_list[i] = abilty_growth(match_battle_list[i])
    return match_battle_list


def player_conducting(player_battle_list, energy, max_energy):
    conductor = ['공격 전도체', '무효화 전도체', '생산 전도체', '에너지 전도체']
    conductor_where = []
    conductor_what = []
    for i in range(4):
        if player_battle_list[i] == '':
            continue
        elif cards_kinds[player_battle_list[i][0]]['특성'] in conductor and len(conductor_where) < 2:
            conductor_where.append(i)
            conductor_what.append(cards_kinds[player_battle_list[i][0]]['특성'])
            for i in player_battle_list[conductor_where[0]:conductor_where[1]+1]:
                if i == '':
                    if '생산 전도체' in conductor_what:
                        i = ['L33pB0t', cards_kinds['L33pB0t']['공격력'], cards_kinds['L33pB0t']['체력']]
                elif i != '':
                    if '공격 전도체' in conductor_what:
                        i[1] += 1
                    elif '무효화 전도체' in conductor_what:
                        pass
                    elif '에너지 전도체' in conductor_what:
                        energy = max_energy
    return player_battle_list, energy, max_energy


def match_conducting(match_battle_list, energy, max_energy):
    conductor = ['공격 전도체', '무효화 전도체', '생산 전도체', '에너지 전도체']
    conductor_where = []
    conductor_what = []
    for i in range(4):
        if match_battle_list[i] == '':
            continue
        elif cards_kinds[match_battle_list[i]]['특성'] in conductor and len(conductor_where) <= 2:
            conductor_where.append(i)
            conductor_what.append(cards_kinds[match_battle_list[i][0]]['특성'])
            for i in match_battle_list[conductor_where[0]:conductor_where[1]+1]:
                if i == '':
                    if '생산 전도체' in conductor_what:
                        i = ['L33pB0t', cards_kinds['L33pB0t']['공격력'], cards_kinds['L33pB0t']['체력']]
                elif i != '':
                    if '공격 전도체' in conductor_what:
                        i[1] += 1
                    elif '무효화 전도체' in conductor_what:
                        pass
                    elif '에너지 전도체' in conductor_what:
                        energy = max_energy
    return match_battle_list, energy, max_energy


def my_mox_search(gem, player_battle_list):
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
    return gem


def match_mox_search(gem, match_battle_list):
    if '루비 목스' in match_battle_list and '루비' not in gem or '고란즈의 목스' in match_battle_list and '루비' not in gem \
            or '오를루의 목스' in match_battle_list and '루비' not in gem or '위대한 목스' in match_battle_list and '루비' \
            not in gem:
        gem.append('루비')
    if '사파이어 목스' in match_battle_list and '사파이어' not in gem or '블린의 목스' in match_battle_list and '사파이어' not \
            in gem or '오를루의 목스' in match_battle_list and '사파이어' not in gem or '위대한 목스' in match_battle_list and\
            '사파이어' not in gem:
        gem.append('사파이어')
    if '에메랄드 목스' in match_battle_list and '에메랄드' not in gem or '블린의 목스' in match_battle_list and '에메랄드' not \
            in gem or '고란즈의 목스' in match_battle_list and '에메랄드' not in gem or '위대한 목스' in match_battle_list and\
            '에메랄드' not in gem:
        gem.append('에메랄드')
    return gem


def print_battle_plate(match_ready_list, match_battle_list, player_battle_list):
    print(match_ready_list)
    print(match_battle_list)
    print(player_battle_list)


def draw(battle_deck, hand):
    drawed_card = r.choice(battle_deck)
    battle_deck.remove(drawed_card)
    hand.append(drawed_card)
    return battle_deck, hand


def start_draw(battle_deck, hand):
    for i in range(3):
        battle_deck, hand = draw(battle_deck, hand)
    return battle_deck, hand


def card_set(hand, energy, max_energy, bone, gem, match_ready_list, match_battle_list, player_battle_list, battle_deck):
    print(f'에너지: {energy}, 뼈: {bone}, 보석: {gem}')
    print(*hand)
    can_place = True

    # 비용 처리
    while True:
        if not hand:
            print('너의 손에는 아무것도 없다.')
            return hand, energy, max_energy, bone, player_battle_list, match_battle_list, battle_deck
        set_card = input("놓을 카드를 입력하세요.(카드 이름) 턴 넘길 땐 '1'을 입력.")
        if set_card == '1':
            return hand, energy, max_energy, bone, player_battle_list, match_battle_list, battle_deck
        elif set_card not in hand:
            print('그런 이름의 카드는 없다.')
            continue
        else:
            if cards_kinds[set_card]['비용'] != '없음':
                # 비용이 피일 때
                if cards_kinds[set_card]['비용'][0] == '피':
                    need_blood = cards_kinds[set_card]['비용'][1]
                    blood_card_list = player_battle_list
                    can_be_blood = 0
                    for i in range(4):
                        if blood_card_list[i] != '':
                            if cards_kinds[blood_card_list[i]]['희생 여부'] == '다중' or \
                               cards_kinds[blood_card_list[i]]['희생 여부'] == '가능':
                                can_be_blood += 1
                            elif cards_kinds[blood_card_list[i]]['희생 여부'] == '불가능':
                                can_place = False
                    if can_be_blood >= need_blood:
                        while need_blood > 0:
                            print(blood_card_list)
                            blood_card = int(input('희생할 카드의 자리를 입력하세요.(1, 2, 3, 4)'))
                            if blood_card_list[blood_card-1] != '':
                                if cards_kinds[blood_card_list[blood_card-1]]['희생 여부'] == '다중':
                                    need_blood -= 1
                                elif cards_kinds[blood_card_list[blood_card-1]]['희생 여부'] == '가능':
                                    if cards_kinds[blood_card_list[blood_card - 1]]['특성'] == '고귀한 희생':
                                        need_blood -= 2
                                    need_blood -= 1
                                    player_battle_list[blood_card-1] = ''
                                    bone += 1
                                elif cards_kinds[blood_card_list[blood_card-1]]['희생 여부'] == '불가능':
                                    print('이 카드는 희생할 수 없습니다.')
                                    blood_card_list.remove(blood_card-1)
                            else:
                                print('그곳엔 희생할 것이 없다.')
                        break
                    else:
                        print('그것을 내기 위한 피가 부족하다.')
                        return energy, bone, player_battle_list
                # 비용이 에너지일 때
                elif cards_kinds[set_card]['비용'][0] == '에너지':
                    if energy >= cards_kinds[set_card]['비용'][1]:
                        energy -= cards_kinds[set_card]['비용'][1]
                        print(f'에너지: {energy}')
                    else:
                        print('이봐. 너 지금 에너지 부족한 거 안 보여?')
                        can_place = False
                # 비용이 뼈일 때
                elif cards_kinds[set_card]['비용'][0] == '뼈':
                    if bone >= cards_kinds[set_card]['비용'][1]:
                        bone -= cards_kinds[set_card]['비용'][1]
                        print(f'뼈: {bone}')
                    else:
                        print('그것을 내기 위한 뼈가 부족하구나.')
                        can_place = False
                # 비용이 보석일 때
                elif cards_kinds[set_card]['비용'][0] == '보석':
                    can_place_gem = True
                    print(f'보석: {gem}')
                    need_gem = [cards_kinds[set_card]['비용'][1] for _ in range(len(cards_kinds[set_card]['비용'][1]))]
                    if '루비' in need_gem and '루비' in gem:
                        need_gem.remove('루비')
                    elif '사파이어' in need_gem and '사파이어' in gem:
                        need_gem.remove('사파이어')
                    elif '에메랄드' in need_gem and '에메랄드' in gem:
                        need_gem.remove('에메랄드')
                    else:
                        for i in range(len(cards_kinds[set_card]['비용'][1])):
                            if need_gem[i] not in gem:
                                can_place_gem = False
                                can_place = False
                    if not can_place_gem:
                        print('그것에 필요한 보석이 없다.')
        break

    # 놓을 자리 처리
    if can_place:
        while True:
            print_battle_plate(match_ready_list, match_battle_list, player_battle_list)
            card_space = int(input('놓을 자리를 입력하세요.(1, 2, 3, 4)'))
            # 자리 교정
            if card_space < 1 or card_space > 4:
                print('정확한 자리를 입력하세요.')
                continue
            # 이미 있음
            elif player_battle_list[card_space-1] != '':
                print('이미 카드가 그 자리에 있습니다.')
                continue
            # 소환 성공 시
            elif player_battle_list[card_space-1] == '':
                player_battle_list[card_space-1] = [set_card, cards_kinds[set_card]['공격력'], cards_kinds[set_card]['체력']]
                hand.remove(set_card)
            # 소환 시 발동하는 특성
            for i in range(4):   # 수호자
                if cards_kinds[set_card]['특성'] == '수호자' and match_battle_list[card_space-1] == '':
                    player_battle_list[card_space-1] = match_battle_list[card_space-1]
                    match_battle_list[i] = ''
            if cards_kinds[set_card]['특성'] == '보석 의존증':
                if not gem or cards_kinds[set_card]['비용'] not in gem:
                    set_card = ''
                    bone += 1
            if cards_kinds[set_card]['특성'] == '보초':
                if match_battle_list[card_space-1] != '':
                    if match_battle_list[card_space-1][2] >= 1:
                        match_battle_list[card_space-1][2] -= 1
                    else:
                        match_battle_list[card_space-1] = ''
            if cards_kinds[set_card]['특성'] == '배터리 운반자':
                max_energy += 1
                energy += 1
            if cards_kinds[set_card]['특성'] == '손재주':
                hand = []
                battle_deck, hand = start_draw(battle_deck, hand)
                battle_deck, hand = draw(battle_deck, hand)
            if cards_kinds[set_card]['특성'] == '심리적 뵤기':
                moxes = 0
                for i in range(len(hand)):
                    if hand[i] == '루비 목스' or hand[i] == '사파이어 목스' or hand[i] == '에메랄드 목스' or \
                        hand[i] == '블린의 목스' or hand[i] == '고란즈의 목스' or hand[i] == '오를루의 목스' or \
                        hand[i] == '마그누스 목스':
                        moxes += 1
                for i in range(moxes):
                    battle_deck, hand = draw(battle_deck, hand)
            if cards_kinds[set_card]['특성'] == '생식력':
                hand.append('들쥐')
            if cards_kinds[set_card]['특성'] == '폭탄 바주카':
                for i in range(4):
                    if player_battle_list[i] == '':
                        player_battle_list[i] = ['봄버봇', cards_kinds['봄버봇']['공격력'], cards_kinds['봄버봇']['체력']]
                for i in range(4):
                    if match_battle_list[i] == '':
                        match_battle_list[i] = ['봄버봇', cards_kinds['봄버봇']['공격력'], cards_kinds['봄버봇']['체력']]
    print(f'에너지: {energy}, 뼈: {bone}, 보석: {gem}')
    print_battle_plate(match_ready_list, match_battle_list, player_battle_list)
    return hand, energy, max_energy, bone, player_battle_list, match_battle_list, battle_deck


def match_set(bone, gem, match_ready_list, match_battle_list, player_battle_list):
    print_battle_plate(match_ready_list, match_battle_list, player_battle_list)
    set_card = input('대기할 카드를 입력하세요.(카드 이름)')
    card_space = int(input('놓을 자리를 입력하세요.(1, 2, 3, 4)'))
    if set_card in cards_kinds.keys():
        if cards_kinds[set_card]['특성'] == '보석 의존증':
            if not gem or cards_kinds[set_card]['비용'] not in gem:
                set_card = ''
        if cards_kinds[set_card]['특성'] == '보초':
            if player_battle_list[card_space - 1] != '':
                if player_battle_list[card_space - 1][1] > 1:
                    player_battle_list[card_space - 1][2] -= 1
                else:
                    player_battle_list[card_space - 1] = ''
        if cards_kinds[set_card]['특성'] == '폭탄 바주카':
            for i in range(4):
                if player_battle_list[i] == '':
                    player_battle_list[i] = ['봄버봇', cards_kinds['봄버봇']['공격력'], cards_kinds['봄버봇']['체력']]
            for i in range(4):
                if match_battle_list[i] == '':
                    match_battle_list[i] = ['봄버봇', cards_kinds['봄버봇']['공격력'], cards_kinds['봄버봇']['체력']]
    match_ready_list[card_space-1] = [set_card, cards_kinds[set_card]['공격력'], cards_kinds[set_card]['체력']]
    print_battle_plate(match_ready_list, match_battle_list, player_battle_list)
    return bone, match_ready_list


def player_unauto_abilty(player_battle_list, battle_deck, hand, energy, bone, gem):
    unauto_abiltys = ['도굴', '뼈 프린터', '자극', '진정한 학자', '팽창']
    player_unauto_abiltys = []
    for i in player_battle_list:
        if cards_kinds[i]['특성'] in unauto_abiltys:
            player_unauto_abiltys.append(cards_kinds[i]['특성'])

    player_unauto = input(f'발동 가능한 특성 = {player_unauto_abiltys}')
    if player_unauto == '도굴' and player_unauto in player_unauto_abiltys and bone <= 1:
        bone -= 1
        hand.append('해골')
    elif player_unauto == '뼈 프린터' and player_unauto in player_unauto_abiltys and energy <= 1:
        energy -= 1
        bone += 1
    elif player_unauto == '자극' and player_unauto in player_unauto_abiltys and energy <= 3:
        energy -= 3
        for i in player_battle_list:
            if i[0] == '자극 마법사':
                i[1] += 1
                i[2] += 1
    elif player_unauto == '진정한 학자' and player_unauto in player_unauto_abiltys and '사파이어' in gem:
        player_battle_list.remove('마스터 블린')
        draw(battle_deck, hand)
    elif player_unauto == '팽창' and player_unauto in player_unauto_abiltys and bone <= 2:
        bone -= 2
        for i in player_battle_list:
            if i[0] == '팽창 마법사':
                i[1] += 1
                i[2] += 1
    elif player_unauto == '전기 주사위' and player_unauto in player_unauto_abiltys and energy <= 1:
        energy -= 1
        for i in player_battle_list:
            if i[0] == '피버봇':
                i[1] += r.randint(1, 6)
    return player_battle_list, battle_deck, hand, energy, bone, gem


def card_attack(hand, bone, my_health, match_battle_list, player_battle_list, all_cards):
    attack_moves = ['다람쥐 분만', '밀치기', '이동', '해골 선원']
    for i in range(4):
        if player_battle_list[i] != '':
            player_abilty = cards_kinds[player_battle_list[i][0]]['특성']
        if match_battle_list[i] != '':
            match_abilty = cards_kinds[match_battle_list[i][0]]['특성']

        if player_battle_list[i] != '':
            player_abilty = cards_kinds[player_battle_list[i][0]]['특성']
            match_abilty = cards_kinds[match_battle_list[i][0]]['특성']
            # 특수 공격력
            if isinstance(cards_kinds[player_battle_list[i][0]]['공격력'], list):
                if player_battle_list[i][1][0] == 'ㄱㅓㅇㅜㄹㅜㅇㅓㄱ':
                    player_battle_list[i][1][1] = match_battle_list[i][1]
                elif player_battle_list[i][1][0] == '카드 세는 자':
                    player_battle_list[i][1][1] = len(hand)
                elif player_battle_list[i][1][0] == '타종수':
                    player_battle_list[i][1][1] = 4-i
            # 상대 편에 카드가 없을 때 내 카드의 공격력만큼 체력 회복 (+약탈자)(+굴살이)
            if match_battle_list[i] == '':
                if player_abilty == '약탈자':
                    hand.append(r.choice(all_cards))
                for j in range(4):
                    if '굴살이' in player_abilty and player_battle_list[j] == '':
                        player_battle_list[j] = player_battle_list[i]
                        player_battle_list[i] = ''
                else:
                    my_health += player_battle_list[i][1]
            # 다른 특성들
            elif match_battle_list[i] != '':
                # 특성 파뤼
                if player_abilty == '비행':
                    if cards_kinds[match_battle_list[i]]['특성'] == '비행 방어':
                        match_battle_list[i][2] -= player_battle_list[i][1]
                    else:
                        if cards_kinds[player_battle_list[i]]['특성'] == '약탈자':
                            hand.append(r.choice(all_cards))
                elif player_abilty == '잠수' or player_abilty == '크라켄 잠수':
                    my_health += match_battle_list[i][1]
                elif player_abilty == '즉사':
                    match_battle_list[i] = ''
                    bone += 1
                elif player_abilty == '이분공격':
                    try:
                        match_battle_list[i-1][2] -= player_battle_list[i][1]
                    except:
                        continue
                    try:
                        match_battle_list[i+1][2] -= player_battle_list[i][1]
                    except:
                        continue
                elif player_abilty == '삼분공격':
                    try:
                        match_battle_list[i-1][2] -= player_battle_list[i][1]
                    except:
                        continue
                    match_battle_list[i][2] -= player_battle_list[i][1]
                    try:
                        match_battle_list[i+1][2] -= player_battle_list[i][1]
                    except:
                        continue
                elif match_abilty == '강철 덫':
                    player_battle_list[i] = ''
                    bone += 1
                elif match_abilty == '루비 심장':
                    match_battle_list[i] = ['루비 목스', cards_kinds['루비 목스']['공격력'], cards_kinds['루비 목스']['체력']]
                elif match_abilty == '가시':
                    player_battle_list[i][2] -= 1
                elif match_abilty == '역겨움':
                    player_battle_list[i][2] -= 0
                # 데미지 계산
                else:
                    # 체력 계산
                    match_battle_list[i][2] -= player_battle_list[i][1]
                    # 이동 특성
                    if cards_kinds[i]['특성'] in attack_moves:
                        move_direction = r.choice(['left', 'right'])
                        if cards_kinds[i]['특성'] == '다람쥐 분만':
                            if move_direction == 'left':
                                if player_battle_list[i-1] == '':
                                    player_battle_list[i-1] = player_battle_list[i]
                                    player_battle_list[i] = ['다람쥐', cards_kinds['다람쥐']['공격력'], cards_kinds['다람쥐']['체력']]
                                elif player_battle_list[i - 1] == '':
                                    player_battle_list[i+1] = player_battle_list[i]
                                    player_battle_list[i] = ['다람쥐', cards_kinds['다람쥐']['공격력'], cards_kinds['다람쥐']['체력']]
                                else:
                                    pass
                            elif move_direction == 'right':
                                if player_battle_list[i+1] == '':
                                    player_battle_list[i+1] = player_battle_list[i]
                                    player_battle_list[i] = ['다람쥐', cards_kinds['다람쥐']['공격력'], cards_kinds['다람쥐']['체력']]
                                elif player_battle_list[i+1] == '':
                                    player_battle_list[i-1] = player_battle_list[i]
                                    player_battle_list[i] = ['다람쥐', cards_kinds['다람쥐']['공격력'], cards_kinds['다람쥐']['체력']]
                                else:
                                    pass
                        elif cards_kinds[i]['특성'] == '이동':
                            if move_direction == 'left':
                                if player_battle_list[i-1] == '':
                                    player_battle_list[i-1] = player_battle_list[i]
                                    player_battle_list[i] = ''
                                elif player_battle_list[i-1] != '':
                                    player_battle_list[i+1] = player_battle_list[i]
                                    player_battle_list[i] = ''
                                else:
                                    pass
                            elif move_direction == 'right':
                                if player_battle_list[i+1] == '':
                                    player_battle_list[i+1] = player_battle_list[i]
                                    player_battle_list[i] = ''
                                elif player_battle_list[i+1] != '':
                                    player_battle_list[i-1] = player_battle_list[i]
                                    player_battle_list[i] = ''
                                else:
                                    pass
                        elif cards_kinds[i]['특성'] == '해골 선원':
                            if move_direction == 'left':
                                if player_battle_list[i-1] == '':
                                    player_battle_list[i-1] = player_battle_list[i]
                                    player_battle_list[i] = ['해골', cards_kinds['해골']['공격력'], cards_kinds['해골']['체력']]
                                elif player_battle_list[i-1] == '':
                                    player_battle_list[i+1] = player_battle_list[i]
                                    player_battle_list[i] = ['해골', cards_kinds['해골']['공격력'], cards_kinds['해골']['체력']]
                                else:
                                    pass
                            elif move_direction == 'right':
                                if player_battle_list[i+1] == '':
                                    player_battle_list[i+1] = player_battle_list[i]
                                    player_battle_list[i] = ['해골', cards_kinds['해골']['공격력'], cards_kinds['해골']['체력']]
                                elif player_battle_list[i+1] == '':
                                    player_battle_list[i-1] = player_battle_list[i]
                                    player_battle_list[i] = ['해골', cards_kinds['해골']['공격력'], cards_kinds['해골']['체력']]
                                else:
                                    pass
                        # 카드 사망 시
                        if match_battle_list[i][2] <= 0:
                            match_battle_list[i] = ''
                        if match_abilty == '루비 심장':
                            player_battle_list[i] = ['루비 목스', cards_kinds['루비 목스']['공격력'], cards_kinds['루비 목스']['체력']]
                        elif player_abilty == '취약성':
                            player_battle_list[i] = ''
                            bone += 1
                        elif player_abilty == '폭탄':
                            try:
                                match_battle_list[i-1][2] -= 10
                                if match_battle_list[i-1][2] <= 0:
                                    match_battle_list[i] = ''
                                    bone += 1
                            except:
                                continue
                            try:
                                match_battle_list[i+1][2] -= 10
                                if match_battle_list[i+1][2] <= 0:
                                    match_battle_list[i] = ''
                                    bone += 1
                            except:
                                continue
                            try:
                                player_battle_list[i][2] -= 10
                                if player_battle_list[i][2] <= 0:
                                    player_battle_list[i] = ''
                                    bone += 1
                            except:
                                continue
                        elif match_abilty == '해빙':
                            if match_battle_list[i][0] == '드라우그르':
                                match_battle_list[i] = ['드라우그르', cards_kinds['드라우그르']['공격력'], cards_kinds['드라우그르']['체력']]
    return hand, bone, my_health, match_battle_list, player_battle_list


def match_ready_go(match_ready_list, match_battle_list):
    for i in range(4):
        if match_battle_list[i] == '':
            match_battle_list[i] = match_ready_list[i]
            match_ready_list[i] = ''
    return match_ready_list, match_battle_list


def match_attack(my_health, hand, bone, match_battle_list, player_battle_list):
    attack_moves = ['다람쥐 분만', '밀치기', '이동', '해골 선원']
    for i in range(4):
        if match_battle_list[i] != '':
            match_abilty = cards_kinds[match_battle_list[i][0]]['특성']
        if player_battle_list[i] != '':
            player_abilty = cards_kinds[player_battle_list[i][0]]['특성']
        if match_battle_list[i] != '':
            if player_battle_list[i] == '':
                my_health -= match_battle_list[i][1]
            # 공격 시 작용하는 특성
            elif player_battle_list[i] != '':
                if match_abilty == '비행':
                    if cards_kinds[match_battle_list[i]]['특성'] == '비행 방어':
                        player_battle_list[i][2] -= match_battle_list[i][1]
                    else:
                        my_health -= match_battle_list[i][1]
                elif player_abilty == '잠수' or player_abilty == '크라켄 잠수':
                    my_health -= match_battle_list[i][1]
                elif match_abilty == '즉사':
                    player_battle_list[i] = ''
                    bone += 1
                elif match_abilty == '이분공격':
                    try:
                        match_battle_list[i-1][2] -= player_battle_list[i][1]
                    except:
                        continue
                    try:
                        match_battle_list[i+1][2] -= player_battle_list[i][1]
                    except:
                        continue
                elif match_abilty == '삼분공격':
                    try:
                        match_battle_list[i-1][2] -= player_battle_list[i][1]
                    except:
                        continue
                    match_battle_list[i][2] -= player_battle_list[i][1]
                    try:
                        match_battle_list[i+1][2] -= player_battle_list[i][1]
                    except:
                        continue
                elif player_abilty == '가시':
                    match_battle_list[i][2] -= 1
                elif player_abilty == '역겨움':
                    match_battle_list[i][2] -= 0
                elif player_abilty == '토끼굴':
                    hand.append('토끼')
                # 데미지 계산
                else:
                    # 체력 계산
                    player_battle_list[i][2] -= match_battle_list[i][1]
                    # 이동 특성
                    if player_abilty in attack_moves:
                        move_direction = r.choice(['left', 'right'])
                        if player_abilty == '다람쥐 분만':
                            if move_direction == 'left':
                                if match_battle_list[i-1] == '':
                                    match_battle_list[i-1] = match_battle_list[i]
                                    match_battle_list[i] = ['다람쥐', cards_kinds['다람쥐']['공격력'], cards_kinds['다람쥐']['체력']]
                                elif match_battle_list[i - 1] == '':
                                    match_battle_list[i+1] = match_battle_list[i]
                                    match_battle_list[i] = ['다람쥐', cards_kinds['다람쥐']['공격력'], cards_kinds['다람쥐']['체력']]
                                else:
                                    pass
                            elif move_direction == 'right':
                                if match_battle_list[i+1] == '':
                                    match_battle_list[i+1] = match_battle_list[i]
                                    match_battle_list[i] = ['다람쥐', cards_kinds['다람쥐']['공격력'], cards_kinds['다람쥐']['체력']]
                                elif match_battle_list[i+1] == '':
                                    match_battle_list[i-1] = match_battle_list[i]
                                    match_battle_list[i] = ['다람쥐', cards_kinds['다람쥐']['공격력'], cards_kinds['다람쥐']['체력']]
                                else:
                                    pass
                        elif player_abilty == '이동':
                            if move_direction == 'left':
                                if match_battle_list[i-1] == '':
                                    match_battle_list[i-1] = match_battle_list[i]
                                    match_battle_list[i] = ''
                                elif match_battle_list[i-1] != '':
                                    match_battle_list[i+1] = match_battle_list[i]
                                    match_battle_list[i] = ''
                                else:
                                    pass
                            elif move_direction == 'right':
                                if match_battle_list[i+1] == '':
                                    match_battle_list[i+1] = match_battle_list[i]
                                    match_battle_list[i] = ''
                                elif match_battle_list[i+1] != '':
                                    match_battle_list[i-1] = match_battle_list[i]
                                    match_battle_list[i] = ''
                                else:
                                    pass
                        elif player_abilty == '해골 선원':
                            if move_direction == 'left':
                                if match_battle_list[i-1] == '':
                                    match_battle_list[i-1] = match_battle_list[i]
                                    match_battle_list[i] = ['해골', cards_kinds['해골']['공격력'], cards_kinds['해골']['체력']]
                                elif match_battle_list[i-1] == '':
                                    match_battle_list[i+1] = match_battle_list[i]
                                    match_battle_list[i] = ['해골', cards_kinds['해골']['공격력'], cards_kinds['해골']['체력']]
                                else:
                                    pass
                            elif move_direction == 'right':
                                if match_battle_list[i+1] == '':
                                    match_battle_list[i+1] = match_battle_list[i]
                                    match_battle_list[i] = ['해골', cards_kinds['해골']['공격력'], cards_kinds['해골']['체력']]
                                elif match_battle_list[i+1] == '':
                                    match_battle_list[i-1] = match_battle_list[i]
                                    match_battle_list[i] = ['해골', cards_kinds['해골']['공격력'], cards_kinds['해골']['체력']]
                                else:
                                    pass
                    # 취약성(자멸)
                    if match_abilty == '취약성':
                        match_battle_list[i] = ''
                    # 카드 사망 시
                    if player_battle_list[i][2] <= 0:
                        player_battle_list[i] = ''
                        bone += 1
                        # 사망 시 작용하는 특성
                        for i in range(4):
                            if player_abilty == '이중 사망':
                                player_battle_list[i] = ''
                                bone += 1
                                for j in range(4):
                                    if i == j:
                                        continue
                                    elif cards_kinds[player_battle_list[i]]['특성'] == '이중 사망':
                                        player_battle_list[i] = ''
                                        bone += 1
                                        for k in range(4):
                                            if k == i:
                                                continue
                                            if k == j:
                                                continue
                                            elif cards_kinds[player_battle_list[i]]['특성'] == '이중 사망':
                                                player_battle_list[i] = ''
                                                bone += 1
                        if player_abilty == '골왕':
                            bone += 3
                        elif player_abilty == '루비 심장':
                            player_battle_list[i] = ['루비 목스', cards_kinds['루비 목스']['공격력'], cards_kinds['루비 목스']['체력']]
                        elif match_abilty == '취약성':
                            match_battle_list[i] = ''
                        elif player_abilty == '강철 덫':
                            player_battle_list[i] = ''
                            bone += 1
                        elif player_abilty == '불사':
                            hand.append(player_battle_list[i][0])
                        elif player_abilty == '폭탄':
                            try:
                                player_battle_list[i-1][2] -= 10
                                if player_battle_list[i-1][2] <= 0:
                                    player_battle_list[i] = ''
                                    bone += 1
                            except:
                                continue
                            try:
                                player_battle_list[i+1][2] -= 10
                                if player_battle_list[i+1][2] <= 0:
                                    player_battle_list[i] = ''
                                    bone += 1
                            except:
                                continue
                            try:
                                match_battle_list[i][2] -= 10
                                if match_battle_list[i][2] <= 0:
                                    match_battle_list[i] = ''
                                    bone += 1
                            except:
                                continue
                        elif player_abilty == '해빙':
                            if player_battle_list[i][0] == '드라우그르':
                                player_battle_list[i] = ['드라우그르', cards_kinds['드라우그르']['공격력'], cards_kinds['드라우그르']['체력']]
    return my_health, hand, bone, match_battle_list, player_battle_list


def win_lose(my_health, hoil):
    win = False
    if my_health >= 10:
        print('승리!')
        win = True
        if my_health > 10:
            hoil += my_health - 10
    elif my_health < 0:
        print('패배')
        win = True
    return hoil, win
