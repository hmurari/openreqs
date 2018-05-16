Feature: Dashboard
	Scenario: Logout
		Given I am on page "Dashboard"
		When I logout
		Then my next page will be home

	Scenario: Search(Keyword)
		Given I am on page "Dashboard"
		When I search(keyword)
		Then my next page will be search_results(keyword)

