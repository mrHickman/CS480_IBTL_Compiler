." #1 answer = Hello World" CR
." #2 answer = IDK" CR

16 32 / 74 16 s>f 3 s>f f** f>s * + 5 10 mod +  
." #3 answer = " . CR

16 s>f 32 s>f f/ 74 s>f 16 s>f 3 s>f f** f* f+ 5 10 mod s>f f+
." #4 answer = " f. CR

16.0e0 32.0e0 f/ 74.0e0 16.0e0 3.0e0 f** f* f+ 5 10 mod s>f f+
." #5 answer = " f. CR

16 s>f 32.0e0 f/ 74.0e0 16 s>f 3 s>f f** f* f+ 5 10 mod s>f f+
." #6 answer = " f. CR

: a 16 ;
: b 32e0 ;
a  s>f b f+ 3.0e0 6 s>f 10.0e0 f/ f* f-
." #7 answer = " f. CR

: lfive 5 3 < IF 7 else 2 endif ;
." #8 answer = " lfive . CR

: gfive 5 3 > IF 7 else 2 endif ;
." #9 answer = " gfive . CR

: loopexmpl 6 0 ?do i . loop ;
." #10 answer = " loopexmpl  CR

: convertint s>f ;
." #11 answer = " 40 convertint CR

: fact recursive dup 0 > IF dup 1 - fact * else drop 1 endif ;  
." #12 answer = " 4 fact . CR

: fib recursive dup 0 = IF drop 0 else dup 1 = IF drop 1 else dup 1 - fib swap 2 - fib + endif endif ;
." #13 answer = " 6 fib . CR

bye
