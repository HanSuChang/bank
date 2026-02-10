class Account:
    def __init__(self, acc_id, balance, name):
        self._acc_id = acc_id
        self._balance = balance
        self._name = name

    def show_info(self):
        print(f"계좌ID: {self._acc_id}, 이름: {self._name}, 잔액: {self._balance}")


acc_arr = []


def show_menu():
    print("-----Menu-----\n1. 계좌개설\n2. 입금\n3. 출금\n4. 계좌번호 전체 출력\n5. 프로그램 종료")


def make_account():
    print("[계좌개설]")
    acc_id = int(input("계좌ID: "));
    name = input("이름: ");
    balance = int(input("입금액: "))
    acc_arr.append(Account(acc_id, balance, name))


def deposit_money():
    print("[입 금]")
    acc_id = int(input("계좌ID: "))
    money = int(input("입금액: "))
    for acc in acc_arr:
        if acc._acc_id == acc_id:
            acc._balance += money
            print("입금 완료!\n")
            return
    print("아이디를 찾을 수 없습니다.\n")


def main():
    while True:
        show_menu()
        try:
            choice = int(input("선택: "))
        except ValueError:
            print("\n숫자만 입력해주세요.\n")
            continue

        if choice == 1:
            make_account()
        elif choice == 2:
            deposit_money()
        elif choice == 4:
            for acc in acc_arr: acc.show_info()
        elif choice == 5:
            break
        else:
            print("아직 구현되지 않은 기능입니다.\n")


if __name__ == "__main__":
    main()

    #3