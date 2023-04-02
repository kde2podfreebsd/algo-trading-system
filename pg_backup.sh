#!/bin/bash

db_name=dbname
db_user=dbuser
db_host=host
backupfolder=~/postgresql/backups 
recipient_email=youremail@example.ru

keep_day=30
sqlfile=$backupfolder/database-$(date +%d-%m-%Y_%H-%M-%S).sql
zipfile=$backupfolder/database-$(date +%d-%m-%Y_%H-%M-%S).zip
mkdir -p $backupfolder

if pg_dump -U $db_user -h $db_host $db_name > $sqlfile ; then
   echo 'Sql dump created'
else
   echo 'pg_dump return non-zero code' | mailx -s 'No backup was created!' $recipient_email
   exit
fi

if gzip -c $sqlfile > $zipfile; then
   echo 'The backup was successfully compressed'
else
   echo 'Error compressing backup' | mailx -s 'Backup was not created!' $recipient_email
   exit
fi
rm $sqlfile 
echo $zipfile | mailx -s -a $sqlfile 'Backup was successfully created' $recipient_email
 
find $backupfolder -mtime +$keep_day -delete
