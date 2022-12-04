def main() -> None:
    bus_inter = 2.5
    bus_rota = 3.0
    academy = 110
    ru = 1

    days = 4 * 5
    account = days * (bus_inter + bus_rota) + 5 * ru + academy
    print(account)


if __name__ == "__main__":
    main()
