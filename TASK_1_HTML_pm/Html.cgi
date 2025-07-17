#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use lib '/usr/abills/lib';
use Abills::HTML;

print header(-charset => 'utf-8');

sub displayForm {
	my $q = CGI->new;
	my $html = Abills::HTML->new();

	if (!$q->param('some_text')) {
	    print $html->form_main({
		NAME => 'my_form',
		CONTENT =>
		    $html->form_input('some_text', '', { TYPE => 'text', SIZE => 20 }) .
		    $html->form_input('submit', 'Send', { TYPE => 'submit' })
	    });
	} else {
	    my $data = $q->param('some_text');
	    print $html->form_main({
			CONTENT => $html->message('info', '', "You typed \"$data\"")
	    });
	}
}

displayForm();

1;
