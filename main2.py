# [1+2단계] 계좌 개설 기능이 포함된 통합 코드

class Account:
    def __init__(self, acc_id, balance, name):
        self._acc_id = acc_id
        self._balance = balance
        self._name = name

    # 계좌 정보를 보여주는 기본 기능 (추후 3단계에서 활용)
    def show_info(self):
        print(f"계좌ID: {self._acc_id}, 이름: {self._name}, 잔액: {self._balance}")


# 은행의 고객 명부 (저장소)
acc_arr = []


def show_menu():
    print("-----Menu-----")
    print("1. 계좌개설")
    print("2. 입금 (미구현)")
    print("3. 출금 (미구현)")
    print("4. 계좌번호 전체 출력 (미구현)")
    print("5. 프로그램 종료")


def make_account():
    print("\n[계좌개설]")
    try:
        acc_id = int(input("계좌ID (숫자): "))
        name = input("이름: ")
        balance = int(input("초기 입금액: "))

        # 새로운 계좌 객체를 만들어 명부(acc_arr)에 추가
        acc_arr.append(Account(acc_id, balance, name))
        print("계좌 개설이 완료되었습니다!\n")
    except ValueError:
        print("\n입력 형식이 올바르지 않습니다. 처음부터 다시 시도하세요.\n")


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
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("아직 구현되지 않은 기능입니다. (2, 3, 4번은 다음 단계에서!)\n")


if __name__ == "__main__":
    main()