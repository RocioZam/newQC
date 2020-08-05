CS50 - Web Programming with Python and JavaScript

https://youtu.be/LnBXF9pZ_W8


This project is a management system created with Django. 

Aside from Django, the following  installations are required:

    Django Calendar
    Django Filter 

The charts require Charts.js


The idea is to receive video files for technical review.  The APP checks files for: Frames per Second (speed), codec type, technical issues (drop frames, VBL, sync, etc).

The app also filter tasks by Client, Operator , date and status, finally the application generates statistics and KPIs por the entire operation by all variables mentioned earlier. 

The step by step guideline to be followed is:

1.  The Administrator will see the files with 'pending' status, and author is equal to 'administrator' afterwards the Administrator assigns the files to the QC Operators, modifying the date and author from  Django Admin Panel.
2.  The Calendar and Profile Account will be filled in with all the data previously entered by the Administrator.
3.  The QC Operator can review  Calendar and/or own Profile Account to check  which files were assigned and when.  
4.  When the QC Operator finishes reviewing the video files, he/she must fill-in the form with technical results.


KPI and Client charts are automatically generated.



Justification:

This project is different from previous projects in that it aims to solve practical/real-life corporate needs.  It allows Client Performance measurements as well as the ability to quickly review KPI reports. Furthermore, it shows these reports and indicators in dynamic visual styles and presentations (Charts.js).  
The project is more complex in that it allows Managers to schedule and program personnel tasks, assign them and track in corresponding specific time tables.
# qc
