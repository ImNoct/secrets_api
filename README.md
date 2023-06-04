## Test task with fastAPI
Task text [here](https://github.com/avito-tech/mi-trainee-task)
## API Methods
### GET /generate
Generates new secret and returns `{KEY}`<br>
Request body
```
{  
    "text" : "secret text",
    "code" : "secret code"
}
```
Response and status `201 Created`
```
{
    "key": "{KEY}"
}
```
### GET /secrets/{KEY}
Returns secret text<br>
Request body
```
{
    "code" : "secret code"
}
```
Response
```
{
    "text": "text"
}
```
or `404 Not Found` if secret not exists
```
{
    "detail": "secret with key: {KEY} was not found"
}
```