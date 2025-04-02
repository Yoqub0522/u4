def withdraw(balance):
    print("Pul yechish tizimiga xush kelibsiz!")

    try:
        x = float(input("Qancha pul yechmoqchisiz? "))

        if x <= 0:
            raise ValueError("Pul miqdori manfiy yoki nol bo'lmasligi kerak.")
        if x > balance:
            raise ValueError("Hisobda yetarli mablag' yo'q.")

        balance -= x
        print(f"{x} so'm hisobdan yechildi. Joriy balans: {balance} so'm.")

    except ValueError as e:
        print(f"Xatolik: {e}")

    finally:
        print(f"Jarayon tugadi. Joriy balans: {balance} so'm.")

    return balance


balance = 1000
balance = withdraw(balance)
