def letterCasePermutation(self, s: str) -> List[str]:
        output = []
        def casePerm(s, str_):
            if s == "":
                output.append(str_)
            else:
                s_ = str_ + s[0].lower()
                casePerm(s[1:], s_)
                if not s[0].isdigit():
                    s_ = str_ + s[0].upper()
                    casePerm(s[1:], s_)
        casePerm(s, "")
        return output
