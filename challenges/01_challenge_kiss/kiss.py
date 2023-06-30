from collections import Counter

def count_fruits(fruits: list[str]) -> dict[str, int]:
    """
    Return, for each fruit element, its frequency in the given list.
    """
    counter = dict(Counter(fruits))
    return counter


def main() -> None:
    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}
    assert count_fruits([]) == {}
    assert count_fruits(
        [
            "apple",
            "apple",
            "apple",
            "apple",
            "apple",
            "apple",
        ]
    ) == {"apple": 6}
    try:
        count_fruits(1) # type: ignore
        count_fruits("not a list") # type: ignore
        assert False
    except Exception:
        assert True

if __name__ == "__main__":
    main()
