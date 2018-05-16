Feature: Home
	Scenario: Goto Signup Page
		Given I am on page "Home"
		When I goto signup page
		Then my next page will be signup

	Scenario: Goto Login Page
		Given I am on page "Home"
		When I goto login page
		Then my next page will be login

	Scenario: Goto Search Page
		Given I am on page "Home"
		When I goto search page
		Then my next page will be search

	Scenario: Search "Keyword"
		Given I am on page "Home"
		When I search "keyword"
		Then my next page will be search

