#!/usr/bin/perl

use 5.010;
use strict;
use warnings;

print "Enter the upper bound: ";

my $u = <STDIN>;
my $sum = 0;
for (my $i=0; $i < $u; $i++) {
   if (($i%5 eq 0) or ($i%3 eq 0)){
	$sum += $i;	
   }
}
print "$sum\n";	
