# OpenReqs Requirement Modeling
Swagger like Requirement Modeling and Code Generation.

OpenReqs models Software Requirements into Stateful representations. The idea is this single representation of requirements can be helpful in automatic Software templates generation for development and testing.

Let's take an example and walk-through it. This is the first draft of the proposal and I am open to any suggestions for improvements.

## Example: e-Commerce Web Application

Let's set some ground rules -

* Any application will have some set of states, and some set of actions that can be performed on them. The actions performed would change the state of the application.
* A state of the application is an enumeration of all different things that comprise the state. For example: an e-Commerce web application state may be defined by the URL, Cookies contents and Cart contents.
* A persona is a user who is using the application. This could be a logged in user, guest user, administrator etc. Let's not include persona in the application state, otherwise it would make the state unweildly.
* An action is any action that the user can perform. For example a click, keystroke, URL change or back or forward buttons. For now let's restrict this to user-actions, but this should easily expand to actions that the backend server can perform as well (server pushing some results etc.).

Based on the above, we propose the following generic model that should apply to any application.

* An application consists of a set of finite `states`.
* In each `state`, an `action` can be input to the application - which can change its `state`.
* We can model the entire application by listing down the the relationship between different states, actions and next states.
