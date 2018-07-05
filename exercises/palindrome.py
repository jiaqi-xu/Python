def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        li = list(str(x))
        li.reverse()
        if str(x) == "".join(li):
            return True
        else:
            return False

print(isPalindrome(-121))