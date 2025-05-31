import os


def test_migracion():

    if not os.path.exists("data/output/results.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe en data/output")

    result = {}

    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split("\t")
            result[key] = int(value)

    assert result.get("computational", 0) == 3
    assert result.get("analytics", 0) == 5
