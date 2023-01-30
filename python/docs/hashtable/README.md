# Hashtables

- a data structure which stores data by using a pair of values and keys.

## Challenge

set
- Arguments: key, value
- Returns: nothing
- This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- Should a given key already exist, replace its value from the value argument given to this method.

get
- Arguments: key
- Returns: Value associated with that key in the table

has
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

keys
- Returns: Collection of keys

hash
- Arguments: key
- Returns: Index in the collection for that key

## Approach & Efficiency

BigO
Time => O(n) linear time
Space => O(n) linear space

## API

set
- Arguments: key, value
- Returns: nothing
- This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- Should a given key already exist, replace its value from the value argument given to this method.

get
- Arguments: key
- Returns: Value associated with that key in the table

has
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

keys
- Returns: Collection of keys

hash
- Arguments: key
- Returns: Index in the collection for that key
