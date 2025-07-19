#!/usr/bin/perl
use strict;
use warnings;
use lib '/usr/abills/lib';
use Abills::HTML;

sub display_form {
  my $html = Abills::HTML->new();
  print $html->header();
  $html->form_parse();

  print $html->form_main({
  NAME => 'my_form',
  CONTENT =>
	$html->form_input('some_text', '', { TYPE => 'text', SIZE => 20 }) .
	$html->form_input('submit', 'Send', { TYPE => 'submit' })
  });

  if(defined $FORM{some_text} && $FORM{some_text} ne ''){
	print $html->form_main({
	  CONTENT => $html->message('info', '', "You typed \"$FORM{some_text}\"")
	});
  }
}

display_form();

1;
