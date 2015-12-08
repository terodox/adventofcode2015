import hashlib

DAY4_INPUT = 'iwrupvqb'


class AdventDayFour:
    @staticmethod
    def answer(begin_with):
        count = 0
        while True:
            val_to_hash = DAY4_INPUT + str(count)
            md5 = hashlib.md5()
            md5.update(val_to_hash.encode('utf-8'))
            hashed_value = md5.hexdigest()
            if hashed_value.startswith(begin_with):
                return count
            count += 1


print("Day 4 Part 1: {answer}".format(answer=AdventDayFour.answer('00000')))
print("Day 4 Part 2: {answer}".format(answer=AdventDayFour.answer('000000')))
