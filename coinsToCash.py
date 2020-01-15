def calc_dollars():
    piggyBank = {
        "quarters": 50,
        "nickels": 25,
        "dimes": 8000000,
        "pennies": 12,
}
    dollarAmount = .25 * piggyBank["quarters"]
    dollarAmount += .05 * piggyBank["nickels"]
    dollarAmount += .1 * piggyBank["dimes"]
    dollarAmount += .01 * piggyBank["pennies"]

    print(dollarAmount)

calc_dollars()