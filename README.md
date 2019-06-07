# Collaboration-System-Selenium

1.) .env file : 
PROJECT_PORT = 7000 (Not used anywhere.....)
NOTIFICATION_USER = shubh,admin,raghav,ty
NOTIFICATION_PASSWORD = shubh
IP_ADDRESS= https://172.17.0.1:7000
NOTIFICATION_ROLE = author,publisher,admin
NOTIFICATION_GROUP_ROLE = author,publisher,group admin


2.) Order of testing is mentioned in the report of Notification system Report for system.

3.) Changes in id
The "left-side" needs to be searched and insert id = “right-side” 
Unsubscribe - Unsubscribe
Yes - Yes
Save Changes - savechanges
transition.to_state.name- id =”publish” but at 212 line id = “Visible”
Reject - reject
Update - update
Remove - remove

The link for the comparison is : https://github.com/singhalshubh/hacker-1/pull/1/files

4.) Roles: 
There are 4 users in the system : shubh,admin,raghav,ty.
Password is same for all i.e. “shubh”
Shubh - Community-admin,group-admin
Admin - Community-admin,group-admin
Raghav - Community-publisher,group-publisher
Ty - author for both group and community.

Community : 
There are 2 communities and the testing is done on the “second community” always.
The articles 5,6 are drafts and goes till the published state.
The articles 7 is just visible
Article 9,13 is draft in community
Article 12 is visible.

Group : 
The group formed is only 1.
8,10,11 article is in the group.

