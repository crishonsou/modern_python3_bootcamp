def copy(fn, nfn):
    with open(fn, encoding="UTF8") as f:
        text = f.read()

    with open(nfn, "w") as nf:
        nf.write(text)


copy("story.txt", "story_reverse.txt")
