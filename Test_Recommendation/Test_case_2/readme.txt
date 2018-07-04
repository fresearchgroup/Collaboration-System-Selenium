This test case runs by executing the test_file_driver.py file which runs all other python script.
No need to run other python file other than the test_file_driver.py.
The test_file1.py and test_file2.py set up the environment for this test case.
The test_file3.py contains the test_reco function which test the recommendation.
The test_file4.py tear down (remove) the environment which is required to run this test case.

The idea is that:
Create 2 communities and add 6 published articles in each community. Add 3
users to the system. All this will be done by django admin. The first user will join
community 1 and the second user will join community 2. Now create some views
for the articles in each community. The user in community 1 will give views to
some articles of community 1 and user 2 will do the same for community 2. Some
articles will get more views than the others in each community. For instance,
article 1 from community 1 will get 10 views, article 2 will get 8 views, article 3
will get 2 views and the left wouldn't get any new views by user1 and similarly in
community 2 by user 2. Now Login as user 3 and view articles 2,3 and 4 from
community 1. Finally, train the model.

###################################

The requirements in the .env file:

ADDRESS: This field is the ip address of the docker.
NAME: This field is the username of any existing user in the system(prefered django admin).
PASSWORD: This field is the password of above username.
DEPLOY_ADDRESS: This field is the ip address of the Collaborative system (with ports).
DJANGO_ADMIN_NAME: This field is the username of django admin.
DJANGO_ADMIN_PASSWORD: This field is the password of django admin.
MINIMUM_RECOMMENDATION_PERCENTAGE: This field is set by tester which required, the minimum percentage of test community articles 1 in the recommendation of test user 3.( default: 60% )
IP: This field is the IP address of the system.

####################################

Note: The web driver may fail. Then in that case It is required to remove the test_community1 and test_community2,test_user1,test_user2,test_user3,test_community_article_11,....,etc (if formed, check in django admin).And then run the test_file_driver.py again.

Note: The image is kept because the selenium is creating the community and article. It is required the image file.

Note: The model must be trained after execution of test_file2.py. 
