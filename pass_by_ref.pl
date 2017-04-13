#!/usr/bin/perl

# Examples of pass-by-reference and how to prevent
# argument modification.

use warnings;
use strict;

print "\n";

my $x = 5;
print "1.  Before calling square(\$x), \$x = $x\n";
square($x);
print "    After calling square(\$x), \$x = $x\n\n";

print "2.  Before calling safe_square(\$x), \$x = $x\n";
safe_square($x);
print "    After calling safe_square(\$x), \$x = $x\n\n";

my @a = (1 .. 5);
print "3.  Before calling square_array(\@a), \@a = @a\n";
square_array(@a);
print "    After calling square_array(\@a), \@a = @a\n\n";

print "4.  Before calling safe_square_array(\@a), \@a = @a\n";
safe_square_array(@a);
print "    After calling safe_square_array(\@a), \@a = @a\n\n";


## Changes value of caller's parameter
sub square {
    $_[0] **= 2;
}


## Does not change value of caller's parameter
sub safe_square {
    ## a copy is made
    my $x = shift;
    $x **= 2;
}


## Changes value of caller's parameters
sub square_array {
    for (@_) {
	$_ **= 2;
    }
}

## Does not change value of caller's parameters
sub safe_square_array {
    ## a copy is made
    my @val = @_;
    for (@val) {
	$_ **= 2;
    }
}
