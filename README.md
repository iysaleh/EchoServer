# Advantu Echo Server

This source repository provides a simple Python-based implementation for an Echo Server, an Echo Client, a log archival script, and a pytest based test suite to test these components.

The purpose of this repository is to demonstrate the ability to code in Python to assist Advantu in their hiring decision. All code in this repository is covered under the [MIT-License](License.md)



## Software Requirements
The list of requirements & concepts discussed with Advantu are as follows (with code references):

* Create an [Echo Server](EchoServer.py)
    * A [Client App](EchoClient.py) should be able to say "Hi There" and it should echo it
* Exercise Socket Communication -- Threads or processes talking to each other over a socket [1](EchoServerTest.py?plain=1#L99) [2](EchoServer.py?plain=1#L67) [3](EchoClient.py?plain=1#L27)
* Demonstrate ability to use [PyTest](EchoServerTest.py) [1](EchoServerTest.py?plain=1#L91) [2](EchoServerTest.py?plain=1#L140) [3](EchoServerTest.py?plain=1#L153) 
* Demonstrate use of Enums [1](EchoServer.py?plain=1#L16) [2](EchoServer.py?plain=1#L100) [3](EchoServer.py?plain=1#L114) [4](EchoServer.py?plain=1#L122)
* Demonstrate use of Logging [1](EchoServer.py?plain=1#56) [2](EchoServer.py?plain=1#79) [3](EchoServer.py?plain=1#99)
* Use Python dictionaries & understand how they're laid out [1](EchoServer.py?plain=1#L122) [2](EchoServer.py?plain=1#L114) [3](EchoClient.py?plain=1#L)
* Demonstrate ability to use JSON [1](LogArchive.py?plain=1#L41) [2](LogArchive.py?plain=1#L34)
* Demonstrate the translation of text into spreadsheets using Pandas CSV library [1](LogArchive.py?plain=1#L26)

## Documentation

## Usage Examples
*Start the Echo Server*
```
python EchoServer.py --host localhost --port 7777
```
*Start the Echo Client*
```
python EchoClient.py --host localhost --port 7777
```
*Input messages from the client, see them echoed back from the server*
```
Input: Hello world!
Echo:  Hello world!
```
## Demo
The following section demos how to use the various components of this project.

### Using the EchoServer and EchoClient Demo
![](Demo/DemoEchoServer.gif)

### Using the LogArchive Script Demo
![](Demo/LogArchiveExample.gif)

### Executing the Tests Demo
![](Demo/RunningTheTests.gif)
