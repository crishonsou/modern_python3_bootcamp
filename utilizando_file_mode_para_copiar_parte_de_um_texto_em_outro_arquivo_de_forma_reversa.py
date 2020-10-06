def copy_and_reverse(fn, nfn):
    with open(fn, encoding="UTF8") as f:
        text = f.read()

    with open(nfn, "w") as nf:
        nf.write(text[::-1])


copy_and_reverse("story.txt", "story_reverse.txt")
