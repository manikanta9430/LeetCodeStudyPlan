class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.total=timeToLive
        self.dct={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dct[tokenId]=currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dct and currentTime-self.dct[tokenId]<self.total:
            self.dct[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(currentTime-val<self.total for el,val in self.dct.items())
