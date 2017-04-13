#!/usr/bin/perl

use 5.010;
use strict;
use warnings;

#Having x increment by 1 made the computation take minutes, so since the answer must be divisible by 20
#I had it increment by 20 to vastly improve speed
#It takes about 18 seconds to compute

my $x = 20;

until( ($x%1 eq 0) and ($x%2 eq 0) and ($x%3 eq 0) and ($x%4 eq 0) and ($x%5 eq 0) and ($x%6 eq 0) and ($x%7 eq 0) and
($x%8 eq 0) and ($x%9 eq 0) and ($x%10 eq 0) and ($x%11 eq 0) and ($x%12 eq 0) and ($x%13 eq 0) and ($x%14 eq 0) and 
($x%15 eq 0) and ($x%16 eq 0) and ($x%17 eq 0) and ($x%18 eq 0) and ($x%19 eq 0)  and ($x%20 eq 0)){
   $x = $x + 20; }
   printf "$x\n";
