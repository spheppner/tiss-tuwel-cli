# Additional Notes

## File Download


If you get an url to a file to download from the API, you can download it via a normal HTTP-request, where you append your token:
```
GET <URL>&token=<TOKEN>
```

We verified this for URLs containing `/webservice/pluginfile.php`.

Also consider using our [python client's](https://github.com/tuwel-api/moodle-client-python) `download` method for this purpose

## userid
Most of the time, functions apply to the authenticated user by default.

Sometimes, however, they do not. We found that in some cases setting the userid explicitly is necessary, even
if its stated differently (or not at all) in the function definition.

You can find your userid in TUWEL by following these steps:

 1. Expand the navigation next to your name and profile picture in the top right corner.
 2. Choosing "Profile" in the popup menu.
 3. Find your id as a query parameter in the URL.

### Token Expiration

** TODO: when the project is deployed, describe the token expiration time etc. here.**