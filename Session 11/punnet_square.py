#!/usr/bin/env python3
"""punnet_square.py"""

from collections import defaultdict

# Declare the genotype of the parents (one and two)
# Let 1 correspond to dominant, 0 correspond to recessive
# The alleles are arranged 'color color shape shape'
geno_one = "0000"
geno_two = "1111"

# Print the genotypes for the parents using f strings
print(f"Parent 1 genotype: Color - {geno_one[:2]}, Shape - {geno_one[2:4]}")
print(f"Parent 2 genotype: Color - {geno_two[:2]}, Shape - {geno_two[2:4]}")


def generate_gametes():
    # Use our global variables so we don't have to pass anything in
    global geno_one, geno_two
    # Use list comprehension to get the possible gametes of the two parents
    gametes_one = [geno_one[i] + geno_one[j] for i in range(2) for j in range(2, 4)]
    gametes_two = [geno_two[i] + geno_two[j] for i in range(2) for j in range(2, 4)]

    # Print the possible gametes for each parent
    count = 1
    for i in (gametes_one, gametes_two):
        # Using ternary operator for print
        print(
            "\nParent 1 Possible Gametes:"
            if count == 1
            else "\nParent 2 Possible Gametes:"
        )
        for j in i:
            print(f"Color - {j[0]}, Shape - {j[1]}")
        count += 1

    return gametes_one, gametes_two


def generate_offspring():
    # Start with the gametes from the parents
    game_one, game_two = generate_gametes()

    # Generate the possible gametes for each trait when parents cross
    color_gametes = [
        game_one[i][0] + game_two[j][0] for i in range(4) for j in range(4)
    ]
    shape_gametes = [
        game_one[i][1] + game_two[j][1] for i in range(4) for j in range(4)
    ]

    # Use the ternary operator and list comprehension to reverse the
    # gametes to place dominant traits first when necessary
    color_gametes = [i[::-1] if int(i[0]) < int(i[1]) else i for i in color_gametes]
    shape_gametes = [i[::-1] if int(i[0]) < int(i[1]) else i for i in shape_gametes]

    # Generate offspring by combining the gametes
    offspring = [color_gametes[i] + shape_gametes[i] for i in range(16)]

    # Print the Punnett Square Results. I saw the way demonstrated in
    # the slides, but I would prefer to join the gametes to form full
    # genotypes
    # Additionally, I'm arranging parent one along the top,
    # parent two along the left side.
    print("\nPunnett Square Results:")
    for i in range(4):
        for j in range(3):
            print(f"[{offspring[i + 4 * j]}]", end=" | ")
        print(f"[{offspring[i + 12]}]")

    return offspring


def main():
    # Get our list of possible genotypes of the offspring
    offspring = generate_offspring()

    # Create a dictionary to count the occurrences of each phenotype
    phenotypes = defaultdict(int)
    for i in offspring:
        if int(i[0]) == 1:
            if int(i[2]) == 1:
                phenotypes["Yellow and Round"] += 1
            else:
                phenotypes["Yellow and Wrinkled"] += 1
        else:
            if int(i[2]) == 1:
                phenotypes["Green and Round"] += 1
            else:
                phenotypes["Green and Wrinkled"] += 1

    print("\nPhenotype Ratios:")
    for key in phenotypes:
        print(f"{key}: {phenotypes[key]}/16")


if __name__ == "__main__":
    main()
