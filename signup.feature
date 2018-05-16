Feature: Signup
	Scenario: Valid Signup
		Given I am on page "Signup"
		When I valid signup
		Then my next page will be signup_confirmation

	Scenario: Invalid Signup
		Given I am on page "Signup"
		When I invalid signup
		Then my next page will be signup_failure

