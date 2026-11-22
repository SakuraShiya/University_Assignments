# Write a Python Program To Input a List Of Scores & Display The Score Of The Runner Up.

from math import isfinite

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Scores : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    scores: list[float] = []

    for i in range(1, n + 1):
        try:
            score = float(input(f"Please Enter Score {i} : "))
        except ValueError:
            print("Invalid Input, Please Enter a Valid Number For Score.")
            return

        if not isfinite(score):
            print("Invalid Input, Please Enter a Finite Number For Score.")
            return

        scores.append(score)

    print()
    print(f"The Given Scores Are : {', '.join(f'{score:.2f}' for score in scores)}")

    unique_scores = set(scores)

    if len(unique_scores) < 2:
        print("There Is No Runner Up Score As All Scores Are The Same.")
    else:
        runner_up = sorted(unique_scores)[-2]
        print(f"The Runner Up Score Is : {runner_up:.2f}")

if __name__ == "__main__":
    main()
