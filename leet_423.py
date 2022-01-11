def originalDigits(self, s):
        ct = Counter(s)
        res = [
            ct["z"],
            ct["o"] - ct["z"] - ct["w"] - ct["u"],
            ct["w"],
            ct["t"] - ct["w"] - ct["g"],
            ct["u"],
            ct["f"] - ct["u"],
            ct["x"],
            ct["s"] - ct["x"],
            ct["g"],
            ct["i"] - ct["x"] - ct["g"] - ct["f"] + ct["u"],
        ]
        return "".join(str(d) * c for d, c in enumerate(res))