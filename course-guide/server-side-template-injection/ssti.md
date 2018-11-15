# Server side template injection

#### What is it in a nutshell?

This is the course guide for server-side template injection.

Template engines are widely used by web applications to present dynamic data via web pages and emails. Unsafely embedding user input in templates enables Server-Side Template Injection, a frequently critical vulnerability that is extremely easy to mistake for Cross-Site Scripting (XSS), or miss entirely. Unlike XSS, Template Injection can be used to directly attack web servers' internals and often obtain Remote Code Execution (RCE), turning every vulnerable application into a potential pivot point.

Follow the full source to find how to discover this vulnerability and how to determine the templating engine
that is being used by the application.

[full source here](https://portswigger.net/blog/server-side-template-injection)

#### Give away!

Included [here](https://github.com/RiieCco/owasp-bay-area/tree/master/course-guide/server-side-template-injection/report.html) is the scan report of a Burp intruder scan on the target. Use this scan report to pinpoint the exact location of the vulnerability.










