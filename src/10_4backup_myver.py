#!/usr/bin/python
# Filename: backup_myver.py

import os
import time

source = raw_input("Input your folder which want to backup:")

target_dir = raw_input("Input your target folder which you will put your backup files")

if not os.path.exists(source):
    print "No found the source folder"
    #os.mkdir(source) # make directory
    #print 'Successfully created source directory', source
    
if not os.path.exists(target_dir):
    print "No found the target folder"
    os.mkdir(target_dir) # make directory
    print 'Successfully created target directory', target_dir
    
#today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
#now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
'''comment = raw_input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successfully created directory', today'''
    

#zip_command = "tar -cvzf '%s' %s" % (target, ' '.join(source))
zip_command = "zip -qr '%s' %s" % (target_dir, source)

print "the zip_command is: &s" % str(zip_command)

'''
# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target_dir
else:
    print 'Backup FAILED' '''