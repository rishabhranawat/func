### Func

#### The Next Step In APIs

APIs are the highways of modern day internet architecture. It is what has enabled extremely useful services to proliferate and change the world for the better.

APIs are great, however, there is a fundamental limitation. They are fundamentally designed for machines.

It is clear that the world is headed in a direction where we want to able to talk to APIs the way we talk to humans - in plain, simple language.

Now, this does not remove the need for an interface. Visual interfaces in many cases are still a better UX experience than just chat.

A wide range of use cases can be boiled down to just interfacing with APIs better. And if humans were given the ability to directly interface with APIs without the need to go through clunky software and overly complicated interface, we could change the world.

To this end, we introduce a new paradigm -  Language Programming Interface.

#### Service providers should provide service. Language models should provide language. Developers should not have to plumb. Let us provide the interface -- the plumbing, the roads.

We want to be the language infrastructure company for you.

#### Okay, but, specifically, what are we trying to solve?
There are the following few problems that we face when developing LLM based applications:
* For every existing and new API you need to plumb the function signatures
* This is not a problem that the LLM creator should solve
* This is not a problem the API provider should solve
* This is not a problem the Developer should solve

#### Language Programming Interface and Execution
We will build a library that will do the plumbing for the most important and critical APIs. We will be LLM agnostic but begin with OpenAI. This will be provided as an open source library that developers can use to build applications.

There are two parts:
1.) Understanding which function a particular language query wants to execute
2.) To actually execute that query

(2.) requires deployment integrations etc.,