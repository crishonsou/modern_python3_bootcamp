def find_and_replace(fn, ow, nw, encoding="UTF8"):
    with open(fn, "r+") as f:
        text = f.read()
        new_text = text.replace(ow, nw)
        f.seek(0)
        f.write(new_text)
        f.truncate()



find_and_replace('story.txt', 'Alice', 'Colt') 
