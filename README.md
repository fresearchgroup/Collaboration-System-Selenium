# Collaboration-System-Selenium

# Notification-system-Testing-using-selenium<br/>

1.) .env file : <br/>
      NOTIFICATION_PORT = 7000<br/>
      NOTIFICATION_USER = shubh,admin,raghav,ty<br/>
      NOTIFICATION_PASSWORD = shubh<br/>
      IP_ADDRESS= 172.17.0.1<br/>
      NOTIFICATION_ROLE = author,publisher,admin<br/>
      NOTIFICATION_GROUP_ROLE = author,publisher,group admin<br/><br/>

2.) Order of testing is mentioned in the report of Notification system Report for system.<br/>
<br/>
3.) Changes in id<br/>
    The "left-side" needs to be searched and insert id = “right-side”  <br/>
      Unsubscribe - Unsubscribe<br/>
      Yes - Yes<br/>
      Save Changes - savechanges<br/>
      transition.to_state.name- id =”publish” but at 212 line id = “Visible”<br/>
      Reject - reject<br/>
      Update - update<br/>
      Remove - remove<br/>
      <br/>
     The link for the comparison is : https://github.com/singhalshubh/hacker-1/pull/1/files<br/>
     
4.) Roles:  <br/>
There are 4 users in the system : shubh,admin,raghav,ty.<br/>
Password is same for all i.e. “shubh”<br/>
Shubh - Community-admin,group-admin<br/>
Admin - Community-admin,group-admin<br/>
Raghav - Community-publisher,group-publisher<br/>
Ty - author for both group and community.<br/><br/>
Community : <br/>
There are 2 communities and the testing is done on the “second community” always.<br/>
The articles 5,6 are drafts and goes till the published state.<br/>
The articles 7 is just visible<br/>
Article 9,13 is draft in community<br/>
Article 12 is visible.<br/><br/>
Group : <br/>
The group formed is only 1.<br/>
8,10,11 article is in the group.<br/>

