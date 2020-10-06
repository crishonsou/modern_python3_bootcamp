def statistics(fn):
    with open(fn, encoding="UTF8") as f:
        lines = f.readlines()
        return {"lines": len(lines),
                "words": sum(len(line.split(" ")) for line in lines),
                "characters": sum(len(line) for line in lines)}



print(statistics("story.txt"))
