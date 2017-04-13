#!/usr/bin/perl

use warnings;
use strict;

## @_ contains the list of arguments
## passed to print_args. We iterate
## over @_ with foreach.
sub print_args {
    foreach my $arg (@_) {
	print "$arg\n";
    }
}

## @_ contains the list of arguments
## passed to print_args. $_[$i] refers
## to the $i-th element of @_.
sub print_args2 {
    for(my $i=0; $i < @_; $i++) {
	print "arg $i is $_[$i]\n";
    }
}

my @args = ('Perl', "Python", 2, 3.14, 70);

print 'Calling print_args(@args):', "\n";
print_args(@args);
print "\n";

print 'Calling print_args2(@args):', "\n";
print_args2(@args);
print "\n";

