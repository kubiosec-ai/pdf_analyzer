# Getting Started with OWASP WebGoat 4.0 and SoapUI: Hacking Web Services - An Introduction

**Version 1.0**  
*Philippe Bogaerts*  
[Philippe.Bogaerts@radarhack.com](mailto:Philippe.Bogaerts@radarhack.com)  
[www.radarhack.com](http://www.radarhack.com)  

**Reviewed by Erwin Geirnaert**  
[erwin.geirnaert@zionsecurity.com](mailto:erwin.geirnaert@zionsecurity.com)  
[www.zionsecurity.com](http://www.zionsecurity.com)  

## Table of Contents

1. [Introduction](#introduction)
2. [A Word on WebGoat 4.0](#a-word-on-webgoat-40)
3. [A Word on SoapUI](#a-word-on-soapui)
4. [Installing WebGoat 4.0](#installing-webgoat-40)
5. [Installing SoapUI](#installing-soapui)
6. [Understanding Web Services](#understanding-web-services)
7. [Exploring WebGoat](#exploring-webgoat)
8. [Invoking Web Services Directly](#invoking-web-services-directly)
9. [Time to Hack](#time-to-hack)
10. [Conclusion](#conclusion)

---

## 1. Introduction

Service-Oriented Architecture (SOA), web services, WS-security, and associated technologies have become business-critical components of modern IT infrastructure and applications. Security efforts must focus on applications in use, as they are the focal points for potential vulnerabilities. This paper aims to educate and raise awareness about web services exploitation, targeting those interested in enhancing cybersecurity.

All tools discussed are available at [OWASP](http://www.owasp.org) and [SoapUI](http://www.soapui.org).

## 2. A Word on WebGoat 4.0

From OWASP:
> WebGoat is a deliberately insecure J2EE web application maintained by OWASP designed to teach web application security lessons through practical exploitation of vulnerabilities. For more information, visit [OWASP WebGoat Project](http://www.owasp.org/index.php/Category:OWASP_WebGoat_Project).

## 3. A Word on SoapUI

From the SOAPUI website:
> SoapUI is a desktop application for inspecting, invoking, developing, and testing web services over HTTP. It is mainly for developers and testers of web services across platforms like Java and .NET. SoapUI supports interactive and automated testing through command-line tools and requires Java 1.5. It is licensed under the LGPL.

For more details, visit [SoapUI](http://www.soapui.org).

## 4. Installing WebGoat 4.0

**Steps:**

1. Download and unzip `Windows_WebGoat-4.0_Release.zip`.
2. Ensure port 80 is free by stopping any services like IIS or Apache, and programs like Skype that might use port 80. Use `netstat –an` to check.
3. Start WebGoat by running `WebGoat.bat` in the installation directory.
4. Connect to [http://127.0.0.1/WebGoat/attack](http://127.0.0.1/WebGoat/attack) and log in with username: `guest` and password: `guest`.
5. Start exploring lessons.

**Note:** You can change the Tomcat connector port by editing `server.xml` in `tomcat\conf`.

## 5. Installing SoapUI

**Steps:**

1. Ensure you have a Java Runtime Environment or Developer Kit installed.
2. Download `soapui-1.5-bin.zip`, unzip it and launch `soapui.bat` from the `bin` folder.
3. The SoapUI interface should start up allowing you to interact with web services.

## 6. Understanding Web Services

Web services facilitate application-to-application communication, unlike traditional user-to-application models. They allow developers to leverage existing services on corporate, partner, or public networks.

A common use case is integrating an SMS service in an application. By reusing an existing web service, developers can send SMS alerts with minimal code. Web services utilize XML for data representation, making them platform-independent.

For a starting point in WebGoat, visit: [WebGoat Screen 14](http://127.0.0.1/WebGoat/attack?Screen=14&menu=1110).

Learn about web service operations, syntax, parameters, and responses using WSDL files, such as the one at [WSDL File](http://127.0.0.1/WebGoat/services/WSDLScanning?WSDL).

SOAP (Simple Object Access Protocol) provides a network protocol-agnostic messaging framework used in web services communication, typically over HTTP or HTTPS.

## 7. Exploring WebGoat

Visit [WebGoat Attack](http://127.0.0.1/WebGoat/attack?menu=1110) to begin exploring how web services operate. There you can see how an application constructs SOAP messages to query databases for credit card information, simulating real-world scenarios.

## 8. Invoking Web Services Directly

Instead of a web interface, use SoapUI for direct access:

1. Create a new project in SoapUI and import WSDL files for the desired service.
2. SoapUI automatically generates requests for operations.
3. Modify SOAP messages to test different inputs and observe responses.

Access a WSDL at [WsSqlInjection WSDL](http://127.0.0.1/WebGoat/services/WsSqlInjection?WSDL).

## 9. Time to Hack

We can exploit poorly secured web services akin to web application vulnerabilities, like SQL injection. Analyze code to see vulnerabilities:

```java
String query = "SELECT * FROM user_data WHERE userid = " + accountNumber;
```

By crafting requests that exploit this, such as:
```SQL
SELECT * FROM user_data WHERE userid = 101 OR 1=1;
```

Simulate this attack with a crafted SOAP request, achieving unauthorized data access in this training scenario.

## 10. Conclusion

Web services are susceptible to familiar web attacks; each application component must secure and safeguard against such vulnerabilities. This educational paper aims to enlighten readers about web service exploits and highlights the importance of secure coding practices.

For further questions or comments, contact [xxradar@radarhack.com](mailto:xxradar@radarhack.com).
