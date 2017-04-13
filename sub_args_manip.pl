#!/usr/bin/perl

use warnings;
use strict;

###### Example 1 ########
# This example demonstrates how the argument values can
# be assigned from @_.
sub add2 {
    my ($x, $y) = @_;
    return $x + $y;
}

print 'add2(1, 2) = ', add2(1, 2), "\n";

## 3 and 4 are ignored.
print 'add2(1, 2, 3, 4) = ', add2(1, 2, 3, 4), "\n";

## "Perl" and "Python" are ignored.
print 'add2(1, 2, "Perl", "Python") = ', add2(1, 2, "Perl", "Python"), "\n";

## $y is not initialized and defaults to 0. There will be
## a warning, but no crash.
print 'add2(1) = ', add2(1), "\n"; 

## Neither $x nor $y are initialized. Both default to 0. There will be
## a warning, but no crash.
print 'add2()  = ', add2(), "\n\n"; 

###### Example 2 ########
# This example illustrates how shift() can
# be used to extract argument values from @_.
sub mult2 {
    my ($x, $y);
    $x = shift();
    $y = shift();
    return $x * $y;
}

## $x = 2, $y = 4.
print 'mult2(2, 4) = ', mult2(2, 4), "\n";

## $x = 2, $y = 4, 3 and 4 are ignored.
print 'mult2(2, 4, 3, 4) = ', mult2(2, 4, 3, 4), "\n";
print 'mult2(1, 2, "Perl", "Python") = ', mult2(1, 2, "Perl", "Python"), "\n";

## $x = 1, $y is not initialized, defaults to 0
print 'mult2(1) = ', mult2(1), "\n"; 

## Neither $x nor $y are initialized. Both default to 0. Warning
## but no crash.
print 'mult2()  = ', mult2(), "\n"; ## $x and $y default to 0


