class Hand
  def initialize(line)
    @cards = line.split(" ")
    @a = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    @values = []
    @suits = []
    for i in 0..4
      @values[i] = @a.index(@cards[i][0]) + 2
      @suits[i] = @cards[i][1]
    end

    @sorted = []
    #sort values
    i = 0
    while (i < 5)
      low = @values[0]
      j = 0
      while (j < @values.length)
        if (0 != j and low > @values[j])
          low = @values[j]
        end
        j = j + 1
      end
      @sorted[i] = low
      @values.delete_at(@values.index(low))
      i = i + 1
    end
    @values = @sorted
  end

  def self.whoWins(hand1, hand2)
    if (hand1.getRoyalFlush > 0 or hand2.getRoyalFlush > 0)
      if (hand1.getRoyalFlush > 0)
        return 0
      end
    end

    if (hand1.getStraightFlush > 0 or hand2.getStraightFlush > 0)
      if(hand1.getStraightFlush > hand2.getStraightFlush)
        return 0
      else
        return 1
      end
    end

    if (hand1.getFourOfAKind > 0 or hand2.getFourOfAKind > 0)
      if (hand1.getFourOfAKind == hand2.getFourOfAKind > 0)
        return Hand.breakTie(hand1, hand2)
      else
        if(hand1.getFourOfAKind > hand2.getFourOfAKind)
          return 0
        else
          return 1
        end
      end
    end

    if (hand1.getFullHouse[1] > 0 or hand2.getFullHouse[1] > 0)
      if (hand1.getFullHouse[1] == hand2.getFullHouse[1])
        if(hand1.getFullHouse[0] > hand2.getFullHouse[0])
          return 0
        else
          return 1
        end
      else
        if(hand1.getFullHouse[1] > hand2.getFullHouse[1])
          return 0
        else
          return 1
        end
      end
    end

    if (hand1.getFlush != 0 or hand2.getFlush != 0)
      if (hand1.getFlush == hand2.getFlush)
        return Hand.breakTie(hand1, hand2)
      else
        if(hand1.getFlush != 0 and hand2.getFlush == 0)
          return 0
        else
          return 1
        end
      end
    end

    if (hand1.getStraight > 0 or hand2.getStraight > 0)
      if(hand1.getStraight > hand2.getStraight)
        return 0
      else
        return 1
      end
    end

    if (hand1.getThreeOfAKind > 0 or hand2.getThreeOfAKind > 0)
      if (hand1.getThreeOfAKind == hand2.getThreeOfAKind > 0)
        return Hand.breakTie(hand1, hand2)
      else
        if(hand1.getThreeOfAKind > hand2.getThreeOfAKind)
          return 0
        else
          return 1
        end
      end
    end

    if ((hand1.getTwoPair[0] > 0 and hand1.getTwoPair[1] > 0) or (hand2.getTwoPair[0] > 0 and hand2.getTwoPair[1] > 0))
      if (hand1.getTwoPair[0] == 0 or hand1.getTwoPair[1] == 0)
        high1 = 0
        high12 = 0
      else
        if (hand1.getTwoPair[0] > hand1.getTwoPair[1])
          high1 = hand1.getTwoPair[0]
          high12 = hand1.getTwoPair[1]
        else
          high1 = hand1.getTwoPair[1]
          high12 = hand1.getTwoPair[0]
        end
      end

      if (hand2.getTwoPair[0] == 0 or hand2.getTwoPair[1] == 0)
        high2 = 0
        high22 = 0
      else
        if (hand2.getTwoPair[0] > hand2.getTwoPair[1])
          high2 = hand2.getTwoPair[0]
          high22 = hand2.getTwoPair[1]
        else
          high2 = hand2.getTwoPair[1]
          high22 = hand2.getTwoPair[0]
        end
      end

      if (high1 > high2)
        return 0
      else
        if (high1 == high2)
          if (high12 > high22)
            return 0
          else
            if (high12 == high22)
              return Hand.breakTie(hand1, hand2)
            else
              return 1
            end
          end
        else
          return 1
        end
      end
    end

    if (hand1.getOnePair > 0 or hand2.getOnePair > 0)
      if (hand1.getOnePair == hand2.getOnePair > 0)
        return Hand.breakTie(hand1, hand2)
      else
        if(hand1.getOnePair > hand2.getOnePair)
          return 0
        else
          return 1
        end
      end
    end

    return Hand.breakTie(hand1, hand2)

  end


  def self.breakTie(hand1, hand2)
    if (hand1.getHighCard > hand2.getHighCard)
      return 0
    else
      return 1
    end
  end

  def getHighCard()
    highest = @values[0]
    for i in 1..4
      current = @values[i]
      if (current > highest)
        highest = current
      end
    end
    return highest
  end

  def getOnePair()
    pairs = getTwoPair
    if (pairs[0] > pairs[1])
      return pairs[0]
    else
      return pairs[1]
    end
  end

  def getTwoPair()
    a = 0
    b = 0
    for i in 0..4
      current = @values[i]
      for j in i..4
        if (i != j and @values[j] == current)
          if (a == 0)
            a = current
          else
            b = current
          end
        end
      end
    end
    return a, b
  end

  def getThreeOfAKind()
    for i in 0..2
      if (@values[i] == @values[i+1] and @values[i] == @values[i+2])
        return @values[i]
      end
    end
    return 0
  end

  def getStraight()
    flag = true
    for i in 0..3
      if (@values[i] != @values[i+1] - 1)
        flag = false
        break
      end
    end
    if (flag == true)
      return @values[0]
    else
      return 0
    end
  end

  def getFlush()
    i = 0
    flag = true
    while (i < 4)
      if (@suits[i] != @suits[i+1])
        flag = false
        break
      end
      i = i + 1
    end
    if (flag == true)
      return @suits[0]
    else
      return 0
    end
  end

  def getFullHouse()
    p = getTwoPair
    t = getThreeOfAKind
    if (p[0] != 0 and t != 0 and p[0] != t)
      return p[0], t
    else
      if (p[1] != 0 and t != 0 and p[1] != t)
        return p[1], t
      else
        return 0, 0
      end
    end
  end

  def getFourOfAKind()
    for i in 0..1
      if (@values[i] == @values[i+1] and @values[i] == @values[i+2] and @values[i] == @values[i+3])
        return @values[i]
      end
    end
    return 0
  end

  def getStraightFlush()
    s = getStraight
    f = getFlush
    if (s != 0 and f != 0)
      return s
    else
      return 0
    end
  end

  def getRoyalFlush()
    s = getStraightFlush
    if (s == 10)
      return s
    else
      return 0
    end
  end

end

def evaluate(line)
  hand1 = Hand.new(line[0..13])
=begin
  print "high card:\t", hand1.getHighCard, "\n"
  print "one pair:\t", hand1.getOnePair, "\n"
  print "three of a kind:\t", hand1.getThreeOfAKind, "\n"
  print "straight:\t", hand1.getStraight, "\n"
  print "flush:\t", hand1.getFlush, "\n"
  print "full house:\t", hand1.getFullHouse, "\n"
  print "four of a kind:\t", hand1.getFourOfAKind, "\n"
  print "straight flush:\t", hand1.getStraightFlush, "\n"
  print "royal flush:\t", hand1.getRoyalFlush, "\n"
  hand2 = Hand.new(line[15..-1])
=end
  hand2 = Hand.new(line[15..-1])
  win = Hand.whoWins(hand1, hand2)
  #quickly check symmetry to help find potential bugs
  winR = Hand.whoWins(hand2, hand1)
  if (win == winR)
    puts "Problem with line ", line, "\n"
  end

  if (win == 0)
    puts "Player 1 wins!"
  else
    puts "Player 2 wins!"
  end

  return win
end

f = File.open("p054_poker.txt", "r")
count = 0
f.each_line do |line|
  puts line
  if (evaluate(line) == 0)
    count = count + 1
  end
end

puts count