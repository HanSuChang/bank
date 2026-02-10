class Account:
    def __init__(self, acc_id, balance, name):
        self._acc_id = acc_id
        self._balance = balance
        self._name = name

    def get_acc_id(self):
        return self._acc_id

    def deposit(self, money):
        self._balance += money

    def withdraw(self, money):
        if self._balance < money:
            return 0
        self._balance -= money
        return money

    def show_info(self):
        print(f"계좌ID: {self._acc_id}")
        print(f"이름: {self._name}")
        print(f"잔액: {self._balance}\n")

# 데이터 저장소
acc_arr = []

def show_menu():
    print("-----Menu-----")
    print("1. 계좌개설")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌번호 전체 출력")
    print("5. 프로그램 종료")

def make_account():
    print("[계좌개설]")
    acc_id = int(input("계좌ID: "))
    name = input("이름: ")
    balance = int(input("입금액: "))
    acc_arr.append(Account(acc_id, balance, name))
    print("개설 완료!\n")

def deposit_money():
    print("[입  금]")
    acc_id = int(input("계좌ID: "))
    money = int(input("입금액: "))
    for acc in acc_arr:
        if acc.get_acc_id() == acc_id:
            acc.deposit(money)
            print("입금완료\n")
            return
    print("유효하지 않은 ID 입니다.\n")

def withdraw_money():
    print("[출  금]")
    acc_id = int(input("계좌ID: "))
    money = int(input("출금액: "))
    for acc in acc_arr:
        if acc.get_acc_id() == acc_id:
            if acc.withdraw(money) == 0:
                print("잔액부족\n")
            else:
                print("출금완료\n")
            return
    print("유효하지 않은 ID 입니다\n")

def show_all_acc_info():
    for acc in acc_arr:
        acc.show_info()

def main():
    while True:
        show_menu()
        choice = int(input("선택: "))
        print()

        if choice == 1:
            make_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            show_all_acc_info()
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()

    #4