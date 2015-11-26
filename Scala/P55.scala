object P55 {
  def main(args: Array[String]) {
    val s = for (x <- 0 to 10000 if isLychrel(x.toString())) yield true
    println(s.length)
  }

  def isLychrel(num: String): Boolean = {
    _isLychrel(num, 0)
  }

  def _isLychrel(num: String, i: BigInt): Boolean = {
    if (i > 50) {
      true
    } else {
      val num_r: String = reverse(num)
      val num_new: String = (BigInt(num_r) + BigInt(num)).toString()
      if (isPalindrome(num_new)) {
        false
      } else {
        _isLychrel(num_new, i + 1)
      }
    }
  }

  def reverse(num: String): String = {
    _reverse(num, 0)
  }

  def _reverse(num: String, i: Int): String = {
    if (i < (num.length() - 1 - i)) {
      val num_builder = new StringBuilder(num)
      num_builder.setCharAt(i, num.charAt(num.length() - 1 - i))
      num_builder.setCharAt(num.length() - 1 - i, num.charAt(i))
      val num_new = num_builder.toString()
      _reverse(num_new, i + 1)
    } else {
      num
    }
  }

  def isPalindrome(num: String): Boolean = {
    _isPalindrome(num, 0)
  }

  def _isPalindrome(num: String, i: Int): Boolean = {
    if (i < (num.length() - 1 - i)) {
      if (num.charAt(i) == num.charAt(num.length() - 1 - i)) {
        _isPalindrome(num, i + 1)
      } else {
        false
      }
    } else {
      true
    }
  }
}
