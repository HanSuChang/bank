class Account:
    def __init__(self, acc_id, balance, name):
        self._acc_id = acc_id
        self._balance = balance
        self._name = name

        #__init__: 새로운 계좌를 만들 때 처음 실행되는 부분
        #계좌번호:acc_id, 잔액:balance, 이름:name

    def get_acc_id(self):
        return self._acc_id

    def deposit(self, money):
        self._balance += money
    # deposit(money):입금, 잔액(balance)에 받은 돈을 더합니다.

    def withdraw(self, money):
        if self._balance < money:
            return 0
        self._balance -= money
        return money
    # withdraw(money):출금, 만약 잔액보다 빼려는 돈이 많으면 0을 돌려주고(실패), 충분하면 잔액을 깎고 돈을 줌

    def show_info(self):
        print(f"계좌ID: {self._acc_id}")
        print(f"이름: {self._name}")
        print(f"잔액: {self._balance}\n")
    # show_info(): 이 계좌의 정보를 화면에 예쁘게 출력해주는 기능입니다.

acc_arr = [] # 데이터 저장소[은행의 '고객 명부' 또는 '파일철']


def show_menu():
    print("-----Menu-----")
    print("1. 계좌개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌번호 전체 출력")
    print("5. 프로그램 종료")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("선택: "))
        except ValueError:
            print("\n숫자만 입력해주세요.\n")
            continue

        if choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("아직 구현되지 않은 기능입니다.\n")

if __name__ == "__main__":
    main()