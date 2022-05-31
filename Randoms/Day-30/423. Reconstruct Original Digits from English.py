class Solution:
    def originalDigits(self, s: str) -> str:
        count_letters = collections.Counter(s)
        mapping = {}
        
        mapping["0"] = count_letters["z"]
        mapping["2"] = count_letters["w"]
        mapping["4"] = count_letters["u"]
        mapping["6"] = count_letters["x"]
        mapping["8"] = count_letters["g"]
        mapping["3"] = count_letters["h"] - mapping["8"]
        mapping["5"] = count_letters["f"] - mapping["4"]
        mapping["7"] = count_letters["s"] - mapping["6"]
        mapping["9"] = count_letters["i"] - mapping["5"] - mapping["6"] - mapping["8"]
        mapping["1"] = count_letters["n"] - mapping["7"] - 2 * mapping["9"]

        result = [key * mapping[key] for key in sorted(mapping.keys())]
        return "".join(result)
