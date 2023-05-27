#!/bin/bash

db_name='postgres'
db_user='postgres'
db_host='192.168.144.2'
backupfolder=$PWD/db_backups

keep_day=30
sqlfile=$backupfolder/database-$(date +%d-%m-%Y_%H-%M-%S).sql
zipfile=$backupfolder/database-$(date +%d-%m-%Y_%H-%M-%S).zip
mkdir -p $backupfolder

if pg_dump -U $db_user -h $db_host $db_name > $sqlfile ; then
   echo 'Sql dump created'
else
   echo 'pg_dump return non-zero code | No backup was created!'
   exit
fi

if gzip -c $sqlfile > $zipfile; then
   echo 'The backup was successfully compressed'
else
   echo 'Error compressing backup | Backup was not created!'
   exit
fi
rm $sqlfile
echo $zipfile

find $backupfolder -mtime +$keep_day -delete
