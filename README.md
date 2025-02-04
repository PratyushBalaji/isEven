# Implementing isEven

Since bitwise operations are in theory faster than division, I wanted to know if a bit-op based isEven function would perform better than the naive implementation. 
The results were, quite surprising. 
This then spiralled into trying to implement isEven in as many weird ways as possible.

## Implementations : 
### Naive :
- modulo
### Bitwise
- bitshiftEquality
- bitshiftXOR
- bitwiseXOR
- bitwiseAND
- bitwiseOR

### Iterative & Memoized
- iterative
- memoized
### Division
- floatDivision
- intDivision
### String Manipulation
- base10Check
- binaryCheck

## Benchmark results : 

Rank | Test | Time (s)
--- | --- | ---
1 | `bitwiseAND` | 0.03980480000609532
2 | `modulo` | 0.04658449999988079
3 | `bitwiseOR` | 0.04972169999219477
4 | `bitwiseXOR` | 0.05661261100001097
5 | `bitshiftEquality` | 0.06841870000062045
6 | `intDivision` | 0.07277319999411702
7 | `bitshiftXOR` | 0.07857530000910629
8 | `binaryCheck` | 0.10371320000558626
9 | `floatDivision` | 0.10890150000341237
10 | `base10Check` | 0.12126970000099391

Parameters : 
- range : 1,1000000000
- number of tests : 1000000

I could not test iterative and memoized because :
- iterative just took too long as an O($n$) algorithm, especially since the generated numbers could be upto 1000000000 in my benchmark
- memoized has worst case O($n$) too, making it slow, but to make it worse : if a number was more than 999 away from the nearest memo entry, it would exceed the maximum recursion depth

Regardless, I did some testing with lower random ranges, here are the results : 

(range : 1,1500)

Test | Time (s)
--- | ---
`iterative` | anywhere from 2.186090699993656 to 15.538369899993995
`memoized` | 0.04976370000804309 (when it doesn't crash from `recursion depth exceeded`)

If recursion depth was not an issue, memoized would on average be rank 3! 
Tail recursion isn't really a thing in Python, but we could make memo iterative, and on average it should perform decently well (Although consuming a ton of memory)

## Conclusion

The naive, `return num % 2 == 0` solution turned out to be pretty high up the ranks when it comes to timing. 
Even with scale, it outperforms pretty much everything. 
Although the bitwise AND is slightly better, you aren't really losing much runtime and its not as clear that you're finding a remainder so it might not be best to use it in your code. 

While this little experiment turned out to be kinda useless, I might still keep adding to my implementations, just for the sake of finding creative algorithms to check if a number is even.
