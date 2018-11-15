# CORS misconfiguration

CORS defines a way in which a browser and server can interact to determine whether or not it is safe to allow the cross-origin request. It allows for more freedom and functionality than purely same-origin requests.

We find a lot of vulnerabilities these days that have CORS misconfigured.
This misconfiguration allows to make XHR get requests on an authenticated users behalf
and steal sensitive information from the server!

#### The issue?

Rather than explaining myself please refer to the following blog to read all about the 
issue at hand:

The source is found [here](https://github.com/RiieCco/owasp-bay-area/tree/master/course-guide/server-side-template-injection/report.html)


### Spoiler 1

You can find this link after loggin in with either:

```
link: http://0.0.0.0:8081/login
user : admin:admin
```

Or by finding a obscure backdoor by running "dirb" against the web-server


Please refer to the following page:

```
http://0.0.0.0:8081/confidential
```

Here we will find this page:

![target page](../img/cors-page.png)

Whenever we do a GET request on this page and we add an origin header to the request we 
create the following response.

![request/response](../img/req-resp-cors.png)








