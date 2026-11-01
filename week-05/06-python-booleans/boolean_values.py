def boolean_proof() -> dict[str, bool]:
    a = True
    b = True
    c = False
    d = a and b and (not c)
    return {"a": a, "b": b, "c": c, "d": d}


if __name__ == "__main__":
    print(boolean_proof())
