#!/usr/bin/perl

###########################
# Examples of recursive
# subroutines in Perl
###########################

use warnings;
use strict;

##########################
# recursive definition of
# the factorial function
##########################
sub factorial
{
    my $x = shift;
    if ( $x <= 1 ) {
	return 1;
    }
    else {
	return $x * factorial($x-1);
    }
}

##########################
# recursive definition of
# the fibonacci function
##########################
sub fibonacci
{
    my $x = shift;
    if ( $x == 0 or $x == 1 ) {
	return $x;
    }
    else {
	return fibonacci($x-1) + fibonacci($x-2);
    }
}

print 'factorial(5) = ' . factorial(5) . "\n";
print 'fibonacci(8) = ' . fibonacci(8) . "\n";

