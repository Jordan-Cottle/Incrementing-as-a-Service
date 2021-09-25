""" This module is for your persistence layer.

Most applications need to persist some data. When the server restarts you want it to
remember what it was doing. Database engines are the most common and powerful way to
store data long term. A local database like sqlite is easy to set up and provides a lot
of the benefits of having a database manage your data versus trying to do it yourself.

Avoid putting business logic into this module. It should only provide a simplified interface
to store and retrieve data.
"""