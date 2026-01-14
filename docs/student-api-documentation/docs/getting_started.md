# Getting Started

## Authentication

For authentication with the API you need a Moodle web service token, that authenticates your user with the web service.

To that end, access the following URL in a browser:

```url
https://tuwel.tuwien.ac.at/admin/tool/mobile/launch.php?service=moodle_mobile_app&passport=student_api
```

If you are presented with a login prompt, authenticate yourself as usual.

There will be a (failed) attempt to redirect you to:

```html
moodlemobile://token=<BASE64_ENCODED_TOKEN>
```

You can access this string in the developer console of your browser. Decoding `<BASE64_ENCODED_TOKEN>` will result in a string of the form:

```html
<PASSPORT_VALIDATION>:::<TOKEN>[:::<PRIVATE_TOKEN>]
```
The second component (`<TOKEN>`) is the desired **web service token**.
You can use this token until it expires (see [Token Expiration](notes.md)).

When using the provided Python client, you can pass the Base64 encoded string directly.


## Calling Functions

The API is a collection of so called web service functions.

Call (via the browser, curl, or your programming language of choice):
```html
https://tuwel.tuwien.ac.at/moodle/webservice/rest/server.php?wstoken=<TOKEN>&wsfunction=<WS_FUNCTION>&moodlewsrestformat=json
```
where `<TOKEN>` refers to your web service token, and `<WS_FUNCTION>` is the name of the `WS_FUNCTION` you want to call. 

Function arguments can be appended to the call as GET-parameters. See the following example:

```html
...?wstoken=<TOKEN>&wsfunction=mod_quiz_get_quizzes&moodlewsrestformat=json&courseids[0]=1&courseids[1]=2
```

This would call the endpoint `mod_quiz_get_quizzes`, using `json`-format with the parameters `{courseids: [1,2]}`.

Alternatively, you can do the same as a POST request, with parameters in the request body instead of the URL.

This is of course not feasible for repeated use. We recommend to use one of the provided clients or to create your own.

More Information: <https://docs.moodle.org/dev/Creating_a_web_service_client>

Please find a [curated list of functions](functions.md) and [detailed documentation](all_functions.md).

## Clients

We provide JavaScript and Python API-clients. Feel free to use them as a starting point & extend/modify them to fit your needs.

 * Python: <https://github.com/tuwel-api/moodle-client-python>
 * JavaScript: <https://github.com/tuwel-api/moodle-client-javascript>

### Usage


Both examples call mod_quiz_get_quizzes_by_courses with parameter `courseids=[]`, then print the response. 
Find more detailed information in the respective repositories.

#### Python

```python
from moodle_client import MoodleClient

token = 'YOUR_API_TOKEN'
client = MoodleClient(token, 'https://tuwel.tuwien.ac.at')
response = client.send('mod_quiz_get_quizzes_by_courses', {'courseids': []})
print(response) 
```

#### JavaScript

```javascript
const {MoodleRestClient} = require('./moodle-rest-client');
const clientConfig = {
    protocol: 'https',
    port: '443',
    subdirectory: ''
}
const token = 'YOUR_API_TOKEN'
const client = new MoodleRestClient('tuwel.tuwien.ac.at', token, clientConfig)
client.send('mod_quiz_get_quizzes', {courseids: []}).then(console.log)

```
