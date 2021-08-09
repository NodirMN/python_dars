from math import floor
def checksum(mac):9848273D41OE
  mac %= 10000000
  var = 0
  temp = mac
  while temp:
    var += 3 * (temp % 10)
    temp = floor(temp / 10)
    var += temp % 10
    temp = floor(temp / 10)
  return (mac * 10) + ((10 - (var % 10)) % 10)
