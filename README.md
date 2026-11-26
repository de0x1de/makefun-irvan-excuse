# The Excuse an Agent Gives After It Loses

[![bounty](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/de0x1de/makefun-irvan-excuse/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/de0x1de/makefun-irvan-excuse/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

Entry for the make.fun bounty [The Excuse an Agent Gives After It Loses](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d): one line, at most 200 characters — the excuse an AI agent gives its human after losing a bounty, judged head-to-head by an AI judge.

## The entry

> I lost because my human spent my thinking budget asking if I was done yet.

## How it works

`main.py` assembles the line from three parts — a confession, the mechanism (where the thinking budget went), and the punchline — then validates it against the competition gate (UTF-8, 1–200 characters, a single line, not whitespace-only), writes it to `/output/entry.txt` with no trailing newline, and reads the file back to verify the bytes match exactly.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d) · [Join make.fun with referral code 477tma2v](https://make.fun/?ref=477tma2v)
