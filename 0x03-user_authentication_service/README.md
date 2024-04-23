This is the readme file for the project 0x03-user_authentication_service
0. User model
 create a SQLAlchemy model named User for a database table named users

1. create user
complete the DB class provided below to implement the add_user method.

2. Find user
implement the DB.find_user_by method

3. update user
implement the DB.update_user method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None.

4. Hash password
define a _hash_password method that takes in a password string arguments and returns bytes.

5. Register user
implement the Auth.register_user in the Auth class provided

6. Basic Flask app
Create a Flask app that has a single GET route ("/") and use flask.jsonify to return a JSON payload of the form

7. Register user
implement the end-point to register a user

8. Credentials validation
implement the Auth.valid_login method

9. Generate UUIDs
implement a _generate_uuid function in the auth module

10. Get session ID
implement the Auth.create_session method

11. Log in
implement a login function to respond to the POST /sessions route

12. Find user by session ID
implement the Auth.get_user_from_session_id method

13. Destroy session
implement Auth.destroy_session

14. Log out
 implement a logout function to respond to the DELETE /sessions route

15. User profile
implement a profile function to respond to the GET /profile route.

16. Generate reset password token
implement the Auth.get_reset_password_token method

17. Get reset password token
implement a get_reset_password_token function to respond to the POST /reset_password route

18. Update password
implement the Auth.update_password method

19. Update password end-point
implement the update_password function in the app module to respond to the PUT /reset_password route
