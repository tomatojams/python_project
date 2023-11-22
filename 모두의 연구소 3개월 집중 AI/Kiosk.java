# 문제 3-3. 클래스 업데이트  
# 앞에서 구현했던 메서드들을 Kiosk 클래스에 추가합니다. 직접 코드를 작성해 보세요! 

class Kiosk:
    def __init__(self):
        self.menu = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']
        self.price = [2000, 3000, 3000, 2500, 2500, 3000]
        self.temp = 'HOT'

    # 메뉴 출력 메서드
    def menu_print(self):
        for i in range(len(self.menu)):
            print(i + 1, self.menu[i], ' : ', self.price[i], '원')

    # 주문 메서드
    def menu_select(self):
        self.order_menu = []  # 주문 리스트
        self.order_price = []  # 가격 리스트

        n = 0
        while n < 1 or len(self.menu) < n:
            n = int(input("음료를 번호를 입력하세요 : "))  # 음료 번호 입력

            # 메뉴판에 있는 음료 번호일 때
            if 1 <= n <= len(self.menu):
                self.order_price.append(self.price[n-1])  # 가격 리스트에 추가합니다.
                self.price_sum = self.price[n-1]  # 합계 금액

                # 메뉴판에 없는 번호일 때
            else:
                print("없는 메뉴입니다. 다시 주문해 주세요.")


        # 음료 온도 물어보기
        t = 0  # 기본값을 넣어주고
        while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
            t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
            # 문제 2-3의 답을 입력하세요. 
            if t == 1:
                temp = "HOT"
            elif t == 2:
                temp = "ICE"

            else:
                print("1과 2 중 하나를 입력하세요.\n")

        self.order_menu.append(self.temp + ' ' + self.menu[n-1])  # 주문 리스트에 추가합니다.
        # 문제 2-2의 답을 입력하세요. 
        print(self.temp, self.menu[n-1], ' : ', self.price_sum, '원')  # 온도 속성을 추가한 주문 결과를 출력합니다.

        # 추가 주문 또는 지불
        while n != 0:  # 지불을 선택하기 전까지 반복합니다.
            print()  # 줄 바꾸면서 
            n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : "))  # 추가 주문 또는 지불
            if n > 0 and n < len(self.menu) + 1:
                # 추가 음료 온도 
                t = 0  # 기본값을 넣어주고
                while t != 1 and t != 2:  # 1이나 2를 입력할 때까지 물어보기
                    t= int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
                    # 문제 2-3. 음료의 온도에 따라 temp 변수를 "HOT" 또는 "ICE"로 지정하세요.   
                    # 힌트: if문을 활용해보세요.        
                    # [[YOUR CODE]]   
                    if t == 1:
                        temp = "HOT"
                    elif t == 2:
                        temp = "ICE"
                    else:
                        print("1과 2 중 하나를 입력하세요.\n")
                    # 문제 2-4. 추가 음료의 온도를 입력받고, 가격 리스트, 주문 리스트, 합계 금액을 업데이트해보세요.
                    # [[YOUR CODE]]
                self.order_menu.append(self.temp + ' ' + self.menu[n-1])
                self.order_price.append(self.price[n-1])
                self.price_sum = sum(self.order_price)
                print('추가 주문 음료',self.order_menu[-1], ':', self.order_price[-1], '원\n', '합계 : ', self.price_sum, '원')
            else :
                if n == 0 :  # 지불을 입력하면
                    print("주문이 완료되었습니다.")
                    print(self.order_menu, self.order_price)  # 확인을 위한 리스트를 출력합니다.
                else :  # 없는 번호를 입력할 때
                    print("없는 메뉴입니다. 다시 주문해 주세요.")
#%%


    # 지불
    def pay(self):
        payment = input("""현금('cash' or 1) → '직원을 호출하겠습니다.'  
    카드('card' or 2) → 'IC칩 방향에 맞게 카드를 꽂아주세요.'"""  )

    # 주문서 출력 
    def table(self):

        # 외곽
        print('⟝' + '-' * 30 + '⟞')
        for i in range(5):
            print('|' + ' ' * 31 + '|')

        # 주문 상품명 : 해당 금액
        for i in range(len(self.order_menu)):
            print(self.order_menu[i], ' : ', self.order_price[i])

        print('합계 금액 :', sum(self.order_price))

        # 외곽
        for i in range(5):
            print('|' + ' ' * 31+ '|')
        print('⟝' + '-' * 30 + '⟞')