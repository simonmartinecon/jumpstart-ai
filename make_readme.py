"""Generate README.md (shown on GitHub) from slides.tex.

Run from the project folder:  python make_readme.py
Each frame becomes a section; lists, tables, prompt boxes, code listings and
folder trees are converted to Markdown, using the same included files as the slides.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "slides.tex"
OUT = ROOT / "README.md"


def braced(s, i):
    """Return (content, end) of the brace group starting at s[i] == '{'."""
    assert s[i] == "{", s[i:i + 30]
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{" and s[j - 1] != "\\":
            depth += 1
        elif s[j] == "}" and s[j - 1] != "\\":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
    raise ValueError("unbalanced braces")


def replace_cmd(s, cmd, fn, nargs=1):
    """Replace \\cmd{a}{b}... (nargs brace groups) by fn(a, b, ...)."""
    out, i = [], 0
    pat = re.compile(r"\\" + cmd + r"(?![A-Za-z])\s*(\[[^\]]*\])?\s*(?=\{)")
    while (m := pat.search(s, i)):
        out.append(s[i:m.start()])
        j, args = m.end(), []
        for _ in range(nargs):
            a, j = braced(s, j)
            args.append(a)
        out.append(fn(*args))
        i = j
    out.append(s[i:])
    return "".join(out)


def anchor(title):
    a = re.sub(r"[^\w\- ]", "", title.lower()).strip()
    return a.replace(" ", "-")


def inline(s, labels):
    """Convert inline LaTeX markup to Markdown."""
    s = re.sub(r"slides?~(?=\\ref)", "", s)
    s = replace_cmd(s, "ref", lambda k: f"[{labels[k]}](#{anchor(labels[k])})")
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = replace_cmd(s, "icon", lambda a: "")
    s = re.sub(r"\\fa[A-Za-z]+\*?", "", s)
    s = replace_cmd(s, "textcolor", lambda c, t: t, nargs=2)
    s = replace_cmd(s, "href", lambda u, t: f"[{t}]({u})", nargs=2)
    s = replace_cmd(s, "url", lambda u: f"<{u}>")
    s = s.replace("\\email", "[simon.martin@univie.ac.at](mailto:simon.martin@univie.ac.at)")
    s = replace_cmd(s, "textbf", lambda t: f"**{t}**")
    s = replace_cmd(s, "textit", lambda t: f"*{t}*")
    s = replace_cmd(s, "emph", lambda t: f"*{t}*")
    s = replace_cmd(s, "file", lambda t: f"`{t}`")
    s = replace_cmd(s, "texttt", lambda t: f"`{t}`")
    for a, b in [("``", '"'), ("''", '"'), ("---", "—"), ("--", "–"),
                 ("\\dots{}", "..."), ("\\dots", "..."), ("\\%", "%"),
                 ("\\_", "_"), ("e.g.\\ ", "e.g. "), ("\\enspace", " "),
                 ("$\\rightarrow$", "→"), ("~", " "), ("\\par", "")]:
        s = s.replace(a, b)
    s = re.sub(r"\\(small|footnotesize|scriptsize|tiny|smallskip|medskip|bigskip)\b", "", s)
    s = re.sub(r"\\vspace\*?\{[^}]*\}", "", s)
    s = re.sub(r"\{\s*([^{}]*?)\s*\}", r"\1", s)  # leftover grouping braces
    return re.sub(r"[ \t]+", " ", s).strip()


def table(body, labels):
    """tabularx body -> Markdown table."""
    body = re.sub(r"\\(toprule|midrule|bottomrule)", "", body)
    rows = [r.strip() for r in body.split("\\\\") if r.strip()]
    rows = [[inline(c, labels) for c in r.split("&")] for r in rows]
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    md = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * n]
    md += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n" + "\n".join(md) + "\n"


def dirtree(path):
    """dirtree input file -> plain-text tree in a code block."""
    lines = []
    for m in re.finditer(r"^\.(\d) (.*?)(?:\\DTcomment\{(.*?)\})?\.$",
                         (ROOT / path).read_text(), re.M):
        name = re.sub(r"\\fa[A-Za-z]+\\ ", "", m.group(2)).strip()
        name = "  " * (int(m.group(1)) - 1) + name
        lines.append(f"{name:<28}{'# ' + m.group(3) if m.group(3) else ''}".rstrip())
    return "\n```text\n" + "\n".join(lines) + "\n```\n"


def listing(opts, path, seen):
    if path.endswith(".md"):  # whole documents: link instead of pasting
        if path in seen:
            return ""
        seen.add(path)
        return f"\n→ See [{path}]({path}).\n"
    lang = {".do": "stata", ".tex": "latex", ".py": "python"}.get(Path(path).suffix, "")
    return f"\n```{lang}\n{(ROOT / path).read_text().rstrip()}\n```\n"


def frame_body(body, labels, seen):
    body = re.sub(r"\\renewcommand\{\\arraystretch\}\{[^}]*\}", "", body)
    body = replace_cmd(body, "lstset", lambda a: "")
    while (i := body.find("\\begin{tabularx}")) >= 0:
        _, j = braced(body, i + len("\\begin{tabularx}"))  # width
        _, j = braced(body, j)                              # column spec
        k = body.index("\\end{tabularx}", j)
        body = body[:i] + table(body[j:k], labels) + body[k + len("\\end{tabularx}"):]
    body = replace_cmd(body, "prompt", lambda t: f"\n> 💬 *{inline(t, labels)}*\n")
    body = re.sub(r"\\begin\{keybox\}(.*?)\\end\{keybox\}",
                  lambda m: f"\n> {inline(m.group(1), labels)}\n", body, flags=re.S)
    body = re.sub(r"\\input\{([^}]*)\}", lambda m: dirtree(m.group(1)), body)
    body = re.sub(r"\\lstinputlisting(\[[^\]]*\])?\{([^}]*)\}",
                  lambda m: listing(m.group(1), m.group(2), seen), body)
    body = re.sub(r"\\(begin|end)\{columns?\}(\[[^\]]*\])?(\{[^}]*\})?", "", body)

    out, stack, in_code = [], [], False
    for line in body.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            out += ["", s] if in_code else [s, ""]
            continue
        if in_code:
            out.append(line)
            continue
        if s.startswith(">"):  # each quote box on its own
            out += ["", s, ""]
            continue
        if s.startswith("|"):
            out.append(s)
            continue
        if m := re.match(r"\\begin\{(itemize|enumerate)\}", s):
            stack.append(m.group(1))
            out.append("")
            continue
        if re.match(r"\\end\{(itemize|enumerate)\}", s):
            stack.pop()
            out.append("")
            continue
        indent = "  " * (len(stack) - 1)
        if s.startswith("\\item[]"):
            out.append(indent + "  " + inline(s[7:], labels))
        elif s.startswith("\\item"):
            mark = "1." if stack[-1] == "enumerate" else "-"
            out.append(f"{indent}{mark} {inline(s[5:], labels)}")
        else:
            t = inline(s, labels)
            if t:
                out.append(t + "\n" if not stack else indent + "  " + t)
    md = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


def main():
    tex = SRC.read_text(encoding="utf8")
    preamble, doc = tex.split("\\begin{document}")

    def macro(name):
        m = re.search(r"\\" + name + r"\{", preamble)
        return braced(preamble, m.end() - 1)[0]

    frames = []
    for m in re.finditer(r"\\begin\{frame\}(\[[^\]]*\])?", doc):
        i = m.end()
        title = ""
        if doc[i] == "{":
            title, i = braced(doc, i)
        body = doc[i:doc.index("\\end{frame}", i)]
        frames.append((title, body))

    labels = {}
    for title, body in frames:
        for k in re.findall(r"\\label\{([^}]*)\}", body):
            labels[k] = inline(title, {})

    date = inline(macro("date"), {})
    md = [
        "<!-- Generated from slides.tex by make_readme.py. Do not edit by hand. -->",
        f"# {inline(macro('title'), {})}",
        f"*{inline(macro('subtitle'), {})}*",
        f"{inline(macro('author'), {})} · \\email · "
        "[sites.google.com/view/simonmartinecon](https://sites.google.com/view/simonmartinecon/)",
        f"{date} · PDF version: [slides.pdf](slides.pdf)",
    ]
    md = [inline(x, labels) if "\\email" in x else x for x in md]

    seen = set()
    for title, body in frames:
        if not title:  # title page
            continue
        md.append(f"## {inline(title, labels)}\n\n{frame_body(body, labels, seen)}")

    OUT.write_text("\n\n".join(md) + "\n", encoding="utf8")
    print(f"Wrote {OUT.name}: {len(frames) - 1} sections")


if __name__ == "__main__":
    main()
