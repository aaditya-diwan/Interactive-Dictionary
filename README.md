# Interactive-Dictionary
I have created an Interactive Dictionary using Python.
The data is stored in JSON format, to get the most appropriate meaning for the word ,
I have used the get_close_matches object in the difflib library to get the
most closest match in the JSON data.
The JSON Data consists of the key and value pairs
key : Word
value : Meaning
It has many interactive features like
1)If we want to search for a word like 'data' and we type 'DaTa' it will correct the word and show it's right meaning.
2)If we type 'Dat' instead of data it will ask whether you meant 'data' instead ?
and many more interactive features are present.
