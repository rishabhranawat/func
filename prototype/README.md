### Func

#### The Next Step In APIs

APIs are the highways of modern-day internet architecture. APIs are great, however, there is a fundamental design choice that limits them - they are designed to communicate with other programs.  It is clear that the world is headed in a direction where we want to be able to talk to APIs the way we talk to humans - in plain, simple language. 

We, at func, want to develop the next frontier of APIs and we call these Language Programming Interfaces (LPIs).

#### Service providers should provide service. Language models should provide language. Developers should not have to plumb. Let us provide the interface, the plumbing, and the roads.

Three main veins:
* For every existing and new API a developer needs to do a great deal of arduous plumbing.
    * This is not a problem that the LLM creator should solve
    * This is not a problem the API provider should solve
    * This is not a problem the Developer should solve
* Any backend service should be ablone to interface with an LLM.
* Improving LLM function call detection and construction.

We want to focus on the first two to begin with.

#### Language Programming Interface and Execution
1. Providing the plumbing (Pythonic Library) so that interacting with any API should be a matter of a few lines of code.
2. Provide an execution framework so that eventually the function call can be natively executed.

#### Demonstration

```
import funclib.lib

chat_response = agent.chat_completion_request(
    messages, functions=funclib.lib.funcs()
)
```
[Prototype Demo](https://github.com/rishabhranawat/func/assets/10802684/cfde71a1-aea2-4fbf-be1f-99ae1a47086f)
