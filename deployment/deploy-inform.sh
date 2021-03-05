#!/bin/bash

## safety measure ##
exit 1

identity="..."
subject="Access link and detailed information about your exam"
accmails=$PWD/sep-mails

for accmail in $accmails/*
do
	acc=`basename $accmail`
	echo "# $acc <= $accmail"

	kmail -s "$subject" --identity "$identity" --composer --body "$(cat $accmail)" "$acc"
	sleep 3
	qdbus org.kde.kmail /kontact/kmail_composer_1 org.kde.kmail.mailcomposer.send 1
	sleep 3
done
