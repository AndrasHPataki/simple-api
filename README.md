# E.M.D PATTERN
*A new Restful API standardization model.*

**EMD** is an acronym for **Endpoint-Method-Database**. It is a software design standard, focused on reusing code and separating **REST** concepts into interconnected layers. It aims to structure the dynamic and simple development of **APIs**; From which the delivery of the data (usually in **JSON**) is separate from the methods that interact with the database.
The Use of the **EMD** Model leads to efficient parallel development.

The **EMD** Model was developed primarily for applications in the **Python language**, more specifically for the Web Framework FLASK.

## A new exclusive model for APIs

Emd was designed to develop Apis REST with just "one click"; It was inspired by the "Flask Factory" model, which is defined in the documentation as "... nice ways to further improve the experience".
 The advantage of the EMD method is its ready-made structure and ready to be used, without the need for configuration.
 
## Explaining the separation

In summary, an **EMD** application is divided into three (3) major parts:
##### ENDPOINTS
>The endpoints file is responsible for allocating all access URLs available in its API. It is the gateway for the user making the request; it is also common in this space, for variables to pass to execute specific requests.
>
##### METHODS
>A Rest application is defined by a list of different methods that will run on a server. For this, there is the Methods file, where all functions / classes responsible for REST operations will be. This file interacts directly with your application's database and yields feedback to the user.
>
##### DATA BASE
>This is the file used to interact / create your database, it is reserved exclusively for this purpose, and it generally does not receive imports other than itself.


## I want to use, where do I download?

For the time being the EMD Model has only one **FLASK** model ready to serve. Feel free to improve or modify.

### For Flask Developers
