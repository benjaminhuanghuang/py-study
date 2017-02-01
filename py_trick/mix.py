class Reverse(object):
    def reverse_str(self):
        result = super(Reverse, self).__str__()
        result = result[::-1]
        return result



class SubReverse(Reverse, list):
    pass


sr = SubReverse([1, 2, 3])
print sr.reverse_str()
