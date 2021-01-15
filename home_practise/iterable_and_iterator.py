from abc import ABC

class Wallet(ABC):
    def __init__(self):
        pass


class BigWallet(Wallet):
    def __init__(self, papers, coins):
        self.papers = list(papers)
        self.coins = list(coins)
        self.consist = BigWallet._get_money(papers, coins)
        self.total = sum(self.papers + self.coins)

    def __iter__(self, papers=False, coins=False):
        return IterBigWallet(self.consist)

    @staticmethod
    def _get_money(papers, coins):
        entire = []
        for value in papers:
            entire.append(value * 100)
        for value in coins:
            entire.append(value)
        return entire


class IterBigWallet(BigWallet):

    def __init__(self, wallet):
        self.wallet = wallet
        self.index = 0

    def __len__(self):
        count = 0
        while True:
            try:
                self.wallet[count]
            except Exception as e:
                break
            count += 1
        return count+1

    def __next__(self):
        try:
            value = self.wallet[self.index]
        except IndexError:
             raise StopIteration()
        self.index += 1
        return value

    def __iter__(self):
        return self

first = BigWallet(papers=(1,2,3), coins=(10,25))
print(first.total)
iterka = iter(first)
print(iterka)
print(next(iterka))
print(next(iterka))
print(next(iterka))
print(next(iterka))
print(len(iterka))

class Repeator():
    def __init__(self, word):
        self.word = word

    #def __iter__(self):
    #   return ReapeatorIterator(self.word)

    #or just
    def __iter__(self):
       for i in self.word:
           yield i.lower()
       else:
           raise StopIteration

class ReapeatorIterator(Repeator):
    def __init__(self, word):
        self.word = word
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self.word[self.counter]
        except:
            raise StopIteration
        self.counter +=1
        return value

repeater = Repeator("Hello")
for i in repeater:
    print(i)  # hello