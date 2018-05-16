Feature: Login
	Scenario: Valid Login With "Username", "Password"
		Given I am on page "Login"
		When I valid login with "username", "password"
		Then my next page will be dashboard

	Scenario: Invalid Login
		Given I am on page "Login"
		When I invalid login
		Then my next page will be login_failure

