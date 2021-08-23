#!/usr/bin/python3.8

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
#    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.


def bit_operation():
      """Bit operations on numbers 5 and 6
      
      
      Returns:
      Bitwise AND (&): x & y
      Bitwise OR  (|): x | y
      Bitwise NOT (~): ~x
      Bitwise XOR (^): x ^ y
      Left Shift  (<<): x << 2
      Right Shift (>>): x >> 2
      """

      result = {}

      result['Bitwise AND (&): 5 & 6 ='] = 5 & 6
      result['Bitwise OR  (|): 5 | 6 ='] = 5 | 6
      result['Bitwise NOT (~): ~5 ='] = ~5
      result['Bitwise NOT (~): ~6 ='] = ~6
      result['Bitwise OR  (|): 5 ^ 6 ='] = 5 ^ 6
      result['Left Shift  (<<): x << 2 ='] = 5 << 2
      result['Right Shift (>>): x >> 2 ='] = 5 >> 2

      return result


if __name__ == '__main__':
      for el in bit_operation():
            print(el, bit_operation()[el])
