Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:\Users\CJ\Desktop\Python\calvin_makelky_HW4.py =========
>>> ht
[('A', 8), [[('B', 3), [('C', 1), ('D', 1), ['C', 'D'], 2], ['B', 'C', 'D'], 5], [[('E', 1), ('F', 1), ['E', 'F'], 2], [('G', 1), ('H', 1), ['G', 'H'], 2], ['E', 'F', 'G', 'H'], 4], ['B', 'C', 'D', 'E', 'F', 'G', 'H'], 9], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], 17]
>>> huffman_encode(['B','A','C'],ht)
[1, 0, 0, 0, 1, 0, 1, 0]
>>> huffman_encode(['A','B','B','A'],ht)
[0, 1, 0, 0, 1, 0, 0, 0]
>>> huffman_decode([0,1,0,0,1,0,0,0],ht)
['A', 'B', 'B', 'A']
>>> huffman_decode([1,0,0,0,1,0,1,0],ht)
['B', 'A', 'C']
>>> 
